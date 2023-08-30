scores = input("enter list of student scores: ").split()

for n in range(0, len(scores)):
    scores[n] = int(scores[n])

maxScore = 0

for score in scores:
    if score > maxScore:
        maxScore = score
print("the max score is : ",maxScore)
