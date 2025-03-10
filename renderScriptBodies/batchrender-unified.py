# Sanity checks before rendering
bpy.data.objects["rig"].data.pose_position = 'POSE'
bpy.data.objects["Armature - Helirope"].data.pose_position = 'POSE'
bpy.data.objects["Armature - Rock"].data.pose_position = 'POSE'
for j in range(1,26):
	helpers.enablePropRenderlayer(j)



objectList = [
	"Weapon", "Vest", "Backpack", "Hat",
	"Face", "Legs", "Body", "Item", "Helmet"
]

rifleActions = [
	"Standing - Rifle - Aim", "Crouch - Rifle - Aim & Shoot", "Prone - Rifle - Crawl & Shoot",
	"Standing - Rifle - Shoot low", "Standing - Rifle - Hip Aim", "Standing - Rifle - Hip Shoot low",
	"Standing - Rifle - Aim Badass", "Crouch - Rifle - Aim & Shoot Badass", "Prone - Rifle - Crawl & Shoot Badass",	"Standing - Rifle - Hip Aim Badass",
	"Standing - Rifle - Aim & Shoot - Female", "Crouch - Rifle - Aim & Shoot - Female", "Prone - Rifle - Crawl & Shoot - Female",
	"Standing - Rifle - Shoot low - Female", "Standing - Rifle - Hip Aim - Female", "Standing - Rifle - Hip Shoot low - Female",
	"Standing - Rifle - Hip Aim Water", "Standing - Rifle - Aim Water", "Standing - Rifle - Aim & Shoot - Female Water",
	"Standing - Rifle - Hip Aim - Female Water"
]

pistolActions = [
	"Standing - Pistol - Aim & Shoot", "Crouch - Pistol - Aim & Shoot", "Standing - Pistol - Shoot low",
	"Standing - Pistol - Aim & Shoot - One Handed", "Standing - Pistol - Aim Badass", 
	"Standing - Pistol - Aim & Shoot - Female", "Crouch - Pistol - Aim & Shoot - Female",
	"Standing - Pistol - Shoot low - Female", "Standing - Pistol - Aim & Shoot - One Handed - Female",
	"Prone - Pistol - Crawl & Shoot", "Standing - Pistol - Aim & Shoot Water", "Standing - Pistol - Aim Badass Water",
	"Standing - Pistol - Aim & Shoot - Female Water"
]

dualPistolActions = [
	"Standing - Dual Pistols - Aim & Shoot", "Crouch - Dual Pistol - Aim & Shoot", 
	"Standing - Dual Pistols - Aim & Shoot - Female", "Crouch - Dual Pistol - Aim & Shoot - Female",
	"Prone - Dual Pistol - Shoot", "Standing - Dual Pistols - Aim & Shoot Water", "Standing - Dual Pistols - Aim & Shoot - Female Water"
]

radioActions = [
	"Standing - Empty Hands - Radio", "Crouch - Empty Hands - Radio", "Standing - Empty Hands - Use Remote",
	"Standing - Empty Hands - Radio - Female", "Crouch - Empty Hands - Radio - Female", "Standing - Empty Hands - Use Remote - Female"
]

knifeActions = [
	"Standing - Knife - Stab", "Standing - Knife - Slice", "Standing - Knife - Breath",
	"Standing - Knife - Stab - Female", "Standing - Knife - Slice - Female", "Standing - Knife - Breath - Female"
 ]

deathActions = [
	"Standing - Empty Hands - Hit and die", "Standing - Empty Hands - Hit and die 2", "Prone - Empty Hands - Hit and die",
	"Standing - Empty Hands - Flyback hit"
]



