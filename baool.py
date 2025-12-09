#  python crash course 9-1 & 9-4-  Restaurant
class Restaurant: 
    def __init__(self,res_name, cuis_type):
        self.x=res_name
        self.y=cuis_type
        self.served= 0
    def describe(self):
        return (f'The restaurant is {self.x} and it has {self.y} and has served {self.served} ppl')
    
    def update(self,new_served):
        self.served=new_served
    def add_serves(self,added):
        self.served+= added

res1=Restaurant('Hilton', '5 stars')
print(f'restaurant name is {res1.x}')
print(res1.describe())
print('----modified report of served customers-----')
res1.update(1_000_000)
print(res1.describe())
print("////New increment report of served customers///")
res1.update(1_000_000)
res1.add_serves(5_000)
print(res1.describe())


x,y,z='-','|','-'
print(x*20,y*20,z*20)

# 9-3: Users
class User:
    def __init__(self, first, last, age, job):
        self.f = first
        self.l = last
        self.age = age
        self.j = job
        self.c= 'American'

    def describe(self):
        print( f"""he's {self.f} {self.l}, a {self.age} yrs old  {self.j}""".title())


p1 = User("Bob", "camen", 23, "enterprenur")
p2 = User("Carol", "nester", 32, "pro football player")
print(f"know {p1.f}?")
p1.describe()
print(f"what about {p2.f}?")
p2.describe()
