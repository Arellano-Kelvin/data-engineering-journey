"""from pathlib import Path
p = Path('spam.txt')
p.write_text('Hello, world!')
13
p.read_text()
'Hello, world!'"""
"""from pathlib import Path
hello_file = open(Path.home() / 'hello.txt', encoding='UTF-8')"""
"""hello_content = hello_file.read()
hello_content"""
try:
#try 
    with open('example.txt', 'r') as f:
        content = f.read()
    print(content)
except FileNotFoundError:
    print("File not found – creating a new one.")
    with open('example.txt', 'w') as f:
        f.write("Default content created.")
        def get_positive_int() -> int:
            while True:
                try:
                    num = int(input("Enter positive number: "))
                    if num <= 0:
                        raise ValueError("Must be positive!")
                        return num
                except ValueError as e:
                    print(f"Invalid: {e}. Try again.")
import re

messy = "Price: $1,234.56   extra spaces!!"
cleaned = re.sub(r'[^\d.]', '', messy)  # remove non-digit/non-dot
print(cleaned)  # "1234.56"
