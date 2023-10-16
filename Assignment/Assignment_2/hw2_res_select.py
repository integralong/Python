#Lauren Song
#U79789182
#Restaurant Selector

vegetarian = input('Is anyone in your party a vegetarian?').lower()
vegan = input('Is anyone in your party a vegan?').lower()
glutenfree = input('Is anyone in your party gluten free?').lower()
print('Here are your restaurant choices:')


if vegan == 'yes':
    print('Farmacy Vegan Kitchen')
elif glutenfree == 'yes':
    print('Wood Fired Pizza Wine Bar')
    print('Farmacy Vegan Kitchen')
elif vegetarian == 'yes':
    print('Villaggio’s Ristorante Italiano')
    print('Wood Fired Pizza Wine Bar')
    print('Farmacy Vegan Kitchen')
else:
    print('Council Oak Steaks and Seafood')
    print('Villaggio’s Ristorante Italiano')
    print('Wood Fired Pizza Wine Bar')
    print('Farmacy Vegan Kitchen')