for i in range(len(animationArray)):
	# Set up specific animation and its end frame
	currentAction = animationArray[i][0]
	bpy.data.objects["rig"].animation_data.action = bpy.data.actions.get(currentAction)
	bpy.context.scene.frame_end = animationArray[i][1]


	# Setup output folders according to current animation
	outputfolder = "//output/" + currentAction
	for j in range(1,5):
		bpy.data.node_groups["JA2 Layered Sprite - Body Group"].nodes["File Output.00"+str(j)].base_path = outputfolder
	bpy.data.node_groups["JA2 Layered Sprite - Body Shadow Group"].nodes["File Output"].base_path = outputfolder
	bpy.data.node_groups["JA2 - Full Body Group"].nodes["File Output.026"].base_path = outputfolder
	
	# Prop 1, 2, 3...10 outputs
	for j in range(1,26):
		if j < 10:
			number = "00" + str(j)
		else:
			number = "0" + str(j)
		bpy.data.scenes["camera 1"].node_tree.nodes["File Output." + number].base_path = outputfolder	
	

	# Hide objects in renders
	for object in bpy.data.objects:
		objectName = object.name
		if any(substring in objectName for substring in objectList):
			object.hide_render = True
		if "MuzzleFlash" in objectName:
			object.hide_render = True
			object.animation_data.action = bpy.data.actions.get("HideMuzzleFlash")
		if "BloodPool" in objectName:
			object.hide_render = True
			object.animation_data.action = bpy.data.actions.get("HideMuzzleFlash")			

	# Bodytypes
	bpy.data.objects["Body - RGM"].hide_render = True
	bpy.data.objects["Body - BGM"].hide_render = False
	bpy.data.objects["Body - FGM"].hide_render = True
	bpy.data.objects["RGM - Vest Target"].hide_render = True
	bpy.data.objects["BGM - Vest Target"].hide_render = True
	bpy.data.objects["FGM - Vest Target"].hide_render = True
	bpy.data.objects["Body - Elite Camo"].hide_render = True
	bpy.data.objects["SpaceMarine__mesh"].hide_render = True
	bpy.data.objects["Body - FGM - Head"].hide_render = True # For EOD suit
	bpy.data.objects["Body - RGM - Head"].hide_render = True # For EOD suit
	bpy.data.objects["Body - RGM - Legs"].hide_render = True # For EOD vest, when prone


	# Camera scale and bodytype specific setup
	if bpy.data.objects["Body - RGM"].hide_render == False:
		helpers.setCameraOrthoScale(6.6)
	if bpy.data.objects["Body - BGM"].hide_render == False:
		helpers.setCameraOrthoScale(6.0)
	if bpy.data.objects["Body - FGM"].hide_render == False:
		helpers.setCameraOrthoScale(6.6)
	if bpy.data.objects["Body - Elite Camo"].hide_render == False:
		bpy.data.node_groups["Background Group"].nodes["Switch"].check = True
	if bpy.data.objects["SpaceMarine__mesh"].hide_render == False:
		helpers.setCameraOrthoScale(6.0)
		bpy.data.objects["SM_arm_left"].hide_render = False
		bpy.data.objects["SM_arm_right"].hide_render = False
		bpy.data.objects["sm_chest"].hide_render = False
		bpy.data.objects["sm_helmet"].hide_render = False
		bpy.data.objects["sm_jetpack"].hide_render = False
		bpy.data.objects["sm_leg_left"].hide_render = False
		bpy.data.objects["sm_leg_right"].hide_render = False
		bpy.data.objects["sm_pelvis"].hide_render = False
		bpy.data.objects["sm_shoulder_left"].hide_render = False
		bpy.data.objects["sm_shoulder_right"].hide_render = False
		bpy.data.node_groups["Background Group"].nodes["Switch"].check = True
	else:
		bpy.data.objects["SM_arm_left"].hide_render = True
		bpy.data.objects["SM_arm_right"].hide_render = True
		bpy.data.objects["sm_chest"].hide_render = True
		bpy.data.objects["sm_helmet"].hide_render = True
		bpy.data.objects["sm_jetpack"].hide_render = True
		bpy.data.objects["sm_leg_left"].hide_render = True
		bpy.data.objects["sm_leg_right"].hide_render = True
		bpy.data.objects["sm_pelvis"].hide_render = True
		bpy.data.objects["sm_shoulder_left"].hide_render = True
		bpy.data.objects["sm_shoulder_right"].hide_render = True

	
	# Set up water animations
	if "Water" in currentAction:
		helpers.updateWaterVisibility(True)
		for j in range(1,26):
			helpers.disablePropGroundshadows(j)
	else:
		helpers.updateWaterVisibility(False)
		for j in range(1,26):
			helpers.enablePropGroundshadows(j)


	# Set body file outputs
	propsOnly = True
	layeredBody = True
	if propsOnly:
		helpers.disableLayeredbodyOutput()
		helpers.disableFullbodyOutput()
	elif layeredBody:
		helpers.disableFullbodyOutput()
		helpers.enableLayeredbodyOutput()
	else:
		helpers.enableFullbodyOutput()
		helpers.disableLayeredbodyOutput()


	# Display props in renders depending on the set
	renderSet = 23
	if renderSet == 0:
		# Do not render props
		for j in range(1,26):
			helpers.disablePropRenderlayer(j)
		
		if currentAction in deathActions and layeredBody == False:
			#bpy.data.objects["BloodPool"].hide_render = False
			#bpy.data.objects["BloodPool"].animation_data.action = bpy.data.actions.get("Standing - Empty Hands - Hit and die - Blood Pool")
			#bpy.data.objects["BloodPool.Prone"].hide_render = False
			#bpy.data.objects["BloodPool.Prone"].animation_data.action = bpy.data.actions.get("Prone - Get Hit And Die - Blood")
			bpy.data.objects["BloodPool.FlyBack"].hide_render = False
			bpy.data.objects["BloodPool.FlyBack"].animation_data.action = bpy.data.actions.get("Standing - Empty Hands - Flyback hit - Blood")
		
		
	elif renderSet == 1:
		bpy.data.objects["Weapon - FN FAL"].hide_render = False
		bpy.data.objects["Weapon - M16"].hide_render = False
		bpy.data.objects["Weapon - AK47"].hide_render = False
		bpy.data.objects["Weapon - FAMAS"].hide_render = False
		bpy.data.objects["Weapon - SCAR-H"].hide_render = False
		bpy.data.objects["Weapon - Barrett"].hide_render = False
		bpy.data.objects["Weapon - Dragunov"].hide_render = False
		bpy.data.objects["Weapon - PSG1"].hide_render = False
		bpy.data.objects["Weapon - TRG42"].hide_render = False
		bpy.data.objects["Weapon - Mossberg Patriot"].hide_render = False
		bpy.data.objects["Weapon - P90"].hide_render = False
		bpy.data.objects["Weapon - Thompson M1A1"].hide_render = False
		bpy.data.objects["Weapon - PPSH41"].hide_render = False
		bpy.data.objects["Weapon - HK MP5"].hide_render = False
		bpy.data.objects["Weapon - Shotgun"].hide_render = False
		bpy.data.objects["Weapon - Saiga 12K"].hide_render = False
		bpy.data.objects["Weapon - SPAS12"].hide_render = False
		bpy.data.objects["Weapon - UZI SMG"].hide_render = False
		bpy.data.objects["Weapon - RPK"].hide_render = False
		bpy.data.objects["Weapon - SAW"].hide_render = False
		bpy.data.objects["Weapon - PKM"].hide_render = False
		bpy.data.objects["Weapon - Mosin Nagant"].hide_render = False
		bpy.data.objects["Weapon - M14"].hide_render = False
		bpy.data.objects["Weapon - Milkor"].hide_render = False
		bpy.data.objects["Weapon - Rocket Rifle"].hide_render = False
		# Display muzzleflashes only in relevant animations
		if currentAction in rifleActions:
			bpy.data.objects["MuzzleFlash - FN FAL"].hide_render = False
			bpy.data.objects["MuzzleFlash - M16"].hide_render = False
			bpy.data.objects["MuzzleFlash - AK47"].hide_render = False
			bpy.data.objects["MuzzleFlash - FAMAS"].hide_render = False
			bpy.data.objects["MuzzleFlash - SCAR-H"].hide_render = False
			bpy.data.objects["MuzzleFlash - Barrett"].hide_render = False
			bpy.data.objects["MuzzleFlash - Dragunov"].hide_render = False
			bpy.data.objects["MuzzleFlash - PSG1"].hide_render = False
			bpy.data.objects["MuzzleFlash - TRG42"].hide_render = False
			bpy.data.objects["MuzzleFlash - Mossberg Patriot"].hide_render = False
			bpy.data.objects["MuzzleFlash - P90"].hide_render = False
			bpy.data.objects["MuzzleFlash - Thompson M1A1"].hide_render = False
			bpy.data.objects["MuzzleFlash - PPSH41"].hide_render = False
			bpy.data.objects["MuzzleFlash - MP5"].hide_render = False
			bpy.data.objects["MuzzleFlash - Shotgun"].hide_render = False
			bpy.data.objects["MuzzleFlash - Saiga 12K"].hide_render = False
			bpy.data.objects["MuzzleFlash - SPAS12"].hide_render = False
			bpy.data.objects["MuzzleFlash - UZI SMG"].hide_render = False
			bpy.data.objects["MuzzleFlash - RPK"].hide_render = False
			bpy.data.objects["MuzzleFlash - SAW"].hide_render = False
			bpy.data.objects["MuzzleFlash - PKM"].hide_render = False
			bpy.data.objects["MuzzleFlash - Mosin Nagant"].hide_render = False
			bpy.data.objects["MuzzleFlash - M14"].hide_render = False
			bpy.data.objects["MuzzleFlash - FN FAL"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - M16"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - AK47"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - FAMAS"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - SCAR-H"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Barrett"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Dragunov"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - PSG1"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - TRG42"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Mossberg Patriot"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - P90"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Thompson M1A1"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - PPSH41"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - MP5"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Shotgun"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Saiga 12K"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - SPAS12"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - UZI SMG"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - RPK"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - SAW"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - PKM"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Mosin Nagant"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - M14"].animation_data.action = bpy.data.actions.get(currentAction)
			
	elif renderSet == 2:
		# Default case is regular male
		bpy.data.objects["Vest - Flak Jacket"].hide_render = False
		bpy.data.objects["Backpack - Backpack"].hide_render = False
		bpy.data.objects["Hat - Beret"].hide_render = False
		bpy.data.objects["Hat - Helmet"].hide_render = False
		bpy.data.objects["Face - Gasmask"].hide_render = False
		bpy.data.objects["Face - NVG"].hide_render = False
		bpy.data.objects["Hat - Booney"].hide_render = False
		bpy.data.objects["Legs - Kneepad - Left"].hide_render = False
		bpy.data.objects["Legs - Kneepad - Right"].hide_render = False
		bpy.data.objects["Hat - Camo Helmet"].hide_render = False
		bpy.data.objects["Vest - Long Sleeved"].hide_render = False
		bpy.data.objects["Hat - Ballcap"].hide_render = False
		bpy.data.objects["Vest - Kevlar"].hide_render = False
		bpy.data.objects["Hat - Balaclava"].hide_render = False
		bpy.data.objects["Vest - Spectra"].hide_render = False
		bpy.data.objects["Legs - Holster - Right"].hide_render = False
		bpy.data.objects["Legs - Holster - Left"].hide_render = False
		# EOD suit requires a lot of special handling so the EOD vest is hidden by default
		bpy.data.objects["Helmet - EOD"].hide_render = False
		bpy.data.objects["Vest - EOD"].hide_render = True
		bpy.data.objects["Vest - EOD - BGM"].hide_render = True
		bpy.data.objects["Legs - EOD"].hide_render = False
		
		# Modifiers
		bpy.data.objects["Vest - Flak Jacket"].modifiers["Shrinkwrap"].target = bpy.data.objects["RGM - Vest Target"]
		bpy.data.objects["Hat - Ballcap"].modifiers["Shrinkwrap"].target = bpy.data.objects["Body - RGM"]
		bpy.data.objects["Vest - Kevlar"].modifiers["Shrinkwrap"].target = bpy.data.objects["RGM - Vest Target"]
		
		# Switch the background color to gray for props that use the default bodytype palette
		bpy.data.node_groups["JA2 Layered Sprite - Prop 10"].nodes["Switch.002"].check = False # long sleeves
		bpy.data.node_groups["JA2 Layered Sprite - Prop 11"].nodes["Switch.002"].check = False # ballcap
		bpy.data.node_groups["JA2 Layered Sprite - Prop 13"].nodes["Switch.002"].check = False # balaclava
		
		
		# Change objects depending on the body
		if bpy.data.objects["Body - FGM"].hide_render == False or bpy.data.objects["Body - FGM - Head"].hide_render == False:
			# Hide RGM objects
			bpy.data.objects["Vest - Flak Jacket"].hide_render = True
			bpy.data.objects["Hat - Beret"].hide_render = True
			bpy.data.objects["Hat - Helmet"].hide_render = True
			bpy.data.objects["Hat - Booney"].hide_render = True
			bpy.data.objects["Vest - Long Sleeved"].hide_render = True
			bpy.data.objects["Vest - Kevlar"].hide_render = True
			bpy.data.objects["Hat - Balaclava"].hide_render = True
			bpy.data.objects["Vest - Spectra"].hide_render = True
			bpy.data.objects["Helmet - EOD"].hide_render = True
			# Show RGF specific ones
			bpy.data.objects["Vest - Flak Jacket - Female"].hide_render = False
			bpy.data.objects["Hat - Beret - Female"].hide_render = False
			bpy.data.objects["Hat - Helmet - Female"].hide_render = False
			bpy.data.objects["Hat - Booney - Female"].hide_render = False
			bpy.data.objects["Vest - FGM Long Sleeved"].hide_render = False
			bpy.data.objects["Vest - Kevlar - Female"].hide_render = False
			bpy.data.objects["Hat - Balaclava - RGF"].hide_render = False
			bpy.data.objects["Vest - Spectra - RGF"].hide_render = False
			bpy.data.objects["Helmet - EOD - Female"].hide_render = False

			bpy.data.objects["Vest - Flak Jacket - Female"].modifiers["Shrinkwrap"].target = bpy.data.objects["FGM - Vest Target"]
			bpy.data.objects["Hat - Ballcap"].modifiers["Shrinkwrap"].target = bpy.data.objects["Body - FGM"]
			bpy.data.objects["Vest - Kevlar - Female"].modifiers["Shrinkwrap"].target = bpy.data.objects["FGM - Vest Target"]

		elif bpy.data.objects["Body - BGM"].hide_render == False:
			# Hide RGM objects
			bpy.data.objects["Vest - Long Sleeved"].hide_render = True
			bpy.data.objects["Hat - Balaclava"].hide_render = True
			bpy.data.objects["Vest - Spectra"].hide_render = True
			# Show BGM specific ones
			bpy.data.objects["Vest - BGM Long Sleeved"].hide_render = False
			bpy.data.objects["Hat - Balaclava - BGM"].hide_render = False
			bpy.data.objects["Vest - Spectra - BGM"].hide_render = False

			bpy.data.objects["Vest - Flak Jacket"].modifiers["Shrinkwrap"].target = bpy.data.objects["BGM - Vest Target"]
			bpy.data.objects["Hat - Ballcap"].modifiers["Shrinkwrap"].target = bpy.data.objects["Body - BGM"]
			bpy.data.objects["Vest - Kevlar"].modifiers["Shrinkwrap"].target = bpy.data.objects["BGM - Vest Target"]
		
		
		# Disable unused renderlayers			
		helpers.disablePropRenderlayer(18) #EOD Vest
		helpers.disablePropRenderlayer(19) #EOD Pants
		helpers.disablePropRenderlayer(20)
		helpers.disablePropRenderlayer(21)
		helpers.disablePropRenderlayer(22)
		helpers.disablePropRenderlayer(23)
		helpers.disablePropRenderlayer(24)
		helpers.disablePropRenderlayer(25)
		
	elif renderSet == 3:
		bpy.data.objects["Weapon - HK USP"].hide_render = False
		bpy.data.objects["Weapon - HK USP - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - HK MP5K"].hide_render = False
		bpy.data.objects["Weapon - HK MP5K - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Desert Eagle 50"].hide_render = False
		bpy.data.objects["Weapon - Desert Eagle 50 - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - SW500"].hide_render = False
		bpy.data.objects["Weapon - SW500 - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - UZI MP"].hide_render = False
		bpy.data.objects["Weapon - UZI MP Left"].hide_render = False
		bpy.data.objects["Weapon - SawnOff"].hide_render = False
		bpy.data.objects["Weapon - SawnOff - Left Hand"].hide_render = False
		# Display muzzleflashes only in relevant animations
		if currentAction in dualPistolActions:
			leftMuzzleFlashAction = "Dual Pistols - Aim & Shoot - Left Muzzleflash"
			if currentAction == "Prone - Dual Pistol - Shoot":
				leftMuzzleFlashAction = "Prone - Dual Pistol - Shoot - Left Muzzleflash"
			bpy.data.objects["MuzzleFlash - HK USP"].hide_render = False
			bpy.data.objects["MuzzleFlash - HK USP - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - HK MP5K"].hide_render = False
			bpy.data.objects["MuzzleFlash - HK MP5K - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Desert Eagle 50"].hide_render = False
			bpy.data.objects["MuzzleFlash - Desert Eagle 50 - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - SW500"].hide_render = False
			bpy.data.objects["MuzzleFlash - SW500 - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - UZI MP"].hide_render = False
			bpy.data.objects["MuzzleFlash - UZI MP Left"].hide_render = False
			bpy.data.objects["MuzzleFlash - SawnOff"].hide_render = False
			bpy.data.objects["MuzzleFlash - SawnOff - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - HK USP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - HK USP - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - HK MP5K"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - HK MP5K - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Desert Eagle 50"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Desert Eagle 50 - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - SW500"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - SW500 - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - UZI MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - UZI MP Left"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - SawnOff"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - SawnOff - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
		if currentAction in pistolActions:
			bpy.data.objects["MuzzleFlash - HK USP"].hide_render = False
			bpy.data.objects["MuzzleFlash - HK MP5K"].hide_render = False
			bpy.data.objects["MuzzleFlash - Desert Eagle 50"].hide_render = False
			bpy.data.objects["MuzzleFlash - SW500"].hide_render = False
			bpy.data.objects["MuzzleFlash - UZI MP"].hide_render = False
			bpy.data.objects["MuzzleFlash - SawnOff"].hide_render = False
			bpy.data.objects["MuzzleFlash - HK USP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - HK MP5K"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Desert Eagle 50"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - SW500"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - UZI MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - SawnOff"].animation_data.action = bpy.data.actions.get(currentAction)
	
		for j in range(1,11):
			helpers.disablePropRenderlayer(j)
		helpers.disablePropRenderlayer(13)
		helpers.disablePropRenderlayer(14)
		helpers.disablePropRenderlayer(15)
		helpers.disablePropRenderlayer(16)
		helpers.disablePropRenderlayer(17)
		helpers.disablePropRenderlayer(18)
		helpers.disablePropRenderlayer(19)
		helpers.disablePropRenderlayer(20)
		helpers.disablePropRenderlayer(21)
		helpers.disablePropRenderlayer(22)
		helpers.disablePropRenderlayer(23)
		helpers.disablePropRenderlayer(24)
		helpers.disablePropRenderlayer(25)
		
	elif renderSet == 4:
		if currentAction in radioActions:
			bpy.data.objects["Weapon - Radio"].hide_render = False
		if currentAction == "Standing - Empty Hands - Flip Rock":
			bpy.data.objects["Item - Rock"].hide_render = False
			bpy.data.objects["Armature - Rock"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.node_groups["JA2 Layered Sprite - Prop 24"].nodes["Switch.002"].check = False
		# Show rope only in helidrop animation
		if currentAction == "Helidrop":
			bpy.data.objects["Item - Helirope"].hide_render = False
			bpy.data.objects["Armature - Helirope"].animation_data.action = bpy.data.actions.get("Helirope - ArmatureAction")
		
		
		helpers.disablePropRenderlayer(1)
		for j in range(3,24):
			helpers.disablePropRenderlayer(j)
		
	elif renderSet == 5:
		bpy.data.objects["Weapon - Combat Knife"].hide_render = False
		bpy.data.objects["Weapon - Combat Knife"].animation_data.action = bpy.data.actions.get("DisplayProp")
		bpy.data.objects["Weapon - Crowbar"].hide_render = False
		if currentAction in knifeActions:
			bpy.data.objects["Weapon - Combat Knife"].hide_render = False
			bpy.data.objects["Weapon - Combat Knife"].animation_data.action = bpy.data.actions.get(currentAction)
		if currentAction == "Crouch - Knife - Stab - Female" or currentAction == "Crouch - Knife - Stab":
			bpy.data.objects["Weapon - Combat Knife"].hide_render = True
			bpy.data.objects["Weapon - Combat Knife"].animation_data.action = bpy.data.actions.get("HideMuzzleFlash")
			bpy.data.objects["Weapon - Combat Knife Alt hold"].hide_render = False
		if currentAction == "Standing - Knife - Throw - Female" or currentAction == "Standing - Knife - Throw":
			bpy.data.objects["Weapon - Combat Knife"].hide_render = False
			bpy.data.objects["Weapon - Combat Knife Alt hold"].hide_render = True
			bpy.data.objects["Weapon - Combat Knife"].animation_data.action = bpy.data.actions.get(currentAction)
		if currentAction == "Standing - Crowbar - Hit - Female" or currentAction == "Standing - Crowbar - Hit":
			bpy.data.objects["Weapon - Crowbar"].hide_render = False
		
		helpers.disablePropRenderlayer(2)
		for j in range(4,26):
			helpers.disablePropRenderlayer(j)
		
	elif renderSet == 6:
		bpy.data.objects["Weapon - LAW"].hide_render = False
		if currentAction == "Crouch - Mortar - Fire":
			bpy.data.objects["Weapon - Mortar Tube"].hide_render = False
			bpy.data.objects["Weapon - Mortar Legs"].hide_render = False
			bpy.data.objects["Armature - Mortar"].animation_data.action = bpy.data.actions.get(currentAction)
		
		for j in range(3,26):
			helpers.disablePropRenderlayer(j)
			
	elif renderSet == 7:
		bpy.data.objects["Weapon - FNFAL"].hide_render = False
		bpy.data.objects["Weapon - Galil AR"].hide_render = True
		if currentAction in rifleActions:
			bpy.data.objects["MuzzleFlash - Galil AR"].hide_render = True
			bpy.data.objects["MuzzleFlash - FNFAL"].hide_render = False
			bpy.data.objects["MuzzleFlash - FNFAL"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Galil AR"].animation_data.action = bpy.data.actions.get(currentAction)

		for j in range(1,8):
			helpers.disablePropRenderlayer(j)
		for j in range(9,26):
			helpers.disablePropRenderlayer(j)

	elif renderSet == 8:
		bpy.data.objects["Weapon - AMD65"].hide_render = False
		bpy.data.objects["Weapon - SV98"].hide_render = False
		bpy.data.objects["Weapon - SA24"].hide_render = False
		bpy.data.objects["Weapon - MP41/44"].hide_render = False
		bpy.data.objects["Weapon - M501"].hide_render = False
		bpy.data.objects["Weapon - AWM"].hide_render = False
		bpy.data.objects["Weapon - R93"].hide_render = False
		bpy.data.objects["Weapon - M24"].hide_render = False
		bpy.data.objects["Weapon - M40A1"].hide_render = False
		if currentAction in rifleActions:
			bpy.data.objects["MuzzleFlash - AMD65"].hide_render = False
			bpy.data.objects["MuzzleFlash - SV98"].hide_render = False
			bpy.data.objects["MuzzleFlash - SA24"].hide_render = False
			bpy.data.objects["MuzzleFlash - MP41/44"].hide_render = False
			bpy.data.objects["MuzzleFlash - M501"].hide_render = False
			bpy.data.objects["MuzzleFlash - AWM"].hide_render = False
			bpy.data.objects["MuzzleFlash - R93"].hide_render = False
			bpy.data.objects["MuzzleFlash - M24"].hide_render = False
			bpy.data.objects["MuzzleFlash - M40A1"].hide_render = False
			bpy.data.objects["MuzzleFlash - AMD65"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - SV98"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - SA24"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - MP41/44"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - M501"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - AWM"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - R93"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - M24"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - M40A1"].animation_data.action = bpy.data.actions.get(currentAction)

		for j in range(2,18):
			helpers.disablePropRenderlayer(j)

	elif renderSet == 9:
		bpy.data.objects["Weapon - Winchester 1895"].hide_render = False
		bpy.data.objects["Weapon - SR47"].hide_render = False
		bpy.data.objects["Weapon - SVU"].hide_render = False
		if currentAction in rifleActions:
			bpy.data.objects["MuzzleFlash - Winchester 1895"].hide_render = False
			bpy.data.objects["MuzzleFlash - SR47"].hide_render = False
			bpy.data.objects["MuzzleFlash - SVU"].hide_render = False
			bpy.data.objects["MuzzleFlash - Winchester 1895"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - SR47"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - SVU"].animation_data.action = bpy.data.actions.get(currentAction)

		for j in range(1,6):
			helpers.disablePropRenderlayer(j)
		for j in range(7,16):
			helpers.disablePropRenderlayer(j)
		for j in range(17,24):
			helpers.disablePropRenderlayer(j)
		for j in range(25,26):
			helpers.disablePropRenderlayer(j)

	elif renderSet == 10:
		bpy.data.objects["Weapon - Machete"].hide_render = False
		bpy.data.objects["Weapon - Machete"].animation_data.action = bpy.data.actions.get("DisplayProp")
		bpy.data.objects["Weapon - Machete 2"].hide_render = False
		bpy.data.objects["Weapon - Machete 2"].animation_data.action = bpy.data.actions.get("DisplayProp")
		bpy.data.objects["Weapon - Fighting Knife"].hide_render = False
		bpy.data.objects["Weapon - Fighting Knife"].animation_data.action = bpy.data.actions.get("DisplayProp")
		bpy.data.objects["Weapon - Katana"].hide_render = False
		bpy.data.objects["Weapon - Katana"].animation_data.action = bpy.data.actions.get("DisplayProp")
		bpy.data.objects["Weapon - Sabre"].hide_render = False
		bpy.data.objects["Weapon - Sabre"].animation_data.action = bpy.data.actions.get("DisplayProp")
		bpy.data.objects["Weapon - Rambo Knife"].hide_render = False
		bpy.data.objects["Weapon - Rambo Knife"].animation_data.action = bpy.data.actions.get("DisplayProp")
		bpy.data.objects["Weapon - Ka-Bar Cutlass"].hide_render = False
		bpy.data.objects["Weapon - Ka-Bar Cutlass"].animation_data.action = bpy.data.actions.get("DisplayProp")
		bpy.data.objects["Weapon - KCB Knife"].hide_render = False
		bpy.data.objects["Weapon - KCB Knife"].animation_data.action = bpy.data.actions.get("DisplayProp")
		bpy.data.objects["Weapon - Box Knife"].hide_render = False
		bpy.data.objects["Weapon - Box Knife"].animation_data.action = bpy.data.actions.get("DisplayProp")
		bpy.data.objects["Weapon - Umbrella"].hide_render = False
		bpy.data.objects["Weapon - Umbrella"].animation_data.action = bpy.data.actions.get("DisplayProp")
		bpy.data.objects["Weapon - Baton"].hide_render = False
		bpy.data.objects["Weapon - Baton"].animation_data.action = bpy.data.actions.get("DisplayProp")
		bpy.data.objects["Weapon - Nightstick"].hide_render = False
		bpy.data.objects["Weapon - Nightstick"].animation_data.action = bpy.data.actions.get("DisplayProp")
		bpy.data.objects["Weapon - Shovel"].hide_render = False
		bpy.data.objects["Weapon - Shovel"].animation_data.action = bpy.data.actions.get("DisplayProp")
		bpy.data.objects["Weapon - Stunner"].hide_render = False
		bpy.data.objects["Weapon - Stunner"].animation_data.action = bpy.data.actions.get("DisplayProp")
		bpy.data.objects["Weapon - Pipe Wrench"].hide_render = False
		bpy.data.objects["Weapon - Pipe Wrench"].animation_data.action = bpy.data.actions.get("DisplayProp")
		bpy.data.objects["Weapon - Fire Axe"].hide_render = False
		bpy.data.objects["Weapon - Fire Axe"].animation_data.action = bpy.data.actions.get("DisplayProp")
		if currentAction in knifeActions:
			bpy.data.objects["Weapon - Machete"].hide_render = False
			bpy.data.objects["Weapon - Machete"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - Machete 2"].hide_render = False
			bpy.data.objects["Weapon - Machete 2"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - Fighting Knife"].hide_render = False
			bpy.data.objects["Weapon - Fighting Knife"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - Katana"].hide_render = False
			bpy.data.objects["Weapon - Katana"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - Sabre"].hide_render = False
			bpy.data.objects["Weapon - Sabre"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - Rambo Knife"].hide_render = False
			bpy.data.objects["Weapon - Rambo Knife"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - Ka-Bar Cutlass"].hide_render = False
			bpy.data.objects["Weapon - Ka-Bar Cutlass"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - KCB Knife"].hide_render = False
			bpy.data.objects["Weapon - KCB Knife"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - Box Knife"].hide_render = False
			bpy.data.objects["Weapon - Box Knife"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - Umbrella"].hide_render = False
			bpy.data.objects["Weapon - Umbrella"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - Baton"].hide_render = False
			bpy.data.objects["Weapon - Baton"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - Nightstick"].hide_render = False
			bpy.data.objects["Weapon - Nightstick"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - Shovel"].hide_render = False
			bpy.data.objects["Weapon - Shovel"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - Stunner"].hide_render = False
			bpy.data.objects["Weapon - Stunner"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - Pipe Wrench"].hide_render = False
			bpy.data.objects["Weapon - Pipe Wrench"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - Fire Axe"].hide_render = False
			bpy.data.objects["Weapon - Fire Axe"].animation_data.action = bpy.data.actions.get(currentAction)
		if currentAction == "Crouch - Knife - Stab - Female" or currentAction == "Crouch - Knife - Stab":
			bpy.data.objects["Weapon - Machete"].hide_render = True
			bpy.data.objects["Weapon - Machete"].animation_data.action = bpy.data.actions.get("HideMuzzleFlash")
			bpy.data.objects["Weapon - Machete Alt hold"].hide_render = False
			bpy.data.objects["Weapon - Machete 2"].hide_render = True
			bpy.data.objects["Weapon - Machete 2"].animation_data.action = bpy.data.actions.get("HideMuzzleFlash")
			bpy.data.objects["Weapon - Machete 2 Alt hold"].hide_render = False
			bpy.data.objects["Weapon - Fighting Knife"].hide_render = True
			bpy.data.objects["Weapon - Fighting Knife"].animation_data.action = bpy.data.actions.get("HideMuzzleFlash")
			bpy.data.objects["Weapon - Fighting Knife Alt hold"].hide_render = False
			bpy.data.objects["Weapon - Katana"].hide_render = True
			bpy.data.objects["Weapon - Katana"].animation_data.action = bpy.data.actions.get("HideMuzzleFlash")
			bpy.data.objects["Weapon - Katana Alt hold"].hide_render = False
			bpy.data.objects["Weapon - Sabre"].hide_render = True
			bpy.data.objects["Weapon - Sabre"].animation_data.action = bpy.data.actions.get("HideMuzzleFlash")
			bpy.data.objects["Weapon - Sabre Alt hold"].hide_render = False
			bpy.data.objects["Weapon - Rambo Knife"].hide_render = True
			bpy.data.objects["Weapon - Rambo Knife"].animation_data.action = bpy.data.actions.get("HideMuzzleFlash")
			bpy.data.objects["Weapon - Rambo Knife Alt hold"].hide_render = False
			bpy.data.objects["Weapon - Ka-Bar Cutlass"].hide_render = True
			bpy.data.objects["Weapon - Ka-Bar Cutlass"].animation_data.action = bpy.data.actions.get("HideMuzzleFlash")
			bpy.data.objects["Weapon - Ka-Bar Cutlass Alt hold"].hide_render = False
			bpy.data.objects["Weapon - KCB Knife"].hide_render = True
			bpy.data.objects["Weapon - KCB Knife"].animation_data.action = bpy.data.actions.get("HideMuzzleFlash")
			bpy.data.objects["Weapon - KCB Knife Alt hold"].hide_render = False
			bpy.data.objects["Weapon - Box Knife"].hide_render = True
			bpy.data.objects["Weapon - Box Knife"].animation_data.action = bpy.data.actions.get("HideMuzzleFlash")
			bpy.data.objects["Weapon - Box Knife Alt hold"].hide_render = False
			bpy.data.objects["Weapon - Umbrella"].hide_render = True
			bpy.data.objects["Weapon - Umbrella"].animation_data.action = bpy.data.actions.get("HideMuzzleFlash")
			bpy.data.objects["Weapon - Umbrella Alt hold"].hide_render = False
		if currentAction == "Standing - Knife - Throw - Female" or currentAction == "Standing - Knife - Throw":
			bpy.data.objects["Weapon - Machete"].hide_render = False
			bpy.data.objects["Weapon - Machete Alt hold"].hide_render = True
			bpy.data.objects["Weapon - Machete"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - Machete 2"].hide_render = False
			bpy.data.objects["Weapon - Machete 2 Alt hold"].hide_render = True
			bpy.data.objects["Weapon - Machete 2"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - Fighting Knife"].hide_render = False
			bpy.data.objects["Weapon - Fighting Knife Alt hold"].hide_render = True
			bpy.data.objects["Weapon - Fighting Knife"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - Katana"].hide_render = False
			bpy.data.objects["Weapon - Katana Alt hold"].hide_render = True
			bpy.data.objects["Weapon - Katana"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - Sabre"].hide_render = False
			bpy.data.objects["Weapon - Sabre Alt hold"].hide_render = True
			bpy.data.objects["Weapon - Sabre"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - Rambo Knife"].hide_render = False
			bpy.data.objects["Weapon - Rambo Knife Alt hold"].hide_render = True
			bpy.data.objects["Weapon - Rambo Knife"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - Ka-Bar Cutlass"].hide_render = False
			bpy.data.objects["Weapon - Ka-Bar Cutlass Alt hold"].hide_render = True
			bpy.data.objects["Weapon - Ka-Bar Cutlass"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - KCB Knife"].hide_render = False
			bpy.data.objects["Weapon - KCB Knife Alt hold"].hide_render = True
			bpy.data.objects["Weapon - KCB Knife"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - Box Knife"].hide_render = False
			bpy.data.objects["Weapon - Box Knife Alt hold"].hide_render = True
			bpy.data.objects["Weapon - Box Knife"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["Weapon - Umbrella"].hide_render = False
			bpy.data.objects["Weapon - Umbrella Alt hold"].hide_render = True
			bpy.data.objects["Weapon - Umbrella"].animation_data.action = bpy.data.actions.get(currentAction)

		for j in range(1,10):
			helpers.disablePropRenderlayer(j)
		for j in range(17,26):
			helpers.disablePropRenderlayer(j)

	#Regular Male
	elif renderSet == 11:
		bpy.data.objects["Hat - Altyn"].hide_render = True
		bpy.data.objects["Hat - Ushanka"].hide_render = True
		bpy.data.objects["Hat - US Officer Cap"].hide_render = True
		bpy.data.objects["Hat - Soviet Officer Cap"].hide_render = True
		bpy.data.objects["Hat - Russian Cap"].hide_render = True
		bpy.data.objects["Hat - SWAT Helmet"].hide_render = True
		bpy.data.objects["Hat - Steel Helmet"].hide_render = True
		bpy.data.objects["Face - Goggles"].hide_render = True
		bpy.data.objects["Vest - Dyneema"].hide_render = True
		bpy.data.objects["Hat - Twaron Helmet"].hide_render = True
		bpy.data.objects["Hat - Dyneema Helmet"].hide_render = True
		bpy.data.objects["Hat - Spectra Helmet"].hide_render = True
		bpy.data.objects["Vest - Flak Vest"].hide_render = True
		bpy.data.objects["Vest - Twaron"].hide_render = True
		bpy.data.objects["Hat - Kevlar Helmet"].hide_render = True
		bpy.data.objects["Hat - Black Cap"].hide_render = True
		bpy.data.objects["Vest - Guardian"].hide_render = True
		bpy.data.objects["Backpack - Big Radio Set"].hide_render = True
		bpy.data.objects["Face - Extended Ear"].hide_render = True
		bpy.data.objects["Vest - SWAT Vest 2"].hide_render = False
		bpy.data.objects["Combat Pack - Combat Pack"].hide_render = True
		bpy.data.objects["Combat Pack - Medium Radio Set 2"].hide_render = True
		#bpy.data.objects["Combat Pack - Combat Pack 2"].hide_render = True
		#bpy.data.objects["Combat Pack - Combat Pack 3"].hide_render = True
		bpy.data.objects["Legs - SWAT Leggings"].hide_render = False

		for j in range(1,20):
			helpers.disablePropRenderlayer(j)
		for j in range(21,25):
			helpers.disablePropRenderlayer(j)

	#Big Male
	elif renderSet == 12:
		bpy.data.objects["Hat - Altyn"].hide_render = True
		bpy.data.objects["Hat - Ushanka"].hide_render = True
		bpy.data.objects["Hat - US Officer Cap - BGM"].hide_render = True
		bpy.data.objects["Hat - Soviet Officer Cap - BGM"].hide_render = True
		bpy.data.objects["Hat - Russian Cap"].hide_render = True
		bpy.data.objects["Hat - SWAT Helmet"].hide_render = True
		bpy.data.objects["Hat - Steel Helmet"].hide_render = True
		bpy.data.objects["Face - Goggles"].hide_render = True
		bpy.data.objects["Vest - Dyneema - BGM"].hide_render = True
		bpy.data.objects["Hat - Twaron Helmet"].hide_render = True
		bpy.data.objects["Hat - Dyneema Helmet"].hide_render = True
		bpy.data.objects["Hat - Spectra Helmet"].hide_render = True
		bpy.data.objects["Vest - Flak Vest - BGM"].hide_render = True
		bpy.data.objects["Vest - Twaron - BGM"].hide_render = True
		bpy.data.objects["Hat - Kevlar Helmet"].hide_render = True
		bpy.data.objects["Hat - Black Cap"].hide_render = True
		bpy.data.objects["Vest - Guardian - BGM"].hide_render = True
		bpy.data.objects["Backpack - Big Radio Set"].hide_render = True
		bpy.data.objects["Face - Extended Ear"].hide_render = True
		bpy.data.objects["Vest - SWAT Vest 2 - BGM"].hide_render = False
		bpy.data.objects["Combat Pack - Combat Pack"].hide_render = True
		bpy.data.objects["Combat Pack - Medium Radio Set 2"].hide_render = True
		#bpy.data.objects["Combat Pack - Combat Pack 2"].hide_render = True
		#bpy.data.objects["Combat Pack - Combat Pack 3"].hide_render = True
		bpy.data.objects["Legs - SWAT Leggings - BGM"].hide_render = False

		for j in range(1,20):
			helpers.disablePropRenderlayer(j)
		for j in range(21,25):
			helpers.disablePropRenderlayer(j)

	#Female
	elif renderSet == 13:
		bpy.data.objects["Hat - Altyn - Female"].hide_render = True
		bpy.data.objects["Hat - Ushanka - Female"].hide_render = True
		bpy.data.objects["Hat - US Officer Cap - Female"].hide_render = True
		bpy.data.objects["Hat - Soviet Officer Cap - Female"].hide_render = True
		bpy.data.objects["Hat - Russian Cap - Female"].hide_render = True
		bpy.data.objects["Hat - SWAT Helmet - Female"].hide_render = True
		bpy.data.objects["Hat - Steel Helmet - Female"].hide_render = True
		bpy.data.objects["Face - Goggles - Female"].hide_render = True
		bpy.data.objects["Vest - Dyneema - Female"].hide_render = True
		bpy.data.objects["Hat - Twaron Helmet"].hide_render = True
		bpy.data.objects["Hat - Dyneema Helmet - Female"].hide_render = True
		bpy.data.objects["Hat - Spectra Helmet - Female"].hide_render = True
		bpy.data.objects["Vest - Flak Vest - Female"].hide_render = True
		bpy.data.objects["Vest - Twaron - Female"].hide_render = True
		bpy.data.objects["Hat - Kevlar Helmet - Female"].hide_render = True
		bpy.data.objects["Hat - Black Cap - Female"].hide_render = True
		bpy.data.objects["Vest - Guardian - Female"].hide_render = True
		bpy.data.objects["Backpack - Big Radio Set"].hide_render = True
		bpy.data.objects["Face - Extended Ear - Female"].hide_render = True
		bpy.data.objects["Vest - SWAT Vest 2 - Female"].hide_render = False
		bpy.data.objects["Combat Pack - Combat Pack"].hide_render = True
		bpy.data.objects["Combat Pack - Medium Radio Set 2"].hide_render = True
		#bpy.data.objects["Combat Pack - Combat Pack 2"].hide_render = True
		#bpy.data.objects["Combat Pack - Combat Pack 3"].hide_render = True
		bpy.data.objects["Legs - SWAT Leggings - Female"].hide_render = False

		for j in range(1,20):
			helpers.disablePropRenderlayer(j)
		for j in range(21,25):
			helpers.disablePropRenderlayer(j)

	#Regular Male
	elif renderSet == 14:
		#bpy.data.objects["Legs - Spectra Armor Plates 2"].hide_render = True
		bpy.data.objects["Legs - Spectra Leggings 2"].hide_render = False
		#bpy.data.objects["Legs - Kevlar Armor Plates 2"].hide_render = False
		bpy.data.objects["Legs - Kevlar Leggings 2"].hide_render = False
		#bpy.data.objects["Legs - Twaron Armor Plates 2"].hide_render = False
		bpy.data.objects["Legs - Twaron Leggings 2"].hide_render = False
		#bpy.data.objects["Legs - Dyneema Armor Plates 2"].hide_render = False
		bpy.data.objects["Legs - Dyneema Leggings 2"].hide_render = False
		bpy.data.objects["Vest - Dress Uniform"].hide_render = True
		bpy.data.objects["Legs - Dress Uniform Pants"].hide_render = True
		bpy.data.objects["Vest - Zylon Vest"].hide_render = True
		bpy.data.objects["Legs - Zylon Pants"].hide_render = True
		bpy.data.objects["Vest - SWAT Vest 2"].hide_render = True
		bpy.data.objects["Legs - SWAT Leggings"].hide_render = True

		for j in range(5,26):
			helpers.disablePropRenderlayer(j)

	#Big Male
	elif renderSet == 15:
		#bpy.data.objects["Legs - Spectra Armor Plates 2 - BGM"].hide_render = True
		bpy.data.objects["Legs - Spectra Leggings 2 - BGM"].hide_render = False
		#bpy.data.objects["Legs - Kevlar Armor Plates 2 - BGM"].hide_render = False
		bpy.data.objects["Legs - Kevlar Leggings 2 - BGM"].hide_render = False
		#bpy.data.objects["Legs - Twaron Armor Plates 2 - BGM"].hide_render = False
		bpy.data.objects["Legs - Twaron Leggings 2 - BGM"].hide_render = False
		#bpy.data.objects["Legs - Dyneema Armor Plates 2 - BGM"].hide_render = False
		bpy.data.objects["Legs - Dyneema Leggings 2 - BGM"].hide_render = False
		bpy.data.objects["Vest - Dress Uniform - BGM"].hide_render = True
		bpy.data.objects["Legs - Dress Uniform Pants - BGM"].hide_render = True
		bpy.data.objects["Vest - Zylon Vest - BGM"].hide_render = True
		bpy.data.objects["Legs - Zylon Pants - BGM"].hide_render = True
		bpy.data.objects["Vest - SWAT Vest 2 - BGM"].hide_render = True
		bpy.data.objects["Legs - SWAT Leggings - BGM"].hide_render = True

		for j in range(5,26):
			helpers.disablePropRenderlayer(j)

	#Female
	elif renderSet == 16:
		#bpy.data.objects["Legs - Spectra Armor Plates 2 - Female"].hide_render = True
		bpy.data.objects["Legs - Spectra Leggings 2 - Female"].hide_render = False
		#bpy.data.objects["Legs - Kevlar Armor Plates 2 - Female"].hide_render = False
		bpy.data.objects["Legs - Kevlar Leggings 2 - Female"].hide_render = False
		#bpy.data.objects["Legs - Twaron Armor Plates 2 - Female"].hide_render = False
		bpy.data.objects["Legs - Twaron Leggings 2 - Female"].hide_render = False
		#bpy.data.objects["Legs - Dyneema Armor Plates 2 - Female"].hide_render = False
		bpy.data.objects["Legs - Dyneema Leggings 2 - Female"].hide_render = False
		bpy.data.objects["Vest - Dress Uniform - Female"].hide_render = True
		bpy.data.objects["Legs - Dress Uniform Pants - Female"].hide_render = True
		bpy.data.objects["Vest - Zylon Vest - Female"].hide_render = True
		bpy.data.objects["Legs - Zylon Pants - Female"].hide_render = True
		bpy.data.objects["Vest - SWAT Vest 2 - Female"].hide_render = True
		bpy.data.objects["Legs - SWAT Leggings - Female"].hide_render = True

		for j in range(5,26):
			helpers.disablePropRenderlayer(j)

	#Gear rework
	elif renderSet == 17:
		bpy.data.objects["Face - NVG 1"].hide_render = False
		bpy.data.objects["Face - NVG 3"].hide_render = False
		bpy.data.objects["Face - NVG 4"].hide_render = False

		for j in range(4,26):
			helpers.disablePropRenderlayer(j)

	elif renderSet == 18:
		bpy.data.objects["Weapon - M1911"].hide_render = False
		bpy.data.objects["Weapon - M1911 - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - VZ61 MP"].hide_render = False
		bpy.data.objects["Weapon - VZ61 MP - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Revolver"].hide_render = False
		bpy.data.objects["Weapon - Revolver - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Contender"].hide_render = False
		bpy.data.objects["Weapon - Contender - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Calico"].hide_render = False
		bpy.data.objects["Weapon - Calico - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - CMMG"].hide_render = False
		bpy.data.objects["Weapon - CMMG - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - OA93"].hide_render = False
		bpy.data.objects["Weapon - OA93 - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Shorty"].hide_render = False
		bpy.data.objects["Weapon - Shorty - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - MP7 MP"].hide_render = False
		bpy.data.objects["Weapon - MP7 MP - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Ingram M10 MP"].hide_render = False
		bpy.data.objects["Weapon - Ingram M10 MP - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - SR2 Veresk MP"].hide_render = False
		bpy.data.objects["Weapon - SR2 Veresk MP - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Micro Uzi MP"].hide_render = False
		bpy.data.objects["Weapon - Micro Uzi MP - Left Hand"].hide_render = False
		# Display muzzleflashes only in relevant animations
		if currentAction in dualPistolActions:
			leftMuzzleFlashAction = "Dual Pistols - Aim & Shoot - Left Muzzleflash"
			if currentAction == "Prone - Dual Pistol - Shoot":
				leftMuzzleFlashAction = "Prone - Dual Pistol - Shoot - Left Muzzleflash"
			bpy.data.objects["MuzzleFlash - M1911"].hide_render = False
			bpy.data.objects["MuzzleFlash - M1911 - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - VZ61 MP"].hide_render = False
			bpy.data.objects["MuzzleFlash - VZ61 MP - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Revolver"].hide_render = False
			bpy.data.objects["MuzzleFlash - Revolver - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Contender"].hide_render = False
			bpy.data.objects["MuzzleFlash - Contender - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Calico"].hide_render = False
			bpy.data.objects["MuzzleFlash - Calico - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - CMMG"].hide_render = False
			bpy.data.objects["MuzzleFlash - CMMG - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - OA93"].hide_render = False
			bpy.data.objects["MuzzleFlash - OA93 - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Shorty"].hide_render = False
			bpy.data.objects["MuzzleFlash - Shorty - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - MP7 MP"].hide_render = False
			bpy.data.objects["MuzzleFlash - MP7 MP - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Ingram M10 MP"].hide_render = False
			bpy.data.objects["MuzzleFlash - Ingram M10 MP - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - SR2 Veresk MP"].hide_render = False
			bpy.data.objects["MuzzleFlash - SR2 Veresk MP - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Micro Uzi MP"].hide_render = False
			bpy.data.objects["MuzzleFlash - Micro Uzi MP - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - M1911"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - M1911 - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - VZ61 MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - VZ61 MP - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Revolver"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Revolver - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Contender"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Contender - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Calico"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Calico - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - CMMG"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - CMMG - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - OA93"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - OA93 - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Shorty"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Shorty - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - MP7 MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - MP7 MP - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Ingram M10 MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Ingram M10 MP - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - SR2 Veresk MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - SR2 Veresk MP - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Micro Uzi MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Micro Uzi MP - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
		if currentAction in pistolActions:
			bpy.data.objects["MuzzleFlash - M1911"].hide_render = False
			bpy.data.objects["MuzzleFlash - M1911"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - VZ61 MP"].hide_render = False
			bpy.data.objects["MuzzleFlash - VZ61 MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Revolver"].hide_render = False
			bpy.data.objects["MuzzleFlash - Revolver"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Contender"].hide_render = False
			bpy.data.objects["MuzzleFlash - Contender"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Calico"].hide_render = False
			bpy.data.objects["MuzzleFlash - Calico"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - CMMG"].hide_render = False
			bpy.data.objects["MuzzleFlash - CMMG"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - OA93"].hide_render = False
			bpy.data.objects["MuzzleFlash - OA93"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Shorty"].hide_render = False
			bpy.data.objects["MuzzleFlash - Shorty"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - MP7 MP"].hide_render = False
			bpy.data.objects["MuzzleFlash - MP7 MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Ingram M10 MP"].hide_render = False
			bpy.data.objects["MuzzleFlash - Ingram M10 MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - SR2 Veresk MP"].hide_render = False
			bpy.data.objects["MuzzleFlash - SR2 Veresk MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Micro Uzi MP"].hide_render = False
			bpy.data.objects["MuzzleFlash - Micro Uzi MP"].animation_data.action = bpy.data.actions.get(currentAction)

		for j in range(25,26):
			helpers.disablePropRenderlayer(j)

	elif renderSet == 19:
		bpy.data.objects["Weapon - Agram 2000 MP"].hide_render = False
		bpy.data.objects["Weapon - Agram 2000 MP - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Mini SAF MP"].hide_render = False
		bpy.data.objects["Weapon - Mini SAF MP - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - AEK919K MP"].hide_render = True
		bpy.data.objects["Weapon - AEK919K MP - Left Hand"].hide_render = True
		bpy.data.objects["Weapon - Stechkin MP"].hide_render = False
		bpy.data.objects["Weapon - Stechkin MP - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - PP93 MP"].hide_render = True
		bpy.data.objects["Weapon - PP93 MP - Left Hand"].hide_render = True
		bpy.data.objects["Weapon - TMP MP"].hide_render = True
		bpy.data.objects["Weapon - TMP MP - Left Hand"].hide_render = True
		bpy.data.objects["Weapon - Automag V"].hide_render = True
		bpy.data.objects["Weapon - Automag V - Left Hand"].hide_render = True
		bpy.data.objects["Weapon - Makarov"].hide_render = False
		bpy.data.objects["Weapon - Makarov - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Mini Uzi MP"].hide_render = False
		bpy.data.objects["Weapon - Mini Uzi MP - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - 93R"].hide_render = False
		bpy.data.objects["Weapon - 93R - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Wildey"].hide_render = False
		bpy.data.objects["Weapon - Wildey - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Mk23"].hide_render = False
		bpy.data.objects["Weapon - Mk23 - Left Hand"].hide_render = False
		# Display muzzleflashes only in relevant animations
		if currentAction in dualPistolActions:
			leftMuzzleFlashAction = "Dual Pistols - Aim & Shoot - Left Muzzleflash"
			if currentAction == "Prone - Dual Pistol - Shoot":
				leftMuzzleFlashAction = "Prone - Dual Pistol - Shoot - Left Muzzleflash"
			bpy.data.objects["MuzzleFlash - Agram 2000 MP"].hide_render = False
			bpy.data.objects["MuzzleFlash - Agram 2000 MP - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Mini SAF MP"].hide_render = False
			bpy.data.objects["MuzzleFlash - Mini SAF MP - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - AEK919K MP"].hide_render = True
			bpy.data.objects["MuzzleFlash - AEK919K MP - Left Hand"].hide_render = True
			bpy.data.objects["MuzzleFlash - Stechkin MP"].hide_render = False
			bpy.data.objects["MuzzleFlash - Stechkin MP - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - PP93 MP"].hide_render = True
			bpy.data.objects["MuzzleFlash - PP93 MP - Left Hand"].hide_render = True
			bpy.data.objects["MuzzleFlash - TMP MP"].hide_render = True
			bpy.data.objects["MuzzleFlash - TMP MP - Left Hand"].hide_render = True
			bpy.data.objects["MuzzleFlash - Automag V"].hide_render = True
			bpy.data.objects["MuzzleFlash - Automag V - Left Hand"].hide_render = True
			bpy.data.objects["MuzzleFlash - Makarov"].hide_render = False
			bpy.data.objects["MuzzleFlash - Makarov - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Mini Uzi MP"].hide_render = False
			bpy.data.objects["MuzzleFlash - Mini Uzi MP - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - 93R"].hide_render = False
			bpy.data.objects["MuzzleFlash - 93R - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Wildey"].hide_render = False
			bpy.data.objects["MuzzleFlash - Wildey - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Mk23"].hide_render = False
			bpy.data.objects["MuzzleFlash - Mk23 - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Agram 2000 MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Agram 2000 MP - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Mini SAF MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Mini SAF MP - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - AEK919K MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - AEK919K MP - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Stechkin MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Stechkin MP - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - PP93 MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - PP93 MP - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - TMP MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - TMP MP - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Automag V"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Automag V - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Makarov"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Makarov - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Mini Uzi MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Mini Uzi MP - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - 93R"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - 93R - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Wildey"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Wildey - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Mk23"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Mk23 - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
		if currentAction in pistolActions:
			bpy.data.objects["MuzzleFlash - Agram 2000 MP"].hide_render = False
			bpy.data.objects["MuzzleFlash - Agram 2000 MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Mini SAF MP"].hide_render = False
			bpy.data.objects["MuzzleFlash - Mini SAF MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - AEK919K MP"].hide_render = True
			bpy.data.objects["MuzzleFlash - AEK919K MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Stechkin MP"].hide_render = False
			bpy.data.objects["MuzzleFlash - Stechkin MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - PP93 MP"].hide_render = True
			bpy.data.objects["MuzzleFlash - PP93 MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - TMP MP"].hide_render = True
			bpy.data.objects["MuzzleFlash - TMP MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Automag V"].hide_render = True
			bpy.data.objects["MuzzleFlash - Automag V"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Makarov"].hide_render = False
			bpy.data.objects["MuzzleFlash - Makarov"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Mini Uzi MP"].hide_render = False
			bpy.data.objects["MuzzleFlash - Mini Uzi MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - 93R"].hide_render = False
			bpy.data.objects["MuzzleFlash - 93R"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Wildey"].hide_render = False
			bpy.data.objects["MuzzleFlash - Wildey"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Mk23"].hide_render = False
			bpy.data.objects["MuzzleFlash - Mk23"].animation_data.action = bpy.data.actions.get(currentAction)

		for j in range(5,7):
			helpers.disablePropRenderlayer(j)
		for j in range(9,15):
			helpers.disablePropRenderlayer(j)
		for j in range(25,26):
			helpers.disablePropRenderlayer(j)

	elif renderSet == 20:
		bpy.data.objects["Weapon - VZ82 MP"].hide_render = False
		bpy.data.objects["Weapon - VZ82 MP - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Hi-Power"].hide_render = False
		bpy.data.objects["Weapon - Hi-Power - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - 38 Special"].hide_render = False
		bpy.data.objects["Weapon - 38 Special - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - P226 Light"].hide_render = False
		bpy.data.objects["Weapon - P226 Light - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Luger"].hide_render = False
		bpy.data.objects["Weapon - Luger - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - M29"].hide_render = False
		bpy.data.objects["Weapon - M29 - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Python"].hide_render = False
		bpy.data.objects["Weapon - Python - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - G11 PDW"].hide_render = False
		bpy.data.objects["Weapon - G11 PDW - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - FiveSeven"].hide_render = False
		bpy.data.objects["Weapon - FiveSeven - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Dart Gun"].hide_render = False
		bpy.data.objects["Weapon - Dart Gun - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - P226 SAS"].hide_render = False
		bpy.data.objects["Weapon - P226 SAS - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - M1911 High Cap"].hide_render = False
		bpy.data.objects["Weapon - M1911 High Cap - Left Hand"].hide_render = False
		# Display muzzleflashes only in relevant animations
		if currentAction in dualPistolActions:
			leftMuzzleFlashAction = "Dual Pistols - Aim & Shoot - Left Muzzleflash"
			if currentAction == "Prone - Dual Pistol - Shoot":
				leftMuzzleFlashAction = "Prone - Dual Pistol - Shoot - Left Muzzleflash"
			bpy.data.objects["MuzzleFlash - VZ82 MP"].hide_render = False
			bpy.data.objects["MuzzleFlash - VZ82 MP - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Hi-Power"].hide_render = False
			bpy.data.objects["MuzzleFlash - Hi-Power - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - 38 Special"].hide_render = False
			bpy.data.objects["MuzzleFlash - 38 Special - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - P226 Light"].hide_render = False
			bpy.data.objects["MuzzleFlash - P226 Light - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Luger"].hide_render = False
			bpy.data.objects["MuzzleFlash - Luger - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - M29"].hide_render = False
			bpy.data.objects["MuzzleFlash - M29 - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Python"].hide_render = False
			bpy.data.objects["MuzzleFlash - Python - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - G11 PDW"].hide_render = False
			bpy.data.objects["MuzzleFlash - G11 PDW - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - FiveSeven"].hide_render = False
			bpy.data.objects["MuzzleFlash - FiveSeven - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - P226 SAS"].hide_render = False
			bpy.data.objects["MuzzleFlash - P226 SAS - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - M1911 High Cap"].hide_render = False
			bpy.data.objects["MuzzleFlash - M1911 High Cap - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - VZ82 MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - VZ82 MP - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Hi-Power"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Hi-Power - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - 38 Special"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - 38 Special - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - P226 Light"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - P226 Light - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Luger"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Luger - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - M29"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - M29 - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Python"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Python - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - G11 PDW"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - G11 PDW - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - FiveSeven"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - FiveSeven - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - P226 SAS"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - P226 SAS - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - M1911 High Cap"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - M1911 High Cap - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
		if currentAction in pistolActions:
			bpy.data.objects["MuzzleFlash - VZ82 MP"].hide_render = False
			bpy.data.objects["MuzzleFlash - VZ82 MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Hi-Power"].hide_render = False
			bpy.data.objects["MuzzleFlash - Hi-Power"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - 38 Special"].hide_render = False
			bpy.data.objects["MuzzleFlash - 38 Special"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - P226 Light"].hide_render = False
			bpy.data.objects["MuzzleFlash - P226 Light"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Luger"].hide_render = False
			bpy.data.objects["MuzzleFlash - Luger"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - M29"].hide_render = False
			bpy.data.objects["MuzzleFlash - M29"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Python"].hide_render = False
			bpy.data.objects["MuzzleFlash - Python"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - G11 PDW"].hide_render = False
			bpy.data.objects["MuzzleFlash - G11 PDW"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - FiveSeven"].hide_render = False
			bpy.data.objects["MuzzleFlash - FiveSeven"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - P226 SAS"].hide_render = False
			bpy.data.objects["MuzzleFlash - P226 SAS"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - M1911 High Cap"].hide_render = False
			bpy.data.objects["MuzzleFlash - M1911 High Cap"].animation_data.action = bpy.data.actions.get(currentAction)

		for j in range(25,26):
			helpers.disablePropRenderlayer(j)

	elif renderSet == 21:
		bpy.data.objects["Weapon - Automag III"].hide_render = False
		bpy.data.objects["Weapon - Automag III - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Tokarev"].hide_render = False
		bpy.data.objects["Weapon - Tokarev - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - M29 SATAN"].hide_render = False
		bpy.data.objects["Weapon - M29 SATAN - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Anaconda"].hide_render = False
		bpy.data.objects["Weapon - Anaconda - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - MR96"].hide_render = False
		bpy.data.objects["Weapon - MR96 - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - P226"].hide_render = False
		bpy.data.objects["Weapon - P226 - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Desert Eagle 44"].hide_render = False
		bpy.data.objects["Weapon - Desert Eagle 44 - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Desert Eagle 357"].hide_render = False
		bpy.data.objects["Weapon - Desert Eagle 357 - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Gyurza"].hide_render = False
		bpy.data.objects["Weapon - Gyurza - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Ruger SR9"].hide_render = False
		bpy.data.objects["Weapon - Ruger SR9 - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Beretta M9"].hide_render = False
		bpy.data.objects["Weapon - Beretta M9 - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - EMF Hartford"].hide_render = False
		bpy.data.objects["Weapon - EMF Hartford - Left Hand"].hide_render = False
		# Display muzzleflashes only in relevant animations
		if currentAction in dualPistolActions:
			leftMuzzleFlashAction = "Dual Pistols - Aim & Shoot - Left Muzzleflash"
			if currentAction == "Prone - Dual Pistol - Shoot":
				leftMuzzleFlashAction = "Prone - Dual Pistol - Shoot - Left Muzzleflash"
			bpy.data.objects["MuzzleFlash - Automag III"].hide_render = False
			bpy.data.objects["MuzzleFlash - Automag III - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Tokarev"].hide_render = False
			bpy.data.objects["MuzzleFlash - Tokarev - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - M29 SATAN"].hide_render = False
			bpy.data.objects["MuzzleFlash - M29 SATAN - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Anaconda"].hide_render = False
			bpy.data.objects["MuzzleFlash - Anaconda - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - MR96"].hide_render = False
			bpy.data.objects["MuzzleFlash - MR96 - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - P226"].hide_render = False
			bpy.data.objects["MuzzleFlash - P226 - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Desert Eagle 44"].hide_render = False
			bpy.data.objects["MuzzleFlash - Desert Eagle 44 - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Desert Eagle 357"].hide_render = False
			bpy.data.objects["MuzzleFlash - Desert Eagle 357 - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Gyurza"].hide_render = False
			bpy.data.objects["MuzzleFlash - Gyurza - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Ruger SR9"].hide_render = False
			bpy.data.objects["MuzzleFlash - Ruger SR9 - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Beretta M9"].hide_render = False
			bpy.data.objects["MuzzleFlash - Beretta M9 - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - EMF Hartford"].hide_render = False
			bpy.data.objects["MuzzleFlash - EMF Hartford - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Automag III"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Automag III - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Tokarev"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Tokarev - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - M29 SATAN"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - M29 SATAN - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Anaconda"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Anaconda - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - MR96"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - MR96 - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - P226"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - P226 - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Desert Eagle 44"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Desert Eagle 44 - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Desert Eagle 357"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Desert Eagle 357 - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Gyurza"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Gyurza - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Ruger SR9"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Ruger SR9 - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Beretta M9"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Beretta M9 - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - EMF Hartford"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - EMF Hartford - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
		if currentAction in pistolActions:
			bpy.data.objects["MuzzleFlash - Automag III"].hide_render = False
			bpy.data.objects["MuzzleFlash - Automag III"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Tokarev"].hide_render = False
			bpy.data.objects["MuzzleFlash - Tokarev"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - M29 SATAN"].hide_render = False
			bpy.data.objects["MuzzleFlash - M29 SATAN"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Anaconda"].hide_render = False
			bpy.data.objects["MuzzleFlash - Anaconda"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - MR96"].hide_render = False
			bpy.data.objects["MuzzleFlash - MR96"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - P226"].hide_render = False
			bpy.data.objects["MuzzleFlash - P226"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Desert Eagle 44"].hide_render = False
			bpy.data.objects["MuzzleFlash - Desert Eagle 44"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Desert Eagle 357"].hide_render = False
			bpy.data.objects["MuzzleFlash - Desert Eagle 357"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Gyurza"].hide_render = False
			bpy.data.objects["MuzzleFlash - Gyurza"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Ruger SR9"].hide_render = False
			bpy.data.objects["MuzzleFlash - Ruger SR9"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Beretta M9"].hide_render = False
			bpy.data.objects["MuzzleFlash - Beretta M9"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - EMF Hartford"].hide_render = False
			bpy.data.objects["MuzzleFlash - EMF Hartford"].animation_data.action = bpy.data.actions.get(currentAction)

		for j in range(25,26):
			helpers.disablePropRenderlayer(j)

	elif renderSet == 22:
		bpy.data.objects["Weapon - M83 Premier Grade"].hide_render = False
		bpy.data.objects["Weapon - M83 Premier Grade - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Redhawk"].hide_render = False
		bpy.data.objects["Weapon - Redhawk - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Super Redhawk Alaskan"].hide_render = False
		bpy.data.objects["Weapon - Super Redhawk Alaskan - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Delta Elite"].hide_render = False
		bpy.data.objects["Weapon - Delta Elite - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Kimber Eclipse"].hide_render = False
		bpy.data.objects["Weapon - Kimber Eclipse - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - LAR Grizzly"].hide_render = False
		bpy.data.objects["Weapon - LAR Grizzly - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - P7M8"].hide_render = False
		bpy.data.objects["Weapon - P7M8 - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - AK Pistol"].hide_render = False
		bpy.data.objects["Weapon - AK Pistol - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Pepper Spray"].hide_render = False
		bpy.data.objects["Weapon - Pepper Spray - Left Hand"].hide_render = False
		bpy.data.objects["Weapon - Jatimatic MP"].hide_render = True
		bpy.data.objects["Weapon - Jatimatic MP - Left Hand"].hide_render = True
		# Display muzzleflashes only in relevant animations
		if currentAction in dualPistolActions:
			leftMuzzleFlashAction = "Dual Pistols - Aim & Shoot - Left Muzzleflash"
			if currentAction == "Prone - Dual Pistol - Shoot":
				leftMuzzleFlashAction = "Prone - Dual Pistol - Shoot - Left Muzzleflash"
			bpy.data.objects["MuzzleFlash - M83 Premier Grade"].hide_render = False
			bpy.data.objects["MuzzleFlash - M83 Premier Grade - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Redhawk"].hide_render = False
			bpy.data.objects["MuzzleFlash - Redhawk - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Super Redhawk Alaskan"].hide_render = False
			bpy.data.objects["MuzzleFlash - Super Redhawk Alaskan - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Delta Elite"].hide_render = False
			bpy.data.objects["MuzzleFlash - Delta Elite - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Kimber Eclipse"].hide_render = False
			bpy.data.objects["MuzzleFlash - Kimber Eclipse - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - LAR Grizzly"].hide_render = False
			bpy.data.objects["MuzzleFlash - LAR Grizzly - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - P7M8"].hide_render = False
			bpy.data.objects["MuzzleFlash - P7M8 - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - AK Pistol"].hide_render = False
			bpy.data.objects["MuzzleFlash - AK Pistol - Left Hand"].hide_render = False
			bpy.data.objects["MuzzleFlash - Jatimatic MP"].hide_render = True
			bpy.data.objects["MuzzleFlash - Jatimatic MP - Left Hand"].hide_render = True
			bpy.data.objects["MuzzleFlash - M83 Premier Grade"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - M83 Premier Grade - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Redhawk"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Redhawk - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Super Redhawk Alaskan"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Super Redhawk Alaskan - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Delta Elite"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Delta Elite - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Kimber Eclipse"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Kimber Eclipse - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - LAR Grizzly"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - LAR Grizzly - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - P7M8"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - P7M8 - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - AK Pistol"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - AK Pistol - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
			bpy.data.objects["MuzzleFlash - Jatimatic MP"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Jatimatic MP - Left Hand"].animation_data.action = bpy.data.actions.get(leftMuzzleFlashAction)
		if currentAction in pistolActions:
			bpy.data.objects["MuzzleFlash - M83 Premier Grade"].hide_render = False
			bpy.data.objects["MuzzleFlash - M83 Premier Grade"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Redhawk"].hide_render = False
			bpy.data.objects["MuzzleFlash - Redhawk"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Super Redhawk Alaskan"].hide_render = False
			bpy.data.objects["MuzzleFlash - Super Redhawk Alaskan"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Delta Elite"].hide_render = False
			bpy.data.objects["MuzzleFlash - Delta Elite"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Kimber Eclipse"].hide_render = False
			bpy.data.objects["MuzzleFlash - Kimber Eclipse"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - LAR Grizzly"].hide_render = False
			bpy.data.objects["MuzzleFlash - LAR Grizzly"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - P7M8"].hide_render = False
			bpy.data.objects["MuzzleFlash - P7M8"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - AK Pistol"].hide_render = False
			bpy.data.objects["MuzzleFlash - AK Pistol"].animation_data.action = bpy.data.actions.get(currentAction)
			bpy.data.objects["MuzzleFlash - Jatimatic MP"].hide_render = True
			bpy.data.objects["MuzzleFlash - Jatimatic MP"].animation_data.action = bpy.data.actions.get(currentAction)

		for j in range(19,26):
			helpers.disablePropRenderlayer(j)

	elif renderSet == 23:
		bpy.data.objects["Weapon - Shotgun"].hide_render = False
		bpy.data.objects["Weapon - SPAS12"].hide_render = False

		for j in range(1,15):
			helpers.disablePropRenderlayer(j)
		for j in range(16,17):
			helpers.disablePropRenderlayer(j)
		for j in range(18,26):
			helpers.disablePropRenderlayer(j)

	# RENDER AWAYYY!
	bpy.ops.render.render(animation=True)