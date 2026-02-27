#Reverse a String
x="python"
print(x[::-1])

#Check Palindrome
def is_palindrome(s):
    s=s.lower()
    return s==s[::-1]
print(is_palindrome("madam"))
print(is_palindrome("hello"))


#Count Vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in s:
        if ch in vowels:
            count += 1

    return count

print(count_vowels("education"))

#Menu-Driven Program
def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

def is_palindrome(s):
    s = s.lower()
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

def count_vowels(s):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in s:
        if ch in vowels:
            count += 1
    return count


while True:
    print("\n--- MENU ---")
    print("1. Reverse a string")
    print("2. Check palindrome")
    print("3. Count vowels")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "4":
        print("Goodbye ")
        break

    text = input("Enter a string: ")

    if choice == "1":
        print("Reversed:", reverse_string(text))

    elif choice == "2":
        if is_palindrome(text):
            print("It is a palindrome ")
        else:
            print("It is NOT a palindrome ")

    elif choice == "3":
        print("Vowel count:", count_vowels(text))

    else:
        print("Invalid choice! Try again.")
