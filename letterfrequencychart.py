alphabet = "abcdefghijklmnopqrstuvwxyz"

def frequency_chart(message):
    keyvaluedict = {}
    list = ""
    for i in range(0,len(alphabet)):
        count = 0
        for letter in message:
            if letter == alphabet[i]:
                count += 1
            else:
                pass
        keyvaluedict[alphabet[i]] = count
        list = list + alphabet[i] + ":" + str(count) + " "

    return [list, keyvaluedict]
