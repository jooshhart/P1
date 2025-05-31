import random
aD20=list(range(1, 21))
aD12=list(range(1, 13))
aD10=list(range(1, 11))
aD8=list(range(1, 9))
aD6=list(range(1, 7))
aD4=list(range(1, 5))
chaceoldman="false"
trollfight="false"
direction_headed="N/A"
direction="N/A"
havemap="false"
oldmantalk="N/A"
staying="N/A"
DR=0
def printstats():
    print ("STR=",STR)
    print ("DEX=",DEX)
    print ("CON=",CON)
    print ("INT=",INT)
    print ("WIS=",WIS)
    print ("CHA=",CHA)
familiar="N/A"
damage="N/A"
done = "no"
LVL=1
Class = ("N/A")
Race = ("N/A")
#ask for Race
while (done=="no"):
    Race = input ("What are you? (add a dot to the end to give info rather than choosing a race):  \n1=human \n2=elf \n3=dwarf \n4=orc \n5=grandparian \n")
    if (Race=="1"):
        Race="human"
        done="yes"
    elif (Race=="2"):
        Race="elven"
        done="yes"
    elif (Race=="3"):
        Race="dwarf"
        done="yes"
    elif (Race=="4"):
        Race="orc"
        done="yes"
    elif (Race=="5"):
        Race="grandparian"
        done="yes"
    elif (Race=="1."):
        print ("A human is average at everything, a human can choose any class and gets no stat bonus/reductions")
    elif (Race=="2."):
        print ("An elf is tall and skiny with pointy ears. They live for a long time (about 160 years), do not like dwarves, and are never sorcerers or barbarians. Their stat changes are (-1,+1,0,0,0,+1)")
    elif (Race=="3."):
        print ("A dwarf is short and strong, often with a beard (but never a wizard beard). They do not like elves and are usually fighters or barbarians, but sometimes they are clerics. Their stat changes are (+1,0,+1,0,0,-1)")
    elif (Race=="4."):
        print ("A orc is a strong idiot and is usually evil. They  ideal for a barbarion. Their stat changes are (+2,0,+2,-1,-2,-2)")
    elif (Race=="5."):
        print ("A grandparian looks simalar to a human, other than that they look 102 years older than they are. They are usually wizards and incapable of being any physical fighter class. Their stat changes are (-1,-1,-1,+1,+1,+1)")
    elif (Race=="Nope, I want to cheat and be a dragon!"):
        print ("OK, fine cheater, you have to be a sorcerer, and no familiar though!")
        Race="dragon"
        done="true"
    else:
         print ("error input",Race,"is invalid")
done="no"
#ask for class
while (done=="no"):
    Class = input ("What is your class? add a dot to the end to give info rather than choosing a class \n1=wizard \n2=sorcerer \n3=fighter \n4=barbarion \n5=ranger \n6=cleric\n")
    if (Class=="1"):
        Class="wizard"
        done="yes"
    elif (Class=="2"):
        Class="sorcerer"
        done="yes"
    elif (Class=="3"):
        Class="fighter"
        done="yes"
    elif (Class=="4"):
        Class="barbarian"
        done="yes"
    elif (Class=="5"):
        Class="ranger"
        done="yes"
    elif (Class=="6"):
        Class="cleric"
        done="yes"
    elif (Class=="1."):
        print ("A wizard is an arcane (normal magic) spellcaster. Wizards are quite uncommon because they need to study their spellbooks for 1 hour per day, and they need to prepare what spells they think they will use before the spells are needed.")
        print ("A wizard however, can have a familiar (a companion that serves you, usually a small animal), learn as many arcane spells as he wants, and have an awesome beard. Stat change=(-1,-1,0,+1,+1,0)")
    elif (Class=="2."):
        print ("Like a wizard, a sorcerer is an aracne spellcaster, but a sorcerer does not need to study. A sorcerer also can use any spell he knows as long as he still has some spell slots available. A sorcerer can have a familiar, and can cast ")
        print ("more spells/day than a wisard but cannot learn new spells other than from leveling up, does not get a wizard beard, and has slightly lower level spells. Stat change=(-1,-1,0,+1,0,+1)")
    elif (Class=="3."):
        print ("A fighter uses skills with weapons, armor and shields to fight, and uses mostly strength, dexterity, and constitution. A fighter does not use spells. Stat change=(+1,+1,+1,-1,-1,-1)")
    elif (Class=="4."):
        print ("A barbarion uses pure strength to try to solve any problem, prefering not to have armor, and to have a heavy weapon such as a battleaxe. Stat change=(+2,0,+1,-1,-2,-1)")
    elif (Class=="5."):
        print ("A ranger uses skill with a bow or simmalar weapon to kill targets from far away to avoid getting damaged A ranger is the only class with a net positive stat change. Stat change=(-1,+1,0,0,+1,0)")
    elif (Class=="6."):
        print ("Clerics are rare, because like wizards they need to prepare their spells before the day starts, which takes an hour. They are good at healing. A cleric can always switch a prepared spell for a healing spell")
        print ("(a spell with 'cure' in the name like cure light wounds). A cleric cannot do much damage to enemies (unless the enemy is undead, because healing hurts undead) Stat change=(-1,-1,0,0,+1,+1)")
    else:
        print ("error input",Class,"is invalid")
