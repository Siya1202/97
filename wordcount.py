string=input("enter your introduction : ")
charactercount=0
wordcount=1
for i in string:
    charactercount=charactercount+1
    #   print(charactercount)
    if(i==' '):
        wordcount=wordcount+1 
        print(wordcount)   
        