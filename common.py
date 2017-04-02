import random

class Common:
    def randomText(self,characters):
        posibleCharacters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z',' ','1','2','3','4','5','6','7','8','9']
        returnedText = ""
        for i in range(0,characters):
            returnedText = returnedText+random.choice(posibleCharacters)
        return returnedText