#make sure Race and class makes sense
    if (Race=="elven" and (Class=="sorcerer" or Class=="barbarian")):
        print ("An elf can't be a sorcerer or barbarian")
        done = ("no")
    elif (Race=="dwarf" and (Class=="wizard" or Class=="sorcerer" or Class=="ranger")):
        print ("A dwarf can't be a wizard, sorcerer, or ranger")
        done = ("no")
    elif (Race=="orc" and (Class=="wizard" or Class=="sorcerer" or Class=="ranger" or Class=="cleric")):
        print ("A orc can't be a wizard, sorcerer, ranger, or cleric")
        done = ("no")
    elif (Race=="grandparian" and (Class=="fighter" or Class=="barbarian" or Class=="ranger")):
        print ("A grandparian can't be a fighter, barbarian, or ranger")
        done = ("no")
    elif (Race=="dragon" and (Class=="fighter" or Class=="barbarian" or Class=="ranger" or Class=="wizard" or Class=="cleric")):
        print ("I SAID YOU ONLY GET SORCERER YOU GRANDMA, THATS IT! YOU DON't GET TO BE A DRAGON ANYMORE!")
        Race="human"
        done = ("no")
print ("You are a",Race,Class)
#Calculate stats
if (Race=="human"):
    STR=10
    DEX=10
    CON=10
    INT=10
    WIS=10
    CHA=10
elif (Race=="elven"):
    STR=9
    DEX=11
    CON=10
    INT=10
    WIS=10
    CHA=11
elif (Race=="dwarf"):
    STR=11
    DEX=10
    CON=11
    INT=10
    WIS=10
    CHA=9
elif (Race=="orc"):
    STR=12
    DEX=10
    CON=12
    INT=9
    WIS=8
    CHA=8
elif (Race=="grandparian"):
    STR=9
    DEX=9
    CON=9
    INT=11
    WIS=11
    CHA=11
elif (Race=="dragon"):
    STR=50
    DEX=2
    CON=30
    INT=31
    WIS=32
    CHA=31
if (Class=="wizard"):
    STR=STR-1
    DEX=DEX-1
    CON=CON
    INT=INT+1
    WIS=WIS+1
    CHA=CHA
elif (Class=="sorcerer"):
    STR=STR-1
    DEX=DEX-1
    CON=CON
    INT=INT+1
    WIS=WIS
    CHA=CHA+1
elif (Class=="fighter"):
    STR=STR+1
    DEX=DEX+1
    CON=CON+1
    INT=INT-1
    WIS=WIS-1
    CHA=CHA-1
elif (Class=="barbarian"):
    STR=STR+2
    DEX=DEX
    CON=CON+2
    INT=INT-1
    WIS=WIS-2
    CHA=CHA-1
elif (Class=="ranger"):
    STR=STR-1
    DEX=DEX+1
    CON=CON
    INT=INT
    WIS=WIS+1
    CHA=CHA
elif (Class=="cleric"):
    STR=STR-1
    DEX=DEX-1
    CON=CON
    INT=INT
    WIS=WIS+1
    CHA=CHA+1
