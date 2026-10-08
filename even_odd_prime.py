# Even/Odd and Prime Number Checker

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


def check_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True


number = int(input("Enter a number: "))

print("\n--- Result ---")
print("Number is:", check_even_odd(number))

if check_prime(number):
    print("It is a Prime Number.")
else:
    print("It is not a Prime Number.")
