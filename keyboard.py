# I had this great script, but my keyboard broke and I can't indent
# any of my code. Can you indent it for me?

cats = ['Grizabella', 'Rum Tum Tugger', 'Demeter', 'Munkustrap',
'Mistoffelees', 'Macavity', 'Rumpleteazer', 'Mungo Jerry', 'Skimbleshanks']

instruments = ['keyboard', 'cello', 'bass', 'flute', 'pipe', 'piano',
'violin', 'oboe', 'triangle']

def get_cat_and_instrument(position):
cat = cats[position]
instrument = instruments[position]
return "{} plays the {}".format(cat, instrument)

# Print out my cat orchestra one by one
total_cats = len(cats)
position = 0

while True:
if position >= total_cats:
    break

print get_cat_and_instrument(position)
position += 1

# Could you do the assignment of cats and instruments any other ways?