'''
Given a string s containing just the characters
'(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: false

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''
#String -> Boolean

#Output True if All open brackets are closed in
#correct order with correct brackets.

s = "(([]){})" #Input string

#Every bracket must be closed by the correct pair bracket.
#Internal brackes must be closed before external brackets.
#There is no information in between.

def isValid (s) :
    #A list to temporary hold the brackets.
    #This is to keep the count of open and clsoed brackets.
    TempHolderFolder = []

    #condition of pairs opening string & closing string
    so = ["(","[","{"]
    sc = [")","]","}"]

    for i in range(len(s)) :
        #if it is closing string
        if s[i] in so :
            TempHolderFolder.append(s[i])
        if s[i] in sc :
            #getting index of closed bracket from closed bracket list
            #note that this is the same index as in open bracket list
            sci = sc.index(s[i])
            #if there is no pair - False
            if so[sci] not in TempHolderFolder :
                return False
            #if there is a pair add to list
            if so[sci] in TempHolderFolder :
                TempHolderFolder.append(sc[sci])
            #locating each bracket (furthest and last in list)
            idel1 = len(TempHolderFolder) - TempHolderFolder[::-1].index(sc[sci]) - 1 #from right first closed bracket
            idel2 = len(TempHolderFolder) - TempHolderFolder[::-1].index(so[sci]) - 1 #furthest first open bracket
            if (idel1 - idel2) % 2 != 1 :
                return False
            #since in between is an even number these brackets can be removed.
            del TempHolderFolder[idel1]
            del TempHolderFolder[idel2]

    #Once all of the loops are done it is time to check if TempHolderFolder is empty.
    #If not, something didn't have a pair.
    if len(TempHolderFolder) != 0 :
        return False
    else :
        return True

print(isValid (s))

'''
#Someone else's code from Leetcode.
#could have done this way - it loops through until all adjacent pairs are gone.
#Therefore, each next loop creates a hole.

def isValid(s):
    s1 = ""
    s = s
    while(s1!=s):
        s1=s
        s = s.replace("()", "")
        s = s.replace("[]", "")
        s = s.replace("{}", "")
    return s==""
print(isValid (s))
'''
'''
#This does not check the internal strings but it needs to.

#Therefore, need to check every pair not every i of the string.
def isValid (s) :
    #cannot have a pair if there is an uneven amount of characters
    if len(s) % 2 != 0 :
        return False
    # checked character pairs
    CheckedValues = {}
    #for every character sum that character and it's pair and compare
    #if there is the same amount of each
    for i in range(len(s)) :
        # if value has already been checked we are jumping to next character
        if s[i] in CheckedValues : continue

        string1count = 0
        string2count = 0

        #condition of pairs
        if s[i] == "(" :
            scs2 = ")"
        if s[i] == ")" :
            scs2 = "("
        if s[i] == "[" :
            scs2 = "]"
        if s[i] == "]" :
            scs2 = "["
        if s[i] == "{" :
            scs2 == "}"
        if s[i] == "}" :
            scs2 == "{"

        #counting each variable count in the string
        if s[i] in s :
            string1count = string1count + 1
        if scs2 in s :
            string2count = string2count + 1
        #Checking the counts, if they are different it is auto False
        if string1count != string2count :
            return False
    else : True

print(isValid (s))
'''

'''
#if were only next to each other as initial instructions said.
        if i+1 < len(s) :
            if i % 2 != 0 : continue
            print(s[i] + s[i+1])
            #If any of the valid inputs match the pair continue checking
            if s[i] + s[i+1] in [s1, s2, s3] : continue
            #If input did not match the above pair return False
            else :
                return False
    return True
'''
