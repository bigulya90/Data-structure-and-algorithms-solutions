"""
input = [("first", "second")], where "first - duplicate", "second" is original
solution:
1. go over the list and count how many times the file in the list
if more then one, than check for last modified date --> latest - duplicate
"""

def find_duplicate(message):
    count = 0
    list_dict = {}
    duplicates = []
    stack = [message]

    while len(message):
        current_path = stack.pop()


    for i in message:
        if i in list_dict:
            count[i] += 1
        else:
            count[i] = 1
