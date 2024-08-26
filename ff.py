def encrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s-65) %26 +65)
        else:
            result += chr(( ord(char) + s -97) % 26 + 97)
    return result
def decrypt(text,s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) - s-65) %26 +65)
        else:
            result += chr((ord(char) - s -97) %26 +97)
    return result
text = "ATTACK"
s = 6
print("Text : " +text)
print("Shift : " + str(s))
encryptword=encrypt(text,s)
print("Cipher:" +encryptword)
decryptword=decrypt(encryptword,s)
print("Plain Text:" +decryptword)
        
