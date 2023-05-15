'''
날짜, 알파벳 같은 것 처럼 개수가 몇개 없는 것은 아싸리 이렇게 만들어놓고
하는것이 더 이득인 듯 하다 
'''

def solution(a, b):
    
    month = {'1':'31', '2':'29', '3':'31', '4':'30', '5':'31', 
            '6':'30', '7':'31', '8':'31', '9':'30', '10':'31', 
            '11':'30', '12':'31'}
    total = 0
    
    for i in range(1, a):
        total += int(month[str(i)])
    
    total += b
    
    if total % 7 == 0:
        return "THU"
    elif total % 7 == 1:
        return "FRI"
    elif total % 7 == 2:
        return "SAT"
    elif total % 7 == 3:
        return "SUN"
    elif total % 7 == 4:
        return "MON"
    elif total % 7 == 5:
        return "TUE"
    elif total % 7 == 6:
        return "WED"