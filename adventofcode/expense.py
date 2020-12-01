def is_equal_to_2020(entry1: int, entry2: int):
    return entry1 + entry2 == 2020


def get_number_summing_2020(entries):
    local_entries = entries[:]
    potential_result = ()
    while local_entries and not potential_result:
        first_number = local_entries.pop(0)
        potential_result = [(first_number, other_entry)
                            for other_entry in local_entries
                            if is_equal_to_2020(first_number, other_entry)]
    return potential_result[0]
