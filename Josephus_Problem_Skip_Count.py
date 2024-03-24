Total_Ele = int(input ("Enter the Number of elements "))
Init_Pos = int(input ("Enter the starting position ")) - 1
Skip_Count = int(input ("Enter the number of elements to skip "))

Elements = []
a=1
while a <= Total_Ele:
    Elements.append(a)
    a = a+1

while Init_Pos < Total_Ele:
    j = 1
    while j <= Skip_Count:
        point1 = Elements[Init_Pos] % Total_Ele
       # print("point1 " + str(point1))
        point2 = (Elements[point1]) % Total_Ele
      #  print("point2 " + str(point2))
        Elements[point1] = 0
        Elements[Init_Pos] = point2
        if Init_Pos == point2:
            break

        j = j + 1
      #  print (j)

    if Init_Pos == point2:
        print ("Surviving Element is " + str(Init_Pos+1))
        break
    else:
        Init_Pos = point2


