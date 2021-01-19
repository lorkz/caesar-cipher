import time

def encryption():
    word_1 = input('Word: ').lower()
    word = list(word_1)
    letters = 'abcdefghijklmnoprstuvzwxy'
    letters = list(letters)
    key = int(input('Encryption Key: '))
    letters = letters + letters[0:key]
    i = 0
    while i < len(word):
        z = 0
        while letters[z] != word[i]:
            z = z + 1
        word[i] = letters[z+key]
        i = i + 1
    word = ''.join(word)
    print('Your encrypted word is ' + word)

def decryption():
    word_2 = input('Word: ').lower()
    word_2 = list(word_2)
    key = int(input('Key with which u encrypted: '))
    letters = 'abcdefghijklmnoprstuvzwxy'
    a = list(letters)
    a = a + a[0:key]
    a = a[::-1]
    i = 0
    while i < len(word_2):
        z = 0
        while a[z] != word_2[i]:
            z = z + 1
        word_2[i] = a[z+key]
        i = i + 1
    word_2 = ''.join(word_2)
    print('Your decrypted word is ' + word_2)


def main():
    answer = input('Do you want to encrypt/decrypt (answer with encrypt/decrypt)? ').lower()
    if answer == 'encrypt':
        encryption()
        time.sleep(2)
        answer2 = input('Rerun the program (answer with yes/no)? ').lower()
        if answer2 == 'yes':
            main()
        else:
            print('Thank you and goodbye')
    elif answer == 'decrypt':
        decryption()
        time.sleep(2)
        answer3 = input('Rerun the program (answer with yes/no)? ').lower()
        if answer3 == 'yes':
            main()
        else:
            print('Thank you and goodbye')
    else:
        print('Thank you and goodbye')

main()















