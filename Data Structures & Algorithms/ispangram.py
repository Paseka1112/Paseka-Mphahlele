import sys
import stdio
from instream import InStream
import string
import csv

def ispangram(s):
    """A pangram (from the Greek pan- "all" and gramma "letter") is a short sentence that contains every letter of the alphabet at least onc"""
    alphabet = string.ascii_lowercase
    s = s.lower()
    collected = ''

    for char in s:
        if char in alphabet and char not in collected:
            collected = collected + char
    
    collected = sorted(collected)

    if collected == list(alphabet):  return True
    else:
        return False
        
def main():
    filename = sys.argv[1]
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            s = row[0]
            result = ispangram(s)
            stdio.writeln(result)

if __name__ == '__main__': main()
    



