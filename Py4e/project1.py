fname = input("What is your name?: ")
try:
    gname = input("How old are you?: ")
    age = float(gname)
except:
    print("Oops! Use numbers instead")
    quit()

if age > 15:
    fage = age - 15
    oage = int(fage)
    print("Hi,",fname,".", "I am younger than you by", oage,"years.")

elif age == 15:
    print("Hi,",fname,".", "We are the same age!!")

else:
    hage = 15 - age
    yage = int(hage)
    print("Hi,",fname,".", "I am older than you by", yage,"years.")
