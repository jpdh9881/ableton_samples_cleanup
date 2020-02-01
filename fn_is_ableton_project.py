import os

# Verifies whether a folder is an Ableton Project folder
#
# @param folder	The folder that is being tested
# @return is_project Whether the folder is an Ableton project or not
# 						(True if yes, False if no)
#
def fn_is_ableton_project (folder):
	folder_contents = os.listdir(folder)
	is_project = False # assume its not an Ableton project

	for item in folder_contents:
		item_full_path = os.path.join(folder, item)
		if item_full_path.endswith(".als"):
			is_project True
	
	return is_project