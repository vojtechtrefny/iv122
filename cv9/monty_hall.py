import random

def monty_hall(iterations=1000, strategy="stay"):

    wins = 0

    for i in range(iterations):
        treasure = random.randint(1, 3)
        guess = random.randint(1, 3)

        if strategy == "random":
            current_strategy = random.choice(["stay", "change"])
        else:
            current_strategy = strategy

        if current_strategy == "stay":
            if treasure == guess:
                wins += 1
        elif current_strategy == "change":
            if treasure != guess:
                wins += 1

    return wins / iterations


# not changing decision
print(monty_hall(1000, "stay"), monty_hall(10000, "stay"), monty_hall(100000, "stay"))

# changing decision
print(monty_hall(1000, "change"), monty_hall(10000, "change"), monty_hall(100000, "change"))

# random decision
print(monty_hall(1000, "random"), monty_hall(10000, "random"), monty_hall(100000, "random"))
