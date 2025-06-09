game=""
while (game != "1" and game != "2" and game !="3"):
    game = input("you want to make a game but you don't know what it should be about. \n(1)don't make a game. \n(2)Make a cool game about a someone who will fight a dragon. \n(3)Make a game about the game you are making.")
    if game == ("1"):
         print ("you are bord and have a bad life. the end.")
    elif game == ("2"):
         print("After years of hard work, you make a cool game that lots of people play, and your life is great. the end.")
    elif game == ("3"):
             code=""
    while (code != "1" and code != "2"):
            code = input("Do you want the game to have more detals about the code? \n(1)1=yes. \n(2)2=no.")
            if code == ("1"):
                print ("This is what the code looks like right now:")
                print ("game=""")
                print ("while (game != ",1," and game != ",2," and game !=",3,"):")
                print ("game = input(you want to make a game but you don't know what it should be about. \n(1)don't make a game. \n(2)Make a cool game about a someone who will fight a dragon. \n(3)Make a game about the game you are making.)")
                print ("if game == (",1,"):")
                print ("      print (you are bord and have a bad life. the end.)")
                print ("elif game == (",2,"):")
                print ("      print(After years of hard work, you make a cool game that lots of people play, and your life is great. the end.)")
                print ("elif game == (",3,"):")
                print ("         code=""")
                print ("while (code != ",1," and code != ",2,"):")
                print ("        code = input(Do you want the game to have more detals about the code? \n(1)1=yes. \n(2)2=no.)")
                print ("        if code == (",1,"):")
                print ("(print all this stuff)")
                print ("that is all I have right now")
            if code == ("2"):
                  print ("you are done making a game about the game you are making.")
    else:
        print("Please choose 1, 2, or 3.\n")
