from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("Key.key", "wb") as key_file:
        key_file.write(key)


def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


# write_key()

key = load_key()
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            user, password = data.split("|")
            print("User:", user, "Password:", fer.decrypt(password).decode())


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode = input("would you like to add a new password or view existing ones (view, add)? press q to quit ")

    match mode:
        case "q":
            break
        case "view":
            view()
        case "add":
            add()
        case _:
            print("invalid mode.")
