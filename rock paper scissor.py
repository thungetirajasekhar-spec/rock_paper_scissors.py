import random

options = ["rock", "paper", "scissors"]

user = input("Enter your choice (rock/paper/scissors): ").strip().lower()
python = random.choice(options)

print(f"User choice: {user}")
print(f"Python choice: {python}")

if user == python:
    print("Tie")
elif (user == "rock" and python == "scissors") or \
     (user == "paper" and python == "rock") or \
     (user == "scissors" and python == "paper"):
    print("User wins")
else:
    print("Python wins")
