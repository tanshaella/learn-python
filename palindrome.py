# Write a program that reads from the user a sentence, and determines if it is a palindrome or not.

# Palindrome : A sequence is a palindrome if it reads the same backward as forward.

# Step 1 - Read String
# Step 2 - Prepare string for palindrome checking
# 1. Keep only letters
# 2. Take all letters to lowercase
# Step 3 - Check if palindrome
# 1. Find reversed string
# 2. Compare original string to reversed string
# Step 4 - Announcement

def main():
    print("Please enter a string:")
    user_string = input()
    str_for_checking = prepare_str_for_palindrome_checkup(user_string)
    res = is_palindrome(str_for_checking)
    if(res == True):
        print("Your sentence is a palindrome")
    else:
        print("Your sentence is not a palindrome")

def prepare_str_for_palindrome_checkup(s):
    only_letters_str = keep_only_letters(s)
    return only_letters_str.lower()

def keep_only_letters(s):
    res_str = " "
    for char in s:
        if(char.isalpha() == True):
            res_str = res_str + char
    return res_str

def is_palindrome(s):
    rev_s = reverse_str(s)
    if(s == rev_s):
        return True
    else:
        return False

def reverse_str(s):
    res_str = " "
    for char in s:
        res_str = char + res_str
    return res_str

main()
