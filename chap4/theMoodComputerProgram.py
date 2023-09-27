import random 
print ("I sense your energy. Your true emotions are coming across my screen.") 
print ("You are...") 
mood = random.randrange(3)

if mood == 0:     
    print ("""        -----------\n        |         |\n        | O     O |\n        |    <    |\n        |         |\n        | .     . |\n        |  `...`  |\n        -----------\n                     """) 
elif mood == 1:    
    print ("""        -----------\n        |         |\n        | O     O |\n        |    <    |\n        |         |\n        | ------- |\n        |         |\n        -----------\n                     """) 
elif mood == 2:
    print ("""        -----------\n        |         |\n        | O     O |\n        |    <    |\n        |         |\n        |   .'.   |\n        |  '   '  |\n        -----------\n                      """) 
else:        
    print ("Illegal mood value! (You must be in a really bad mood)." )
    
print ("...today.")
input("\n\nPress the enter key to exit.") 