
# 이것도 --> 한바퀴 도는 개념이니깐 나눈 나머지 개념 잘 이용하면 좋을 것 같다 


# 내가 푼 풀이 인데 
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



# 이게 가장 깔끔한 풀이인 것 같다
def getDayName(a,b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return day[(sum(month[:a-1])+b-1)%7]