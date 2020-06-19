def calc(n):
    cnt = 1
    while n > 0:
        if(n <= cnt):
            print("Bob")
            break
        n -= cnt
        if(n <= 2 * cnt):
            print("Nelson")
            break
        n -= 2 * cnt
        cnt += 1

n = int(input())

calc(n)