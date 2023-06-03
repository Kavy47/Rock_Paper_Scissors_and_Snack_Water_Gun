
print("it is snack water gun or rock paper or scissors\n")
import random
choose = int(input("Choose what do you want to play SWG or RPS\nIf you want play swg than enter 1 \nIf you want to play RPS enter 2\n\nEnter here : "))


def s_w_g():
    u = input("\nselect your choice type s for snack , w for water and g for gun : ")
    
    if("s" in u):
        rplace = u.replace("s","Snack")
    if "w"in u:
        rplace = u.replace("w","Water")
    if "g" in u:
        rplace = u.replace("g","Gun")
    

    print(f"\nYou selected :- {rplace}")
    c = random.randint(1,3)
    if c==1:
        print("Computer selected :- Snack")
    elif c==2:
        print("Computer selected :- Water")
    elif c==3:
        print("Computer selected :- Gun")
    score = 0
    
    if c==1 and "s" in u or c==2 and "w" in u or c==3 and "g" in u:
        result = "Tie"
        print("\nDraw!!")
        

    elif c==1 and "g" in u or c==3 and "w" in u or c==2 and "s" in u:
        result = "won"
        print("\nYou Won!!!")
        

    elif c==1 and "w" in u or c==2 and "g" in u or c==3 and "s" in u:
        result = "Lose"
        print("\nComputer Won!")
        

def r_p_s():
    u = input("\nselect your choice type r for rock , p for paper  and s for scissos :- ")
    
    if("r" in u):
        rplace = u.replace("r","Rock")
    if "p"in u:
        rplace = u.replace("p","Paper")
    if "s" in u:
        rplace = u.replace("s","scissors")
    print(f"\nYou selected :- {rplace}")
    c = random.randint(1,3)
    if c==1:
        print("Computer selected :- Rock")
    elif c==2:
        print("Computer selected :- Paper")
    elif c==3:
        print("Computer selected :- scissors")
    
    if c==1 and "r" in u or c==2 and "p" in u or c==3 and "s" in u:
        score = 0
        print("\nDraw!!")

    elif c==1 and "p" in u or c==3 and "r" in u or c==2 and "s" in u:
        score = 1
        print("\nYou Won!!!")

    elif c==1 and "s" in u or c==2 and "r" in u or c==3 and "p" in u:
        score = -1
        print("\nComputer Won!")


e = 0
k = 10000000
if choose==1:
    while e <= k:
        s_w_g()
elif choose==2:
    while e <= k:
        r_p_s()
else:
    print("Wrong selection!")

