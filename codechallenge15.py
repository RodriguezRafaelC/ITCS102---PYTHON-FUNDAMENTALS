animelist = []
isContinue = True
print("Welcome to Anime Lister!\nEnter 'exit' to stop.")

while isContinue == True:
    anime = input("Enter your favorite anime: ")

    if anime.lower() == "exit":
        print("\nHere is your list of favorite anime:")
        print(animelist)
        break

    animelist.append(anime)
    print(f"{anime} has been added to the list.")