answer = []

num, sequence = map(int, input().split())

queue = [i for i in range(1, num + 1)]

kill = sequence - 1

for i in range(num):
    answer.append(queue.pop(kill))
    kill += sequence - 1
    if len(queue) > 0 : kill %= len(queue)

print(f"<" + ", ".join(list(map(str, answer))) + ">")