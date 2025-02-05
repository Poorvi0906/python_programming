def is_palindrome(string):
    left, right = 0, len(string) - 1
    while right >= left:
        if string[left].upper() != string[right].upper():
            return False
        left += 1
        right -= 1
    return True
print(is_palindrome('malayalam')) 
string = input("Enter a string:")
print(is_palindrome(string))
