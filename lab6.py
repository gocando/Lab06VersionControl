

def main():
    password = None
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()

        option = int(input("Please enter an option:"))

        if option == 1:
            password = input("Please enter your password to encode:")
            print("Your password has been encoded and stored!")
            print()


        elif option == 2:
            if password == None:
                print("No password has been encoded.")
            else:
                decode1 = decode(password)
                print(f"The encoded password is {decode1}, and the original password is {password}")
            print()


        elif option == 3:
            break


        else:
            print("Invalid option. Please choose a option from the menu: ")

if __name__ == "__main__":
    main()

