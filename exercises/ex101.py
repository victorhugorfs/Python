from datetime import datetime

def vote():
    if age < 16:
        print(f"At {age} years old: NOT ALLOWED TO VOTE.")
    elif 16 <= age < 18 or age >= 70:
        print(f"At {age} years old: OPTIONAL VOTING.")
    else:
        print(f"At {age} years old: COMPULSORY VOTING.")

print("-" * 30)

birth_year = int(input("Enter your birth year: "))
current_year = datetime.now().year

age = current_year - birth_year

vote()