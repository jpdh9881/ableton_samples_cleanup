import os
from fn_is_ableton_project import fn_is_ableton_project

# Creates a master list of all samples in a folder and its subfolders
# 	-the program assumes that the folder being searched is a user's "master samples folder"
# 		where they've stored all their saved samples
#	-if an Ableton project folder is encountered, it assumes that this project folder has
#		been put here so that any samples it contains are to be treated as samples to be
#		used in other projects; therefore, its samples are added to the master list of
#		samples
# 
# @param folder The folder to be searched for subfolders and samples
#
# @return li_music_folder_contents List of samples and their paths
#
def fn_search_for_all_samples (folder):
	li_music_folder_contents = []
	folder_contents_fn = os.listdir(folder)

	for item in folder_contents_fn:
		item_full_path = os.path.join(folder, item)
		if os.path.isdir(item_full_path):
			if fn_is_ableton_project (item_full_path):
				pass
			else:
				li_music_folder_contents.extend(fn_search_for_all_samples (item_full_path))
		elif os.path.isfile(item_full_path):
			if item_full_path.endswith((".mp3", ".wav", ".aif", ".aiff", ".flac", ".ogg")):
				li_music_folder_contents.append(item_full_path)
		else:
			print("Problem: " + os.path.abspath(item_full_path))
	li_music_folder_contents.sort()
	return li_music_folder_contents