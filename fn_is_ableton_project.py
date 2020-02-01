import os

# DESCRIPTION
def fn_is_ableton_project (folder):
	folder_contents = os.listdir(folder)

	for item in folder_contents:
		item_full_path = os.path.join(folder, item)
		if item_full_path.endswith(".als"):
			return True