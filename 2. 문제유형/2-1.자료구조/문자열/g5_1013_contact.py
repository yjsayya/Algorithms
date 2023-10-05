"""
    << 정규표현식 >>
    . : 임의의 한 문자와 매치됩니다.
    * : 바로 앞의가 0부터 무한대로 반복됩니다.
    + : 바로 앞의 문자가 최소 1번부터 무한대로 반됩니다.
    ? : 바로 앞의 문자가 0 또는 1회 등장합니다.
    ^ : 문자열의 맨 처음과 매치됩니다.
    $ : 문자열의 끝과 매치됩니다7. [] : 대괄호 안에 문자 집합을 만들어 매치합니다.
    | : A|B와 같이 사용되며 A 또는 B 매치됩니다.
    () : 괄호 안의 정규표현식을 그룹으로 묶습니다.

    이메일 정규 표현식 : \w+@\w+\.\w+(?:\.\w+)?
    ?: --> 선택적

    \w = [a-zA-Z0-9_]

"""

import re

def is_valid_pattern(signal):
    pattern = re.compile("(100+1+|01)+")
    match = pattern.fullmatch(signal)
    if match:
        return "YES"
    else:
        return "NO"

t = int(input())
answer = []
for _ in range(t):
    n = input()
    answer.append(is_valid_pattern(n))

for i in answer:
    print(i)

