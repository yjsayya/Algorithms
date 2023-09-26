""""""
"""
    테스트 케이스 1번 15번을 처음 풀었을 때 통과가 되지 않았따 
"""

# 1. 내가 푼 첫번째 풀이
def solution1(genres, plays):

    gen_dic = dict()
    total_play = dict()
    for i in range(len(genres)):
        gen = genres[i]
        play = plays[i]

        if gen in total_play:
            total_play[gen] += play
            gen_dic[gen].append((play,i))
        else:
            total_play[gen] = play
            gen_dic[gen] = [(play,i)]
    total_play = sorted(total_play, key= lambda x : -total_play[x])
    print(gen_dic)
    print(total_play)

    ans = []
    for k in total_play:
        li = sorted(gen_dic[k], key=lambda x : x[0])
        for _ in range(2):
            if li:
                ans.append(li.pop()[1])

    return ans

# 2. 다른 사람 풀이
def solution2(genres, plays):
    answer = []
    total = {}  # 장르별 총 재생횟수
    gen_dic = {}  # 장르별 [재생횟수&고유번호]

    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genres[i] in total.keys():
            total[genres[i]] += plays[i]
            gen_dic[genres[i]].append((plays[i], i))
        else:
            total[genres[i]] = plays[i]
            gen_dic[genre] = [(play, i)]

    total = sorted(total.items(), key=lambda x: x[1], reverse=True)

    # print(total)
    # print(gen_dic)

    for key in total:
        playlist = gen_dic[key[0]]
        playlist = sorted(playlist, key=lambda x: x[0], reverse=True)
        for i in range(len(playlist)):
            if i == 2:
                break
            answer.append(playlist[i][1])

        # print(playlist)
    return answer

# solution1(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
solution2(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500])
