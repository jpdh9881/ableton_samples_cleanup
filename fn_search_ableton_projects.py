import os
from fn_is_ableton_project import fn_is_ableton_project
from fn_scan_project import fn_scan_project

# Searches a folder and all sub folders for Ableton projects. If an Ableton project is found,
#	call fn_scan_project to build a list of samples within that project and add this list to
#	master list
#
# @param folder The folder to be searched
#
# @return li_samples_used List of samples (and their paths) found within the Ableton projects
# 							within the folder
def fn_search_ableton_projects (folder):
	li_samples_used = []
	folder_contents = os.listdir(folder)

	for item in folder_contents:
		item_full_path = os.path.join(folder, item)

		if os.path.isdir(item_full_path): # item is a folder (i.e. not a file)
			if fn_is_ableton_project (item_full_path): # folder is an Ableton project
				li_samples_used.extend(fn_scan_project (item_full_path)) # add samples within that project to master list
			else: # folder is not an Ableton project: recursively search it for Ableton projects
				li_samples_used.extend(fn_search_ableton_projects(item_full_path))
	return li_samples_used