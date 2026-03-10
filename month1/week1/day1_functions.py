def greet(name: str) -> str: #this is a function that takes a string and 
    #returns a string with the name
    return f"Hello, {name}!"

user_food = input("What is your favorite food? ")

def clean_food(food: str) -> str:
    return food.strip().lower()

cleaned_food = clean_food(user_food)

with open("favorite_food.txt", "w") as file:
    file.write(cleaner_food)

five_favorite_foods = input("Enter your five favorite foods, separated by commas: ")

def clean_foods(foods: str) -> list[str]:
    return foods.strip().lower().split(",")

cleaned_foods = clean_foods(five_favorite_foods)

with open("favorite_foods.txt", "w") as file:
    file.write("\n".join(cleaned_foods))
    print(f"Your five favorite foods have been saved to favorite_foods.txt")