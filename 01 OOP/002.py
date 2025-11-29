class person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
    def age(self):
        print(2025-self.dob)
p1 =person("ram", 2000)
p2 = person("laxman", 1990)
p1.age()
p2.age()

        


        