class Local_fantasy:
    def __init__(self, name, club, ):
        self.name = name
        self.club=club

    def paul(self):
        print(f" {self.name}  supporter of {self.club} is ranked from paul is", 3)

    def varal(self):
        print(f" {self.name} supporter of {self.club} is ranked from paul is", 2)


class National_fantasy(Local_fantasy):

    def __init__(self, name, nick, club):
        super().__init__( name, club)
        self.nick=nick

    def eth(self):
        print(f' {self.name} national rank is', 420)

    def overall(self):
        print(f" {self.name} ,from 10 million players, u r on", 200_000)
    
    def varal(self):
        print('National fantasy doesnot accept varal fantasy, no rank')

abx = Local_fantasy('Abdex','united')
abx = National_fantasy('Abdex','flopper','city')
dandi = Local_fantasy('dandi','Arsenal')
dandi = National_fantasy('dandi','danorith','chelsea')

abx.varal()  # function found in local fantasy
abx.paul()  # function found in local fantasy

