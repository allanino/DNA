from nose.tools import *
from dna.dna import DNA
def test_huff3():
    dna = DNA()
    assert_equal(dna.code['217'],'12012')
    assert_equal(dna.code['8'],'22002')


def testS1():
    pass