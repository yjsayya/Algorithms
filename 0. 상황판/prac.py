
def solution(a,b):
    cal = {
        1:31, 2:29, 3:31, 4:30, 5:31,
        6:30, 7:31, 8:31, 9:30, 10:31,
        11:30, 12:31
    }
    days = {
        1 : "FRI", 2: "SAT", 3: "SUN", 4: "MON",
        5: "TUE", 6: "WED", 0: "THU"
    }
    tot = 0
    for i in range(1,a):
        tot += cal[i]

    return days[(tot+b)%b]
