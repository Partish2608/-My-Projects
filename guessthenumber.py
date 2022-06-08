print("\nHey, Welcome To My Game!")
print("Kindly Enter Player 1's Name:")
p1 = str(input())
print("Kindly Enter Player 2's Name:")
p2 = str(input())
print("\n")
nog = 1
print("-->",p1,", Please Enter a Number From '1 to 100'<<")
x = int(input())
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n>>Now, Enter the Number of Chances you want to give!<<")
y = int(input())
print("\n>>You Have",y,"Chances...<<")
while(nog<= y):
    gn = int(input("--> Guess The Number:<-- \n"))
    if gn<x:
        print(">>",p2," Entered a Smaller Number!<< \n")
    elif gn>x:
        print(">>",p2," Entered a Greater Number!<< \n")
    else:
        print(p2," Won!😊 \n")
        print(p2 ,"took",nog,"number of chances...")
        break
    print(y-nog,"Number of guesses left\n")
    nog = nog + 1
    if (nog>y):
        print(p1,"Won 😊")
        print(">>The Number Was<<",x)