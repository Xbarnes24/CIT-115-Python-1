fMERCURY_GRAVITY = 0.38
fVENUS_GRAVITY = 0.91
fMOON_GRAVITY = 0.165
fMARS_GRAVITY = 0.38
fJUPITER_GRAVITY = 2.34
fSATURN_GRAVITY = 0.93
fURANUS_GRAVITY = 0.92
fNEPTUNE_GRAVITY = 1.12
fPLUTO_GRAVITY = 0.066

sName = input("Enter your name: ")
fWeight = float(input("Enter your weight: "))

print (f"{sName} here are your weights on our Solar system\'s planets:")

#Below is the weights corresponding to the planets.

#print( '{:20}'.format(sName2), format(fSalary2, "15,.2f") )

print(f"{'Weight on Mercury:':25s}{fWeight * fMERCURY_GRAVITY:10.2f}")
print(f"{'Weight on Venus:':25s}{fWeight * fVENUS_GRAVITY :10.2f}")
print(f"{'Weight on Moon:':25s}{fWeight * fMOON_GRAVITY :10.2f}")
print(f"{'Weight Mars:':25s}{fWeight * fMARS_GRAVITY :10.2f}")
print(f"{'Weight on Jupiter:':25s}{fWeight * fJUPITER_GRAVITY :10.2f}")
print(f"{'Weight on Saturn:':25s}{fWeight * fSATURN_GRAVITY :10.2f}")
print(f"{'Weight on Uranus:':25s}{fWeight * fURANUS_GRAVITY :10.2f}")
print(f"{'Weight on Neptune:':25s}{fWeight * fNEPTUNE_GRAVITY :10.2f}")
print(f"{'Weight on Pluto:':25s}{fWeight * fPLUTO_GRAVITY :10.2f}")

