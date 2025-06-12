setup="true"
if setup=="true":
    import time
    import os
    import random
    D20=list(range(1, 21))
    D12=list(range(1, 13))
    D10=list(range(1, 11))
    D8=list(range(1, 9))
    D6=list(range(1, 7))
    D4=list(range(1, 5))
    chaceoldman="false"
    Breakgame="false"
    trollfight="false"
    direction_headed="N/A"
    direction="N/A"
    money=100
    havemap="false"
    oldmantalk="N/A"
    attacks = 1
    staying="N/A"
    zacks=65
    dragon="false"
    dragonfight="false"
    wanttoseejunk="false"
    DR=0
    def printstats():
        print ("STR=",STR)
        print ("DEX=",DEX)
        print ("CON=",CON)
        print ("INT=",INT)
        print ("WIS=",WIS)
        print ("CHA=",CHA)
    def printdragon():
        print ("                                                              █                ██                                         ")
        print ("                                                             █ █                 ██       █                               ")
        print ("                                                           █  █ █                  ██      ██                             ")
        print ("                                                         █    █  █                 ████████████                           ")
        print ("                                                        █     █   █                ███████  ███                           ")
        print ("                                                       █      █    █               ████████████                           ")
        print ("                                                      █       █     █              ████████  ██                           ")
        print ("                                                     █        █      █             █████████___                           ")
        print ("                                                    █         █     █  █     █████████████                                ")
        print ("                                                   █          █       ██████████████████                                  ")
        print ("                                                      ██████████████████████████████████                                  ")
        print ("                                                   █████████████████████████████████████                                  ")
        print ("                                                ████████████████████████████████████████                                  ")
        print ("                                             ██████      ████                       █████                                 ")
        print ("                                           █████         ████                       █████                                 ")
        print ("                               ██████████████            ████                       █████                                 ")
    def combat(badname,badattackname,badhpmax,badinit,baddamage,baddamagedice,badregen,baddamagereduction,badattacks,HP,attack,DEX,attacks):
        initbad=badinit + random.choice(D20); {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"11":11,"12":12,"13":13,"14":14,"15":15,"16":16,"17":17,"18":18,"19":19,"20":20}
        initplayer=DEX-10+random.choice(D20); {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"11":11,"12":12,"13":13,"14":14,"15":15,"16":16,"17":17,"18":18,"19":19,"20":20}
        badattacknum=badattacks
        badhp=badhpmax
        attacknum=attacks
        attacknum=attacks
        if initbad>initplayer:
            print (f"the {badname} goes first.")
            while badattacknum>0 and HP>0:
                damagebad1=baddamage+random.choice(baddamagedice); {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"11":11,"12":12,"13":13,"14":14,"15":15,"16":16,"17":17,"18":18,"19":19,"20":20}
                damagebad=max(damagebad1,0)
                HP=HP-damagebad
                input (f"the {badname} {badattackname} you for {damagebad} damage, and you are at {HP} hp")
                badattacknum=badattacknum-1
            badattacknum=badattacks
        while badhp>0 and HP>0:
            while attacknum>0 and badhp>0:
                damage1=attack+random.choice(D4); {"1":1,"2":2,"3":3,"4":4}
                damage=max(damage1,0)
                badhp=(badhp-max(damage-baddamagereduction,0))
                input (f"your attack is {attack} +1d4. \nYou do for ({damage}-his {baddamagereduction}DR) damage, the {badname} is at {badhp} hp")
                attacknum=attacknum-1
            attacknum=attacks
            badhp=max(badhpmax,badhp+badregen)
            while badattacknum>0 and HP>0:
                damagebad1=baddamage+random.choice(baddamagedice); {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"11":11,"12":12,"13":13,"14":14,"15":15,"16":16,"17":17,"18":18,"19":19,"20":20}
                damagebad=max(damagebad1,0)
                HP=HP-damagebad
                input (f"the {badname} {badattackname} you for {damagebad} damage, and you are at {HP} hp")
                badattacknum=badattacknum-1
            badattacknum=badattacks
        if HP>0:
            print ("you won the battle")
        else:
            print ("you lost the battle")
    done = "no"
    game="on"
    familiar="N/A"
    damage="N/A"
    Jimbo="true"
    LVL=1
    Class = ("N/A")
    Race = ("N/A")
