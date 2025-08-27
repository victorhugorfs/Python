from register import register_person, list_people

FILE = "people.txt"

def menu():
    while True:
        print("\n--- MENU ---")
        print("1 - Register a new person")
        print("2 - List registered people")
        print("3 - Exit")

        option = input("Choose an option: ")

        if option == "1":
            register_person(FILE)
        elif option == "2":
            list_people(FILE)
        elif option == "3":
            print("Exiting the system...")
            break
        else:
            print("Invalid option! Try again.")

if __name__ == "__main__":
    menu()