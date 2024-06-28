import random

# Enters your name
name = input("Who are you?\n")

# Prints out your name
print(f"Hello, {name}!")

# Function to randomize values of coin toss
def coinToss():
    return random.randint(0,1)

# Print the initial statement
print("Tossing a coin...")

# Store the occurances of heads and tails 
heads = 0
tails = 0

# For loop which simulates 3 ronds
for rnd in range(1,4):
    value = coinToss()
    
    if value == 0:
        print(f"Round {rnd}: Heads")
        heads += 1
    
    else:
        print(f"Round {rnd}: Tails")
        tails += 1


# Final result of the game
print(f"Heads: {heads}, Tails: {tails}")

# Decide the winner
if heads > tails:
    print(f"{name} won!")

else:
    print(f"{name} lost!")
    
    

