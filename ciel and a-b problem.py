A,B=map(int,input().split())
correct_answer = A - B
last_digit = correct_answer % 10

if last_digit == 9:
    wrong_answer = correct_answer - 1
else:
    wrong_answer = correct_answer + 1

print(wrong_answer)
