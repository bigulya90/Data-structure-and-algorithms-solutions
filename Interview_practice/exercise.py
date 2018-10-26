import random


exercises = ["dfs_tree",
             "bfs_tree",
             "merge_sort",
             "quick_sort",
             "binary_tree",
             "reverse_list_inplace",
             "large_el_stack",
             "parentheticals",
             "parentheses_validator, "
             "check_for_cycle",
             "left_rotation",
             "merge_binary_tree",
             "search_in_bst",
             "maximum_depth_tree",
             "N-ary Tree Postorder Traversal",
             "Binary Search Tree : Lowest Common Ancestor",
             "is_unique",
             "is_permutation",
             "replace_white space",
             "Palindrome_permutation",
             "rotate_matrix_negative",
             "positive_rotate_matrix",
             "string_rotation",
             "cycle_ll",
             "longest_consec_sequence",
             "find_peak_el_BST",
             "intersection_array",
             "Two_Sum",
             "Valid Perfect Square",
             "Reverse String",
             "To_Lower_Case",
             "Remove Duplicates from Sorted List",
             " Middle of the Linked List",
             "Reverse Linked List",
             "rotation point string"]
while exercises:
    print(exercises.pop(random.randint(0, len(exercises)-1)))
    raw_input()