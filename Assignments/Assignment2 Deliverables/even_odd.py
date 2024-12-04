#!/usr/bin/env python3

# defining functions
def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

# main()
def main():
    num = int(input("Enter an integer: "))
    print()
    if is_even(num):
        print("This is an even number.")
    else:
        print("This is an odd number.")

main()
