print("wellcome to love calculator\n")

yourName = input("what is your name: ")
theirName = input("what are their Name: ")

combine = yourName.lower() + theirName.lower()
t = combine.count("t")
r = combine.count("r")
u = combine.count("u")
e = combine.count("e")

totalTrue = t+r+u+e

l = combine.count("l")
o = combine.count("o")
v = combine.count("v")
e = combine.count("e")

totallove = l+o+v+e
lovescorestr = str(totalTrue) + str(totallove)
lovescore = int(lovescorestr)

print(f"your love percentage is {lovescore}%")


if lovescore < 10 or lovescore > 90:
    print("you go to gether")
elif lovescore >= 40 and lovescore <= 50:
    print("your are alright")
else:
    print("divorce")