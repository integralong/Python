#Week 11 Lecture 2 Part 1

#Topic: class vs instance variables

#---class definition---#

class App:
    appnum = 0 #class variable(only one exist; will be shared among objects)
    
    def __init__(self, name, apptype):
        self.appname = name #attribute (instance variable)
        self.apptype = apptype
        App.appnum += 1

    def __str__(self):
        return f'{self.appname} is a {self.apptype} app'

#end class

#---driver portion---#
def main():
    insta = App('Instagram', 'Photo/Videos Sharing')
    appinfo(insta, 'October', 2010)
    print(f'You have referred to {App.appnum} apps so far.')


    fb = App('Facebook', 'Social Media')
    appinfo(fb, 'February', 2004)
    print(f'You have referred to {App.appnum} apps so far.')
    


def appinfo(aobj, mth, yr):
    print(f'{aobj} that was created in {mth} {yr}.')
    


#---call to main---#
main()


