
pwd = input("What is the master password? ")


def view():
    pass


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd)


while True:
    mode = input("would you like to add a new password or view existing ones (view, add)? press q to quit ")

    match mode:
        case "q":
            break
        case "view":
            pass
        case "add":
            add()
        case _:
            print("invalid mode.")
