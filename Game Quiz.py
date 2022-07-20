print("Hello,Welcome to my computer quiz!....by insane")

user_interest=input("Do you wanna play game?\n")

if  user_interest.lower() != "yes":
    quit()

print("Okay!,Let's move to the game")
score =0
ans=input("What is the expansion of CPU?\n")

if ans.lower() =="central processing unit":
    print("Hurray!,Correct Answer")
    score +=1
else:
    print("Oops!,Wrong Answer")

ans=input("What is the expansion of ALGOL?\n")
if ans.lower() =="algorithmic language":
    print("Hurray!,Correct Answer")
    score +=1
else:
    print("Oops!,Wrong Answer")

ans=input("What is the expansion of XML?\n").lower()
if ans =="extensible markup language":
    print("Hurray!,Correct Answer")
    score +=1
else:
    print("Oops!,Wrong Answer")

ans=input("What is the expansion of XSS?\n")
if ans.lower() =="cross site scripting":
    print("Hurray!,Correct Answer")
    score +=1
else:
    print("Oops!,Wrong Answer")

ans=input("What is the expansion of MU?\n")
if ans.lower() =="memory unit":
    print("Hurray!,Correct Answer")
    score +=1
else:
    print("Oops!,Wrong Answer")

ans=input("What is the expansion of CU?\n")
if ans.lower() =="control unit":
    print("Hurray!,Correct Answer")
    score +=1
else:
    print("Oops!,Wrong Answer")

print("you answered" + str(score) + "Correct")
print("your answer percentage" + str((score/6)*100) + "%")
