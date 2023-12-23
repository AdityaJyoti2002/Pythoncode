n = int(input())

feelings = []
for i in range(n):
    if i % 2 == 0:
        feelings.append("I hate")
    else:
        feelings.append("I love")

    if i < n - 1:
        feelings.append("that")

feelings.append("it")
result = " ".join(feelings)
print(result)
