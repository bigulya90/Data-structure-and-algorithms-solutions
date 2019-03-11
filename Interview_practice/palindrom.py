def check_for_palindrom(message):
    if len(message) > 0:
        odd = set()

        for i in message:
            if i in odd:
                odd.remove(i)
            else:
                odd.add(i)

        return len(odd) <=1


print (check_for_palindrom("civi"))