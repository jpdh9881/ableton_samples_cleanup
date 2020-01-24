# Written March to August 2018
# Python modules
import os
from tkinter import *
from tkinter import ttk

# *** Configure GUI
root = Tk()
root.title("Sample Folder Cleanup")
#	set window attributes
root.resizable(False, False)
window_width = 1000;
window_height = 700;
root.geometry(str(window_width) + "x" + str(window_height))
root.configure(background="#F3E5AB")

# FUNCTIONS
# 	A) BUILD LIST OF ALL SAMPLES IN SAMPLES FOLDER
#
def fn_is_ableton_project (folder):
	folder_contents = os.listdir(folder)

	for item in folder_contents:
		item_full_path = os.path.join(folder, item)
		if item_full_path.endswith(".als"):
			return True
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
#		container for primary function
def fn_search_for_all_samples_cont ():
	folder = tkEN_samples_folder.get()
	li_music_folder_contents = [];
	call_function = fn_search_for_all_samples (folder, li_music_folder_contents)
	print("--------------")
	return call_function

#	(C) BUILD A LIST OF ALL SAMPLES USED IN THE PROJECTS FOLDER
# 		Scan a _known_ project for samples used
def fn_scan_project (project_path, li_samples_used):
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
#		container for primary function
def fn_search_ableton_projects_cont ():
	folder = tkEN_projects_folder.get()
	li_samples_used = [];

	call_function = fn_search_ableton_projects (folder, li_samples_used)

	#print("\n".join(call_function_fn))
	return call_function

#	(C) COMPARE THE TWO FUNCTION
# 		Function to compare two lists; if member of list1 is also a member of list2, add it to li_unused_samples
def fn_compare_lists ():
	li_unused_samples = [];
	list1 = fn_search_for_all_samples_cont ()
	list2 = fn_search_ableton_projects_cont ()

	tkLB_samples_to_move.delete(0, END)

	# strip the file ext.s (in case a sample was used and the ext. was changed somehow)
	list1_fn = [os.path.splitext(item)[0] for item in list1]
	list1_base_fn = [];
	for item in list1_fn:
		list1_base_fn.append(os.path.basename(item))
	list2_fn = [os.path.splitext(item)[0] for item in list2]
	list2_base_fn = [];
	for item in list2_fn:
		list2_base_fn.append(os.path.basename(item))

	for index, item in enumerate(list1_base_fn):
		if item not in list2_base_fn:
			li_unused_samples.append(list1[index])
			#print (item)

    # print li_unused_samples to left listbox
	tkLB_samples_to_move.delete(0, END)
	tkLB_unused_samples.delete(0, END)

	li_unused_samples.sort()
	for index, item in enumerate(li_unused_samples):
		tkLB_unused_samples.insert(END, item)

#	(D) MANIPULATE ITEMS IN LISTBOXES
#		move an item from the left listbox to the right listbox; add a star to the item in the left listbox
def fn_move_items_right ():
	li_samples_on_right = [];
	li_samples_on_right = list(tkLB_samples_to_move.get(0, END));
	li_samples_on_left = [];
	li_samples_on_left = list(tkLB_unused_samples.get(0, END));
	li_samples_to_move = [];
	li_samples_to_move = [tkLB_unused_samples.get(item) for item in tkLB_unused_samples.curselection()]
	for item in li_samples_to_move:
		if item not in li_samples_on_right:
			# colour item in left listbox
			item_index = li_samples_on_left.index(item)
			tkLB_unused_samples.itemconfig(item_index, bg="gray")
			# add item to right array
			li_samples_on_right.append(item)

	# sort right array
	li_samples_on_right.sort()
	tkLB_samples_to_move.delete(0, END)
	# repopulate the right listbox
	for item in li_samples_on_right:
		tkLB_samples_to_move.insert(END, item)

