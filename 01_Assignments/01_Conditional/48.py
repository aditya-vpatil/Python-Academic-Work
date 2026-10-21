'''Print language choice using match case'''


lang = input("Enter language (Python, Java, C++): ").capitalize()
match lang:
    case "Python": print("You chose Python scripting")
    case "Java": print("You chose Java application development")
    case "C++": print("You chose C++ systems programming")
    case _: print("Language not listed")
