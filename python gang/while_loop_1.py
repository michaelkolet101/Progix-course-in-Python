# for i in range(20)

rate = int(input("ENTER A RATE PER MINUT: "))
company = 0
i = 5
while i > 0:
    name = input("ENTER NAME: ")
    minuts_number = int(input("ENTER MINUTS NUMBER: "))
    sum = minuts_number * rate
    print(name, sum)
    company += sum
    i -= 1

print("company", company)

