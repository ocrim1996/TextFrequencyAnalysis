import math
import re
import string
import sys
from collections import Counter
import matplotlib.pyplot as plt
import pandas


# Shows the list of functions that can be run, and the user chooses one of them.
def option_menu():
    while True:
        print("---- TEXT FREQUENCY ANALYSIS (EXERCISE 3.1) " + "-" * 200)
        print("List of available functions:")
        print("1) Frequency histogram of the 26 letters.")
        print("2) Empirical distribution, coincidence index and entropy of m-grams distribution.")
        print("3) Exit.\n")
        try:
            chosen_function = int(input("\U0000270F Select the number of the function to run: "))
            if 1 <= chosen_function <= 3:
                return chosen_function
            else:
                print("\nYou must enter a number from 1 to 3\n")
        except ValueError:
            print("\nYou must enter a number from 1 to 3\n")
        input("Press Enter to continue.\n")


# Returns the txt file inserted in input by the user.
def get_text_file():
    # Opens and reads the input txt file.
    file_name = input("\U0000270F Insert the path of the TXT file: ")
    try:
        file = open(file_name, 'r')
    except FileNotFoundError:
        print("\nFile not found!\n")
        sys.exit(0)

    # The txt file is cleaned up and only 26 characters remain.
    text = clean_up_text(file.read())
    return text


# Prepares and returns the text with only the 26 characters of the alphabet, without numbers and punctuation.
def clean_up_text(text):
    text = text.lower()
    text = text.replace('\n', '').replace(' ', '').replace('-', '')
    text = re.sub('[% s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\d+', '', text)
    text = text.replace('è', 'e').replace('é', 'e').replace('à', 'a').replace('ù', 'u').replace('ò', 'o').replace('ì',
                                                                                                                  'i')
    return text


# Plots the histogram of frequencies.
def create_frequencies_histogram(data):
    counts = Counter(data)
    df = pandas.DataFrame.from_dict(counts, orient='index')
    df.plot(kind='bar', color='blue', legend=None)
    plt.title("Character Frequencies")
    plt.ylabel('Frequency')
    plt.xlabel('Characters')
    plt.savefig('frequency_histogram.pdf')
    plt.show()


# Generates and return m-grams of the input text.
def generate_grams(text, m):
    m_grams = [text[i:i + m] for i in range(0, len(text))]
    return m_grams


# Generates and return the empirical distribution of m-grams.
def get_empirical_distribution(text, m):
    ed = {}
    grams = generate_grams(text, m)
    for g in grams:
        if g in ed:
            ed[g] = ed[g] + 1
        else:
            ed[g] = 1
    for g in ed:
        ed[g] = ed[g] / len(grams)

    # Orders by key the results of empirical distribution.
    ed_items = ed.items()
    ed = sorted(ed_items)
    ed = dict(ed)
    return ed


# Calculates and returns the coincidence index of the empirical distribution of m-grams.
def get_coincidence_index(empirical_distribution):
    c_index = 0
    for p in empirical_distribution:
        c_index = c_index + (empirical_distribution[p]) ** 2
    return c_index


# Calculates and returns the entropy of the empirical distribution of m-grams.
def get_entropy(empirical_distribution):
    entropy = 0
    for i in empirical_distribution:
        probability = empirical_distribution[i]
        entropy = entropy + probability * math.log(probability, 2)
    return -1 * entropy


# Exposes all the functions for the various choices.
def main():
    while True:

        # Asks the user what function wants to run.
        choice = option_menu()

        # Runs the function selected by the user
        if choice == 1:
            text = get_text_file()

            # Creates a list and order the characters in alphabetical order so that the histogram goes from A to Z.
            data = list(text)
            data.sort()

            # Plots the frequency histogram.
            create_frequencies_histogram(data)

        elif choice == 2:
            text = get_text_file()

            # The user inserts the value of m (1-gram, 2-gram, 3-gram, 4-gram etc.)
            m = int(input("\U0000270F Insert the integer value of m (m-grams): "))

            # Calculates the empirical distribution of m-grams.
            empirical_distribution = get_empirical_distribution(text, m)
            print('\n\U00002022 Empirical distribution of ' + str(m) + '-grams : \n', empirical_distribution)

            # Calculates the coincidence index and entropy of the empirical distribution of m-grams.
            coincidence_index = get_coincidence_index(empirical_distribution)
            distribution_entropy = get_entropy(empirical_distribution)
            print('\n\U00002022 Index of coincidence of the ' + str(m) + '-grams distribution:', coincidence_index)
            print('\n\U00002022 Entropy of the ' + str(m) + '-grams distribution:', distribution_entropy, "\n")

        elif choice == 3:
            sys.exit(0)
        input("\nPress Enter to return to the selection menu.\n")


if __name__ == "__main__":
    main()
