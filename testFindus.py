import pyperclip  # Importerer biblioteket for å kopiere til utklippstavlen

# Spør antall Findus'er en ønsker.
def main():
    antall = int(input("Hvor mange Findus'er ønsker du? "))
    skrivFinduser(antall)

# Skriver alle Findus'ene.
def skrivFinduser(n):
    output = ""  
    for i in range(n):
        print("🐈", end=" ") #Gjør at vi får alle kattene i samme linje, ikke flere linjer i terminalen.
        output += "🐈 "  

    print(" ")  # Lager en ny linje etter utskriften
    spør(output)  

# Spør brukeren om de vil kopiere teksten
def spør(output):
    svar = input("Har du lyst å kopiere? (ja/nei) ")  
    if svar == "ja":
        pyperclip.copy(output)  
        print("\nFindus-rekken er kopiert! Prøv å lime den inn (Ctrl+V / Cmd+V).")
    else:
        print("Ok, ha en fin dag!")

main()