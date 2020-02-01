import os
from fn_is_ableton_project import fn_is_ableton_project

#	Scan folder and subfolders for Ableton Projects; do things to those projects
def fn_search_ableton_projects (folder, li_samples_used):
	folder_contents = os.listdir(folder)

	for item in folder_contents:
		item_full_path = os.path.join(folder, item)

		if os.path.isdir(item_full_path):
			if fn_is_ableton_project (item_full_path):
				fn_scan_project (item_full_path, li_samples_used)
			else:
				fn_search_ableton_projects(item_full_path, li_samples_used)
	return li_samples_used