alphabet = "abcdefghijklmnopqrstuvwxyz"


def coder(message, offset):
    coded_mssg = message
    mssg_split = coded_mssg.split()
    decoded_mssg = []
    for word in mssg_split:
        decoded_word = []
        for letter in word:
            if letter == "!":
                decoded_word.append("!")
            else:
                index = alphabet.find(letter)
                index -= offset
                if index < 0:
                    index += 26
                decoded_word.append(alphabet[index])
        decoded_mssg.append(decoded_word)

    mssg = ""
    for word in decoded_mssg:
        mssg += "".join(word) + " "
    print(mssg)


message = "the offset for the second message is fourteen"
coder(message, 10)