#ask for Race
while game=="on":
    done="no"
    os.system('cls')
    q=input ("what do you want to do?\n(1) play game\n(2) info\n(3) quit\n")
    if q=="1":
        os.system('cls')
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
            elif (Race=="zw65gb"):
                y=input ("Umm... I know that zack was 65 good boys, what is your point\n")
                if y=="I'm zack":
                    x=input("no, you can't be zack\n")
                    if x=="You're wrong":
                        print ("ok, whatever, you are zack")
                        Race="zack"
                        done="true"
                    else:
                        print("just go pick your race")
                else:
                    print ("whatever I don't know what you are talking about, just choose your race")
            else:
                print ("error input",Race,"is invalid")
        done="no"
        if Race=="elven":
            print ("you are an elf")
        else:
            print (f"you are a {Race}")
        #ask if Race!="elven":
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
        elif (Race=="zack"):
            STR=10
            DEX=10
            CON=10
            INT=10
            WIS=10
            CHA=10
            attacks=65
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
        if (Class=="wizard" or Class=="sorcerer"):
            done="no"
            while(done=="no"):
                if Race!="zack":
                    familiar=input ("what is your familiar? add a dot for info.\n1=raven \n2=owl \n3=rabbit \n4=toad \n")
                else:
                    familiar=input ("what are your familiars (all of your good boys get the same familiar)? add a dot for info.\n1=raven \n2=owl \n3=rabbit \n4=toad \n")
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
        HPMAX=max(CON-4,1)
        HP=HPMAX
        if (Class=="wizard"):
            attack = 2+(INT-10)
            atk_type = "magic"
        if (Class=="sorcerer"):
            attack = 2+(CHA-10)
            atk_type = "magic"
        if (Class=="fighter"):
            attack = 1+STR-10
            atk_type = "slashing"
        if (Class=="barbarian"):
            attack = 4+STR-10
            atk_type = "Crushing"
        if (Class=="ranger"):
            attack = 2+DEX-10
            atk_type = "piercing"
        if (Class=="cleric"):
            attack = -2+DEX-10
            atk_type = "piercing"
        if (Race=="zack"):
            HPMAX=HPMAX*65
            attacks=zacks
        done="false"
        HP=HPMAX*100


        printstats()
        print ("your HP is",HP,"and you have",money,"gold coins")
        damage_real = attack + random.choice(D4); {"1":1,"2":2,"3":3,"4":4}
        townpossible = ["vill", "berg", "shalic"]
        racepossible = ["dwarf", "elven", "orc", "grandparian", "human"]
        town = random.choice(townpossible)
        town2 = random.choice(townpossible)
        while town2==town:
            town2 = random.choice(townpossible)
        racefake=Race
        while racefake==Race:
            racefake = random.choice(racepossible)
        print (f"as you are traveling from {Race}{town} to {racefake}{town2}, you see a old grandpa!")
        if familiar=="toad":
            print ("the old man comes to talk to you, but after seeing your toad, he thinks you must be a moron, and avoides you.")
            while done=="false":
                Option = input ("will you follow him? 1=yes, 2=no\n")
                if (Option =="1"):
                    print ("after a while you catch up to him.")
                    while done=="false":
                        Option = input ("attack him or talk to him 1=attack 2=talk\n")
                        if (Option=="1"):
                           combat("old man","punches",1,0,-1,D4,0,0,1,HP,attack,DEX,attacks)
                        elif (Option=="2"):
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
        if havemap=="true":
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
            print ("")
            dragon="true"
        elif direction=="east":
            print ("You go 3,000 feet tword the troll, and you see it. it is 15 feet tall and carring a club")
            trollfight="true"
        elif direction=="south":
            print ("you travel around 2,000 feet, but unsuprisingly there is not a lich. You think for a while and find out there would have been a lot of undead if a lich was that close\ncongratulations, you finished the game (more may be added later) (lucky idiot way)")
        elif direction=="west":
            print ("you travel west, but there is no king. \ncongratulations, you finished the game (more may be added later) (strange ending way)")
        elif staying=="true":
            print ("you wait there.\n congatulations, you won! (more may be added later) (lying old man way)")

        if trollfight=="true":
            trollhp=100
            init_player = (DEX-10)+random.choice(D20); {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"11":11,"12":12,"13":13,"14":14,"15":15,"16":16,"17":17,"18":18,"19":19,"20":20}
            init_creature = 2+random.choice(D20); {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"11":11,"12":12,"13":13,"14":14,"15":15,"16":16,"17":17,"18":18,"19":19,"20":20}
            print (f"your initiative is {init_player}.")
            print (f"the troll's initiative is {init_creature}.")
            trolldamage=4+random.choice(D10); {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10}
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
            while HP>0 and trollhp>0:
                input (f"your damage is {attack} + 1d4. Click enter to roll")
                if Race=="zack":
                    while trollhp>0 and zacks>0:
                        damage_real = attack + random.choice(D4); {"1":1,"2":2,"3":3,"4":4}
                        trollhp=min(trollhp,trollhp-damage_real)
                        if (trollhp>0):
                            print (f"the troll is at {trollhp} hp, now do your next zack's attack")
                        zacks=zacks-1
                        time.sleep(.01)
                else:
                    damage_real = attack + random.choice(D4); {"1":1,"2":2,"3":3,"4":4}
                if trollhp>0:
                    print ("the troll is at",trollhp, "hp, but it has 10 automatic healing")
                    trollhp=min(trollhp+10,100)
                    print (f"so it is at {trollhp} hp")
                    trolldamage=4+random.choice(D10); {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10}
                    creaturedamage = max(trolldamage-DR,0)
                    zacks=65*(HP/HPMAX)
                    HP=HP-creaturedamage
                    print (f"the troll did {creaturedamage} damage, and you are at {HP} hp.")
                else:
                    print ("the troll is at",trollhp,"hp, you must have cheated, this fight is supposed to be impossible to win.\n You win (the cheater way)")
                if HP<=0:
                    print ("you died, you lose")
        if dragon=="true":
            print ("after south north for about 12 miles you see a brass dragon in the mouth of a cave. He looks like this, and is 10 feet tall")
            printdragon()
            come = input ("He sees you, but appears to be waiting for you. Will you approch him?\n(1) yes\n(2) no\n")
            if come=="1":
                x=input ("What do you want? You aren't zack multipleboys, are you?\n(1) I am\n(2) I'm not\n")
                if x=="1" and Race!="zack":
                    bluff= (CHA-10)+random.choice(D20); {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"11":11,"12":12,"13":13,"14":14,"15":15,"16":16,"17":17,"18":18,"19":19,"20":20}
                    dragoninsight=10+random.choice(D20); {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"11":11,"12":12,"13":13,"14":14,"15":15,"16":16,"17":17,"18":18,"19":19,"20":20}
                    print (f"Your bluff scored {bluff}, and his insight scored {dragoninsight}")
                    if bluff>=dragoninsight:
                        
                        y=input("I don't like zack. Get out of my teritory. \n(1) leave \n(2) fight\n(3) how big is your teritory?")
                        if y=="1":
                            print ("you leave")
                            dragonfight="false"
                        if y=="2":
                            dragonfight="true"
                            mercy="zack attacks"
                    if dragoninsight>bluff:
                        print ("What could you possibly have to gain, lying to get yourself killed?")
                        dragonfight="true"
                        mercy=("non-zack lies")
                if x=="1" and Race=="zack":
                    y=input("I don't like zack, get out of my teritory \n(1) leave \n(2) fight\n\,(3) how big is your teritory?")
                    if y=="1":
                        print ("you leave")
                        dragonfight="false"
                    if y=="2":
                        dragonfight="true"
                        mercy="zack attacks"
                if x=="2" and Race!="zack":
                    y=input("I see, what do you want\n(1) all of your money\n(2) to find a lich\n(3) I just want to kill you\n")
                    if y=="1" or y=="3":
                        dragonfight="true"
                        mercy="non-zack attacks"
                    elif y=="2":
                        print("What lich?")
                if x=="2" and Race=="zack":
                    bluff=(CHA-10)+random.choice(D20); {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"11":11,"12":12,"13":13,"14":14,"15":15,"16":16,"17":17,"18":18,"19":19,"20":20}
                    dragoninsight=10+random.choice(D20); {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"11":11,"12":12,"13":13,"14":14,"15":15,"16":16,"17":17,"18":18,"19":19,"20":20}
                    print (f"Your bluff scored {bluff}, and his insight scored {dragoninsight}")
                    if bluff>=dragoninsight:
                        y=input("I see, what do you want\n(1) all of your money\n(2) to find a lich\n(3) I just want to kill you\n")
                        if y=="1" or x=="3":
                            dragonfight="true"
                            mercy="non-zack attacks"
                        elif y=="2":
                            print("What lich?")
                    if dragoninsight>bluff:
                        print ("Exactily as I thought. Zack, you are a moron lying to me")
                        dragonfight="true"
                        mercy="zacklies"
            elif come=="2":
                input ("you do not go in his lair\n you finished the game (the nah I'm too scared way)")
        if dragonfight=="true":
            combat("brass dragon","attacks",200,0,10,D10,0,10,3,HP,attack,DEX,attacks)
            "so combat() can change the class things, but not variables outside of itself?"
            if HP>0:
                if mercy=="non-zack lies":
                    print("A little while later, you wake up. You are pinned to the floor by the dragon, and he says\nYou have quite high bravery saying that you are zack\nI respect that about you...\nIf you want to be my servant, you are qualified.")
                    HP=1
                    servent = input ("will you accept his offer?\n(1) yes\n(2) no\n")
                    if servent=="1":
                        print ("The dragon lifts his claws, and you are free")
                        run = input ("will you run away or stay?\n(1) run\n(2) stay\n")
                        if run=="1":
                            print ("It wasn't bravery, you stupid humanoid! You just want to lie at every opportunity! You stupid, little, lying...")
                            input ("The dragon continues to say stuff, but he does not chase you, so you can no longer hear what he is saying. You are free\n You finished the game (The I like to lie way)")
                        if run=="2":
                            input ("for your first day, I expect you to meet with my other servents and talk to them. They are farther in the cave down the right. Tell them I sent you, so they can teach you.\n You finished the game (the dragon servent way)\n")
                    if servent=="2":
                        input ("... OK, I wish you luck, however if you continue to lie to creatures more powerful than you, you will likely be killed.\n You finished the game (the brave dude way)")
                elif mercy=="zack attacks":
                    input ("I fell much safer now that zack is dead.\n(click enter to restart)")
                elif mercy=="non-zack attacks":
                    if random.choice(D20)>10:
                        input ("So many people try to steal from my treasue, but end up just adding to it... (he kills you)\n You finished the game (the robber is killed way)")
                    else:
                        input ("You wake up a while later, quite hurt, and with no equipment or money. The dragon says 'You can keep your life robber, but I expect that you will repay me. Get out before I change my mind'\n You finished the game (the ...at least I'm alive way)")
                        money=0
                        HP=1
                elif mercy=="zack lies":
                    input ("I fell much safer now that zack is dead.\n(click enter to restart)")
            elif HP>0:
                x=input ("kill him, or mercy?\n(1) kill\n(2) mercy\n")
                if x=="1":
                    input ("You kill him. Will you explore his cave, or leave?\n(1) explore\n(2) leave\n")
                    dragon="dead"
                if x=="2" and (mercy=="zack attacks" or mercy=="zack lies"):
                    if Race=="zack":
                        y=input ("He is barily alive, and speaks slowly \n'zack? I... I always thought you were... bloodthirsty and... evil. You're just... letting me leave?\n(1) Yes\n(2) No, it's more fun to kill you like this\n(3) There is no need to leave, you can keep your stuff")
                        if (y=="1"):
                            input ("... Thank you. My stuff is to the right. My servents are to the left... (click enter to continue)")
                        if (y=="2"):
                            input ("... That makes more sense (you kill him). Will you explore his cave, or leave?\n(1) explore\n(2) leave")
                            dragon="dead"
                        if (y=="3"):
                            z=input ("... Thank you... What is it you want?\n(1) I want to learn the draconic language\n(2) I want to free your slaves\n(3) I want you to fly me to...")
                            if z=="1":
                                print ("No... just kill me. I will not teach zack... Anything!")
                            if z=="2":
                                print ("I ")
                    elif Race!="zack":
                        y=input ("He is barily alive, and speaks slowly \n'zack? I... I always thought you were... bloodthirsty and... evil. You're just... letting me leave?\n(1) Yes\n(2) No, it's more fun to kill you like this\n(3) There is no need to leave, you can keep your stuff\n(4) I'm not zack")

                elif x=="2":
                    y=input (f"He is barily alive, and speaks slowly \n'You're... sparing my life?... Who are you?\n(1) tell him your name\n(2) I'm not sparing your life, tell me where your money is before I kill you\n(3) I'm a(n) {Race}{Class}.")
                            
                            
                            
                            
                if z=="1":
                    print ("I... That sounds fun. Draconic is a language that never changes. It was exactily the same 1,000 years. Most languages either did not exist, or changed so much that you no longer understand them in 1,000 years")
                    print ("(4 months later) (you know Draconic)")
    if q=="2":
        w=input("what do you want to know\n(1) stats\n(2) races\n(3) classes\n(4) bestiary\n")
        if w=="1":
            print ("Stats tell you about a creature. Stats are always listed like this (9,15,11,2,5,3)\nThis creature would have 9 strength, 15 dexterity, 11 constitution, 2 intellegence\n 5 wisdom, and 3 chrisma. This would probably be the stats of a magical beast")
        elif w=="2":
            print ("Races are creatures you can be. For these purposes a dragon is not considered a race, but a grandparian is, because in this game you can be a grandparian, but not a dragon. A grandparian has a picture, because you might not know what it is.")
            e=input ("Which race do you want to know about?\n(1) human\n(2) elf\n(3) dwarf\n(4) orc\n(5) grandparian\n") 
            if (e=="1"):
                print ("A human is average at everything, a human can choose any class and gets no stat bonus/reductions")
                print ("                         █████████                   ")
                print ("                        █  █   █  █                  ")
                print ("                       █   _____   █                 ")
                print ("                        █         █                  ")
                print ("                         █████████                   ")
                print ("                             █                       ")
                print ("                     █████████████████               ")
                print ("                             █                       ")
                print ("                             █                       ")
                print ("                             █                       ")
                print ("                            █ █                      ")
                print ("                           █   █                     ")
                print ("                          █     █                    ")
                print ("                         █       █                   ")
            elif (e=="2"):
                print ("An elf is tall and skiny with pointy ears. They live for a long time (about 160 years), do not like dwarves, and are never sorcerers or barbarians. Their stat changes are (-1,+1,0,0,0,+1)")
                print ("                                                                                                                          ")
                print ("                                     █  █████████  █                                                                      ")
                print ("                                    █ ██  █  █   ██ █                                                                     ")
                print ("                                     ██   _____   ██                                                                      ")
                print ("                                       █         █                                                                        ")
                print ("                                        █████████                                                                         ")
                print ("                                           █                                                                              ")
                print ("                                ███████████████████████                                                                   ")
                print ("                                           █                                                                              ")
                print ("                                           █                                                                              ")
                print ("                                           █                                                                              ")
                print ("                                           █                                                                              ")
                print ("                                           █                                                                              ")
                print ("                                          █ █                                                                             ")
                print ("                                         █   █                                                                            ")
                print ("                                        █     █                                                                           ")
                print ("                                       █       █                                                                          ")
                print ("                                      █         █                                                                         ")                          
            elif (e=="3"):
                print ("A dwarf is short and strong, often with a beard (but never a wizard beard). They do not like elves and are usually fighters or barbarians, but sometimes they are clerics. Their stat changes are (+1,0,+1,0,0,-1)")            
                print ("                                                                                                                          ")
                print ("                                                                                                                          ")
                print ("                                         ████████                                                                         ")
                print ("                                        █  █  █  █                                                                        ")
                print ("                                       █   ____   █                                                                       ")
                print ("                                        █        █                                                                        ")
                print ("                                         ████████                                                                         ")
                print ("                                         ████████                                                                         ")
                print ("                                       ████████████                                                                       ")
                print ("                                            █                                                                             ")
                print ("                                           █ █                                                                            ")
                print ("                                          █   █                                                                           ")
                print ("                                         █     █                                                                          ")             
            elif (e=="4"):
                print ("A orc is a strong idiot and is usually evil. They are ideal for a barbarion. Their stat changes are (+2,0,+2,-1,-2,-2)")
                print ("                                                                                                                          ")
                print ("                                                █████████                                                                 ")
                print ("                                               █ █   █   █                                                                ")
                print ("                                              █   ____    █                                                               ")
                print ("                                               █         █                                                                ")
                print ("                                                █████████                                                                 ")
                print ("                                                   █                                                                      ")
                print ("                                      ███████████████████████████                                                         ")
                print ("                                      ███████████████████████████                                                         ")
                print ("                                                   █                                                                      ")
                print ("                                                   █                                                                      ")
                print ("                                                   █                                                                      ")
                print ("                                                  █ █                                                                     ")
                print ("                                                 █   █                                                                    ")
                print ("                                                █     █                                                                   ")
                print ("                                               █       █                                                                  ")
                print ("                                              █         █                                                                 ")
            elif (e=="5"):
                print ("A grandparian looks simalar to a human, other than that they look 102 years older than they are. They are usually wizards and incapable of being any physical fighter class. Their stat changes are (-1,-1,-1,+1,+1,+1)")
                print ("                                                            ██                                                            ")
                print ("                                                             ██                                                           ")
                print ("                                                            ▌ *▐                                                          ")
                print ("                                                           █  C █                                                         ")
                print ("                                                          ▌ * C  ▐                                                        ")
                print ("                                                         █ C   *  █                                                       ")
                print ("                                                        ▌ * C C *  ▐                                                      ")
                print ("                                                        ████████████                                                      ")
                print ("                                                       █            █                                                     ")
                print ("                                                      █    █   █     █                                                    ")
                print ("                                                      █      .       █                                                    ")
                print ("                                                      █   L_____     █                                                    ")
                print ("                                                       █            █    ▄▄▄▄                                             ")
                print ("                                                        ████████████    ▌    ▐                                            ")
                print ("                                                         ▌   █   ▐      ▌>  <▐                                            ")
                print ("                                                          ▌  █  ▐        ████                                             ")
                print ("                                                           ▌ █ ▐          ██                                              ")
                print ("                                                            ▌█▐           ██                                              ")
                print ("                                                             ▌            ██                                              ")
                print ("                                                ████████████████████████████                                              ")
                print ("                                                             █            ██                                              ")
                print ("                                                             █            ██                                              ")
                print ("                                                             █            ██                                              ")
                print ("                                                             █            ██                                              ")
                print ("                                                             █            ██                                              ")
                print ("                                                            ▌ ▐           ██                                              ")
                print ("                                                           ▌   ▐          ██                                              ")
                print ("                                                          ▌     ▐         ██                                              ")
                print ("                                                         ▌       ▐        ██                                              ")
        elif w=="3":
            print ("what class do you want to know about (you don't get pictures)")
            e=input ("(1) wizard\n(2) sorcerer\n(3) fighter\n(4) barbarian\n(5) ranger\n(6) cleric\n")
            if (e=="1"):
                print ("A wizard is an arcane (normal magic) spellcaster. Wizards are quite uncommon because they need to study their spellbooks for 1 hour per day, and they need to prepare what spells they think they will use before the spells are needed.")
                print ("A wizard however, can have a familiar (a companion that serves you, usually a small animal), learn as many arcane spells as he wants, and have an awesome beard. Stat change=(-1,-1,0,+1,+1,0)")
            elif (e=="2"):
                print ("Like a wizard, a sorcerer is an aracne spellcaster, but a sorcerer does not need to study. A sorcerer also can use any spell he knows as long as he still has some spell slots available. A sorcerer can have a familiar, and can cast ")
                print ("more spells/day than a wisard but cannot learn new spells other than from leveling up, does not get a wizard beard, and has slightly lower level spells. Stat change=(-1,-1,0,+1,0,+1)")
            elif (e=="3"):
                print ("A fighter uses skills with weapons, armor and shields to fight, and uses mostly strength, dexterity, and constitution. A fighter does not use spells. Stat change=(+1,+1,+1,-1,-1,-1)")
            elif (e=="4"):
                print ("A barbarion uses pure strength to try to solve any problem, prefering not to have armor, and to have a heavy weapon such as a battleaxe. Stat change=(+2,0,+1,-1,-2,-1)")
            elif (e=="5"):
                print ("A ranger uses skill with a bow or simmalar weapon to kill targets from far away to avoid getting damaged A ranger is the only class with a net positive stat change. Stat change=(-1,+1,0,0,+1,0)")
            elif (e=="6"):
                print ("Clerics are rare, because like wizards they need to prepare their spells before the day starts, which takes an hour. They are good at healing. A cleric can always switch a prepared spell for a healing spell")
                print ("(a spell with 'cure' in the name like cure light wounds). A cleric cannot do much damage to enemies (unless the enemy is undead, because healing hurts undead) Stat change=(-1,-1,0,0,+1,+1)")
        elif w=="4":
            print (" ______________________________________________________")
            print ("|                                                      |")
            print ("|                                                      |")
            print ("|                 Bestiary                             |")
            print ("|    A book of creatures you can fight in this game    |")
            print ("|      page 1 . . . . . . . . . . . . . troll          |")
            print ("|      page 2 . . . . . . . . . . . . . dragon         |")
            print ("|      page 3 . . . . . . . . . . . . . old man        |")
            print ("|      page 4 . . . . . . . . . . . . . gaurd          |")
            print ("|             (book does not work yet)                 |")
            print ("|                                                      |")
            print ("|                                                      |")
            print ("|                                                      |")
            print ("|                                                      |")
            print ("|                                                      |")
            print ("|                                                      |")
            print ("|                                                      |")
            print ("|                                                      |")
            print ("|                                                      |")
            print ("|                                                      |")
            print ("|                                                      |")
            print ("|                                                      |")
            print ("|                                                      |")
            print ("|                                                      |")
            print ("|                                                      |")
            print ("|                                                      |")
            print ("|                                                      |")
            print ("|                                                      |")
            print ("|                                                      |")
            print ("|                                                      |")
            print ("L______________________________________________________")
        input ("click enter to continue")
    if q=="3":
        game="off"
        input ("I did not know where else to put the unfinshed art, so you get to see it now. Click enter.")
        os.system('cls')
