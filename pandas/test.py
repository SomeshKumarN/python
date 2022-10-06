
from enum import Enum
import numbers
from re import M
import string
import sample as ktr
from sample import vishnutestmodule as dd


def customPrint():
    print("printing from test.py")

def referPrint():
    ktr.testmodule.testfunctionPrint()
    dd.testfunctionPrint()


customPrint()
referPrint()


"""number: int, float

text : string

decisioning : bool

sequencing : list, tuple

set sequencing: set

dictionary :dict

map - """

def functionname(arguments):
    return 



class Students(Enum):
    VISHNU=989898989
    SOMESH=898998899
    VEERAA=789798989

SOMESH=23423423

print(Students.SOMESH.value)
SOMESH=000000
print(SOMESH)