from cryptography.fernet import Fernet

'''
#CALL ONCE: function to generate encryption key and save to key file
def make_key():
    key = Fernet.generate_key()
    with open('key.key', 'wb') as f:
        f.write(key)

#calling make key function only once and commenting it
# make_key()
'''

#returns encryption key from the key file
def load_key():
    with open('key.key', 'rb') as f:
        key = f.read()
        return key

#adding more complexity to the key by using key + master_pwd from user
# master_pwd = input('Enter Master Password: ')
# key = load_key() + master_pwd.encode()
key = load_key()

#all the passwords will be encrypted using this fernet
fer = Fernet(key)

def encrypt_pwd(pwd):
    return fer.encrypt(pwd.encode()).decode()

def decrypt_pwd(pwd):
    return fer.decrypt(pwd.encode()).decode()

def view():
    try:
        with open('passwords.txt', 'r') as f:
            for line in f.readlines():
                line = line.rstrip()
                accnt_name, pwd = line.split('|')
                pwd = decrypt_pwd(pwd)
                print('Account:', accnt_name, '| Password:', pwd)
    except Exception:
        print('No passwords saved yet')

def add():
    account_name = input('Account Name: ')
    pwd = input('Password: ')
    pwd = encrypt_pwd(pwd)
    with open('passwords.txt', 'a') as f:
        f.write(account_name + '|' + str(pwd) + '\n')

print('\nWelcome to your Password Manager!\n')

while True:
    mode = input('Enter Mode View/Add or Q to Exit: ').lower()

    if mode == 'q':
        break

    if mode == 'view':
        view()
    elif mode == 'add':
        add()
    else:
        print('Invalid Input!')
        continue