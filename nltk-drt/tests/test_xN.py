"""
Test suit for the temporaldrt module
"""
__author__ = "Alex Kislev, Emma Li, Peter Makarov"
__version__ = "1.0"
__date__ = "Tue, 24 Aug 2010"

import sys, os, pytest
sys.path.append("..")

from nltk_drt.util import Tester
from nltk_drt.wntemporaldrt import DrtParser

#background knowledge
BK = {
    'earlier' : r'all x y z.(earlier(x,y) & earlier(y,z) -> earlier(x,z)) & all x y.(earlier(x,y) -> -overlap(x,y))',

    'include' : r'all x y z.((include(x,y) & include(z,y)) -> (overlap(x,z)))',

    'die' : r'all x z y.((die(x) & AGENT(x,y) & die(z) & AGENT(z,y)) -> x = z)',

    'husband' : r'(([t,x,y],[POSS(y,x), husband(y)]) -> ([s],[married(s),THEME(s,x),overlap(t,s)]))',

    'married' : r'(([t,s],[married(s),THEME(s,x),overlap(t,s)]) -> ([x,y],[POSS(y,x), husband(y)]))',

    'own' : r'(([s,x,y],[own(s),AGENT(s,x),PATIENT(s,y)]) -> ([],[POSS(y,x)]))',

    'POSS' : r'(([t,y,x],[POSS(y,x)]) -> ([s],[own(s),AGENT(s,x),PATIENT(s,y),overlap(t,s)]))',

   'dead' : r'(([t,s,e,x],[include(s,t),abut(e,s),die(e),AGENT(e,x)]) -> ([],[dead(s),THEME(s,x),overlap(t,s)]))'
    }


@pytest.mark.xn_problem
def test_xn_problem(subtests):

    tester = Tester('file:./nltk-drt/data/grammar.fcfg', DrtParser, subtests)

    cases = [
        (11, "If Jones is away, he has left London.", "([n,x,z8],[(([s],[away(s), THEME(s,x), overlap(n,s)]) -> ([s018,e],[include(s018,n), overlap(s,s018), leave(e), AGENT(e,x), PATIENT(e,z8), abut(e,s018)])), London{sg,n}(z8), Jones{sg,m}(x)])"),
    ]
    tester.test(cases)


HASH_LINE = "#"*80

def print_header(header):
    len_hash = (74 - len(header)) // 2
    print("\n\t# {0} #\n\t### {1} {2} {1} ###\n\t# {0} #\n\n".format(HASH_LINE, "#"*len_hash, header))

TESTS = [("xN Problem", test_xn_problem)
         ]


def main():
    """Main function to start it all."""
    tester = Tester('file:../data/grammar.fcfg', DrtParser)
    for header, test in TESTS:
        print_header("Testing %s" % header)
        test(tester)
    print("\n\t{0} THE  END {0}".format("#"*37))

if __name__ == '__main__':
    main()
