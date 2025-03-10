import pyperclip  # Importer biblioteket for å kopiere til utklippstavlen

def spørOmEmoji():
    emoji = [
    "❤", "😀", "😂", "💀", "😭", "🖕", "😍", "😊", "😎", "🥺", 
    "😅", "😆", "🙌", "👏", "💪", "✨", "🌟", "👍", "👎", "🙄", 
    "🥳", "🔥", "💥", "🎉", "🎈", "🥰", "😜", "😋", "😝", "🥱", 
    "😒", "😌", "😤", "😩", "🥺", "🤗", "🤩", "😇", "😈", "🤭", 
    "😷", "🤒", "🥴", "🤤", "🤡", "😺", "😻", "😼", "😽", "😹", 
    "😻", "😿", "😼", "😎", "🤓", "😶", "🙃", "😪", "😷", "😵", 
    "🥶", "🥵", "😱", "🤯", "🤔", "😳", "😠", "😧", "😦", "😵‍💫", 
    "😤", "😡", "😠", "💩", "🫣", "🫡", "🫠", "🤐", "🧐", "😬", 
    "😺", "🧛", "🧟", "🧝", "🧙", "🦸", "🦹", "🤖", "👽", "💀", 
    "👻", "🎃", "😈", "👹", "👺", "👻", "👽", "👁", "👀", "👅", 
    "🍕", "🍔", "🌭", "🍩", "🍪", "🍎", "🍉", "🍓", "🍒", "🥑", 
    "🥔", "🌮", "🍣", "🍺", "🍻", "🥤", "🍸", "🍷", "🥂", "🎶", 
    "📱", "💻", "🖥", "🎮", "🎲", "🧸", "📸", "⏰", "🕒", "🔑", 
    "🧳", "🛏", "🧼", "🎁", "🌍", "🌎", "🌏", "🏖", "🏝", "⛱", 
    "🏠", "🏡", "🏢", "🚗", "🚙", "🚕", "🚓", "🚕", "✈️", "🚀", 
    "🚂", "🛳", "🛵", "🏍", "⛷", "🏀", "⚽️", "🏈", "🎾", "🏉", 
    "🎯", "🎯", "⚾️", "🏏", "🏑", "🏒", "🏓", "🧗", "🏄", "🚴", 
    "⛹️", "🤸", "🤼", "🍆", "😩", "☕", "🍉", "🌶", "🍓", "🧀", 
    "🍴", "🥩", "🍞", "🥖", "🫛", "🍦", "🍧", "🍪", "🥨", "🍯", 
    "🍭", "🍬", "🍡", "🥠", "🍮", "🧃", "🥝", "🍋", "🍊", "🍌", 
    "🍍", "🍑", "🥭", "🍍", "🍉", "🌽", "🍜", "🥖", "🍙", "🥠", 
    "🥢", "🥣", "🥒", "🍅", "🧄", "🧅", "🍚", "🍜", "🥟", "🍤", 
    "🦐", "🦑", "🥥", "🍪", "🍔", "🍤", "🥘", "🥣", "🫛", "🥩", 
    "🍖", "🦴", "🍝", "🥧", "🥡", "🐶", "🐱", "🐭", "🐹", "🐰", 
    "🐸", "🐯", "🐨", "🐻", "🐼", "🐧", "🐦", "🐤", "🐣", "🐥", 
    "🐍", "🦋", "🐛", "🐜", "🐦", "🐝", "🐞", "🦗", "🦗", "🐜", 
    "🐘", "🦌", "🦔", "🦒", "🦓", "🦝", "🦢", "🦩", "🦜", "🦚", 
    "🦆", "🦤", "🦦", "🦘", "🦙", "🦕", "🦗", "🦦", "🦩", "🦣",
    "🐯", "🐅", "🐆", "🐈", "🦁", "🐩", "🐕", "🐇", "🐈‍⬛", "🐾",
]


    # Vis emojiene og spør brukeren om valget
    for i, em in enumerate(emoji):
        print(f"{i}: {em}", end='  ')
        if (i + 1) % 10 == 0:  # Ny linje hver 10. emoji
            print()

    valg = int(input("\nVelg nummeret på din emoji: "))
    
    # Sørg for at valget er gyldig
    if 0 <= valg < len(emoji):
        print(f"Du valgte: {emoji[valg]}")
        return emoji[valg]
    else:
        print("Ugyldig valg!")

def spørOmAntall():
    emoji = spørOmEmoji()  # Hent den valgte emojien
    antall = int(input("Hvor mange emojier ønsker du? Skriv antall: "))
    
    # Lag en streng med det ønskede antallet emojier
    output = " ".join([emoji] * antall)
    print(f"Her er {antall} emojier: {output}")
    
    # Spør om brukeren vil kopiere til utklippstavlen
    if input("Vil du kopiere til utklippstavlen? (ja/nei) ").lower() == "ja":
        pyperclip.copy(output)
        print("Emojiene er kopiert!")
    else:
        print("Ok, ha en fin dag!")

# Kjøre hovedfunksjonen
spørOmAntall()
