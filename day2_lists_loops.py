meals=['Doro_wot', 'Eggs', 'Tibs', 'Shiro', 'Beyaynet']

for meal in meals:
    print(meal, end = " ")

print("\n")


for i in range(1,21):
    if i%3 == 0 and i%5 == 0:
        print("fizzbuzz", end = " ")
    elif i%5 == 0:
        print("buzz", end = " ")
    elif i%3 == 0:
        print("fizz", end = " ")
    else:
        print(i, end = " ")