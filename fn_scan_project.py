import os

# Scans an Ableton project folder and builds a list of all samples saved in the folder
#
# @param project_path The path of the Ableton Project folder
# @return A list of all samples in the Ableton folder
#
def fn_scan_project (project_path):
	li_samples_used = [] # for building list of all samples in the Ableton project
	imported = os.path.join(project_path, "Samples/Imported")
	processed_cons = os.path.join(project_path, "Samples/Processed/Consolidate")
	processed_rev = os.path.join(project_path, "Samples/Processed/Reverse")
	consolidated = os.path.join(project_path, "Samples/Consolidated")
	recorded = os.path.join(project_path, "Samples/Recorded")

	if os.path.isdir(imported):
		folder_contents = os.listdir(imported)
		for item in folder_contents:
			if item.endswith((".mp3", ".wav", ".aif", ".aiff", ".flac", ".ogg")):
				item_full_path = os.path.join(imported, item)
				li_samples_used.append(item_full_path)
	if os.path.isdir(processed_cons):
		folder_contents = os.listdir(processed_cons)
		for item in folder_contents:
			if item.endswith((".mp3", ".wav", ".aif", ".aiff", ".flac", ".ogg")):
				item_full_path = os.path.join(processed_cons, item)
				li_samples_used.append(item_full_path)
	if os.path.isdir(processed_rev):
		folder_contents = os.listdir(processed_rev)
		for item in folder_contents:
			if item.endswith((".mp3", ".wav", ".aif", ".aiff", ".flac", ".ogg")):
				item_full_path = os.path.join(processed_rev, item)
				li_samples_used.append(item_full_path)
	return li_samples_used