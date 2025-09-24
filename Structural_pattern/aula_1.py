from dataclasses import dataclass


def execute_command(command: str):
    if command == 'ls':
        print('$ listing files')
    elif command == 'cd':
        print('$ changing directory')
    else:
        print('$ command not implemented')

    print('...rest of the code')
    
