text = "    hello, and welcome to day 3 of   "
## strip() removes whitespace from the beginning and end of the string
## upper() converts the string to uppercase
cleaned_text = text.strip().upper()
print(cleaned_text)

words = cleaned_text.split()
#split() splits the string into a list of words
print("Number of words:", len(words))
#length of list
print("First word:", words[0])
#first word in list
print("Last word:", words[-1])
#last word in list
print("First 3 words:", words[:3])
#first 3 words
print("Last 3 words:", words[-3:])
#last 3 words
print("Words in reverse order:", words[::-1])
#words in reverse order
print("Words in alphabetical order:", sorted(words))
#sorted() sorts the list in alphabetical order

## function practice
def clean_text(S:str) -> str:
    return S.strip().upper().replace(" ", "_")
print(clean_text("    try and make this text all uppercase and replace spaces with underscores   "))

## regex basics using humre
import re
from humre import *

# 1. Define the pattern (regexStr)
# This is the "Human Readable" part that humre is famous for
phone_pattern = either(OPEN_PAREN + exactly(3, DIGIT) + CLOSE_PAREN, exactly(3, DIGIT)) + '-' + exactly(3, DIGIT) + '-' + exactly(4, DIGIT)

# 2. Compile it and search the text
contact = "John Doe, john.doe@example.com, 123-456-7890"
match_obj = re.search(phone_pattern, contact)

if match_obj:
    # .group() gets the full string match
    full_phone = match_obj.group() 
    
    print(f"Phone: {full_phone}")
    print(f"Pattern: {phone_pattern}")
else:
    print("No phone number found.")