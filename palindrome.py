number = input("Enter a number: ")
is_palindrome = True

# Loop through half of the number's length
for i in range(len(number) // 2):
    if number[i] != number[-i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print(f"{number} is a palindrome.")
else:
    print(f"{number} is not a palindrome.")