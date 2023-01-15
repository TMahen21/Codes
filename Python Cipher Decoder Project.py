alphabet = "abcdefghijklmnopqrstuvwxyz"


def decoder1(message, offset):
    coded_mssg = message
    mssg_split = coded_mssg.split()
    decoded_mssg = []
    for word in mssg_split:
        decoded_word = []
        for letter in word:
            if letter == "!" or letter == "." or letter == "'":
                decoded_word.append(letter)
            else:
                index = alphabet.find(letter)
                index += offset
                if index > 25:
                    index = index % 26
                decoded_word.append(alphabet[index])
        decoded_mssg.append(decoded_word)

    mssg = ""
    for word in decoded_mssg:
        mssg += "".join(word) + " "
    print(mssg)


message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px " \
          "ptgm mh dxxi hnk fxlltzxl ltyx. "
print(decoder1(message, 7))

