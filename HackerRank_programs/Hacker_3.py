if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(student_marks)
    student_score = student_marks[query_name]
    print(student_score)
    avg_marks=(student_score[0]+student_score[1]+student_score[2])/3
    print("%.2f"%avg_marks)
