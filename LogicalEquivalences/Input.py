import os
import platform

def _clear() -> None:
    RunningOS = platform.system()
    if RunningOS == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def TestType() -> tuple[int,int]:
    ErrorFlag : bool = False
    while True:
        _clear()
        print("1. Test for Name\n2. Test for Equation\n")

        if ErrorFlag:
            print("Enter either 1 or 2\n")

        try:
            Input : int = int(input("Input : "))
            if Input == 1:
                return 0,1
            elif Input == 2:
                return 1,0
            else:
                raise ValueError
        except ValueError:
            ErrorFlag = True

def Answer(correct_option : int,input_info : str) -> bool:
    ErrorFlag : bool = False
    while True:
        _clear()
        print(input_info)

        if ErrorFlag: 
            print("Enter a number between 0-9\n")

        try:
            Input : int = int(input("Input : "))
            if Input < 0 or Input > 9: 
                raise ValueError
            return Input == correct_option
        except ValueError:
            ErrorFlag = True
        
def Replay() -> bool:
    print("\nReplay?\n\n1. Yes\n2. No\n")

    try:
        Input : int = int(input("Input : "))
        return Input == 1
    except ValueError: 
        return False