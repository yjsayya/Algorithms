def solution(people, limit):
    cnt = 0
    people.sort()
    ship = []

    for i in range(len(people)):
        next_i = i + 1

        if next_i == len(people):
            break

        if len(ship) == 2:
            ship.clear()
            continue

        ship.append(people[i])
        if people[i] + people[next_i] > limit:
            ship.clear()
        else:
            ship.append(people[next_i])

        cnt += 1
    if len(ship) == 0:
        return cnt + 1
    else:
        return cnt

print(solution([40,40,40,90,80,70], 240))