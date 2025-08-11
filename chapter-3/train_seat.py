seat_type = input("Enter seat type (sleeper/ac/general/luxury)").lower()


match seat_type:
    case "sleeper":
        print("Sleeper - No Ac Available")
    case "ac":
        print("AC Available")
    case "general":
        print("No AC Available")
    case "luxury":
        print("AC Available")
    case _:
        print("Invalid seat type")        