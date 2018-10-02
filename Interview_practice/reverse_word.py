def reverse_char(message, left, right):
    while left < right:
        message[left], message[right] = message[right], message[left]
        left += 1
        right += 1

def reverse_word(message):

    reverse_char(message, 0, len(message) - 1)

    cur_word_index = 0

    for i in range(message):
        if (i == len(message)) or (message[i] == " "):
            reverse_char(message, cur_word_index, i -1)
            cur_word_index = i + 1
    return 


