row1 = ["☐","☐","☐"]
row2 = ["☐","☐","☐"]
row3 = ["☐","☐","☐"]
map = [row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}")
posision = input("where did you want to put the treasure: ")

hori = int(posision[0])
vert = int(posision[1])

select_row = map[hori - 1]
select_row[vert - 1] = "☒"



print(f"{row1}\n{row2}\n{row3}")


