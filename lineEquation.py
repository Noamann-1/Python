import random

# Random slope and intercept
m = random.randint(1, 10)   # slope
c = random.randint(1, 20)   # intercept

print(f"Slope (m) = {m}, Intercept (c) = {c}")

# Generate 5 random x values and compute y
for i in range(5):
    x = random.randint(0, 10)
    y = m * x + c
    print(f"x = {x}, y = {y}")
