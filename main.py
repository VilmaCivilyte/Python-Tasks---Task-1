# Turimas "users" masyvas. 

# Parašykite funkcijas, kurios atliks nurodytas užduotis:
# 1. funkcija "filterDogOwers" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins "users", kurie turi augintinį.
# 2. funkcija "filterAdults" - kaip argumentą priims masyvą ir duoto masyvo 
# atveju grąžins masyvą su "users", kurie yra pilnamečiai.

users = [
  { "id": '1', "name": 'John Smith', "age": 20, "hasDog": True },
  { "id": '2', "name": 'Ann Smith', "age": 24, "hasDog": False },
  { "id": '3', "name": 'Tom Jones', "age": 31, "hasDog": True },
  { "id": '4', "name": 'Rose Peterson', "age": 17, "hasDog": False },
  { "id": '5', "name": 'Alex John', "age": 25, "hasDog": True },
  { "id": '6', "name": 'Ronald Jones', "age": 63, "hasDog": True },
  { "id": '7', "name": 'Elton Smith', "age": 16, "hasDog": True },
  { "id": '8', "name": 'Simon Peterson', "age": 30, "hasDog": False },
  { "id": '9', "name": 'Daniel Cane', "age": 51, "hasDog": True },
]

# def fifilterDogOwers(users):
#     for i in range (len(users)): # 
#       name = users[i].get("name") # gaunu name, kuriuos idedu i print
#       if users[i].get("hasDog") == True: # if f-ja tikrinu kurie name turi augintinius
#         print(f"{name}", "turi šunį")
#       else:
#         print(f"{name}", "neturi šuns")


def fifilterDogOwers(users):
    has_Dog = []
    for i in range (len(users)): # kiekvienai masyvo users reiksmei sukuriamas ciklas
      if users[i].get("hasDog") == True: # tikrinu ar reiksme hasDog yra True
        has_Dog.append(users[i].get("name")) # jei True, tada reiksme idedu i masyva has_Dog
    print(has_Dog) # atspausdinu sarasa name, kurie turi augintini

fifilterDogOwers(users)

def filterAdults(users):
    adults = []
    for x in range (len(users)): # sukuriamas ciklas, kiekvienai reiksmei patikrinti
      if users[x].get("age") >= 18: # tikrinu ar users age yra daugiau/lygu 18
        adults.append(users[x].get("name")) # jei True, tada reiksme idedu i masyva adults
        # adults.append(users[x]) # jei noreciau, kad atspausdintu pilna sarasa su visom reiksmem (kuriems daugiau nei 18)
    print(adults) # atspausdinu sarasa su name, kurie turi daugiau nei 18 metu

filterAdults(users)
