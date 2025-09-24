def execute_command(command):
    match command.split():
        case ['ls' | 'list', *directories] if len(directories) > 1:
            for directory in directories:
                print('$ listing ALL directories from', directory)
        case ['ls' | 'list', *directories] if len(directories) <= 1:
            print('$ listing ONE directory from', directories[0])
        case ['cd', path]:
            print('$ changing directory to', path)
        case _:  # Não obrigatório
            print('$ command not implemented')

    print('...rest of the code')