message = str(input("Input message to encrypt: "))

alphabet_encrypt = "QTGABCDEFHIJKLMNOPRSUVXYZ"
alphabet_decrypt = "QTGABCDEFHIJKLMNOPRSUVXYZ"

def encrypt_message(message, alphabet_encrypt):
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


def decrypt_message(message, alphabet_decrypt):
    message = message.upper()
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    position = 0
    for i in message:
        if i == " ":
            message = message.replace(i, " ")
            position = position + 1
        else:
            message = message.replace(message[position], alphabet[alphabet.find(i)])
            position = position + 1
    return message


print(encrypt_message(message, alphabet_encrypt))
print(decrypt_message(message,alphabet_decrypt))