print ("your stats are (NOTE stats are worth much more in this game than in most DnD games, an INT of 7 means you are about the stupidest person anyone knows while an INT of 13 means you are about the smartest person anyone knows)")
printstats()
#pick stats
done = ("no")
while (done=="no"):
    stat1=input ("what stat do you want to increase? you can choose 3, but only put the first one here add a dot to the end for info: \n1=STR \n2=DEX \n3=CON \n4=INT \n5=WIS \n6=CHA \n")
    if (stat1=="1."):
        print ("STR affects how much you can carry, how much damage physical attacks do, and your intimidation.")
    elif (stat1=="2."):
        print ("DEX affects your reaction speed, evasion, accuracy, and damage with ranged weapons.")
    elif (stat1=="3."):
        print ("CON affects your max hp, recovering rate, chances of getting sick, and imunity to poison.")
    elif (stat1=="4."):
        print ("INT affects your knowledge, and how fast you learn things. A wizard also gains spellpower and amount of spells based on intelligence.")
    elif (stat1=="5."):
        print ("WIS affects how well you know what the best choice is, makes it harder to be tricked, and makes you good at giving advice. In this game it only increases your choices in a conversation, and for clerics makes your spells better")
    elif (stat1=="6."):
        print ("CHA affects how good you are at talking; Giving speaches, making friends, minpulating people, or bartering for a better price. It also makes a sorcerer a better spellcaster.")
    elif (stat1=="1"):
        STR=STR+1
        done=("yes")
    elif (stat1=="2"):
        DEX=DEX+1
        done=("yes")
    elif (stat1=="3"):
        CON=CON+1
        done=("yes")
    elif (stat1=="4"):
        INT=INT+1
        done=("yes")
    elif (stat1=="5"):
        WIS=WIS+1
        done=("yes")
    elif (stat1=="6"):
        CHA=CHA+1
        done=("yes")
    else:
        print ("that is invalid, try again")
done = ("no")
while (done=="no"):
    stat2=input ("what is you second stat? \n")
    if (stat1==stat2):
        print ("you can only choose the same stat one time")
    elif (stat2=="1"):
        STR=STR+1
        done=("yes")
    elif (stat2=="2"):
        DEX=DEX+1
        done=("yes")
    elif (stat2=="3"):
        CON=CON+1
        done=("yes")
    elif (stat2=="4"):
        INT=INT+1
        done=("yes")
    elif (stat2=="5"):
        WIS=WIS+1
        done=("yes")
    elif (stat2=="6"):
        CHA=CHA+1
        done=("yes")
    else:
        print ("that is invalid, try again")
done = ("no")
while (done=="no"):
    stat3=input ("what is you third stat? \n")
    if (stat3==stat2 or stat3==stat1):
        print ("you can only choose the same stat one time")
    elif (stat3=="1"):
        STR=STR+1
        done=("yes")
    elif (stat3=="2"):
        DEX=DEX+1
        done=("yes")
    elif (stat3=="3"):
        CON=CON+1
        done=("yes")
    elif (stat3=="4"):
        INT=INT+1
        done=("yes")
    elif (stat3=="5"):
        WIS=WIS+1
        done=("yes")
    elif (stat3=="6"):
        CHA=CHA+1
        done=("yes")
    else:
        print ("that is invalid, try again")
#familiar
if (Class=="wizard" or Class=="sorcerer" and Race!="dragon"):
    done="no"
    while(done=="no"):
        familiar=input ("what is your familiar? add a dot for info. A familliar counts as the same level as you for pourposes of HP calculation \n1=raven \n2=owl \n3=rabbit \n4=toad \n")
        if (familiar=="1"):
            familiar="raven"
            done="yes"
        elif (familiar=="2"):
            familiar="owl"
            done="yes"
        elif (familiar=="3"):
            familiar="rabbit"
            done="yes"
        elif (familiar=="4"):
            print ("you have chosen a TOAD!!! WHY WOULD ANYONE CHOOSE THAT?!")
            familiar="toad"
            done="yes"
        elif (familiar=="1."):
            print ("A raven usuall looks the best for a arcane spellcaster. It's stats are (2,13,6,2,3,2)")
        elif (familiar=="2."):
            print ("An owl bigger than a raven, and usually you cannot carry it on your shoulder. It's stats are (3,12,6,2,3,3)")
        elif (familiar=="3."):
            print ("A rabbit makes you look like a magicion and can follow you without getting tired or standing on your shoulder It gets extra intelligence for making you look like a magician. It's stats are (2,11,8,4,3,2)")
        elif (familiar=="4."):
            print ("a toad makes you look like stupid, and does not do much. It's stats are (2,11,8,2,3,2)")
    if (familiar!= "toad"):
        print (f"you chose a {familiar} as a familiar.")
