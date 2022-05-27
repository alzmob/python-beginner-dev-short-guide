from ast import While


print("Let's talk! Enter 'quit' before!")

while True:
    user = input("You: ")
    print(f"user: {user}")

    if user == "quit":
        break