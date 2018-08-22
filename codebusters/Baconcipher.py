baconcipher = "AAAAAAAAABAAABAAAABBAABAAAABABAABBAAABBBABAAAABAAAABAABABABAABABBABBAAABBABABBBAABBBBBAAAABAAABBAABABAABBBAABBBABAABABABBABBABABBB"
alphabet = "abcdefghijklmnopqrstuvwxyz"

# unfortunately, this doesn't actually make bacon. Sorry. :/
def make_bacon(message):
    plain_numbers = []
    message = message.lower()
    finalmessage = ""
    og_num = 0
    for le in message:
        if le in alphabet:
            og_num = alphabet.find(le)
            plain_numbers.append(og_num)
        else:
            plain_numbers.append(le)
    for i in range(0, len(plain_numbers)):
        try:
            x = (plain_numbers[i])*5
            finalmessage = finalmessage + baconcipher[x:x+5]
        except TypeError:
            finalmessage = finalmessage + plain_numbers[i]
    print(finalmessage)
    return message