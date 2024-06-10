def collatz(number):
    if number % 2 == 0:
        result = number // 2
    else:
        result = 3 * number + 1
    print(result)
    return result
    
user_input = input("Please enter an integer: ")
number = int(user_input)

while number != 1:
    number = collatz(number)


tEst = 10
varA = 11
varB = 12