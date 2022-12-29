
print()
print("zadanie 1")
print()

shopping = {
    "warzywniak": ["buraki", "ziemniaki"],
    "piekarnia": ["bułka", "chleb"]
}

print()

for shop, item in enumerate(shopping["warzywniak"]):
     shopping["warzywniak"][shop] = item.title()

for shop, item in enumerate(shopping["piekarnia"]):
     shopping["piekarnia"][shop] = item.title()


for shop, item in shopping.items():
   print(f"Ide do sklepu {shop.title()} i kupuje{item}")
print()

counter = 0
for shop, item in shopping.items():
    counter = counter + len(item)
print(f"W sumie kupuje {counter} rzeczy")


print()
print("zadanie 2")
print()

list = []
for i in range(1,101):
    if i%5==0:
       list.append(i)
print(f"lista liczb podzielnych przez{list}")
print()

cubes = [number * number * number for number in list]
print(f"Te szesciany {cubes} uzyskano dzięki list comprehension")

print("nowe zmiany")
print ("jeszcze jedne zmiany")