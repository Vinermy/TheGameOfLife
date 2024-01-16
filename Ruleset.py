from typing import Annotated


class Ruleset2D(object):
    """
    A class to represent a set of rules for a 2d cellular automata
    """
    rules: dict[tuple[int, ...], int]

    def __init__(self, rule_list: Annotated[list[int], 512]) \
            -> None:
        """
        Generates a ruleset from a list of values of the center cell.
        Every number from 0 to 511 gets converted to a configuration of
        a 3 by 3 piece of game field. The corresponding value in the
        rule_list determines the new state of the center cell

        :param rule_list: List of states of the center cell
        """
        self.rules = {}
        for i in range(512):
            conf = bin(i)[2::]
            conf = '0' * (9 - len(conf)) + conf
            configuration = tuple(map(int, conf))
            self.rules[configuration] = rule_list[i]


    def get_new_state(self, chunk: list[int]) -> int:
        """
        Get a new state of the center cell given a three-by-three chunk
        :param chunk: A three-by-three chunk of cells
        :return: New state of the center cell
        """
        chunk = tuple(chunk)
        return self.rules[chunk]


def from_b_s(b: list[int], s: list[int]) -> Ruleset2D:
    """
    Generates a ruleset from b/s notation.
    :param b: List of living neighbors count for the center cell to
    be born
    :param s: List of living neighbors count for the center cell to
    survive
    """
    rule_list = []
    for i in range(512):
        # Get the 3 by 3 field configuration
        conf = bin(i)[2::]
        conf = '0' * (9 - len(conf)) + conf
        configuration = tuple(map(int, conf))

        if configuration[4]:  # If the center cell is alive
            count = sum(configuration) - 1
            if count in s:
                rule_list.append(1)  # The center cell lives
            else:
                rule_list.append(0)  # The center cell dies
            continue

        else:  # If the center cell is not alive
            count = sum(configuration)
            if count in b:
                rule_list.append(1)  # The center cell is now alive
            else:
                rule_list.append(0)  # The center cell stays dead
            continue

    r = Ruleset2D(rule_list=rule_list)
    return r
