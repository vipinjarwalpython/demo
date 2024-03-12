# If Else Conditions --
"""
example 1 
num = int(input("Enter Number - "))

if (num%2==0):
    print(f"This number {num} - is odd")
else:
    print(f"This number {num} - is even")
"""

"""
example 2
age = int(input("Enter your age: "))

if age < 18:
    print("your can not give vote")
else:
    print("you can give vote")
"""


# Nested If else Conditions

"""
example 1
age = int(input("Enter your age: "))

if age < 18:
    print("minor age")

elif age >= 18 and age <= 35:
    print("adult age")

elif age > 35 and age <= 50:
    print("senior mid age")

else:
    print("senior citizen age")
"""


"""
# Loops
lst = [i for i in range(1, 11)]
even_num = []
sum_even = 0
odd_num = []
sum_odd = 0

for i in lst:
    if i % 2 == 0:
        even_num.append(i)
        sum_even = sum_even + i

    else:
        odd_num.append(i)
        sum_odd = sum_odd + i

print(f"even_num")
print(odd_num)
print(sum_even)
print(sum_odd)
"""

i = 1
even_num = []
sum_even = 0
odd_num = []
sum_odd = 0

c = 0

while i < 11:
    if i % 2 == 0:
        even_num.append(i)
        sum_even = sum_even + i

    else:
        odd_num.append(i)
        sum_odd = sum_odd + i

    i = i + 1
    c = c + 1

print(f"even-number = {even_num}")
print(f"odd-number = {odd_num}")
print(f"even-number-sum = {sum_even}")
print(f"odd-number-sum = {sum_odd}")
print(c)
