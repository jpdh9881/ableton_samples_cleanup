import os
from fn_search_for_all_samples import fn_search_for_all_samples
from fn_search_ableton_projects import fn_search_ableton_projects

# Compares two lists: if member of list1 is not a member of list2, add it to li_unused_samples
#
# @param list1
# @param list2 List to be compared to
#
# @return List of list1 items which are not in list2
#
def fn_find_unused_samples (list1, list2):
	li_unused_samples = [];

	# strip the file ext.s (in case a sample was used and the ext. was changed somehow)
	list1_stripped = [os.path.splitext(item)[0] for item in list1]
	list1_bases = [];
	for item in list1_stripped:
		list1_bases.append(os.path.basename(item))

	list2_stripped = [os.path.splitext(item)[0] for item in list2]
	list2_bases = [];
	for item in list2_stripped:
		list2_bases.append(os.path.basename(item))

	for index, item in enumerate(list1_bases):
		if item not in list2_bases:
			li_unused_samples.append(list1[index])
			#print (item)

	li_unused_samples.sort()
	return li_unused_samples