#Code Example 12-2
flowers = {"white": "lily",
               "red": "rose",
               "blue": "carnation",
               "yellow": "buttercup"}
colors = list(flowers.keys())
colors.sort()
show_colors = "Colors of flowers: "
for color in colors:
    show_colors += color + " "
print(show_colors)
pick_color = input("Enter a color: ")
pick_color = pick_color.lower()
if pick_color in flowers:
   name = flowers[pick_color]
   print("Flower name: " + name)
else:
   print("There is no " + pick_color + " flower.")