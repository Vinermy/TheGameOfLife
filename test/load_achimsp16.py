import sys
from pprint import pprint

sys.path.insert(0, "../")
from SaveLoad import load_from_file

pprint(load_from_file("achimsp16.txt"))