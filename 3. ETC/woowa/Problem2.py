""""""
"""

"""

def solution(cryptogram):
    while isDuplicated(cryptogram):
        cryptogram = deleteDuplicatedAlphabet(cryptogram)
    return cryptogram

def deleteDuplicatedAlphabet(code):
    ans = ''
    previous = code[0]

    for i in range(1, len(code)):
        if previous != code[i]:
            ans += code[i-1]
            previous = code[i]


    return ans if code[-2] == code[-1] else ans + code[-1]

print(deleteDuplicatedAlphabet("aabbcc"))
print(deleteDuplicatedAlphabet("zyllyz"))
print(deleteDuplicatedAlphabet("kkk"))
print(deleteDuplicatedAlphabet("asdf"))




def isDuplicated(code):
    for i in range(1,len(code)):
        if code[i-1] == code[i]:
            return True
    return False

