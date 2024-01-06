import time

# Els caràcters valids a la contrassenya
validCharacters = "1234567890"
maxCharacters=4


# L'usuari introdueix un número que el programa hackejarà per força bruta.
# He protegit l'entrada de l'usuari
# perquè el password acompleixi les regles imposades.
passOK = False
while not passOK:
    errorTrobat = False
    print(f"  - Els caràcters vàlids són : {validCharacters}")
    print(f"  - El màxim de caràcters és : {maxCharacters}")
    passwordToGuess = str(input("Introdueix el password que el programa endevinarà per força bruta :"))
    print ()
    if len(passwordToGuess) > 0 and len(passwordToGuess) <= maxCharacters:
        for ch in passwordToGuess:
            if ch not in validCharacters:
                errorTrobat = True
                print("!! El password introduit conté caràcters no permesos")
    else:
        print(f"!! El número de characters ha de ser mínim 1 i màxim {maxCharacters}")
        errorTrobat = True
    if not errorTrobat:
        passOK = True

print("Passwort acceptat, ara el hackejaré per força bruta")
numPasswordsTried=0
numPasswordsFinal =0
passwordGuessedOK = ""

# Engego el cronometre
timeStart = time.time()

# Haureu d'anar ampliant el loop per màxim número de caràcters
heEncertat = False
timeEnd = 0

# Passwords de 1 caràcter
for ch1 in validCharacters:
    numPasswordsTried +=1
    guess = ch1
    print(guess)
    if guess == passwordToGuess:
        heEncertat = True
        passwordGuessedOK=guess
        numPasswordsFinal = numPasswordsTried
        timeEnd= time.time()

# Passwords de 2 caràcters
if not heEncertat:
    for ch1 in validCharacters:
        for ch2 in validCharacters:
            numPasswordsTried +=1
            guess = ch1 + ch2
            print(guess)
            if guess == passwordToGuess:
                heEncertat = True
                passwordGuessedOK=guess
                numPasswordsFinal = numPasswordsTried
                timeEnd= time.time()

# Passwords de 3 caràcters
if not heEncertat:
    for ch1 in validCharacters:
        for ch2 in validCharacters:
            for ch3 in validCharacters:
                numPasswordsTried +=1
                guess = ch1 + ch2 + ch3
                print(guess)
                if guess == passwordToGuess:
                    heEncertat = True
                    passwordGuessedOK=guess
                    numPasswordsFinal = numPasswordsTried
                    timeEnd= time.time()

# Passwords de 4 caràcters
if not heEncertat:
    for ch1 in validCharacters:
        for ch2 in validCharacters:
            for ch3 in validCharacters:
                for ch4 in validCharacters:
                    numPasswordsTried +=1
                    guess = ch1 + ch2 + ch3 +ch4
                    print(guess)
                    if guess == passwordToGuess:
                        heEncertat = True
                        passwordGuessedOK=guess
                        numPasswordsFinal = numPasswordsTried
                        timeEnd= time.time()

# Això és una protecció d'errors per si per un error no troba el password.
if timeEnd == 0:
    timeEnd= time.time()
duration = timeEnd - timeStart
print(f"\nLa CPU havia d'endevinar el password {passwordToGuess}")
print(f"   La CPU diu que el teu password es {passwordGuessedOK}")
print(f"   Ho ha deduit en {numPasswordsFinal} intents i temps {duration}")