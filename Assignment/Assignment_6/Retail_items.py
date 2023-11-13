#Lauren Song
#U79789182
#Retail items

class RetailItem:
    itemnum = 0
    def __init__(self, typ, amt, price):
        self.itemtyp = typ
        self.itemamt = amt
        self.itemprice = price
        RetailItem.itemnum += 1
        
    def __str__(self):
        return self.itemtyp.ljust(29) + self.itemamt.rjust(7) + f'${self.itemprice}'.rjust(20)
    
def main():
    ilist = []
    for i in range(number):
        typ = input(f'Name of item {i+1}:')
        amt = input(f'Amount of item {i+1}:')
        price = input(f'Price of item {i+1}:')
        print()

        #create an item object
        iobj = RetailItem(typ, amt, price)
        #create object to the list
        ilist.append(iobj)
    return ilist

def displayitems(iteml):
    if not iteml:
        print("No items")
    else:
        print(f'Here is a summary of {number} items you added:')
        print(f"Item{'':<29}Amount{'':<11}Price")
        print('-'*60)
    for a in iteml:
        print(a)#iteml - list of objects

        
number = int(input('How many itmes will you add today?'))
items = main()
displayitems(items)


