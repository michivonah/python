# Christmas "wichteln" random people picker
# Michi von Ah

import random

names = ["sepp", "max", "hans", "maria"]
avail = names.copy()
picked = []


for person in names:
    selection = random.choice(avail)

    while selection == person:
        selection = random.choice(avail)
    avail.remove(selection)
    print(f'{person} wichtelt {selection}')


# Example output:
# sepp wichtelt an hans
# max wichtelt an maria
# hans wichtelt an max
# maria wichtelt an sepp