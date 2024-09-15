from random import randint,shuffle
import json
import Input

def main():

    with open("d.json",'r') as jsonFile:
        Laws : list[str] = json.load(jsonFile)
        #list[Name of Law, Law equation]
    
    Known,Unknown = Input.TestType()
    while True:

        shuffle(Laws)
        RandomOption : int = randint(0,9)

        InputInfo : str = ""
        for i,Law in enumerate(Laws):
            InputInfo += f"{i}. {Law[Known]}\n"
        InputInfo += f"\n{Laws[RandomOption][Unknown]}\n"

        Correct : bool = Input.Answer(RandomOption,InputInfo)
        if Correct: 
            print("\nCorrect!")
        else: 
            print(f"\nIncorrect\nAnswer : {Laws[RandomOption][Known]}")

        Replay : bool = Input.Replay()
        if not Replay:
            return

if __name__ == "__main__":
    main()