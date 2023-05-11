# 카카오 채용연계형 인턴십 문제

# hash를 통해서 푸는 문제였는데 안 풀어봤더니 ㅇㅈㄹ이 나버림 
# 꼭 기억하자 몇개 없을 때는 이런식으로 미리 dic{} 만들어서 풀면 될 듯


# 내가 첫번째로 푼 풀이
    # --> 아주 개 ㅈㄹ을 했네 이윤종 ㅂㅅ
def solution(s):
    answer = []
    
    while len(s) != 0:
        if s[0] == 'z':
            answer.append('0')
            s = s[4:]
        elif s[0] == 'o':
            answer.append('1')
            s = s[3:]
        elif s[0] == 't' and s[1] == 'w':
            answer.append('2')
            s = s[3:]
        elif s[0] == 't' and s[1] == 'h':
            answer.append('3')
            s = s[5:]
        elif s[0] == 'f' and s[1] == 'o':
            answer.append('4')
            s = s[4:]
        elif s[0] == 'f' and s[1] == 'i':
            answer.append('5')
            s = s[4:]
        elif s[0] == 's' and s[1] == 'i':
            answer.append('6')
            s = s[3:]
        elif s[0] == 's' and s[1] == 'e':
            answer.append('7')
            s = s[5:]
        elif s[0] == 'e':
            answer.append('8')
            s = s[5:]
        elif s[0] == 'n':
            answer.append('9')
            s = s[4:]
        else:
            answer.append(s[0])
            s = s[1:]
            
        
    return int("".join(answer))


# 이렇게 푸는게 가장 깔끔한 풀이인 듯 
def solution1(s):
    num_dic = {"zero":"0", "one":"1", "two":"2", "three":"3", "four":"4", "five":"5", "six":"6", "seven":"7", "eight":"8", "nine":"9"}
    answer = s
    for key, value in num_dic.items():
        answer = answer.replace(key, value)
    return int(answer)


# 이런 풀이도 있네
def solution2(s):
    words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

    for i in range(len(words)):
        s = s.replace(words[i], str(i))

    return int(s)
