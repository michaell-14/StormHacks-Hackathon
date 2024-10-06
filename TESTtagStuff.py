import tagStuff

animalRead = tagStuff.readTag() #call Victor's readTag function to get the value associated with the tag's UID
foodRead = tagStuff.readTag() #call Victor's readTag function to get the value associated with the tag's UID
checkMatch = tagStuff.checkMatch(animalRead, foodRead) #call Victor's checkMatch function to check if the animal and food match

if checkMatch == True:
    print("Match!")
else:
    print("No match.")