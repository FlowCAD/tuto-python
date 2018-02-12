# First conditionnal test
def greater_less_equal_5(answer):
    if answer > 5:
        return "+1"
    elif answer < 5:
        return "-1"
    else:
        return "ok"

print greater_less_equal_5(4)
print greater_less_equal_5(5)
print greater_less_equal_5(6)


# Second conditionnal test
def the_flying_circus(arg1, arg2):
    if arg1 > arg2 and arg2 != 0:
        return False
    elif arg1 < arg2 and arg1 != 0:
        return True
    else:
        not arg1 == arg2

print the_flying_circus(10, 100)


# Third conditionnal test
def clinique():
    print "Vous entrez dans la clinique !"
    print "Voulez-vous prendre la porte de droite ou de gauche ?"
    reponse = raw_input("Tapez 'droite' ou 'gauche' puis validez avec 'Entree'.").lower()
    if reponse == "gauche" or reponse == "g":
        print "Vous etes dans la salle d'attente."
    elif reponse == "droite" or reponse == "d":
        print "Vous etes dans la salle d'operation. Sortez vite !"
    else:
        print "Vous n'avez choisi ni la droite ni la gauche, essayez encore !"
        clinic()
clinique()