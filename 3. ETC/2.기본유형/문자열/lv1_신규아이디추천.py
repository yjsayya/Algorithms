# 2021 kakao blind recruitment
# 3단계 푸는거 한번 보고
# if, elif 잘 고려해야하는데 --> 이걸 못찾아서 계속 오류 봄 시부레


# 디테일을 잡았어야하는 문제!!!
def solution(new_id):
    specialChar = ['-', '_', '.']

    # 1단계
    new_id = new_id.lower()

    # 2단계
    for i in new_id:
        if not i.isalpha() and not i.isdigit() and i not in specialChar:
            new_id = new_id.replace(i, "")

    # 3단계
    # dot_list = []
    # for j in new_id:
    #     if len(dot_list) == 0:
    #         if j == '.':
    #             dot_list.append(j)
    #     elif len(dot_list) == 1:
    #         if j == '.':
    #             dot_list.append(j)
    #         else:
    #             dot_list.clear()
    #     else:
    #         if j == '.':
    #             dot_list.append(j)
    #         else:
    #             new_id = new_id.replace("".join(dot_list), '.')
    #             dot_list.clear()
    while new_id.find('..') != -1:
        new_id = new_id.replace('..', '.')

    # 4단계
    if len(new_id) != 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) != 0 and new_id[-1] == '.':
        new_id = new_id[:-1]

    # 5단계
    if len(new_id) == 0:
        new_id = "a"

    # 6단계
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    # 7단계
    if len(new_id) < 3:
        last_word = new_id[-1]
        while len(new_id) < 3:
            new_id += last_word

    return new_id