planet = "Pluto"
pluto_mass = 1.303 * 10**22
earth_mass = 5.9722 * 10**24
population = 52910390
#         2 decimal points   3 decimal points, format as percent     separate with commas
print("{} weighs about {:.2} kilograms ({:.3%} of Earth's mass). It is home to {:,} Plutonians.".format(
    planet, pluto_mass, pluto_mass / earth_mass, population,
))

num = 35.267825343  # 3526.78%
print("this {:.3%} is a test".format(num))


arr = ['Mari', 'Joy', 'Butsi']

for name in arr:
    print(name)

for i in range(len(arr)):
    print(arr[i], i)

for (i, name) in enumerate(arr):
    print(name, i)
