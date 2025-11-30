class Pet:
    all = []
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception("Invalid pet type")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    def __repr__(self):
        return f"<Pet name={self.name} pet_type={self.pet_type}>"

    @classmethod
    def clear_all(cls):
        cls.all = []

class Owner:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise Exception("Name must be a non-empty string.")
        self.name = name
        Owner.all.append(self)

    def __repr__(self):
        return f"<Owner name={self.name}>"

    @classmethod
    def clear_all(cls):
        cls.all = []

    def pets(self):
        """Returns a list of pets belonging to this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def get_sorted_pets(self):
        """Returns a sorted list of pets belonging to this owner."""
        return sorted(self.pets(), key=lambda pet: pet.name)

    def add_pet(self, pet):
        """Adds a pet to this owner's collection of pets."""
        if isinstance(pet, Pet):
            pet.owner = self
        else:
            raise Exception("pet must be an instance of Pet")

    @classmethod
    def find_by_name(cls, name):
        """Finds an owner by their name."""
        return next((owner for owner in cls.all if owner.name == name), None)