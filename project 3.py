import random

def fight():
    playerhealth= 100
    bosshealth = random.randint(100,300)
    print("Time to fight!!!")

    while True:
        playerattack=random.randint(10,100)
        bossattack= random.randint(10,50)
        playerdefend=random.randint(10,50)
        playerheal=random.randint(10,50)
        bossaction= random.randint(1,999)
        bossdefend= random.randint(10,100)
        print("Your health is at: "+ str(playerhealth))
        print("Gorelock's health is at: "+ str(bosshealth))
        print("Press 1 to Attack")
        print("Press 2 to Defend")
        print("Press 3 to Heal")
        playeraction=input("Your Turn: ")
   
        if playeraction == "1":
            print("You hit gorelock for " + str(playerattack) + " damage")
            if bossaction % 2 == 0:
                print("Gorelock chooses to attack as well you take " + str(bossattack) + " Damage" )
                bosshealth= bosshealth-playerattack
                bosshealth
                playerhealth= playerhealth - bossattack
                playerhealth
                
            elif bossaction % 2 !=0:
                print("Gorelock chooses to defend blocking " + str(bossdefend) + " Damage")
                if bossdefend >= playerattack:
                    print("Gorelock takes no damage")
                else:
                    playerattack= playerattack-bossdefend
                    bosshealth= bosshealth-playerattack  

        if playeraction== "2":
            print("You defend againist the attack blocking " + str(playerdefend) + " damage")
            if bossaction % 2 == 0:
                print("Gorelock chooses to attack you take " + str(bossattack) + " Damage" )
                if playerdefend >= bossattack:
                     print("You take no damage.")
                else:
                     bossattack=bossattack-playerdefend
                     playerhealth=playerhealth-bossattack
                           
            elif bossaction % 2 !=0:
                            print("Gorelock chooses to defend as well.")
                            print("Whelp onto the next turn.")

                            
            else: 
                bossattack= bossattack-playerdefend
                playerdefend= playerhealth-playerattack
            
        if playeraction =="3":
            print("You heal for " +str(playerheal)+ " Health")
            playerhealth= playerhealth + playerheal
            if bossaction % 2 == 0:
                print("Gorelock chooses to attack you take " + str(bossattack) + " Damage" )
                playerhealth= playerhealth-bossattack
            elif bossaction %2 ==0:
                 print("Gorelock defends")    
        if playerhealth <=0:
            print("you have died!")
            break
        if bosshealth <= 0:
            print("You have won")
            break                
        else:   
            print("Invaild input select 1-3")

fight()
while True:
    anotherone=str(input("Do you want to fight again (yes/no): "))
    if anotherone == "Yes" or anotherone == "yes":
        fight()
    elif anotherone == "No" or anotherone == "no":
        print("Okay, Goodbye.")
        break
    else:
        print("Sorry didn't catch that what did you say.")
        continue
      