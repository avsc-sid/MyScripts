print("What would you like to do?\n1. DNA to Complimentary Stand\n2. DNA to mRNA\n3. mRNA to DNA\n4. mRNA to Protein\n5. mRNA to tRNA\n")

def main():
    match input("\n>>> "):
        case "1":
            dna_to_strand()
        case "2":
            dna_to_mrna()
        case "3":
            mrna_to_dna()
        case "4":
            mrna_to_protein()
        case "5":
            mrna_to_trna()
        case _:
            print("That is not a valid option.")
            exit()

def dna_to_strand():
    dna = input("Enter your DNA sequence here\n>>> ").strip().upper()
    print("\n\n" + translate(dna, "dna"))

def dna_to_mrna():
    dna = input("Enter your DNA sequence here\n>>> ").strip().upper()
    print("\n\n" + translate(dna, "rna"))

def mrna_to_dna():
    mrna = input("Enter your mRNA sequence here\n>>> ").strip().upper()
    print("\n\n" + translate(mrna, "dna"))

def mrna_to_protein():
    pass

def mrna_to_trna():
    mrna = input("Enter your mRNA sequence here\n>>> ").strip().upper()
    print("\n\n" + translate(mrna, "rna"))

def translate(codons: str, end="rna") -> str:
    translated = ""
    for i in codons:
        match i:
            case "A":
                if end == "rna":
                    translated += "U"
                else:
                    translated += "T"
            case "T":
                translated += "A"
            case "C":
                translated += "G"
            case "G":
                translated += "C"
            case "U":
                translated += "T"
    return translated

if __name__ == "__main__":
    main()