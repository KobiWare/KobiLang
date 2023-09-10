Tokens = []
CurrentTok = ""

STDLIBCOMMANDS = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def Tokenize(input):
    input = str(input)
    Tokens.clear()
    CurrentTok = ""

    for x in range(len(input)):
        if input[x] != ';' and input[x] != ' ' and input[x] != '(' and input[x] != ')' and input[x] != '"' and input[x] != ',':
            CurrentTok += input[x]
        else:
            Tokens.append(CurrentTok)
            CurrentTok = ""

    execute_tokens()

def execute_tokens():
    for x in range(len(Tokens)):
        match Tokens[x]:
            case "w":
                for y in range(x+2, len(Tokens)):
                    if Tokens[y] != '"':
                        print(Tokens[y], end=" ")
                    else:
                        print()
                        break
                print()
                break
            case "b":
                break
            case "a":
                num_one = int(Tokens[x+1])
                num_two = int(Tokenize[x+2])
                print(num_one+num_two)
                break
                    
while 1:
    UserInput = input()
    if UserInput[len(UserInput)-1] != ';':
        UserInput += ";"
    Tokenize(UserInput)