if wanttoseejunk=="true":



















































































































































































































































































































































































































































































































































    print ("                                                              █                ██                                         ")
    print ("                                                             █ █                 ██       █                               ")
    print ("                                                           █  █ █                  ██      ██                             ")
    print ("                                                         █    █  █                 ████████████                           ")
    print ("                                                        █     █   █                ███████  ███                           ")
    print ("                                                       █      █    █               ████████████                           ")
    print ("                                                      █       █     █              ████████  ██                           ")
    print ("                                                     █        █      █             █████████___                           ")
    print ("                                                    █         █     █  █     █████████████                                ")
    print ("                                                   █          █       ██████████████████                                  ")
    print ("                                                      ██████████████████████████████████                                  ")
    print ("                                                   █████████████████████████████████████                                  ")
    print ("                                                ████████████████████████████████████████                                  ")
    print ("                                             ██████      ████                       █████                                 ")
    print ("                                           █████         ████                       █████                                 ")
    print ("                               ██████████████            ████                       █████                                 ")



    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                        ████████████                                                      ")
    print ("                                                       █            █                                                     ")
    print ("                                                      █              █                                                    ")
    print ("                                                      █              █                                                    ")
    print ("                                                      █              █                                                     ")
    print ("                                                       █                                                                   ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                                                                          ")
    print ("                                                                               ██                                         ")
    print ("                                                                     █████       ██       █                               ")
    print ("                                                                       ██          ██      ██                             ")
    print ("                                                                       █           ████████████                           ")
    print ("                                                                       █           ███████  ███                           ")
    print ("                                                                        █          ████████████                           ")
    print ("                                                                         █         ████████  ██                           ")
    print ("                                                                          █        █████████___                           ")
    print ("                                                                           █ █████████████                                ")
    print ("                                                                      ██████████████████                                  ")
    print ("                                                      ██████████████████████████████████                                  ")
    print ("                                                   █████████████████████████████████████                                  ")
    print ("                                                ████████████████████████████████████████                                  ")
    print ("                                             ██████      ████                       █████                                 ")
    print ("                                           █████         ████                       █████                                 ")
    print ("                               ██████████████            ████                       █████                                 ")
