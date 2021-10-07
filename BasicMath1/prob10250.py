import sys


def room_number(floor: int, room: int, guest_num: int) -> str:
    floors = list(range(1, floor+1))
    rooms = list(range(1, room+1))
    f_ind = 0
    r_ind = 0
    f_ind = guest_num % floor
    if f_ind == 0:
        f_ind = -1
        r_ind = guest_num // floor - 1
    else:
        f_ind -= 1
        r_ind = guest_num // floor
    floor_num = floors[f_ind]
    room_num = rooms[r_ind]
    if room_num < 10:
        result = str(floor_num) + '0' + str(room_num)
    else:
        result = str(floor_num) + str(room_num)
    return result


if __name__ == '__main__':
    t = int(sys.stdin.readline().rstrip())
    r = list()
    for i in range(t):
        h, w, n = map(int, sys.stdin.readline().rstrip().split())
        r.append(room_number(h, w, n))
    print(*r, sep='\n')
