'''
Write a function to find the longest common prefix string
amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters.
'''

strs = ["ab","a"]

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    Output = ""
    dict = {}

    # If there is no input there is no Output
    if len(strs) < 0 :
        return Output
    # if length is 1 then that is the answer
    if len(strs) == 1 :
        Output += strs[0]
        return Output
    # for every letter in the first word
    for i in range(len(strs[0])):
        # keep track of which word iterating through
        ind = len(strs) - 1
        # while there are words to iterate through
        while ind > 0 :
            # try to compare them
            try:
                # if they are the same, check the next word
                if strs[ind][i] == strs[0][i]:
                    ind -= 1
                # any other case - return collected result
                else:
                    return Output
            # if ran out of index - one of words is not long enough
            except IndexError :
                # therefore return collected result
                return Output
        # if while loop went through for all words add letter to the Output
        if ind == 0 :
            Output += strs[ind][i]
    # if all is checked and it didn't crash - return Output, all words the same
    return Output

print(longestCommonPrefix(strs))

# How Andris would do this
def andrisMethod(strs):
    result = ""
    if (len(strs) == 1):
        return strs[0]

    # for letter index in first word
    for i in range(len(strs[0])):
        # for each word in list
        for j in range(len(strs)):
            # if first word index is larger than length of word we are
            # looking at, OR letter of first word is not equal to l of this w
            if i > len(strs[j]) or strs[0][i] != strs[j][i]:
                # return collected result
                return result
        # otherwose, add the letter to result
        result += strs[0][i]
    # if ran through all of the words return collected wors (all the same)
    return result
