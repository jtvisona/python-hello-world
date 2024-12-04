"""
Jonathan Visona
CPSC6210-02-2024FA
Assignment 7
pig_latin.py
"""

def to_pig_latin( word ):
    ch = word[0]
    if( ch == 'a' or
        ch == 'e' or
        ch == 'i' or
        ch == 'o' or
        ch == 'u' ):
        word += "way"
    else:
        if ch == 'y':
            word = word[1:]
            word += ch
            ch = word[0]
    while( ch != 'a' and
        ch != 'e' and
        ch != 'i' and
        ch != 'o' and
        ch != 'u' and ch!= 'y' ):
        word = word[1:]
        word += ch
        ch = word[0]
    word += "ay"
    return word

def main():
    print( "Pig Latin Translator" )
    print()
    choice = "y"
    while choice.lower() == "y":
        line = input( "Enter text: " ).strip()
        line = line.replace( ".", "" )
        line = line.replace( ",", "" )
        line = line.replace( ";", "" )
        line = line.replace( ":", "" )
        line = line.replace( "!", "" )
        line = line.replace( "?", "" )

        line = line.lower()
        if line == "":    
            print( "Please enter some text, yo." )
        else:
            wordsl = line.split( " " )
            words2 = []
            for word in wordsl:
                words2.append( to_pig_latin (word) )
            pig_latin = " ".join(words2)

            print( "English: ", line )
            print( "Pig Latin: ", pig_latin )
            print()

            choice = input( "Continue? (y/n): " )
            print()
    print ( "Bye!" )

if __name__ == "__main__":
    main()