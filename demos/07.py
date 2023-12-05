talk = "yes"

match talk:
    case "yes":
        print("You said yes")
    case "no":
        print("You said no")
    case "maybe":
        print("You said maybe")
    case _:
        print("I don't understand what you said")
