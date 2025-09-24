from dataclasses import dataclass

def execute_command(command: str):
    match command:
        case "ls":
            print('$ listing files')
        case 'cd':
            print('$ changing directory')
        case _:
            print('$ command not implemented')

    print('...rest of the code')

execute_command("cd")