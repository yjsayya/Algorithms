'''
진법 변환하는 방법 python으로도 꼭 알아두자 

bin() - 2진수로 변환 : '0b ~~'형태의 String으로 반환
oct() - 8진수로 변환 : '0o ~~'형태의 String으로 반환
hex() - 16진수로 변환 : '0x ~~'형태의 String으로 반환

int(숫자String, x진수) --> x진수의 문자열 형태로 변환
'''

def solution(s):
    
    change = 0
    rmvzro = 0
    
    while s != '1':
        
        while '0' in s:
            rmvzro += s.count('0')
            s = s.replace('0', '')
            
        s = bin(len(s))[2:]
        change += 1
    
    return [change, rmvzro] 