print ("Welcome to the Pig Latin Translator!")
print ("It will check if you enter a word (valid entry without digit), \nmove the first letter to the word end, \nand add \"ay\" at the end")

# Start coding here!
pyg = 'ay'
runcount = 5
while runcount:
    original = input("Enter a word:")
    if len(original) and original.isalpha():
        word = original.lower()
        first = word[0]
        new_word = word[1:] + first + pyg
        print (new_word)
    else: 
        print ("Your entry is empty or contains digit")
    runcount-=1
    print ("You have", str(runcount), "times to try")
    