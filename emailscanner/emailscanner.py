email = input("Enter your email address is: ").strip()

username = email[:email.index('@')]
domain = email[email.index('@') + 1:]

print(f"Your username is {username} and email domain is {domain}")