#		remove an item from the right listbox
def fn_remove_items_right ():
	li_samples_on_left = [];
	li_samples_on_left = list(tkLB_unused_samples.get(0, END));
	li_items_to_remove = [];
	li_samples_on_right = list(tkLB_samples_to_move.get(0, END));
	li_items_to_remove = [tkLB_samples_to_move.get(item) for item in tkLB_samples_to_move.curselection()]

	for item in li_items_to_remove:
		# remove colouring from item in left listbox
		item_index = li_samples_on_left.index(item)
		tkLB_unused_samples.itemconfig(item_index, bg="white")
		# remove item from right array
		li_samples_on_right.remove(item)

	# sort right array
	li_samples_on_right.sort()
	tkLB_samples_to_move.delete(0, END)
	#repopulate the right listbox
	for item in li_samples_on_right:
		tkLB_samples_to_move.insert(END, item)
	li_samples_to_move = [];

#	(E) FUNCTION TO MOVE UNUSED SAMPLES TO NEW FOLDER
def move_sample_files_fn ():
	old_folder = tkEN_samples_folder.get()
	new_folder = tkEN_new_folder.get()
	li_samples_to_move = list(tkLB_samples_to_move.get(0, END));

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

# DRAW GUI
#	separator line
canvas = Canvas(root, width=window_width, height=window_height, background="#F3E5AB")
canvas.create_line(5, 70, window_width-5, 70, width=2)
canvas.place(x = 0, y = 0)

#	create Entry: for user to input samples folder
tkLB_samples_folder = Label(root, text="Samples directory:")
tkLB_samples_folder.place(x = 5, y = 6) #DRAW
tkEN_samples_folder = Entry(root, width=77)
tkEN_samples_folder.place(x = 140, y = 5) #DRAW
tkEN_samples_folder.insert(0, "/Users/josephhaley/Music/*samples folder*/")

#	create Entry: for user to input projects folder
tkLB_projects_folder = Label(root, text="Projects directory:")
tkLB_projects_folder.place(x = 5, y = 35) #DRAW
tkEN_projects_folder = Entry(root, width=77)
tkEN_projects_folder.place(x = 140, y = 35) #DRAW
tkEN_projects_folder.insert(0, "/Users/josephhaley/Music/*projects folder*/")

#	create Button: search for unused samples
tkBU_samples_folder = Button(root, text="Search for samples", height=3, command=fn_compare_lists)
tkBU_samples_folder.place(x = window_width-142, y = 7)

#	create Listbox: list of unused samples
tkLL_unused_samples = Label(root, text="All unused samples")
tkLL_unused_samples.place(x = 270, y = 76)
tkLB_unused_samples = Listbox(root, width=40, selectmode=EXTENDED, borderwidth=2)
tkLB_unused_samples.place(x = 5, y = 104, width = 400, height = 560) #DRAW

#	create Listbox: samples to move
tkLL_samples_to_move = Label(root, text="Samples to be moved")
tkLL_samples_to_move.place(x = 592, y = 76)
tkLB_samples_to_move = Listbox(root, width=40, selectmode=EXTENDED, borderwidth=2)
tkLB_samples_to_move.place(x = 592, y = 104, width = 400, height = 560) #DRAW

#	create Button: move item from left to right
tkBU_samples_folder = Button(root, text="Move to > > >", command=fn_move_items_right)
tkBU_samples_folder.place(x = 450, y = 280)

#	create Button: remove item from right and dehighlight item in left
tkBU_samples_folder = Button(root, text="< < < Move to", command=fn_remove_items_right)
tkBU_samples_folder.place(x = 450, y = 315)

# create Entry: for user to input new samples folder
tkLB_new_folder = Label(root, text="Move samples to:")
tkLB_new_folder.place(x = 5, y = window_height-31) #DRAW
tkEN_new_folder = Entry(root, width=80)
tkEN_new_folder.place(x = 140, y = window_height-32) #DRAW
tkEN_new_folder.insert(0, "/Users/josephhaley/Music/*new samples folder*")

#	create Button: move samples to new folder
tkBU_move_samples = Button (root, text="Move samples", command=move_sample_files_fn)
#tkBU_move_samples.config(relief=SUNKEN)
tkBU_move_samples.place(x = 890, y=window_height-31)

# MAINLOOP
root.mainloop()
