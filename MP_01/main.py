import string
import time

def vigenereCipher(text, key, mode):
    str = ""
    index = 0
    keyLen = len(key)
    for char in text:
        char = char.upper()
        if char.isalpha():
            key_char = key[index % keyLen].upper()
            index += 1
            if mode == 0:
                str += chr((ord(char)+ord(key_char)-2*ord('A'))%26+ord('A'))
            else:
                str += chr((ord(char)-ord(key_char)+26)%26+ord('A'))
    return str

def encrypt(plaintext, key):
    return vigenereCipher(plaintext, key, 0)

def decrypt(plaintext, key):
    return vigenereCipher(plaintext, key, 1)

def bruteCrack(ciphertext, keyLen, firstLen, dict):
    with open(dict, 'r') as f:
        words = set(word.strip().upper() for word in f)
    results = []
    for i in range(26**keyLen):
        key = ""
        for j in range(keyLen):
            key += chr(i // (26**j) % 26 + ord('A'))
        plaintext = decrypt(ciphertext, key)
        first_word = plaintext[:firstLen].upper()
        if first_word in words:
            results.append((plaintext,key))
    return results

def bruteForce(ciphertext, keyLen, firstLen):
    dict = ("MP1_dict.txt")
    altStr = ""
    start = time.time()
    attakResult = bruteCrack(ciphertext, keyLen, firstLen, dict)
    for plaintext, key in attakResult:
        altStr += ciphertext + ", " + key + ", " + plaintext + ", " + str(time.time()-start) + "\n"
    return altStr

def main():
    print("Please select an option:")
    print("0. Encrypt")
    print("1. Decrypt")
    print("2. Brute Force")
    selection = int(input("Enter the number of the option you would like to use: "))
    if selection == 0:
        plaintext = input("Plaintext: ").strip().upper()
        key = input("Key: ").strip().upper()
        print("Ciphertext: " + encrypt(plaintext, key))
    elif selection == 1:
        ciphertext = input("Ciphertext: ").strip().upper()
        key = input("Key: ").strip().upper()
        print("Plaintext: " + decrypt(ciphertext, key))
    elif selection == 2: 
        output = "Ciphertext, Key, Plaintext, Time\n"
        output += bruteForce("MSOKKJCOSXOEEKDTOSLGFWCMCHSUSGX",2,6)
        output += bruteForce("PSPDYLOAFSGFREQKKPOERNIYVSDZSUOVGXSRRIPWERDIPCFSDIQZIASEJVCGXAYBGYXFPSREKFMEXEBIYDGFKREOWGXEQSXSKXGYRRRVMEKFFIPIWJSKFDJMBGCC",3,7)
        output += bruteForce("MTZHZEOQKASVBDOWMWMKMNYIIHVWPEXJA",4,10)
        output += bruteForce("SQLIMXEEKSXMDOSBITOTYVECRDXSCRURZYPOHRG",5,11)
        output += bruteForce("LDWMEKPOPSWNOAVBIDHIPCEWAETYRVOAUPSINOVDIEDHCDSELHCCPVHRPOHZUSERSFS",6,9)
        open("output.csv", "w").write(output)

if __name__ == '__main__':
    main()