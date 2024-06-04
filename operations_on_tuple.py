countries = ("spain", "Italy", "India", "England", "Germany")
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[1] = "Finland"
countries = tuple(temp)
# print(temp)
print(countries)
