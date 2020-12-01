from adventofcode.expense import is_equal_to_2020, get_number_summing_2020


class TestIsEqualTo2020:
    def test_given_two_entry_which_summ_equal_2020_return_true(self):
        # arrange
        entry1 = 1721
        entry2 = 299
        # act
        result = is_equal_to_2020(entry1, entry2)
        # assert
        assert result is True

    def test_given_two_entry_which_summ_not_equal_2020_return_false(self):
        # arrange
        entry1 = 1721
        entry2 = 50
        # act
        result = is_equal_to_2020(entry1, entry2)
        # assert
        assert result is False


class TestGetNumberSumming2020:
    def test_given_list_of_number_return_tuple_of_result(self):
        # arrange
        entries = [1721, 979, 366, 299, 675, 1456]
        # act
        result = get_number_summing_2020(entries)

        # assert
        assert 1721 in result
        assert 299 in result

    def test_given_list_of_unordered_number_return_tuple_of_result(self):
        # arrange
        entries = [979, 1721, 366, 299, 675, 1456]
        # act
        result = get_number_summing_2020(entries)

        # assert
        assert 1721 in result
        assert 299 in result