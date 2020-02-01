import os
from fn_is_ableton_project import fn_is_ableton_project

#   	Primary function
def fn_search_for_all_samples (folder, li_music_folder_contents):
	folder_contents_fn = os.listdir(folder)
	for item in folder_contents_fn:
		item_full_path = os.path.join(folder, item)
		if os.path.isdir(item_full_path):
			if fn_is_ableton_project (item_full_path):
				pass
			else:
				fn_search_for_all_samples (item_full_path, li_music_folder_contents)
		elif os.path.isfile(item_full_path):
			if item_full_path.endswith((".mp3", ".wav", ".aif", ".aiff", ".flac", ".ogg")):
				li_music_folder_contents.append(item_full_path)
		else:
			print("Problem in Step 1: " + os.path.abspath(item_full_path))
	li_music_folder_contents.sort()
	return li_music_folder_contents