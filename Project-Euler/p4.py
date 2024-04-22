'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def isPalindrome(num):
    if num == num[::-1]:
        return True
    return False
x = 0
for i in range(999, 99, -1):
    
    for j in range(i, 99, -1):
        
        num = str(i*j)
        if isPalindrome(num) and i*j > x:
            x = i * j
            print(f"{i} * {j} = {x}")
            break
    

