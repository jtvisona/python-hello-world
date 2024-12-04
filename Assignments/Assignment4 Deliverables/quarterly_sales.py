#!/usr/bin/env python3

"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 4
quarterly_sales.py
"""

def display_welcome():
    print("The Quarterly Sales program")
    print()

def get_quarterly_sales():
    sales_list = []
    for i in range(4):
        sales = float(input("Enter sales for Q" + str(i+1) + ": "))
        sales_list.append(sales)
    return sales_list

def process_sales(sales_list):
    # calculate total
    total = sum(sales_list)
    # calculate average
    count = len(sales_list)
    average = round(total / count, 2)
    # get min and max
    lowest_quarter = min(sales_list)
    highest_quarter = max(sales_list)
    # format and display the result
    print()
    print("Total:", total)
    print("Average Quarter:", average)
    print("Lowest Quarter:", lowest_quarter)
    print("Highest Quarter:", highest_quarter)
    print()

def main():
    display_welcome()
    sales_list = get_quarterly_sales()
    process_sales(sales_list)

# if started as the main module, call the main function
if __name__ == "__main__":
    main()
