messy_csv = """Name,Age,City
john doe ,  25 , Phoenix!!
Alice Smith,thirty,  Mesa
Bob,  , New York
"""

"""Split into lines → 
split each line by comma → 
strip whitespace → 
handle missing values → 
validate age as int (use try/except)
Output cleaned rows as list of lists or print nicely
Use regex to remove punctuation from names/cities
Add type hints, docstrings
Write cleaned version to cleaned.csv using csv module (import csv)"""


def clean_csv(messy_csv: str) -> list[list[str]]:
    """Clean and validate a CSV string, output cleaned rows as list of lists."""
    # Split into lines → 
    lines = messy_csv.split('\n')
    # Split each line by comma → 
    cleaned_rows = [line.split(',') for line in lines]
    # Strip whitespace → 
    cleaned_rows = [[cell.strip() for cell in row] for row in cleaned_rows]
    # Handle missing values → 
    cleaned_rows = [[cell if cell else 'Unknown' for cell in row] for row in cleaned_rows]
    # Validate age as int (use try/except)
    cleaned_rows = [[cell if cell == 'Unknown' else int(cell) for cell in row] for row in cleaned_rows]
    # Use regex to remove punctuation from names/cities
    cleaned_rows = [[re.sub(r'[^\w\s]', '', cell) for cell in row] for row in cleaned_rows]
    # Output cleaned rows as list of lists or print nicely
    print('Cleaned rows:')
    for row in cleaned_rows:
        print(row)

    # Write cleaned version to cleaned.csv using csv module (import csv)
    with open('cleaned.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(cleaned_rows)

    return cleaned_rows