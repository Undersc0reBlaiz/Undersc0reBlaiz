#Imports
import csv

#Set up Class Beast
class Beast:
    '''
    Attributes:
        name: str

        Faction: str
        
        type: str
            melee, tank, ranged
            
        behaviour: str
            mobile, turret, flying

        nature: str
            hostile, neutral, passive

        prefered climate: str

        prefered height: int
    '''
    def __init__(self):
        self.name = "unknown"
        self.faction = "unknown"
        self.type = "unknown"
        self.behaviour = "unknown"
        self.nature = "unknown"
        self.preferedTemp = "unknown"
        self.preferedHeight = 0


    def __str__(self):
        output = f"Beast Name: {self.name}\n"
        output += f"Faction: {self.faction}\n"
        output += f"Type: {self.type}\n"
        output += f"Behaviour: {self.behaviour}\n"
        output += f"Nature: {self.nature}\n"
        output += f"Prefered spawn climate: {self.preferedTemp}\n"
        output += f"Prefered spawn height: {self.preferedHeight}\n"
        return output

#Set up Class Location
class Location:
    '''
    Attributes:

        Name: str

        Climate: str

        Height: int
    '''   
    def __init__(self):
        self.name = "unknown"
        self.climate = "unknown"
        self.height = 0
        self.collection = []
        

    def __str__(self):
        output = f"Name: {self.name}\n"
        output += f"Climate: {self.climate}\n"
        output += f"Height: {self.height}\n"
        return output


    def addLoc(self):
        location = Location()
        location.name = input("What is the Location name?")
        location.climate = input("What is the Locations climate?")
        location.height = input("What is the height of the Location?(0-1000)")
        print()
        print(location)
        global datarowsLoc
        datarowsLoc = [f'{location.name}',f'{location.climate}',f'{location.height}']
        with open('LocationList.csv', 'a', encoding='UTF8',newline='')as file:
            writer = csv.writer(file)
            writer.writerow(datarowsLoc)


    def findLoc(self):
        #search by name
        name = input("Please Enter the locations name, including capitalisation: ")
        for location in self.collection:
            if self.name == name:
                print(Location)
            
    #print all beasts in the collection
    def printAllLoc(self):
        print("Locations:")
        for Location in self.collection:
            print()
            print(Location)



        
#Set up Class Faction
class Faction:
    '''
    Faction:
        Name: str

        Intelligence: int

        Leader: str
    '''
    def __init__(self):
        self.name = "unknown"
        self.intelligence = 0
        self.leader = "unknown"
        self.collection = []

    def __str__(self):
        output = f"Faction Name: {self.name}\n"
        output += f"Faction Intelligence: {self.intelligence}\n"
        output += f"Faction Leader: {self.leader}\n"
        return output

    def addFaction(self):
        faction = Faction()
        faction.name = input("What is the Faction name?")
        faction.intelligence = input("What is the Factions intelligence level?")
        faction.leader = input("Who is the leader of the Faction?")
        print()
        print(faction)
        global datarowsFaction
        datarowsFaction = [f'{faction.name}',f'{faction.intelligence}',f'{faction.leader}']
        with open('FactionList.csv', 'a', encoding='UTF8',newline='')as file:
            writer = csv.writer(file)
            writer.writerow(datarowsFaction)
            
    def findFaction(self):
        #search by name
        name = input("Please Enter the factions name, including capitalisation: ")
        for faction in self.collection:
            if self.name == name:
                print(Faction)

    #print all factions in the collection
    def printAllFactions(self):
        print("Factions:")
        for Faction in self.collection:
            print()
            print(Faction)
    
#Set up Class Collection
class MonsterCollection:
    '''
    collection = List of monsters

    count = int
        number of monsters
    '''

    def __init__(self):
        self.collection = []
        self.count = 0

    def __str__(self):
        output = f"Total Number of Monsters: {self.count}\n"
        output += f"Collnection: {self.collection}\n"
        return output
    
#Making commands to edit collection

#add beast function
    def addBeast(self):
        beast = Beast()
        beast.name = input("What is the Beasts name?")
        beast.faction = input("What faction is the Beast apart of?")
        beast.type = input("What type of attacker is the Beast")
        beast.behaviour = input("What is the Beasts behaviour?")
        beast.nature = input("What is the Beasts nature toward the player?")
        beast.preferedTemp = input("What is the Beasts spawn temperature?")
        beast.preferedHeight = input("What is the Beasts spawn height? (0-1000)")
        print()
        print(beast)
        global datarows
        datarows = [f'{beast.name}',f'{beast.faction}',f'{beast.type}',f'{beast.behaviour}',f'{beast.nature}',f'{beast.preferedTemp}',f'{beast.preferedHeight}']
        with open('BestiaryList.csv', 'a', encoding='UTF8',newline='')as file:
            writer = csv.writer(file)
            writer.writerow(datarows)
        self.collection.append(beast)
        self.count += 1
        
#remove beast function
    def remBeast(self):
        entry = str(input("What is the name of the Beast?"))
        number = int(input("What is the Beasts numerical placement in the list? (use PrintAll to find out)"))
        number -= 1
        if 0 <= number < len(self.collection):
            for Beast in self.collection:
                if entry == Beast.name:
                    print("Removed Beast:")
                    print(Beast)
            monster = self.collection.pop(number)
            self.count -= 1
            with open('BestiaryList.csv', 'r') as inp, open('BestiaryList.csv', 'w') as out:
                writer = csv.writer(out)
                for row in csv.reader(inp):
                    if row[0] == entry:
                        writer.writerow(row)
                cols = ['Name','Faction','Type','Behaviour','Hostility','Climate','Height']
                writer.writerow(cols)
                for Beast in self.collection:
                    datarows = [f'{Beast.name}',f'{Beast.faction}',f'{Beast.type}',f'{Beast.behaviour}',f'{Beast.nature}',f'{Beast.preferedTemp}',f'{Beast.preferedHeight}']
                    writer.writerow(datarows)



