
pi = 22 / 7
print("1.1 Value of pi:", pi)
print("Type of pi:", type(pi))

try:
 exec("for = 4")
except SyntaxError:
    print(" Error: 'for' is a reserved keyword in Python and cannot be used as a variable name.")

P = 10000  # Principal
R = 5      # Rate of interest
T = 3      # Time in years
simple_interest = P * R * T / 100
print(" Simple Interest:", simple_interest)






