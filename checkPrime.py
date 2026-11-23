"""
Q2. Prime Number Optimisation

Ek number prime hai ya nahi check karo.

Conditions:
- Naive O(n) approach nahi.
- Optimised O(√n) approach use karo.
- Negative numbers aur 1 handle karo.
"""


def is_prime(num):
    if num <= 1:
        print("It is Not Prime")
        return False

    flag = True
    i = 2
    while i * i <= num:
        if num % i == 0:
            flag = False
            break
        i = i + 1

    return flag

min_Range = int(input("Enter the first range : "))
max_Range = int(input("Enter the second Range : "))

if min_Range > max_Range:
    min_Range , max_Range = max_Range , min_Range

for i in range(min_Range,max_Range+1):
    if is_prime(i) :
        print(i)