from src.pipelines import count_frequencies


def test_solution_has_all_elements():
    input_str = 'abcdefgabcdefg'

    output = count_frequencies(input_str)

    assert output.keys() == set(input_str)
