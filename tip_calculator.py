print("Welcome to Tip Calculator. Please enter the following:")
bill_amount = float(input("Enter the bill amount in $ "))
tip_percentage = float(input("Enter the tip percentage % "))
party_size = int(input("Enter the party size "))

def tip_calculator(bill_amount, tip_percentage):
    tip_amount = bill_amount * tip_percentage / 100
    return bill_amount + tip_amount

def amount_per_person(total, party_size):
    return total / party_size

if party_size <= 0:
    print("Party size must be at least 1.")
else:
    total = tip_calculator(bill_amount, tip_percentage)
    per_person = amount_per_person(total, party_size)

    print(f"Final bill with tip: ${total:.2f}")
    print(f"Amount per person: ${per_person:.2f}")
