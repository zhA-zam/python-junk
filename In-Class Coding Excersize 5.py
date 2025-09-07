'''
In order to promotoe her bistro, Sookie would like to run a Jelly Bean Guessing Game for her
customers. She informs thr customer that the number of jelly beans could be anywhere in the range
of 2000 to 5000.

Each customer gets 3 attempts to guess the number of jelly beans in the jar. If the customer gets
it right in their first attempt, they recieve a 50% off coupon that they can redeem at their next
order. If the first attempt fails, the customer is givem the sum of all digits of the number of
jelly beans as a hint. If the customer is able to guess correctly in the second attempt they get
a 25% off coupon that they can redeem at their next order. If the second attempt fails, the
customer is given the first and last digit of the number of jelly beans as a second and final
hint. If the customer is able to guess correctly in the third attempt they get a 10% off coupon
that they can redeem at their next order. If the customer does not guess correctly in the third
attempt then they don't recieve a discount and Sookie says good bye.

Create a program that asks for the number of jelly beans and displays how much discount the
customer can get in their next order.
'''

# given
jelly_beans = "2014" # Write number as a string so it can be indexed as part of a sequence
max_attempts = 3
# initial
user_attempt = 0
guess = ''
# Sookie wants to continue playing until:
# 1. The customer has guessed the correct number
# Or...
# 2. The max attempts has been reached

while guess != jelly_beans and user_attempt < max_attempts:
    guess = input("Enter Guess: ")
    user_attempt = user_attempt + 1
    if guess != jelly_beans: # answer is incorrect
        # Start giving hints
        if user_attempt == 1:
            total = 0 # initialize the variable that while accumulate the sum
            for digit in jelly_beans:
                total = total + int(digit)
            print(f'HINT #1: {total}')
        elif user_attempt == 2:
            first_digit = jelly_beans[0]
            last_digit = jelly_beans[-1]
            print(f'Hint #2: {first_digit}, {last_digit}')
        else:
            print("Better luck next time!")
    else: # Answer is correct
        if user_attempt == 1:
            print("50% off!")
        elif user_attempt == 2:
            print("25% off!")
        else:
            print("10% off!")
    