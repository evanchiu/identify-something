#!/usr/bin/env python

# identify.py
# Tested with Python 2.7.2+
# Python utility for solving drawsomes 

import sys
import itertools
import commands

class Identifier:
    def __init__(self, filename = None):
        
        # load file if given
        if filename != None:
            self.load(filename)

    def load(self, filename):
        
        # read file
        with open(filename) as f:
            lines = f.readlines()

        # First line is the length of the word
        length = int(lines[0].strip())

        # initialize with the rest of the lines
        self.init(length, lines[1:])

    def init(self, length, lines):
        self.length = length

        # Start with the second line
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
    def search(self):
        for perm in itertools.permutations(self.letters, self.length):
            word = ''.join(perm)
            dictionary = '/usr/share/dict/words.pre-dictionaries-common'
            output = commands.getoutput('grep "^%s$" %s' % (word, dictionary))
            if len(output) > 0:
                print output

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filename = sys.argv[1]
    else:
        print 'usage: %s <filename>' % sys.argv[0]
        exit(1)

    ds = Identifier(filename)
    print ds.length, ds.letters
    ds.search()


