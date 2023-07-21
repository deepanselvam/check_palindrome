def isPalindrome(s):
    if len(s) == 0 or len(s) == 1:
        return 1
    if s[0] == s[-1]:
        return isPalindrome(s[1:-1])
    else:
        return 0

print("Enter the string")
s = input()
st = isPalindrome(s)
print(st)
