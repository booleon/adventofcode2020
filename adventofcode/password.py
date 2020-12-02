class Rule(object):
    def __init__(self, min_lengh: int, max_lengh: int, letter: str):
        self.letter = letter
        self.max = int(max_lengh)
        self.min = int(min_lengh)


class Password(object):

    def __init__(self, password: str, rule: Rule):
        self.string = password
        self.rule = rule

    @classmethod
    def parse(cls, line: str):
        min_max, letter, password = line.split(" ")
        min_length, max_length = min_max.split('-')
        rule = Rule(min_length, max_length, letter[0])
        return Password(password, rule)

    def is_rule_compliant(self):
        number_of_letter = self.string.count(self.rule.letter)
        is_no_more_than_allowed = number_of_letter <= self.rule.max
        is_no_less_than_allowed = number_of_letter >= self.rule.min
        return is_no_less_than_allowed and is_no_more_than_allowed


def count_valid_passwords(lines):
    return len([line for line in lines if Password.parse(line).is_rule_compliant()])
