user_input = input("Enter a pharse:")

pharse = (user_input.replace('of', '')).split()

a = ""

for word in pharse:
    a = a + word[0].upper()

print(f"Acronym of {user_input} is {a}")