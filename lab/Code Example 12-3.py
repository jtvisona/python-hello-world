#
# Code Example 12-3

pets = {
    "dog": {"type": "poodle", "color": "white"},
    "cat": {"type": "Siamese", "color":  "black and white"},
    "bird": {"type": "parrot", "color": "green"}
}
pet = pets["dog"]
pet = pets["bird"]
#print(pet["color"], pet["type"])
pet = "cat"
print(pets[pet]["color"], pets[pet]["type"], pet)
