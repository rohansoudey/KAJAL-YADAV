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
pos1=int(input("Player 1 Enter Position of your choice\n"))
for i in vals:
    if(i==pos1):
        #print("inside if 1 "+pos1)
        vals[i-1]='X'
        counter=0
        for j in vals:
            print(j,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    #else:
        #print("This position is lock")


#one for O    
pos1=int(input("Player 2 Enter Position of your choice\n"))
for i in vals:
    if(i==pos1 and pos1!='X'):
        #print("inside if 1 "+pos1)
        vals[i-1]='O'
        counter=0
        for j in vals:
            print(j,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1


    #else:
        # print("This position is lock")
    
    

#two for X
pos1=int(input("Player 1 Enter Position of your choice\n"))
for i in vals:
    if(i==pos1 and pos1!='O' and pos1!='X
       '):
        #print("inside if 1 "+pos1)
        vals[i-1]='X'
        counter=0
        for j in vals:
            print(j,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
#two for O
pos1=input("Player 2 Enter Position of your choice\n")
if(pos1=='1'):
    if(vals[0]!='X' and vals[0]!='O'):
        vals[0]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1

    else:
        print("This position is lock")
    
    
elif(pos1=='2'):
    if(vals[1]!='X' and vals[1]!='O'):
        vals[1]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
    
elif(pos1=='3'):
    if(vals[2]!='X' and vals[2]!='O'):
        vals[2]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")

elif(pos1=='4'):
    if(vals[3]!='X' and vals[3]!='O'):
        vals[3]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='5'):
    if(vals[4]!='X' and vals[4]!='O'):
        vals[4]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='6'):
    if(vals[5]!='X' and vals[5]!='O'):
        vals[5]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")

elif(pos1=='7'):
    if(vals[6]!='X' and vals[6]!='O'):
        vals[6]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='8'):
    if(vals[7]!='X' and vals[7]!='O'):
        vals[7]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='9'):
    if(vals[8]!='X' and vals[8]!='O'):
        vals[8]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")

#three for X
pos1=input("Player 1 Enter Position of your choice\n")
if(pos1=='1'):
    if(vals[0]!='X' and vals[0]!='O'):
        vals[0]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")

elif(pos1=='2'):
    if(vals[1]!='X' and vals[1]!='O'):
        vals[1]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='3'):
    if(vals[2]!='X' and vals[2]!='O'):
        vals[2]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")

elif(pos1=='4'):
    if(vals[3]!='X' and vals[3]!='O'):
        vals[3]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='5'):
    if(vals[4]!='X' and vals[4]!='O'):
        vals[4]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='6'):
    if(vals[5]!='X' and vals[5]!='O'):
        vals[5]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='7'):
    if(vals[6]!='X' and vals[6]!='O'):
        vals[6]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='8'):
    if(vals[7]!='X' and vals[7]!='O'):
        vals[7]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='9'):
    if(vals[8]!='X' and vals[8]!='O'):
        vals[0]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
#three for O
pos1=input("Player 2 Enter Position of your choice\n")
if(pos1=='1'):
    if(vals[0]!='X' and vals[0]!='O'):
        vals[0]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1

    else:
        print("This position is lock")
    
    
elif(pos1=='2'):
    if(vals[1]!='X' and vals[1]!='O'):
        vals[1]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
    
elif(pos1=='3'):
    if(vals[2]!='X' and vals[2]!='O'):
        vals[2]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")

elif(pos1=='4'):
    if(vals[3]!='X' and vals[3]!='O'):
        vals[3]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='5'):
    if(vals[4]!='X' and vals[4]!='O'):
        vals[4]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='6'):
    if(vals[5]!='X' and vals[5]!='O'):
        vals[5]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")

elif(pos1=='7'):
    if(vals[6]!='X' and vals[6]!='O'):
        vals[6]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='8'):
    if(vals[7]!='X' and vals[7]!='O'):
        vals[7]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='9'):
    if(vals[8]!='X' and vals[8]!='O'):
        vals[8]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
#Four of X
pos1=input("Player 1 Enter Position of your choice\n")
if(pos1=='1'):
    if(vals[0]!='X' and vals[0]!='O'):
        vals[0]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")