#seatch by name
    def findBeast(self):
        name = input("Please Enter the Beasts name, including capitalisation: ")
        for Beast in self.collection:
            if Beast.name == name:
                print(Beast)
        

#get number of beasts
    def getNumBeast(self):
        return self.count
        print(f"Number of Beasts: {self.count}")

#print all beasts in the collection
    def printAllBeasts(self):
        print("Beasts in collection:")
        for Beast in self.collection:
            print()
            print(Beast)

    
#Actual run code
beast = Beast()
monstercollection = MonsterCollection()
location = Location()
faction = Faction()
#Writing into csv file
cols = ['Name','Faction','Type','Behaviour','Hostility','Climate','Height']
datarows = [f'{beast.name}',f'{beast.faction}',f'{beast.type}',f'{beast.behaviour}',f'{beast.nature}',f'{beast.preferedTemp}',f'{beast.preferedHeight}']
#checking if file already has data in it
with open('BestiaryList.csv', 'r')as file:
    csvReader = csv.reader(file, delimiter=',')
    for row in csvReader:
        if str(", ".join(row)) != 'Name, Faction, Type, Behaviour, Hostility, Climate, Height':
            with open('BestiaryList.csv', 'w', encoding='UTF8',newline='')as file:
                writer = csv.writer(file)
                writer.writerow(cols)
        else:
            break
        break

#Location csv file
colsLoc = ['Name','Climate','Height']
datarowsLoc = [f'{location.name}',f'{location.climate}',f'{location.height}']
#checking if file already has data in it
with open('LocationList.csv', 'r')as file:
    csvReader = csv.reader(file, delimiter=',')
    for row in csvReader:
        if str(", ".join(row)) != 'Name, Climate, Height':
            with open('LocationList.csv', 'w', encoding='UTF8',newline='')as file:
                writer = csv.writer(file)
                writer.writerow(colsLoc)
        else:
            break
        break

#Faction csv file
colsFaction = ['Name','Intelligence','Leader']
datarowsFaction = [f'{faction.name}',f'{faction.intelligence}',f'{faction.leader}']
#checking if file already has data in it
with open('FactionList.csv', 'r')as file:
    csvReader = csv.reader(file, delimiter=',')
    for row in csvReader:
        if str(", ".join(row)) != 'Name, Intelligence, Leader':
            with open('FactionList.csv', 'w', encoding='UTF8',newline='')as file:
                writer = csv.writer(file)
                writer.writerow(colsFaction)
        else:
            break
        break

#Adding data from beast csv file into collection
with open('BestiaryList.csv', 'r')as file:
    csvReader = csv.reader(file, delimiter=',')
    next(csvReader)
    for row in csvReader:
        beast = Beast()
        beast.name = row[0]
        beast.faction = row[1]
        beast.type = row[2]
        beast.behaviour = row[3]
        beast.nature = row[4]
        beast.preferedTemp = row[5]
        beast.preferedHeight = row[6]
        monstercollection.collection.append(beast)

#Adding data from location csv file into collection
with open('LocationList.csv', 'r')as file:
    csvReader = csv.reader(file, delimiter=',')
    next(csvReader)
    for row in csvReader:
        location = Location()
        location.name = row[0]
        location.climate = row[1]
        location.height = row[2]
        location.collection.append(location)
#Adding data from beast faction file into collection
with open('FactionList.csv', 'r')as file:
    csvReader = csv.reader(file, delimiter=',')
    next(csvReader)
    for row in csvReader:
        faction = Faction()
        faction.name = row[0]
        faction.intelligence = row[1]
        faction.leader = row[2]
        faction.collection.append(faction)
        

#Beast UI
def beastUI():
    Run = int(input("""
Options:
[1]Add Beast
[2]Remove Beast
[3]Find Beast by name
[4]Return Number of Beasts in bestiary
[5]Print all Beasts
    """))
    if Run == 1:
        monstercollection.addBeast()
    if Run == 2:
        monstercollection.remBeast()
    if Run == 3:
        monstercollection.findBeast()
    if Run == 4:
        monstercollection.getNumBeast()
    if Run == 5:
        monstercollection.printAllBeasts()


def locationUI():
    Run = int(input("""
Options:
[1]Add Location
[2]Find Location
[3]Print all Locations
    """))
    if Run == 1:
        location.addLoc()
    if Run == 2:
        location.findLoc()
    if Run == 3:
        location.printAllLoc()

def factionUI():
    Run = int(input("""
Options:
[1]Add Faction
[2]Find Faction
[3]Print all Factions
    """))
    if Run == 1:
        faction.addFaction()
    if Run == 2:
        faction.findFaction()
    if Run == 3:
        faction.printAllFactions()

    
#Options/UI        

startUI = True
while startUI == True:
    
    Query = int(input("""
Options:
[1]Beast Menu
[2]Location Menu
[3]Faction Menu
[4]Quit
    """))
    if Query == 1:
        beastUI()
    if Query == 2:
        locationUI()
    if Query == 3:
        factionUI()
    if Query == 4:
        exit()
