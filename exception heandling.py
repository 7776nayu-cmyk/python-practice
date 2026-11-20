#prevent prog crashes
#try:runs target code block
#except: catches specfic exception types
#else: runs if no error occers intry
#finlly runs always{e.g.cleanup action}

try:
    val=int(input("n: "))
    res=100/val
except ValueError:
    print("invalid")
except ZeroDivisionError:
    print("cannot")
else:
    print(res)
finally:
    print("exceutiob complet")



    import json