flowers = {"red": "rose", "white": "lily", "yellow": "buttercup"}
print(flowers)
flowers["blue"] = "carnation"
print(flowers)
print("This is a red flower:", flowers.get("red", "none"))
key = "white"
if key in flowers:
    flower = flowers[key]
    print("This is a", key, "flower:", flower)
key = "green"
if key in flowers:
    flower = flowers[key]
    del flowers[key]
    print(flower + " was deleted")
else:
    print("There is no", key, "flower")