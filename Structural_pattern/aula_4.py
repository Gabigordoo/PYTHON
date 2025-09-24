def execute_command(command):
    match command.split():
        case ['ls' | 'list', *directories]:
            for directory in directories:
                print('$ listing directory from', directory)
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')
