def register_person(file):
    name = input("Enter the name: ").strip()
    age = input("Enter the age: ").strip()

    with open(file, "a", encoding="utf-8") as f:
        f.write(f"{name},{age}\n")
    print(f"{name} registered successfully!")


# Function to list all people
def list_people(file):
    try:
        with open(file, "r", encoding="utf-8") as f:
            people = f.readlines()

        if not people:
            print("No people registered yet.")
            return

        print("\n--- Registered People ---")
        for person in people:
            name, age = person.strip().split(",")
            print(f"Name: {name}, Age: {age}")

    except FileNotFoundError:
        print("No records found yet.")