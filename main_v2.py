from cryptography.fernet import Fernet

#function to load key from key2 file
def load_key():
    file = open('key2.key', 'rb')
    key = file.read()
    file.close()
    return key

#master pwd + key = fer --- encryption formula used to save data
master_pwd = input('Enter master password: ')
key = load_key() + master_pwd.encode()
fer = Fernet(key)

'''
def make_key():
    key = Fernet.generate_key()
    with open('key2.key', 'wb') as key_file:
        key_file.write(key)

make_key()
'''

def view():
    with open('passwords2.txt', 'r') as f:
        for line in f.readlines():
            data = (line.rstrip())
            account_name, pwd = data.split('|')
            print('Account:', account_name, '| Password:', fer.decrypt(pwd.encode()).decode())

def add():
    account_name = input('Account name: ')
    pwd = input('Password: ')
    
    with open('passwords2.txt', 'a') as f:
        f.write(account_name + '|' + fer.encrypt(pwd.encode()).decode() + '\n')


while True:
    mode = input('Add new or view existing passwords? Enter Q to quit (Add/View/Q): ').lower()
    if mode == 'q':
        break

    if mode == 'view':
        view()

    elif mode == 'add':
        add()
        pass
    else:
        print('Invalid Mode!')

