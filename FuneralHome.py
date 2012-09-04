# # # # # # # # # # # # # # # # #
#	   THE FUNERAL DIRECTOR		#
#        BY KEVIN SUCKIEL 		#
#           @sueks24			#
#								#
#   FREE TO PLAY & DISTRIBUTE	#
# # # # # # # # # # # # # # # # # 

space = '\n'

print "THE FUNERAL DIRECTOR"
print space
print "Press Y for instructions. Press N to play."
print space
instruct = raw_input("?")
print space
if instruct == 'Y' or instruct == 'y':
    print """
			 --------INSTRUCTIONS--------\n
    		 To play this game the objective\n
    		 is simple, get out of the funeral\n
    		 home alive.  Throughout the game\n
    		 you will be presented situations\n
    		 that require you to choose what\n
    		 option you think would be best.\n
    		 To make a choice is easy, for example\n
    		 Your asked to enter the basement:\n
    		 Enter the basement ( 1 )\n
    		 Go back down the hallway ( 2 )\n
    		 If you want to enter the basement\n
    		 you press 1 in the prompt if not\n
    		 you press 2.  Continue and play\n
    		 and see if you can make it to the end!.\n
			 --------GOOD LUCK--------\n
When your ready press enter."""
    
elif instruct == 'N' or instruct == 'n':
    print "Press Enter to begin."
    
else:
    print """
   		--------INSTRUCTIONS--------\n
   		To play this game the objective\n
    		 is simple, get out of the funeral\n
    		 home alive.  Throughout the game\n
    		 you will be presented situations\n
    		 that require you to choose what\n
    		 option you think would be best.\n
    		 To make a choice is easy, for example\n
    		 Your asked to enter the basement:\n
    		 Enter the basement ( 1 )\n
    		 Go back down the hallway ( 2 )\n
    		 If you want to enter the basement\n
    		 you press 1 in the prompt if not\n
    		 you press 2.  Continue and play\n
    		 and see if you can make it to the end!.\n
			 --------GOOD LUCK--------\n
When your ready press enter."""

blank = raw_input("...")

print "You awake."
print "Your eyes are burned by the bright light."
print "You look around"
print "Where are you? How did you get here?"
print """
You can barely move but you manage to slide your body off the table.
This place looks oddly familiar but doesn't ring a bell.
You begin to look around..."""
print "You see a door."
print "Look to see if it's open ( 1 )?"
print "Lay back on the table ( 2 )"
user_choice1 = raw_input("... ")
if user_choice1 == "1":
    print "Locked!"
elif user_choice1 == "2":
    print "Coward"
    exit("Game Over")
else:
    exit("You didn't play by the rules, enter 1 or 2 You lose!")