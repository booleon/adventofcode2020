from adventofcode.password import Password, count_sled_valid_passwords, ToboganRule, count_tobogan_valid_passwords


class TestPassword:
    class TestParseWithSledRentalRule:
        def test_given(self):
            """
            Given:
            When:
            Then:
            """
            # arrange
            line = "1-3 a: abcde"
            # act
            result = Password.parse_with_sled_rental_rule(line)
            # assert
            assert result.rule.min == 1
            assert result.rule.max == 3
            assert result.rule.letter == "a"
            assert result.string == "abcde"

        def test_big_numbers(self):
            """
            Given:
            When:
            Then:
            """
            # arrange
            line = "19-123 a: abcde"
            # act
            result = Password.parse_with_sled_rental_rule(line)
            # assert
            assert result.rule.min == 19
            assert result.rule.max == 123

    class TestParseWithTobogganRentalRule:
        def test_given(self):
            """
            Given:
            When:
            Then:
            """
            # arrange
            line = "1-3 a: abcde"
            # act
            result = Password.parse_with_sled_tobogan_rule(line)
            # assert
            assert result.rule.first_position == 1
            assert result.rule.second_position == 3
            assert result.rule.letter == "a"
            assert result.string == "abcde"

    class TestEnforce:
        def test_given(self):
            # arrange
            line = "1-3 a: abcde"
            password: Password = Password.parse_with_sled_rental_rule(line)
            # act
            result = password.is_rule_compliant()
            # assert
            assert result is True

        def test_given_min_wrong(self):
            # arrange
            line = "1-3 b: cdefg"
            password: Password = Password.parse_with_sled_rental_rule(line)
            # act
            result = password.is_rule_compliant()
            # assert
            assert result is False

        def test_given_max_wrong(self):
            # arrange
            line = "1-3 b: bbbbbcdefg"
            password: Password = Password.parse_with_sled_rental_rule(line)
            # act
            result = password.is_rule_compliant()
            # assert
            assert result is False


class TestTobogan:
    class TestIsCompliant:
        def test_given_compliant(self):
            # arrange
            first_position = 1
            second_position = 3
            letter = "a"
            password = "abcde"
            # act
            result = ToboganRule(first_position, second_position, letter).is_compliant(password)

            # assert
            assert result is True

        def test_given_not_compliant(self):
            # arrange
            first_position = 1
            second_position = 3
            letter = "b"
            password = "cdefg"
            # act
            result = ToboganRule(first_position, second_position, letter).is_compliant(password)

            # assert
            assert result is False

        def test_given_not_compliant_2letters(self):
            # arrange
            first_position = 2
            second_position = 9
            letter = "c"
            password = "ccccccccc"
            # act
            result = ToboganRule(first_position, second_position, letter).is_compliant(password)

            # assert
            assert result is False


class TestCountSledValidPasswords:
    def test_given_compliant(self):
        # arrange
        lines = ["1-3 a: abcde",
                 "1-3 b: cdefg",
                 "2-9 c: ccccccccc"]
        # act
        result = count_sled_valid_passwords(lines)

        # assert
        assert result == 2


class TestCountToboganValidPasswords:
    def test_given_compliant(self):
        # arrange
        lines = ["1-3 a: abcde",
                 "1-3 b: cdefg",
                 "2-9 c: ccccccccc"]
        # act
        result = count_tobogan_valid_passwords(lines)

        # assert
        assert result == 1