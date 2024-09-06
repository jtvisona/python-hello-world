
# import <module> as alias
# alias.f()

flagT = True
flagF = False

for each in range( 15 ):
    print( f"{each}: ", end="" )
    if each < 6:
        print( f"*{each}*", end=" " )
    elif each == 6:
        pass
    elif each == 7:
        print( f"*{each}*", end=" " )
    elif each == 8:
        continue
    elif each > 8 and each < 11:
        print( f"*{each}*", end=" " )
    else:
        break
