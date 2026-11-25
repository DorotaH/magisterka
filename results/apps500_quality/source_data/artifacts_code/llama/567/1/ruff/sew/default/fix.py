from sys import stdin


def main():
    n = int(stdin.readline())
    prizes = list(map(int, stdin.readline().split()))
    def  find_min_time():
        if n == 1:
            return abs(prizes[0] - 1) + abs(1000000 - prizes[0])
        
        left = 1
        right = prizes[0]
        last_prize = time = 0
        for i in range(1, n):
            if prizes[i] - prizes[i - 1] <= right - left:
                time += max(abs(prizes[i] - left), abs(right - prizes[i]))
                left = prizes[i]
            else:
                time += max(abs(prizes[i - 1] - left), abs(right - prizes[i - 1])
                           ) + abs(prizes[i] - right)
                right = prizes[i]
            last_prize=prizes[i]
        
        return time+max(abs(prizes[n-1]-left), abs(right-prizes[n-1]))

    print(find_min_time())

if __name__=="__main__":
    main()