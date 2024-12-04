#!/usr/bin/env python3

# display program title
print("Table of Powers")

# get input from the user
while True:
    start = int(input("Start number: "))
    stop = int(input("Stop number: "))
    if start > stop:
        print("Start number must be less than stop number. " + 
              "Please try again.")
        continue
    else:
        break

print("\nNumber\tSquared\tCubed")
print("=======================")
for i in range(start, stop+1):
    print(str(i) + "\t" +
          str(i**2) + "\t" +
          str(i**3))
