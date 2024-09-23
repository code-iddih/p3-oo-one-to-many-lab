class Owner:
    def __init__(self, name):
        self.name = name
        self.pets_list = []  # Public list to store pets

    def add_pet(self, pet):
        """Adds a pet to the owner if it's a valid Pet instance."""
        if not isinstance(pet, Pet):
            raise Exception("You can only add an instance of Pet.")
        pet.owner = self  # Set the owner for the pet
        self.pets_list.append(pet)  # Add the pet to the owner's pets list

    def pets(self):
        """Returns a full list of the owner's pets."""
        return self.pets_list

    def get_sorted_pets(self):
        """Returns a sorted list of pets by their names."""
        return sorted(self.pets_list, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []  # Class variable to store all instances of Pet

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        # Validate the pet type
        if pet_type not in self.PET_TYPES:
            raise Exception(f"'{pet_type}' is not a valid pet type. Choose from {self.PET_TYPES}.")

        # Add the pet to the list of all pets
        self.__class__.all.append(self)

        # Automatically add this pet to the owner's pet list if an owner is provided
        if owner is not None:
            owner.add_pet(self)

    def __repr__(self):
        return f"{self.name} ({self.pet_type})"
