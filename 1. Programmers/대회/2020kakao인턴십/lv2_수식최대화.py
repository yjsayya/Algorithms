''''''
"""
    구현 + 문자열 문제
    
    -- ㅈㄴ 어렵다 시부레 ...
    -- 카카오는 진짜 너무 어렵다 시발 ...
    ** eval() 함수 있다는걸 깜빡하고 있었네 ...
"""
def solution(expression):
    operations = [('+', '-', '*'),('+', '*', '-'),('-', '+', '*'),('-', '*', '+'),('*', '+', '-'),('*', '-', '+')]
    answer = []
    for op in operations:
        a = op[0]
        b = op[1]
        temp_list = []
        for e in expression.split(a):
            temp = [f"({i})" for i in e.split(b)]
            temp_list.append(f'({b.join(temp)})')
        answer.append(abs(eval(a.join(temp_list))))
    return max(answer)