printstats()
HPMAX=(max(CON-7,1))+3
HP=HPMAX
if (Class=="wizard"):
    attack = 2+(INT-10)
    atk_type = "magic"
if (Class=="sorcerer"):
    attack = 2+(CHA-10)
    atk_type = "magic"
if (Class=="fighter"):
    attack = 1+DEX-10
    atk_type = "slashing"
if (Class=="barbarian"):
    attack = 4+STR-10
    atk_type = "Crushing"
if (Class=="ranger"):
    attack = -1+DEX-10
    atk_type = "piercing"
if (Class=="cleric"):
    attack = -2+DEX-10
    atk_type = "piercing"
if (Race=="dragon"):
    HPMAX=HPMAX*HPMAX
done="false"
HP=HPMAX



print ("your HP is",HP,)
if Race!="dragon":
    damage_real = attack + random.choice(aD4); {"1":1,"2":2,"3":3,"4":4}
else:
    damage_real = attack + 3*random.choice(aD20); {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"11":11,"12":12,"13":13,"14":14,"15":15,"16":16,"17":17,"18":18,"19":19,"20":20}
townpossible = ["vill", "berg", "shalic"]
racepossible = ["dwarf", "elven", "orc", "grandparian", "human"]
town = random.choice(townpossible)
town2 = random.choice(townpossible)
while town2==town:
    town2 = random.choice(townpossible)
racefake=Race
while racefake==Race:
    racefake = random.choice(racepossible)
if Race!="dragon":
    print (f"as you are traveling from {Race}{town} to {racefake}{town2}, you see a old grandpa!")
else:
    print (f"as you are traveling from your cave to {racefake}{town2}, you see a old grandpa!")
if (familiar=="toad"):
    print ("the old man comes to talk to you, but after seeing your toad, he thinks you must be a moron, and avoides you.")
    while done=="false":
        Option = input ("will you follow him? 1=yes, 2=no\n")
        if (Option =="1"):
            print ("after a while you catch up to him.")
            while done=="false":
                Option = input ("attack him or talk to him 1=attack 2=talk\n")
                if (Option=="1"):
                    done="true"
                    init_player = (DEX-10)+random.choice(aD20); {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"11":11,"12":12,"13":13,"14":14,"15":15,"16":16,"17":17,"18":18,"19":19,"20":20}
                    init_creature = -2+random.choice(aD20); {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"11":11,"12":12,"13":13,"14":14,"15":15,"16":16,"17":17,"18":18,"19":19,"20":20}
                    print (f"your initiative is {init_player}.")
                    print (f"old man's initiative is {init_creature}.")
                    if init_player>=init_creature:
                        print("you go first")
                        yourturn="true"
                    else:
                        print ("he goes first, and punches you for 1 damage")
                        HP=HP-1
                        print ("you are now at {HP} hp, and it is your turn")
                        yourturn="true"
                    if yourturn=="true":
                        while damage!="1" and damage!="2":
                            damage = input (f"1=firebolt ({attack}+1d4 fire damage)\n2=ray of frost ({attack}+1d4 ice damage)\n")
                            if damage!="1" and damage!="2":
                                print (damage, "is invalid, try again")
                        print (f"you deal {damage_real} damage")                    
                        print (f"the old man is at {1-damage_real} hp")
                        print ("the old man is dead")
                        print ("you grab the awesome map from his corpse")
                        havemap="true"
                if (Option=="2"):
                    print ("the old man talks to you and acts like nothing happend")
                    oldmantalk="true"
                    done="true"
        elif (Option=="2"):
            print ("ok, there is nothing for you to do now\nyou finished the game (the I have a usless piece of junk toad way.)")
            done = "true"
else:
    print ("the old man comes to you")
    oldmantalk="true"
