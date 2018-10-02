def parentheticals(message):
    if len(message) > 0:
        count = 0
        icon = (")", "(")
        for i in message:
            if i in icon:
                count +=1
        return count


print parentheticals("i love ) you ((")

def get_closing_paren(sentence, opening_paren_index):
    open_nested_parens = 0

    for position in xrange(opening_paren_index + 1, len(sentence)):
        char = sentence[position]

        if char == '(':
            open_nested_parens += 1
        elif char == ')':
            if open_nested_parens == 0:
                return position
            else:
                open_nested_parens -= 1

    raise Exception("No closing parenthesis :(")