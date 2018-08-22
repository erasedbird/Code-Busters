baconcipher = "AAAAAAAAABAAABAAAABBAABAAAABABAABBAAABBBABAAAABAAAABAABABABAABABBABBAAABBABABBBAABBBBBAAAABAAABBAABABAABBBAABBBABAABABABBABBABABBB"
alphabet = "abcdefghijklmnopqrstuvwxyz"
import getletternumber

# unfortunately, this doesn't actually make bacon. Sorry. :/
def make_bacon(message):
    plain_numbers = []
    message = message.lower()
    finalmessage = ""
    og_num = 0
    for le in message:
        x = getletternumber.get_letter_value(le, alphabet)
        plain_numbers.append(x)
    for i in range(0, len(plain_numbers)):
        try:
            x = (plain_numbers[i])*5
            finalmessage = finalmessage + baconcipher[x:x+5]
        except TypeError:
            finalmessage = finalmessage + plain_numbers[i]
    print(finalmessage)
    return message