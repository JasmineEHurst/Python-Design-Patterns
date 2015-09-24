#Simple dog class
class Dog:

    def __init__(self,name):
        self.name = name

    def speak(self):
        return "Woof!"

class DogFactory:
    #Concrete Factory

    def get_pet(self):
        #Returns a Dog object
        return Dog("RJ")
    def get_food(self):
        #Returns a Dog Food object
        return "Dog Food!"
class PetStore:
    #PetStore houses our Abstract Factory

    def __init__(self, pet_factory = None):
        #pet_Factory is our Abstract Factory
        self._pet_factory = pet_factory

    def show_pet(self):
        #Utility method to display the details of the objects return
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()
        print("Our pet is '{}'!".format(pet.name))
        print("Our pet says hello by '{}'".format(pet.speak()))
        print("Its food is '{}'!".format(pet_food))

# Create a Concrete Factory
factory = DogFactory()
#Create a pet store housing our Abstract Factory
shop = PetStore(factory)
#Invoke the utility method to show the details of our pet
shop.show_pet()
