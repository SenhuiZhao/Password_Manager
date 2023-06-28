import os.path
import bcrypt
from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        # 'wb' write in byte model
        key_file.write(key)
  
write_key()
'''


def write_key(key):
    # if os.path.exists('key.key'):
    #     os.remove('key.key')
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        # 'wb' write in byte model
        key_file.write(key)


def write_password(key):
    if os.path.exists('password.key'):
        os.remove('password.key')
    password = key.encode("utf-8")
    hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
    with open('password.key', 'wb') as key_file:
        key_file.write(hashed_password)


def load_key():
    file = open('key.key', 'rb')
    key = file.read()
    file.close
    return key
    # with open('key.key', 'rb') as file:
    #     key = file.read()
    #     print('key: ', key)
    # return key
# whatever you want to use a function, you have to find before you used


def set_master_key():
    master_key = input('Set a new master key: ')
    write_key(master_key)
    write_password(master_key)
    print('Master key has been set successfully.')


def change_master_key():
    current_key = input('Enter the current master key: ')
    if verify_master_password(current_key):
        new_key = input('Enter a new master key: ')
        # write_key(new_key.encode())
        write_password(new_key)
        print('Master key has been changed successfully.')
    else:
        print('Failed to change the master key.')


def verify_master_password(pwd):
    # master_password = "pwdfile"
    # if pwd == master_password:
    #     return True
    # else:
    #     print("Incorrect master password.")
    #     return False

    if not os.path.isfile('password.key'):
        return False

    with open('password.key', 'rb') as file:
        stored_key = file.read()
        # print(stored_key)
        # print(pwd.encode())

    # if pwd.encode() == stored_key.decode():
    #     return True
    # else:
    #     print('Incorrect master password.')
    #     return False

    input_password = pwd.encode("utf-8")
    if bcrypt.checkpw(input_password, stored_key):
        print("Password is correct.")
        return True
    else:
        print('Incorrect master password.')
        return False


def view():
    if not os.path.isfile('passwords.txt'):
        print('No password have been save.')
        return False
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split('|')
            print('User: ', user, '| Password: ',
                  fer.decrypt(passw.encode()).decode())

            # print(line.rstrip())
            # rstrip() remove the '\n'


def add():
    name = input('Account Name: ')
    pwd = input('Password: ')

    with open('passwords.txt', 'a') as f:
        # with key word, automatically close the file
        # 'w' create a file, or if the file already exist, it will override entire file
        # 'a' pen model, it can write the text file from very end or create a new file if it does not exist
        # 'r' rede model, read file only

        f.write(name + '|' + fer.encrypt(pwd.encode()).decode() + '\n')
        # .encode() turn a string into the bites


def main():
    if not os.path.isfile('key.key'):
        set_master_key()

    master_pwd = input('What is the master password? ')

    if not verify_master_password(master_pwd):
        print('For user information safety, the system exits.')
        exit()

    print("Welcome to the password managerment system!")

    key = load_key() + master_pwd.encode()
    global fer
    fer = Fernet(key)

    # key + password + text to encrypt = random text
    # random text + ky + password = text to encrypt

    while True:
        mode = input(
            'Would you like to add a new password, view existing ones, change the master key, or exit (add, view, change, exit)? ')

        if mode == 'exit':
            print('Thank you for using password manager system! Bye~')
            break
        elif mode == 'view':
            view()
        elif mode == 'add':
            add()
        elif mode == 'change':
            change_master_key()
        else:
            print('Invalid mode.')
            continue


if __name__ == "__main__":
    main()
