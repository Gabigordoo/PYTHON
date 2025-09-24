def name(first_name: str, second_name: str, third_name = None) -> str:
    if isinstance(third_name, str):
        complete_name: str = f"{first_name} {second_name} {third_name}"
    else:    
        complete_name: str = f"{first_name} {second_name}"
    return complete_name
    
print(name(first_name= "Gabriel", second_name="Rocha", third_name="Dias"))    