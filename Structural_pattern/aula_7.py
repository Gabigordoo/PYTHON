def execute_command(command):
    match command.split():
        case ['ls' | 'list', _, *directories, _]:
            for directory in directories:
                print('$ listing ALL directories from', directory)
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')


# execute_command('ls /home/ /Users /mais')
# execute_command('ls /one/')

# With dicts
# case {'name': _, 'last': 'Doe'}:
# case {'name': 'Otávio' as name, 'last': 'Doe'} as data:


def execute_command(command):
    match command:
        case {'command': 'ls', 'directories': [_, *_]}:
            for directory in command['directories']:
                print('$ listing ALL directories from', directory)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')
