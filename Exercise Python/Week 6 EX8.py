message = str(input("Input message to encrypt: "))

alphabet_encrypt = "QTGABCDEFHIJKLMNOPRSUVXYZ"


def subtitution_cipher(message, alphabet_encrypt):
    message = message.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    position = 0
    for i in message:
        if i == " ":
            message = message.replace(i, " ")
            position = position + 1
        else:
            message = message.replace(message[position], alphabet_encrypt[alphabet.find(i)])
            position = position + 1
    return message


print(subtitution_cipher(message,alphabet_encrypt))