done="false"
if oldmantalk=="true":
    print ("the old man says that there is a dangerous area you should know about: \nJust 1 mile north of here there is a dragon!\nthere is also a troll 3,000 feet to the east\nthere is a lich 2000 feet south of here\nIn the west there is an evil king who kills all who enter his kingdom\n")
    while done=="false":
        direction_headed=input ("(1) go north\n(2) go east\n(3) go south\n(4) go west\n(5) stay there and talk\n")
        if direction_headed=="1":
            direction="north"
            done="true"
        elif direction_headed=="2":
            direction="east"
            done="true"
        elif direction_headed=="3":
            direction="south"
            done="true"
        elif direction_headed=="4":
            direction="west"
            done="true"
        elif direction_headed=="5":
            while (done=="false"):
                say=input ("(1) call him a liar\n(2) tell him you don't want to go anywere\n")
                if say=="1":
                    print ("congratulations, you won! (more may be added later) (lying old man way)")
                    done="true"
                elif say=="2":
                    staying="true"
                    done="true"
        else:
            print (direction_headed,"is invalid, try again")
done="false"
if (havemap=="true"):
    print ("the map is filled with nonsence. Notably it says \nJust 1 mile north of here there is a dragon!\nThere is also a troll 3,000 feet to the east\nThere is a lich 2000 feet south of here\nIn the west there is an evil king who kills all who enter his kingdom\n")
    while done=="false":
        direction_headed=input ("(1) Go north\n(2) Go east\n(3) Go south\n(4) Go west\n(5) Stay there\n")
        if direction_headed=="1":
            direction="north"
            done="true"
        elif direction_headed=="2":
            direction="east"
            done="true"
        elif direction_headed=="3":
            direction="south"
            done="true"
        elif direction_headed=="4":
            direction="west"
            done="true"
        elif direction_headed=="5":
            staying="true"
            done="true"
        else:
            print (direction_headed, "is invalid, try again")
done="false"
if direction=="north":
    print ("You travel north for around a mile, but you do not see anything. After thinking about it for a while, you decide that is a good thing, because there is no way you would have defeated a dragon at LVL 1\ncongratulations, you finished the game (more may be added later) (lucky idiot way)")
elif direction=="east":
    print ("You go 3,000 feet tword the troll, and you see it. it is 15 feet tall and carring a club")
    trollfight="true"
elif direction=="south":
    print ("you travel around 2,000 feet, but unsuprisingly there is not a lich. You think for a while and find out there would have been a lot of undead if a lich was that close\ncongratulations, you finished the game (more may be added later) (lucky idiot way)")
elif direction=="west":
    print ("you travel west, but there is no king. \ncongratulations, you finished the game (more may be added later) (strange ending way)")
elif staying=="true":
    print ("you wait there.\n congatulations, you won! (more may be added later) (lying old man way)")


if (trollfight=="true"):
    trollhp=100
    trollhpplayerturn=100
    init_player = (DEX-10)+random.choice(aD20); {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"11":11,"12":12,"13":13,"14":14,"15":15,"16":16,"17":17,"18":18,"19":19,"20":20}
    init_creature = 2+random.choice(aD20); {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"11":11,"12":12,"13":13,"14":14,"15":15,"16":16,"17":17,"18":18,"19":19,"20":20}
    print (f"your initiative is {init_player}.")
    print (f"the troll's initiative is {init_creature}.")
    trolldamage=4+random.choice(aD10); {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10}
    creaturedamage = max(trolldamage-DR,0)
    if init_player>=init_creature:
        print("you go first")
        yourturn="true"
    else:
        print (f"he goes first, and clubs you for {creaturedamage} damage")
        if creaturedamage==0:
            print ("cause u cheated")
        HP=HP-creaturedamage
        print (f"you are now at {HP} hp, and it is your turn")
        if HP>0:
            yourturn="true"
        else:
            print ("you died from a troll on the first turn. You lost.")
    while HP>0 and trollhpplayerturn>0:
        input (f"your damage is {attack} + 1d4. Click enter to roll")
        damage_real = attack + random.choice(aD4); {"1":1,"2":2,"3":3,"4":4}
        trollhpplayerturn=min(trollhp,trollhp-damage_real)
        trollhp=min(trollhpplayerturn+10,100)
        if trollhp>0:
            print ("the troll is at",trollhpplayerturn, "hp, but it has 10 automatic healing, so it is at",trollhp,"hp now, and it is his turn")
            trolldamage=4+random.choice(aD10); {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10}
            creaturedamage = max(trolldamage-DR,0)
            HP=HP-creaturedamage
            print (f"the troll did {creaturedamage} damage, and you are at {HP} hp.")
        else:
            print ("the troll is at",trollhpplayerturn,"hp, you must have cheated, this fight is supposed to be impossible to win.\n You win (the cheater way)")
        if HP<=0:
            print ("you died, you lose")

