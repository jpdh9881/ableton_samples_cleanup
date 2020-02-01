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