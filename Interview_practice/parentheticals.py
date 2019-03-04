def parentheticals(message):
    if len(message) > 0:
        count = 0
        icon = (")", "(")
        for i in message:
            if i in icon:
                count +=1
        return count


parentheticals("i love ) you ((")


def parentheticals(sentence, open_paren_index):
    paren_count = 0

    for position in range(open_paren_index +1, len(sentence)):
        char = sentence[position]

        if char == "(":
            paren_count += 1
        elif char == ")":
            if paren_count == 0:
                return position
            else:
                paren_count -= 1

    raise Exception("No closing paren")

