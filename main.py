import itertools
from english_words import english_words_lower_alpha_set as words

def main():
    #List of all letters used to make words
    letters = []

    #User puts in how many letters and what letters to use
    letterAmount = int(input("How many letters? "))
    for x in range(1, letterAmount + 1):
        letters.append(input("Letter " + str(x) + ": "))

    #List of words made
    result = []

    #Checks through all possible permutations of those letters and checks if that permutation is a word
    for letter in range(3, len(letters) + 1):
        for permutation in itertools.permutations(letters, letter):
            if ''.join(permutation) in words:
                result.append(''.join(permutation))

    #Shows you list of words :)
    print(result)

if __name__ == "__main__":
    main()
