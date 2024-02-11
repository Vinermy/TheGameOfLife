import os
import sys
import time

sys.path.insert(0, "../")
from CellularAutomata2D import CellularAutomata2D
from Ruleset import from_b_s

rules = from_b_s(b=[3], s=[2, 3])
automata = CellularAutomata2D(size=(19, 19), do_wrap=False, ruleset=rules,
                              density=min(1.0,
                                          max(0.0,
                                              float(
                                                  input("Input density:")
                                              )
                                              )
                                          )
                              )

for i in range(20):
    os.system('cls')
    automata.display()
    automata.step()
    time.sleep(0.5)