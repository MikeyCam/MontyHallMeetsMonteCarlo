import random

doors = list(range(100))
trials = 10000
successful_guesses = 0

for i in range(trials):
    car_door = random.choice(doors)
    selected_door = random.choice(doors)
    available_doors = [x for x in doors if x!= selected_door and x!= car_door]
    opened_doors = random.sample(available_doors, len(doors)-2)
    new_choice = [x for x in doors if x not in opened_doors if x != selected_door][0]
    if car_door ==  new_choice:
        successful_guesses += 1

score = successful_guesses / trials
print(score) 


