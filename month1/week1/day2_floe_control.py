# if statement
name = 'John'
if name == 'John':
    print('Hello, John!')
else:
    print('Who are you?')
spam = 0 
# while loop
while spam < 5:
    print('Hello')
    spam = spam + 1
# for loop
for i in range(5):
    print(i)
#input + if/else statement
# The code below prompts the user to enter their age, then converts the input (which is a string) to an integer.
age = int(input("Please enter your age: "))

#password guesser
password = 'password123'
tries = 0
while tries < 3:
    guess = input("Enter the password: ")
    if guess == password:
        print("Access granted")
        break
    else:
        print("Access denied")
        tries += 1
if tries == 3:
    print("Too many attempts")

#for loop with enumerate
# The enumerate() function gives us both the index (position) and the value (food) of each item in the list.
# We use 'index' to know the position of the current food, and 'food' to get the actual item.
# For example, enumerate(['apple', 'banana']) gives us (0, 'apple') and then (1, 'banana').
foods = ['apple', 'banana', 'cherry', 'watermelon', 'orange']
for index, food in enumerate(foods):
    print(food.upper()+" "+str(index))



def run_quiz()->None:
    score=0
    print("Welcome to the food quiz!")
    print('What is the National dish of Japan?')
    answer = input("Enter your answer: ")
    while answer.lower() == "":
        print("Please enter a valid answer.")
        answer = input("Enter your answer: ")
        
    if answer.lower() == 'sushi':
        print("Correct!")
        score += 1
    else:
        print("Incorrect!")