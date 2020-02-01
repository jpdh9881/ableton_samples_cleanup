# Python modules
import os
from tkinter import *
from tkinter import ttk

from fn_search_for_all_samples 			import fn_search_for_all_samples
from fn_search_ableton_projects			import fn_search_ableton_projects
from fns_manipulate_items 				import fn_move_items_right
from fns_manipulate_items 				import fn_remove_items_right
from fn_move_sample_files 				import fn_move_sample_files

# Functions:
# 	fn_is_ableton_project (CLEANED)
#	fn_scan_project	(CLEANED)
#	fn_move_sample_files (CLEANED)
#	fn_compare_lists
#	fn_search_ableton_projects (CLEANED)
#	fn_search_for_all_samples (CLEANED)
#	fns_manipulate_items

# ------------------------------
# CONFIGURE GUI
root = Tk()
root.title("Sample Search and Move")
#	- set window attributes
root.resizable(False, False)
window_width = 1000;
window_height = 700;
root.geometry(str(window_width) + "x" + str(window_height))
root.configure(background="#F3E5AB")

# ------------------------------
# DRAW GUI
#	- separator line
canvas = Canvas(root, width=window_width, height=window_height, background="#F3E5AB")
canvas.create_line(5, 70, window_width-5, 70, width=2)
canvas.place(x = 0, y = 0)

#	- create Entry: for user to input samples folder
tkLB_samples_folder = Label(root, text="Samples directory:")
tkLB_samples_folder.place(x = 5, y = 6) #DRAW
tkEN_samples_folder = Entry(root, width=77)
tkEN_samples_folder.place(x = 140, y = 5) #DRAW
tkEN_samples_folder.insert(0, "/Users/josephhaley/Music/*samples folder*/")

#	- create Entry: for user to input projects folder
tkLB_projects_folder = Label(root, text="Projects directory:")
tkLB_projects_folder.place(x = 5, y = 35) #DRAW
tkEN_projects_folder = Entry(root, width=77)
tkEN_projects_folder.place(x = 140, y = 35) #DRAW
tkEN_projects_folder.insert(0, "/Users/josephhaley/Music/*projects folder*/")

#	- create Button: search for unused samples
tkBU_samples_folder = Button(root,	text="Search for unused samples", \
									height=3, \
									command=fn_compare_lists(	fn_search_for_all_samples_(tkEN_samples_folder.get()), \
																fn_search_ableton_projects(tkEN_projects_folder.get()) \
															))
tkBU_samples_folder.place(x = window_width-142, y = 7)

#	- create Listbox: list of unused samples
tkLL_unused_samples = Label(root, text="All unused samples")
tkLL_unused_samples.place(x = 270, y = 76)
tkLB_unused_samples = Listbox(root, width=40, selectmode=EXTENDED, borderwidth=2)
tkLB_unused_samples.place(x = 5, y = 104, width = 400, height = 560) #DRAW

#	- create Listbox: samples to move
tkLL_samples_to_move = Label(root, text="Samples to be moved")
tkLL_samples_to_move.place(x = 592, y = 76)
tkLB_samples_to_move = Listbox(root, width=40, selectmode=EXTENDED, borderwidth=2)
tkLB_samples_to_move.place(x = 592, y = 104, width = 400, height = 560) #DRAW

#	- create Button: move item from left to right
tkBU_samples_folder = Button(root, text="Move to > > >", command=fn_move_items_right)
tkBU_samples_folder.place(x = 450, y = 280)

#	- create Button: remove item from right and dehighlight item in left
tkBU_samples_folder = Button(root, text="< < < Move to", command=fn_remove_items_right)
tkBU_samples_folder.place(x = 450, y = 315)

#	- create Entry: for user to input new samples folder
tkLB_new_folder = Label(root, text="Move samples to:")
tkLB_new_folder.place(x = 5, y = window_height-31) #DRAW
tkEN_new_folder = Entry(root, width=80)
tkEN_new_folder.place(x = 140, y = window_height-32) #DRAW
tkEN_new_folder.insert(0, "/Users/josephhaley/Music/*new samples folder*")

#	- create Button: move samples to new folder
tkBU_move_samples = Button (root, \
	text="Move samples", \
	command=fn_move_sample_files(	tkEN_samples_folder.get(), \
									tkEN_new_folder.get(), \
									list(tkLB_samples_to_move.get(0, END)) \
								))
#tkBU_move_samples.config(relief=SUNKEN)
tkBU_move_samples.place(x = 890, y=window_height-31)

# ------------------------------
root.mainloop()
