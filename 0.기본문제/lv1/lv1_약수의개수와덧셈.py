



# 내 풀이 - 나는 약수 개수 구하는 함수를 따로 만든 다음에 풀었음 
def findys(n):
    cnt = 0
    for i in range(1,n+1):
        if n % i == 0:
            cnt += 1
    
    return cnt

def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        if findys(i) % 2 == 0:
            answer += i
        else:
            answer -= i
    
    return answer


print(findys(13))



# 다른 사람 풀이 인데 인상적이서 가지고 왔다 ㅇㅋ
def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        if int(i**0.5)==i**0.5:
            answer -= i
        else:
            answer += i
    return answer


# 이런 형변환으로 푸는게 진짜 센스가 좋은 듯 ?!
# 제곱수의 약수의 개수는 홀수개이다!! 
# 이 점을 잘 이용하면 될 것 같다 ㅇㅋ 

# 약수
# 소수
# 제곱수 

# 이 세가지 개념 잘 잡아놔야하지 않을까 싶다? 
