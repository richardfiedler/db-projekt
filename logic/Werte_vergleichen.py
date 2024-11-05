teurer = 0

# StrompreisA und StrompreisB übernehmen

if StrompreisA < StrompreisB:
    teurer = StrompreisB
    billig = StrompreisA
elif StrompreisA > StrompreisB:
    teurer = StrompreisA
    billig = StrompreisB
else:
    teuer = StrompreisA
    billig = StrompreisA