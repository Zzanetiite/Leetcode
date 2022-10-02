'''
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left,
it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.


Constraints:

-231 <= x <= 231 - 1


Follow up: Could you solve it without converting the integer to a string?
'''

x = 1234

# Solution I came up with. It is 5x slower than others
# but uses a bit less memory.
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    if x < 0 :
        return False
    if x == 0 :
        return True
    if x%10 == 0 :
        return False

    sx = str(x)

    if len(sx)%2 == 1 :
        halfRange = (len(sx) + 1 ) / 2
    else :
        halfRange = len(sx) / 2

    i = 0
    while halfRange > 0 :
        halfRange -= 1
        if sx[i] != sx[len(sx) - 1 - i]:
            return False
        print(sx[i], sx[len(sx) - 1 - i], i)
        i += 1

    return True

print(isPalindrome(x))


# Solution from Leetcode - [::-1] reverses a string
def isPalindrome2(x: int) :
	if x < 0:
		return False

	return str(x) == str(x)[::-1]

print(isPalindrome2(x))


# Non-integer solution from leetcode
def isPalindrome3(x: int) :
	if x<0:
		return False

	inputNum = x
	newNum = 0
	while x>0:
		#print (x%10)
		newNum = newNum * 10 + x%10
		x = x//10
		#print(newNum, x)
	return newNum == inputNum

print(isPalindrome3(x))
