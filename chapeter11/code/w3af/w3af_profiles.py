from w3af.core.controlles.w3afCore import w3afCore

w3af = w3afCore()

#list of profiles
profiles = w3af.profiles.get_profile_list()
for profile in profiles:
	print('Profile desc:'+profile.get_desc())
	print('Profile file:'+profile.get_profile_file())
	print('Profile name:'+profile.get_name())
	print('Profile target:'+profile.get_target().get("target"))
	
w3af.profiles.use_profile('profileName')
w3af.profiles.save_current_to_new_profile('profileName','Profile description')
	
