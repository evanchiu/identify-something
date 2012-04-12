#!/usr/bin/env python

# identify.py
# Tested with Python 2.7.2+
# Python utility for solving drawsomes 

import sys
import itertools

class Identifier:
    """A class for parsing input and searching through a Dictionary"""
    def __init__(self, filename = None):
        """Initializes with optional filename"""
        if filename != None:
            self.load(filename)

    def load(self, filename):
        """Loads data from file
        The file must have the number of letters as the first line
        Followed by any number of given letter strings"""
        # read file
        with open(filename) as f:
            lines = f.readlines()

        # First line is the length of the word
        length = int(lines[0].strip())

        # initialize with the rest of the lines
        self.init(length, lines[1:])

    def init(self, length, lines):
        """Sets up the state given the length and the given letter strings"""
        self.length = length

        # Start with the first line
        letters = list(lines[0].strip())

        # Look through other lines for unpotential letters
        for line in lines[1:]:
            # If a letter appears in letters, but not in the other line
            # it is cannot be part of the solution, i.e. unpotential
            unpotential = list(letters[:])
            for other_letter in line:
                try:
                    unpotential.remove(other_letter)
                except:
                    pass

            # Remove unpotential letters
            for bad in unpotential:
                try:
                    letters.remove(bad)
                except:
                    pass

        # Sort the letters and recombine to a single string
        letters.sort()
        self.letters = ''.join(letters)

    # Search through all permutations 
    def search(self, dictionary):
        """Search through dictionary for any permutation of the letters"""
        for perm in itertools.permutations(self.letters, self.length):
            word = ''.join(perm)
            result = dictionary.check(word)
            if result != None:
                print result


class Dictionary:
    """A class to maintain state looking through a dictionary wordlist file
    for calling check on lexicographically ordered strings"""
    
    def __init__(self, length, filename):
        """Initializes to give back words from filename of a given length"""
        self.length = length
        self.handle = open(filename)
        self.next()

    def next(self):
        """Jump to the next word in the dictionary of correct length"""
        self.word = self.handle.readline().strip()
        while len(self.word) != self.length:
            self.word = self.handle.readline().strip()

    def check(self, word):
        """check if word is in the dictionary, note words must be checked in
        alphabetical order. Returns the word if it exists or None if not"""
        while 1:
            if word == self.word:
                return word
            if self.word < word:
                self.next()
            else:
                return None


if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print 'usage: %s <filename>' % sys.argv[0]
        exit(1)

    identifier = Identifier(filename)
    dictionaryFile = '/usr/share/dict/words.pre-dictionaries-common'
    dictionary = Dictionary(identifier.length, dictionaryFile)
    identifier.search(dictionary)


