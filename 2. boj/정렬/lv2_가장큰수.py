

'''
    아이디어
        - 1000이하니깐
        *3 해서 비교하면 되는거임 
'''
def solution(numbers):
    
    li = [str(i) for i in numbers]    
    li.sort(key= lambda x : x*3, reverse=True)
    
    return str(int(''.join(li)))    