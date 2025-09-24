class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        
    @property
    def full_name(self):
        return f"{self.firstname} {self.lastname}"
    
def say_my_name(person: Person) -> list[Person]:
    return [person.__dict__]      

print(say_my_name(Person("Gabriel", "Rocha")))
