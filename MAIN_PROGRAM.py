# ------------------------------
# PYTHON MODULES being used
# import os
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# ------------------------------
# METHODS: for searching folders and building lists
from fn_search_for_all_samples import fn_search_for_all_samples
from fn_search_ableton_projects import fn_search_ableton_projects
from fns_manip_sample_files import fn_move_sample_files
from fns_manip_sample_files import fn_copy_sample_files
from fn_find_unused_samples import fn_find_unused_samples

# ------------------------------
# METHODS: for moving items between the tkinter objects
#	- move an item from the left listbox to the right listbox
def tk_move_items_right ():
	li_samples_on_right = list(tkLB_samples_to_move.get(0, END)) # copy existing contents to array
	li_samples_on_left = list(tkLB_unused_samples.get(0, END))
	li_samples_to_move = [tkLB_unused_samples.get(item) for item in tkLB_unused_samples.curselection()]
	for item in li_samples_to_move:
		if item not in li_samples_on_right:
			# colour item in left listbox
			item_index = li_samples_on_left.index(item)
			tkLB_unused_samples.itemconfig(item_index, bg="gray")
			# add item to right array
			li_samples_on_right.append(item)

	# delete existing contents (we have already copied them to an array)
	tkLB_samples_to_move.delete(0, END)
	# populate the right listbox with modified right array
	for item in li_samples_on_right:
		tkLB_samples_to_move.insert(END, item)

#	- remove an item from the right listbox
def tk_remove_items_right ():
	li_samples_on_left = list(tkLB_unused_samples.get(0, END))
	li_samples_on_right = list(tkLB_samples_to_move.get(0, END))
	li_items_to_remove = [tkLB_samples_to_move.get(item) for item in tkLB_samples_to_move.curselection()]

	for item in li_items_to_remove:
		# remove colouring from item in left listbox
		item_index = li_samples_on_left.index(item)
		tkLB_unused_samples.itemconfig(item_index, bg="white")
		# remove item from right array
		li_samples_on_right.remove(item)

	# delete existing contents (we have already copied them to an array)
	tkLB_samples_to_move.delete(0, END)

	# populate the right listbox with modified right array
	for item in li_samples_on_right:
		tkLB_samples_to_move.insert(END, item)
	li_samples_to_move = []

#	- Widget call method: find all unused samples and write them to the left listbox
def tk_add_unused_samples ():
	li_unused_samples = fn_find_unused_samples( fn_search_for_all_samples(tkEN_samples_folder.get()),\
												fn_search_ableton_projects(tkEN_projects_folder.get())\
												)

	tkLB_samples_to_move.delete(0, END)
	tkLB_unused_samples.delete(0, END)

	for index, item in enumerate(li_unused_samples):
		tkLB_unused_samples.insert(END, item)

# METHODS: for moving and copying files
#	- Confirmation dialogue
def tk_confirm_box (message):
	response = messagebox.askquestion (	"Confirmation", \
										"Are you sure you want to " + message + " these files? You can't undo this.",\
										icon = "warning")
	return response

#	- Widget call method: MOVE selected files to new location
def tk_move_samples ():
	if tk_confirm_box("move") == "yes":
		fn_move_sample_files(	tkEN_samples_folder.get(), \
								tkEN_new_folder.get(), \
								list(tkLB_samples_to_move.get(0, END)) \
							)
	
		tkLB_samples_to_move.delete(0, END)
		tkLB_unused_samples.delete(0, END)
		tk_add_unused_samples ()

#	- Widget call method: COPY selected files to new location
def tk_copy_samples ():
	if tk_confirm_box("copy") == "yes":
		fn_copy_sample_files(	tkEN_samples_folder.get(), \
								tkEN_new_folder.get(), \
								list(tkLB_samples_to_move.get(0, END)) \
							)

# ------------------------------
# CONFIGURE GUI
root = Tk()
root.title("Sample Search and Move")
#	- set window attributes
root.resizable(False, False)
window_width = 1000
window_height = 700
bg_color = "#F3E5AB"
root.geometry(str(window_width) + "x" + str(window_height))
root.configure(background=bg_color)

# ------------------------------
# DRAW GUI
#	- separator line
canvas = Canvas(root, width=window_width, height=window_height, background=bg_color)
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
tkBU_samples_folder = Button(root,	text="Find unused samples", \
									height=3, \
									command=tk_add_unused_samples)
tkBU_samples_folder.place(x = window_width-150, y = 7)

#	- create Listbox: list of unused samples
tkLL_unused_samples = Label(root, text="All unused samples")
tkLL_unused_samples.place(x = 270, y = 76)
tkLB_unused_samples = Listbox(root, width=40, selectmode=EXTENDED, borderwidth=2)
tkLB_unused_samples.place(x = 5, y = 104, width = 400, height = 525) #DRAW

#	- create Listbox: samples to move
tkLL_samples_to_move = Label(root, text="Samples to be moved")
tkLL_samples_to_move.place(x = 592, y = 76)
tkLB_samples_to_move = Listbox(root, width=40, selectmode=EXTENDED, borderwidth=2)
tkLB_samples_to_move.place(x = 592, y = 104, width = 400, height = 525) #DRAW

#	- create Button: move item from left to right
tkBU_samples_folder = Button(root, text="Move to > > >", command=tk_move_items_right)
tkBU_samples_folder.place(x = 450, y = 280)

#	- create Button: remove item from right and dehighlight item in left
tkBU_samples_folder = Button(root, text="Remove item", command=tk_remove_items_right)
tkBU_samples_folder.place(x = 450, y = 315)

#	- separator line
canvas.create_line(5, window_height-36, window_width-5, window_height-36, width=2)
canvas.place(x = 0, y = 0)

#	- create Entry: for user to input new samples folder
tkLB_new_folder = Label(root, text="Move samples to:")
tkLB_new_folder.place(x = 5, y = window_height-31) #DRAW
tkEN_new_folder = Entry(root, width=69)
tkEN_new_folder.place(x = 140, y = window_height-32) #DRAW
tkEN_new_folder.insert(0, "/Users/josephhaley/Music/*new samples folder*")

#	- create Button: move samples to new folder
tkBU_move_samples = Button (root, \
	text="MOVE samples", \
	command=tk_move_samples)
tkBU_move_samples.place(x = window_width-110, y=window_height-31)
#	- create Button: copy samples to new folder
tkBU_move_samples = Button (root, \
	text="COPY samples", \
	command=tk_copy_samples)
tkBU_move_samples.place(x = window_width-220, y=window_height-31)

# ------------------------------
root.mainloop()
