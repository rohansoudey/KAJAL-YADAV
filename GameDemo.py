from array import *
vals=[1,2,3,4,5,6,7,8,9]

counter=0
for i in vals:
    print(i,end=" ")
    if(counter==2):
        print("\n")
        counter=0
    else:
        counter=counter+1
# one for X

try:
    pos1=int(input("Player 1 Enter Position of your choice\n"))
    if(pos1<=9):
        for i in vals:
            if(i==pos1):
                vals[i-1]='X'
                counter=0
            else:
                for j in vals:
                    print(j,end=" ")
                    if(counter==2):
                        print("\n")
                        counter=0
                    else:
                        counter=counter+1
    elif(pos1>9 and pos1!='X' and pos1!='O'):
        print("Invalid Input")
        
    else:
        print("This Position is lock")
except:
    print("Invalid Input")


#one for O    
pos1=int(input("Player 2 Enter Position of your choice\n"))
if(pos1<=9):
    for i in vals:
        if(i==pos1 and pos1!='X'):
            vals[i-1]='O'
            counter=0
            for j in vals:
                print(j,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
elif(pos1>9):
    print("Invalid Input")
else:
    print("This Position is lock")

    #else:
        # print("This position is lock")
    
    

#two for X
pos1=int(input("Player 1 Enter Position of your choice\n"))
if(pos1<=9):
    for i in vals:
        if(i==pos1 and pos1!='O' and pos1!='X'):
            vals[i-1]='X'
            counter=0
            for j in vals:
                print(j,end=" ")
                if(counter==2):
                    print("\n")
                    counter=0
                else:
                    counter=counter+1
elif(pos1>9):
    print("Invalid Input")
else:
    print("This Position is lock")
#two for O

pos1=int(input("Player 2 Enter Position of your choice\n"))
if(pos1<=9):
    for i in vals:
        if(i==pos1 and pos1!='X' and pos1!='O'):
            vals[i-1]='O'
            counter=0
            for j in vals:
                print(j,end=" ")
                if(counter==2):
                    print("\n")
                    counter=0
                else:
                    counter=counter+1
elif(pos1>9):
    print("Invalid Input")
else:
    print("This Position is lock")
#three for X
if(vals[0]=='X' and vals[1]=='X' and vals[2]=='X' or vals[3]=='X' and vals[4]=='X' and vals[5]=='X' or vals[6]=='X' and vals[7]=='X' and vals[8]=='X' or
   vals[0]=='X' and vals[3]=='X' and vals[6]=='X' or vals[1]=='X' and vals[4]=='X' and vals[7]=='X' or vals[2]=='X' and vals[5]=='X' and vals[8]=='X' or
   vals[0]=='X' and vals[4]=='X' and vals[8]=='X' or vals[2]=='X' and vals[4]=='X' and vals[6]=='X'):
    print("Player one wins")
elif(vals[0]=='O' and vals[1]=='O' and vals[2]=='O' or vals[3]=='O' and vals[4]=='O' and vals[5]=='O' or vals[6]=='O' and vals[7]=='O' and vals[8]=='O' or
   vals[0]=='O' and vals[3]=='O' and vals[6]=='O' or vals[1]=='O' and vals[4]=='O' and vals[7]=='O' or vals[2]=='O' and vals[5]=='O' and vals[8]=='O' or
     vals[0]=='O' and vals[4]=='O' and vals[8]=='O' or vals[2]=='O' and vals[4]=='O' and vals[6]=='O'):
    print("Player two wins")
else:
    pos1=int(input("Player 1 Enter Position of your choice\n"))
    if(pos1<=9):
        for i in vals:
            if(i==pos1 and pos1!='O' and pos1!='X'):
                vals[i-1]='X'
                counter=0
                for j in vals:
                    print(j,end=" ")
                    if(counter==2):
                        print("\n")
                        counter=0
                    else:
                        counter=counter+1
    elif(pos1>9):
        print("Invalid Input")
    else:
        print("This Position is lock")
#three for O
if(vals[0]=='X' and vals[1]=='X' and vals[2]=='X' or vals[3]=='X' and vals[4]=='X' and vals[5]=='X' or vals[6]=='X' and vals[7]=='X' and vals[8]=='X' or
   vals[0]=='X' and vals[3]=='X' and vals[6]=='X' or vals[1]=='X' and vals[4]=='X' and vals[7]=='X' or vals[2]=='X' and vals[5]=='X' and vals[8]=='X' or
   vals[0]=='X' and vals[4]=='X' and vals[8]=='X' or vals[2]=='X' and vals[4]=='X' and vals[6]=='X'):
    print("Player one wins")
elif(vals[0]=='O' and vals[1]=='O' and vals[2]=='O' or vals[3]=='O' and vals[4]=='O' and vals[5]=='O' or vals[6]=='O' and vals[7]=='O' and vals[8]=='O' or
   vals[0]=='O' and vals[3]=='O' and vals[6]=='O' or vals[1]=='O' and vals[4]=='O' and vals[7]=='O' or vals[2]=='O' and vals[5]=='O' and vals[8]=='O' or
     vals[0]=='O' and vals[4]=='O' and vals[8]=='O' or vals[2]=='O' and vals[4]=='O' and vals[6]=='O'):
    print("Player two wins")
else:
    pos1=int(input("Player 2 Enter Position of your choice\n"))
    if(pos1<=9):
        for i in vals:
            if(i==pos1 and pos1!='X' and pos1!='O'):
                vals[i-1]='O'
                counter=0
                for j in vals:
                    print(j,end=" ")
                    if(counter==2):
                        print("\n")
                        counter=0
                    else:
                        counter=counter+1
    elif(pos1>9):
        print("Invalid Input")
    else:
        print("This Position is lock")
#Four of X
if(vals[0]=='X' and vals[1]=='X' and vals[2]=='X' or vals[3]=='X' and vals[4]=='X' and vals[5]=='X' or vals[6]=='X' and vals[7]=='X' and vals[8]=='X' or
   vals[0]=='X' and vals[3]=='X' and vals[6]=='X' or vals[1]=='X' and vals[4]=='X' and vals[7]=='X' or vals[2]=='X' and vals[5]=='X' and vals[8]=='X' or
   vals[0]=='X' and vals[4]=='X' and vals[8]=='X' or vals[2]=='X' and vals[4]=='X' and vals[6]=='X'):
    print("Player one wins")
elif(vals[0]=='O' and vals[1]=='O' and vals[2]=='O' or vals[3]=='O' and vals[4]=='O' and vals[5]=='O' or vals[6]=='O' and vals[7]=='O' and vals[8]=='O' or
   vals[0]=='O' and vals[3]=='O' and vals[6]=='O' or vals[1]=='O' and vals[4]=='O' and vals[7]=='O' or vals[2]=='O' and vals[5]=='O' and vals[8]=='O' or
     vals[0]=='O' and vals[4]=='O' and vals[8]=='O' or vals[2]=='O' and vals[4]=='O' and vals[6]=='O'):
    print("Player two wins")
else:
    pos1=int(input("Player 1 Enter Position of your choice\n"))
    if(pos1<=9):
        for i in vals:
            if(i==pos1 and pos1!='O' and pos1!='X'):
                vals[i-1]='X'
                counter=0
                for j in vals:
                    print(j,end=" ")
                    if(counter==2):
                        print("\n")
                        counter=0
                    else:
                        counter=counter+1
    elif(pos1>9):
        print("Invalid Input")
    else:
        print("This Position is lock")
#Four for O
if(vals[0]=='X' and vals[1]=='X' and vals[2]=='X' or vals[3]=='X' and vals[4]=='X' and vals[5]=='X' or vals[6]=='X' and vals[7]=='X' and vals[8]=='X' or
   vals[0]=='X' and vals[3]=='X' and vals[6]=='X' or vals[1]=='X' and vals[4]=='X' and vals[7]=='X' or vals[2]=='X' and vals[5]=='X' and vals[8]=='X' or
   vals[0]=='X' and vals[4]=='X' and vals[8]=='X' or vals[2]=='X' and vals[4]=='X' and vals[6]=='X'):
    print("Player one wins")
elif(vals[0]=='O' and vals[1]=='O' and vals[2]=='O' or vals[3]=='O' and vals[4]=='O' and vals[5]=='O' or vals[6]=='O' and vals[7]=='O' and vals[8]=='O' or
   vals[0]=='O' and vals[3]=='O' and vals[6]=='O' or vals[1]=='O' and vals[4]=='O' and vals[7]=='O' or vals[2]=='O' and vals[5]=='O' and vals[8]=='O' or
     vals[0]=='O' and vals[4]=='O' and vals[8]=='O' or vals[2]=='O' and vals[4]=='O' and vals[6]=='O'):
    print("Player two wins")
else:
    pos1=int(input("Player 2 Enter Position of your choice\n"))
    if(pos1<=9):
        for i in vals:
            if(i==pos1 and pos1!='X' and pos1!='O'):
                vals[i-1]='O'
                counter=0
                for j in vals:
                    print(j,end=" ")
                    if(counter==2):
                        print("\n")
                        counter=0
                    else:
                        counter=counter+1
    elif(pos1>9):
        print("Invalid Input")
    else:
        print("This Position is lock")
#Five of X
if(vals[0]=='X' and vals[1]=='X' and vals[2]=='X' or vals[3]=='X' and vals[4]=='X' and vals[5]=='X' or vals[6]=='X' and vals[7]=='X' and vals[8]=='X' or
   vals[0]=='X' and vals[3]=='X' and vals[6]=='X' or vals[1]=='X' and vals[4]=='X' and vals[7]=='X' or vals[2]=='X' and vals[5]=='X' and vals[8]=='X' or
   vals[0]=='X' and vals[4]=='X' and vals[8]=='X' or vals[2]=='X' and vals[4]=='X' and vals[6]=='X'):
    print("Player one wins")
elif(vals[0]=='O' and vals[1]=='O' and vals[2]=='O' or vals[3]=='O' and vals[4]=='O' and vals[5]=='O' or vals[6]=='O' and vals[7]=='O' and vals[8]=='O' or
   vals[0]=='O' and vals[3]=='O' and vals[6]=='O' or vals[1]=='O' and vals[4]=='O' and vals[7]=='O' or vals[2]=='O' and vals[5]=='O' and vals[8]=='O' or
     vals[0]=='O' and vals[4]=='O' and vals[8]=='O' or vals[2]=='O' and vals[4]=='O' and vals[6]=='O'):
    print("Player two wins")
else:
    pos1=int(input("Player 1 Enter Position of your choice\n"))
    if(pos1<=9):
        for i in vals:
            if(i==pos1 and pos1!='O' and pos1!='X'):
                vals[i-1]='X'
                counter=0
                for j in vals:
                    print(j,end=" ")
                    if(counter==2):
                        print("\n")
                        counter=0
                    else:
                        counter=counter+1
    elif(pos1>9):
        print("Invalid Input")
    else:
        print("This Position is lock")
   

