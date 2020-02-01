import os

# 		Function to compare two lists; if member of list1 is also a member of list2, add it to li_unused_samples
def fn_compare_lists (list1, list2):
	li_unused_samples = [];

	tkLB_samples_to_move.delete(0, END)

	# strip the file ext.s (in case a sample was used and the ext. was changed somehow)
	list1_stripped = [os.path.splitext(item)[0] for item in list1]
	list1_base_fn = [];
	for item in list1_stripped:
		list1_base_fn.append(os.path.basename(item))
	list2_stripped = [os.path.splitext(item)[0] for item in list2]
	list2_base_fn = [];
	for item in list2_stripped:
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