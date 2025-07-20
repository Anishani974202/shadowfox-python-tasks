friends = ["Aditya", "Sneha", "Rahul", "Priya", "Vikram"]

name_lengths = [(name, len(name)) for name in friends]

print("List of name and length tuples:")
print(name_lengths)
Trip Expenses Comparison
python
Copy
Edit
your_expenses = {
    "Hotel": 1200,
    "Food": 800,
    "Transportation": 500,
    "Attractions": 300,
    "Miscellaneous": 200
}

partner_expenses = {
    "Hotel": 1000,
    "Food": 900,
    "Transportation": 600,
    "Attractions": 400,
    "Miscellaneous": 150
}

your_total = sum(your_expenses.values())
partner_total = sum(partner_expenses.values())

if your_total > partner_total:
    print("You spent more than your partner.")
elif your_total < partner_total:
    print("Your partner spent more than you.")
else:
    print("Both spent the same amount.")

max_diff = 0
max_category = ""
for category in your_expenses:
    diff = abs(your_expenses[category] - partner_expenses[category])
    if diff > max_diff:
        max_diff = diff
        max_category = category

print(f"The category with the largest difference is '{max_category}' with a difference of ₹{max_diff}.")
