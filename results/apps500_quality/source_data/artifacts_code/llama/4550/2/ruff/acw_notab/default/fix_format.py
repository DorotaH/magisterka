def check_candy_distribution():
    a, b, c = map(int, input().split())

    total_candies = a + b + c
    if total_candies % 2 != 0:
        return "No"

    total_candies_per_student = total_candies // 2
    student_a_candies = a
    student_b_candies = 0

    if total_candies_per_student < a:
        student_a_candies = total_candies_per_student
        student_b_candies = a - total_candies_per_student
    if total_candies_per_student < b:
        student_a_candies += b - total_candies_per_student
        student_b_candies += b - (total_candies_per_student - student_a_candies)
    return "No" if total_candies_per_student < c else "Yes"


print(check_candy_distribution())
