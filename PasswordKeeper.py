#  Create a password generator that stores records

import random

def main():
    counter = 0
    print('Welcome to your Password Generator')

    while counter >= 0:
        prompt = (input('What is this password for? Type quit to close:'))
        if prompt != 'quit':
            f = open("Password File.txt", "a")
            #  List Variables
            chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*.,/' #  The characters the password generator will pull from
            password_name = prompt
            length = int(input('Input desired password length: '))
            for pwd in range(1):
                password = ''
                for c in range(length):
                    password += random.choice(chars)
            print('Your password for {} is: {}/n'.format(password_name, password), file=f)
            counter +=1
        if prompt == 'quit':
            print('Program closed.')
            break


if __name__ == '__main__':
    main()
