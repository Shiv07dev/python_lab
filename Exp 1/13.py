dict1 = {"comp": "computer", "sci": "science"}
print(dict1["comp"])
dict2 = {"123": "computer", 456: "maths"}
print(dict2["123"])
print(dict1["comp"] + dict2["123"])

# The below lines will give errors if run
print(dict1 + dict2)
print(dict1["computer"] + dict2["computer"])
