from random import randint
treasure_pos = randint(0,100)
flg = "true"
num_attemp = 0
lst = []
while flg == "true":
    x = int(input("Please enter your attempt number between 0 and 100 : ")) 
    if x>=0 and x<=100:
        lst.append(x)
        print(lst)
        num_attemp+=1
        if x == treasure_pos:
            print("Congratulations, you have found the treasure")
            print("Your Number of attempts is : {}".format(num_attemp))
            flg = "false"
        elif num_attemp == 1:
            if (x > treasure_pos and x <= treasure_pos+10) or (x >= treasure_pos-10 and x < treasure_pos):
                print("Close")
            else:
                print("Faraway")
        else:
            if abs(x-treasure_pos) < abs(lst[-2]-treasure_pos):
                print("closer")
            else:
                print("farther")
    else:
        print("you'r out of range, please try again")