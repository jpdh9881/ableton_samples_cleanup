import os
from shutil import copy2

# Moves files from one folder to another if the file is in a list
#	This function changes _only_ the sample's "changing" directory (represented by old_folder),
#	meaning that the subdirectory structure will be retained
#	e.g. 	Old location: /di/rectory/structure/old_folder/guitar/nylon/file.wav
#			New location: /di/rectory/structure/new_folder/guitar/nylon/file.wav
#
# @param old_folder The folder from where files will be moved
# @param new_folder The folder to where files will be moved
# @param li_samples_to_move List of files to be moved from old folder to new folder
#
# @return NONE
def fn_move_sample_files (old_folder, new_folder, li_samples_to_move):

	if not old_folder.endswith("/"):
		old_folder = old_folder + "/"

	if not new_folder.endswith("/"):
		new_folder = new_folder + "/"

	for item in li_samples_to_move:
		new_file_path = item.replace(old_folder, new_folder)
		print("Moved:\t" + item)
		print("   to:\t" + new_file_path)

		os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
		os.rename(item.rstrip(), new_file_path.rstrip())

	print("----")
	print("Done")
	print("----")

# Copies files from one folder to another if the file is in a list
#	This function changes _only_ the sample's "changing" directory (represented by old_folder),
#	meaning that the subdirectory structure will be retained
#	e.g. 	Old location: /di/rectory/structure/old_folder/guitar/nylon/file.wav
#			New location: /di/rectory/structure/new_folder/guitar/nylon/file.wav
#
# @param old_folder The folder from where files will be copied
# @param new_folder The folder to where files will be copied
# @param li_samples_to_move List of files to be copied from old folder to new folder
#
# @return NONE
def fn_copy_sample_files (old_folder, new_folder, li_samples_to_move):

	if not old_folder.endswith("/"):
		old_folder = old_folder + "/"

	if not new_folder.endswith("/"):
		new_folder = new_folder + "/"

	for item in li_samples_to_move:
		new_file_path = item.replace(old_folder, new_folder)
		new_directory = os.path.split(new_file_path)[0]
		print("Copied:\t" + item)
		print("    to:\t" + new_directory + "/")

		os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
		copy2(item.rstrip(), new_file_path)

	print("----")
	print("Done")
	print("----")