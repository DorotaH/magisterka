
def  get_time(time_str):
    h, m = map(int, time_str.split(':'))
    return (h, m)

def  get_minutes(time_str):
    h, m = get_time(time_str)
    return h * 60 + m

def  get_time_str(minutes):
    h = minutes // 60
    m = minutes % 60
    return f"{h:02d}:{m:02d}"

def  get_midpoint(h1, m1, h2, m2):
    total_minutes = get_minutes(f"{h2}:{m2}") - get_minutes(f"{h1}:{m1}")
    midpoint_minutes = total_minutes // 2
    return get_time_str(midpoint_minutes)

def  main():
    time1, time2 = input().split()
    h1, m1 = get_time(time1)
    h2, m2 = get_time(time2)
    print(get_midpoint(h1, m1, h2, m2))

if __name__ == "__main__":
    main()