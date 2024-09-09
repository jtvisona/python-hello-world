# TTDL for Python Hello World repo

## Introduction
The goal is to create a repo that is a personal resource for using Python. At first, the project will be done manually,
but as the repo develops, the goal will be to use the language to develop scripts in the language to advance the contents
of the repo more quickly. Then, as the repo becomes more sophisticated, it will incorporate SQL lite and a user interface
so that repo becomes not just a reference, but an application itself to assist in productivity. Ultimately, the third
phase will be to incorporate LLM technology so that prompts and results can be stored and maintained.

---

## Phase One - Manual Development

### Notes

### Tasks

- [x] Automate the generation of md for wiki by adding code embedding and section formatting for samples
- [ ] Combine numbering and embedding scripts
- [ ] Specify list of files to be numbered, embedded in explanatory text, and appended to a single file
- [ ] Add int(), float(), str() to examples
- [ ] User-regulated loop
- [ ] movie[0], min(), max(), sort()
- [ ] data.count(i)
- [ ] random_list = [0] * 11; number_crunching.py
- [ ] line.replace("\n", "")

def list_movies(movies):
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie}")
    print()

with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(movies)  


import pickle

FILENAME = "movies.bin"

def write_movies(movies):
    with open(FILENAME, "wb") as file:
        pickle.dump(movies, file)

def read_movies():
    with open(FILENAME, "rb") as file:
        movies = pickle.load(file)
    return movies


    movies.pop(index - 1)

with open(FILENAME, newline="") as file

    except FileNotFoundError as e:
        print(f"Could not find {FILENAME} file.")
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()

def read_movies():
    try:
        movies = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
        return movies
    except FileNotFoundError as e:
        print(f"Could not find {FILENAME} file.")
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()

def write_movies(movies):
    try:
        with open(FILENAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(movies)
    except Exception as e:
        print(type(e), e)
        exit_program()

from decimal import Decimal
import locale as lc
future_value = future_value.quantize(Decimal("1.00"))

lc.setlocale(lc.LC_ALL, "en_US")
monthly_investment = lc.currency(monthly_investment, grouping=True)
future_value = lc.currency(future_value, grouping=True)

index1 = full_name.find(" ")
first_name = full_name[:index1]

word_with_spaces = " ".join(word)
words = text.split(" ")

from datetime import datetime, timedelta

def get_invoice_date():
    invoice_date_str = input("Enter the invoice date (MM/DD/YY): ")    
    invoice_date = datetime.strptime(invoice_date_str, "%m/%d/%y")

    # calculate due date and days overdue
due_date = invoice_date + timedelta(days=30)
current_date = datetime.now()
days_overdue = (current_date - due_date).days

date_format = "%B %d, %Y"

while True:
    date_str = input("Enter arrival date (YYYY-MM-DD): ")
    try:
        arrival_date = datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Try again.")
        print()
        continue  # skip next if statement and re-start loop

print(f"Total price:     {locale.currency(total_cost)}")

    print(f"Author:   {book['author']}")
    book_catalog = {
        "Moby Dick": 
            {"author" : "Herman Melville",
             "pubyear" : "1851"},
    }

codes = list(countries.keys())

chapter 14-18