elif(pos1=='2'):
    if(vals[1]!='X' and vals[1]!='O'):
        vals[1]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='3'):
    if(vals[2]!='X' and vals[2]!='O'):
        vals[2]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")

elif(pos1=='4'):
    if(vals[3]!='X' and vals[3]!='O'):
        vals[3]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='5'):
    if(vals[4]!='X' and vals[4]!='O'):
        vals[4]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='6'):
    if(vals[5]!='X' and vals[5]!='O'):
        vals[5]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='7'):
    if(vals[6]!='X' and vals[6]!='O'):
        vals[6]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='8'):
    if(vals[7]!='X' and vals[7]!='O'):
        vals[7]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='9'):
    if(vals[8]!='X' and vals[8]!='O'):
        vals[0]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
#Four for O
pos1=input("Player 2 Enter Position of your choice\n")
if(pos1=='1'):
    if(vals[0]!='X' and vals[0]!='O'):
        vals[0]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1

    else:
        print("This position is lock")
    
    
elif(pos1=='2'):
    if(vals[1]!='X' and vals[1]!='O'):
        vals[1]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
    
elif(pos1=='3'):
    if(vals[2]!='X' and vals[2]!='O'):
        vals[2]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")

elif(pos1=='4'):
    if(vals[3]!='X' and vals[3]!='O'):
        vals[3]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='5'):
    if(vals[4]!='X' and vals[4]!='O'):
        vals[4]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='6'):
    if(vals[5]!='X' and vals[5]!='O'):
        vals[5]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")

elif(pos1=='7'):
    if(vals[6]!='X' and vals[6]!='O'):
        vals[6]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='8'):
    if(vals[7]!='X' and vals[7]!='O'):
        vals[7]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='9'):
    if(vals[8]!='X' and vals[8]!='O'):
        vals[8]='O'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
#Five of X
pos1=input("Player 1 Enter Position of your choice\n")
if(pos1=='1'):
    if(vals[0]!='X' and vals[0]!='O'):
        vals[0]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")

elif(pos1=='2'):
    if(vals[1]!='X' and vals[1]!='O'):
        vals[1]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='3'):
    if(vals[2]!='X' and vals[2]!='O'):
        vals[2]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")

elif(pos1=='4'):
    if(vals[3]!='X' and vals[3]!='O'):
        vals[3]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='5'):
    if(vals[4]!='X' and vals[4]!='O'):
        vals[4]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='6'):
    if(vals[5]!='X' and vals[5]!='O'):
        vals[5]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='7'):
    if(vals[6]!='X' and vals[6]!='O'):
        vals[6]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='8'):
    if(vals[7]!='X' and vals[7]!='O'):
        vals[7]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
elif(pos1=='9'):
    if(vals[8]!='X' and vals[8]!='O'):
        vals[8]='X'
        counter=0
        for i in vals:
            print(i,end=" ")
            if(counter==2):
                print("\n")
                counter=0
            else:
                counter=counter+1
    else:
        print("This position is lock")
if(vals[0]=='X' and vals[1]=='X' and vals[2]=='X' or vals[3]=='X' and vals[4]=='X' and vals[5]=='X' or vals[6]=='X' and vals[7]=='X' and vals[8]=='X' or
   vals[0]=='X' and vals[3]=='X' and vals[6]=='X' or vals[1]=='X' and vals[4]=='X' and vals[7]=='X' or vals[2]=='X' and vals[5]=='X' and vals[8]=='X' or
   vals[0]=='X' and vals[4]=='X' and vals[8]=='X' or vals[2]=='X' and vals[4]=='X' and vals[6]=='X'):
    print("Player one wins")
elif(vals[0]=='O' and vals[1]=='O' and vals[2]=='O' or vals[3]=='O' and vals[4]=='O' and vals[5]=='O' or vals[6]=='O' and vals[7]=='O' and vals[8]=='O' or
   vals[0]=='O' and vals[3]=='O' and vals[6]=='O' or vals[1]=='O' and vals[4]=='O' and vals[7]=='O' or vals[2]=='O' and vals[5]=='O' and vals[8]=='O' or
     vals[0]=='O' and vals[4]=='O' and vals[8]=='O' or vals[2]=='O' and vals[4]=='O' and vals[6]=='O'):
    print("Player two wins")
else:
    print("Match Draw")
   

