


class People:
    def __init__(self, age: int, name: str):
        super().__init__()
        self.age: int = age
        self.name: str = name.strip()

    def say_my_name(self) -> None:
        print(f"My name is {self.name} and my age is {self.age}")

def create_list(peoples: list[People]) -> list[dict[str, int | str]]:
    valid_peoples: list = []
    for people in peoples:
        match people:
            case People(age=age, name=name) if age >= 18 and len(people.name) > 3 :
                valid_peoples.append(people.name)
    return [{"age": people.age *2, "name": people.name} for people in peoples if people.name in valid_peoples]         
    

            
print(create_list([People(20, "Gabriel"), People(19, "Gabriela")]))