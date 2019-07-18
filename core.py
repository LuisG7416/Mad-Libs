#Making user input words (adj, verbs, nouns, etc.) and inputting them into a string

adj1 = input("Choose an Adjective\n")
adj2 = input("Choose another Adjective\n")
typeOfBird =  input("Choose a bird\n")
roomInHouse =  input("Choose a room in a house\n")
verbPastTense =  input("Choose a verb in past tense\n")
verb =  input("Choose a verb\n")
relativeName =  input("Name one of your relatives\n")
noun =  input("Choose a noun\n")
liquidName =  input("Name a liquid\n")
verbEndInIng =  input("Choose a verb ending in Ing\n")
partOfBodyPlural =  input("Choose a part of the body but plural\n")
nounPlural =  input("Choose a plural noun\n")
verbEndInIng2 =  input("Choose another verb ending in Ing\n")
noun2 =  input("Choose another noun\n")




story = ("It was a " + adj1 + ", cold November day. I woke up to the " + adj2 + " smell of " + typeOfBird + " roasting in the " + roomInHouse + " downstairs. I " + verbPastTense + " down the stairs to see if I could help " + verb + " the dinner. My mom said, 'See if " + relativeName + " needs a fresh " + noun + ".' So I carried a tray of glasses full of " + liquidName + " into the " + verbEndInIng + " room. When I got there, I couldn't believe my " + partOfBodyPlural + "! There were " + nounPlural + " " + verbEndInIng2 + " on the " + noun2 + "!")

story2 = ("It was a " + adj1 + " evening during a " + adj2 + " summer. Outside my basement window I saw " + typeOfBird + " trying to get into the " + roomInHouse + "! I " + verbPastTense + " up the stairs to the " + roomInHouse + ". When I got there the " + typeOfBird + " had flown through the window straight into " + relativeName + "! I rushed to call " + noun + " who was drinking " + liquidName + ". 'I have been " + verbEndInIng + " for you.' They had their " +partOfBodyPlural+ " wrapped around " + nounPlural + " '" + relativeName + " had it coming, they did eat " + typeOfBird + " before after all.' " + verbEndInIng2 + " that the damage was already done, I walked away to " + noun2 + ".")   

def numCheck():
    choice = input("Choose a story! Type 1 for Thanksgiving or Type 2 for Birds Revenge.\n")
    if choice == "1":
        print(story)
    elif choice == "2":
        print(story2)
    else:
        choice = input("Please choose one of the stories.\n")
        numCheck()

numCheck()

# if choice.lower == "1":
#     print(story)
# elif choice.lower == "2":
#     print(story2)
# else:
#     if choice.lower == "1":
#         print(story)
#     elif choice.lower == "2":
#         print(story2)

