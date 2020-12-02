from adventofcode.password import Password, count_valid_passwords


class TestPassword:
    class TestParse:
        def test_given(self):
            """
            Given:
            When:
            Then:
            """
            # arrange
            line = "1-3 a: abcde"
            # act
            result = Password.parse(line)
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
            result = Password.parse(line)
            # assert
            assert result.rule.min == 19
            assert result.rule.max == 123


    class TestEnforce:
        def test_given(self):
            # arrange
            line = "1-3 a: abcde"
            password: Password = Password.parse(line)
            # act
            result = password.is_rule_compliant()
            # assert
            assert result is True

        def test_given_min_wrong(self):
            # arrange
            line = "1-3 b: cdefg"
            password: Password = Password.parse(line)
            # act
            result = password.is_rule_compliant()
            # assert
            assert result is False

        def test_given_max_wrong(self):
            # arrange
            line = "1-3 b: bbbbbcdefg"
            password: Password = Password.parse(line)
            # act
            result = password.is_rule_compliant()
            # assert
            assert result is False


class TestMain:
    def test_given(self):
        # arrange
        lines = ["1-3 a: abcde",
                 "1-3 b: cdefg",
                 "2-9 c: ccccccccc"]
        # act
        result = count_valid_passwords(lines)

        # assert
        assert result == 2
