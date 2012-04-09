#!/usr/bin/env python

# identify.py
# Tested with Python 2.7.2+
# Python utility for solving drawsomes 

import sys
import itertools
import commands

class Drawsome:
    def __init__(self, filename = None):
        
        # load file if given
        if filename != None:
            self.load(filename)

    def load(self, filename):
        
        # read file
        with open(filename) as f:
            lines = f.readlines()

        # First line is the length of the word
        self.length = int(lines[0].strip())

        # Start with the second line
        self.letters = list(lines[1].strip())

        # Look through other lines for unpotential letters
        for line in lines[2:]:
            # Find unpotential by removing letters from the other line
            unpotential = list(self.letters[:])
            for other_letter in line:
                try:
                    unpotential.remove(other_letter)
                except:
                    pass

            # Remove unpotential letters
            for bad in unpotential:
                try:
                    self.letters.remove(bad)
                except:
                    pass

        self.letters = ''.join(self.letters)
        print self.length, self.letters

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

    ds = Drawsome(filename)
    ds.search()


