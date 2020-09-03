import random

doors = [1, 2, 3]
trials = 10000
successful_guesses = 0

for i in range(trials):
    car_door = random.choice(doors) 
    selected_door = random.choice(doors)
    if car_door ==  selected_door:
        successful_guesses += 1

score = successful_guesses / trials
print(score) 

