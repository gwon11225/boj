list_1 = [ x for x in range(1,31)]
student = []
answer = []
for _ in range(28):
    a = int(input())
    student.append(a)
for i in range(30):
    if list_1[i] not in student:
        answer.append(list_1[i])
if answer[0] > answer[1]:
    print(answer[1])
    print(answer[0])
elif answer[0] < answer[1]:
    print(answer[0])
    print(answer[1])