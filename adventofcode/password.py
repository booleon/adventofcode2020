from abc import ABC


class Rule(ABC):
    def is_compliant(self, password: str) -> bool:
        pass


class SledRule(Rule):
    def __init__(self, min_lengh: int, max_lengh: int, letter: str):
        self.letter = letter
        self.max = int(max_lengh)
        self.min = int(min_lengh)

    def is_compliant(self, password: str):
        number_of_letter = password.count(self.letter)
        is_no_more_than_allowed = number_of_letter <= self.max
        is_no_less_than_allowed = number_of_letter >= self.min
        return is_no_less_than_allowed and is_no_more_than_allowed


class ToboganRule(Rule):
    def __init__(self, first_position: int, second_position: int, letter: str):
        self.letter = letter
        self.second_position = int(second_position)
        self.first_position = int(first_position)

    def is_compliant(self, password: str):
        first_letter = password[self.first_position - 1]
        second_letter = password[self.second_position - 1]
        is_first_letter_compliant = first_letter == self.letter
        is_second_letter_compliant = second_letter == self.letter
        return is_first_letter_compliant ^ is_second_letter_compliant


class Password:

    def __init__(self, password: str, rule: Rule):
        self.string = password
        self.rule = rule

    @classmethod
    def parse_with_sled_rental_rule(cls, line: str):
        return cls._set_rule(line, SledRule)

    def is_rule_compliant(self):
        return self.rule.is_compliant(self.string)

    @classmethod
    def parse_with_sled_tobogan_rule(cls, line):
        return cls._set_rule(line, ToboganRule)

    @classmethod
    def _set_rule(cls, line: str, rule_model):
        first_second_position, letter, password = line.split(" ")
        first_position, second_position = first_second_position.split('-')
        rule = rule_model(first_position, second_position, letter[0])
        return Password(password, rule)


def count_sled_valid_passwords(lines):
    return len([line for line in lines if Password.parse_with_sled_rental_rule(line).is_rule_compliant()])


def count_tobogan_valid_passwords(lines):
    return len([line for line in lines if Password.parse_with_sled_tobogan_rule(line).is_rule_compliant()])
