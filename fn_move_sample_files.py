import os


# Moves files from one folder to another if the file is in a list
#
# @param old_folder The folder from where files will be moved
# @param new_folder The folder to where files will be moved
# @param li_samples_to_move List of files to be moved from old folder to new folder
#
def fn_move_sample_files (old_folder, new_folder, li_samples_to_move):
	old_folder = tkEN_samples_folder.get()
	new_folder = tkEN_new_folder.get()

	if not old_folder.endswith("/"):
		old_folder = old_folder + "/"

	if not new_folder.endswith("/"):
		new_folder = new_folder + "/"

	for item in li_samples_to_move:
		new_file_path = item.replace(old_folder, new_folder)
		print(new_file_path)
		print(item)

		os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
		os.rename(item.rstrip(), new_file_path.rstrip())

	print("Done")