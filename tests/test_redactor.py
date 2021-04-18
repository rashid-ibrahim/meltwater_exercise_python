from controllers import redactor


# Gonna need some sort of class to hold variables
def test_simple_redact():
    test_words = 'fox, lazily, fence'
    test_string = 'The quick brown fox jumped lazily over the fence.'
    expected = 'The quick brown XXXXXXXX jumped XXXXXXXX over the XXXXXXXX.'

    res = redactor.redact(test_words, test_string)

    assert res == expected


def test_no_redactions():
    test_words = 'python, apples, firefox'
    test_string = 'The quick brown fox jumped lazily over the fence.'
    expected = 'The quick brown fox jumped lazily over the fence.'

    res = redactor.redact(test_words, test_string)

    assert res == expected


def test_spaces_only():
    test_words = 'fox lazily fence'  # NO commas between the words
    test_string = 'The quick brown fox jumped lazily over the fence.'
    expected = 'The quick brown XXXXXXXX jumped XXXXXXXX over the XXXXXXXX.'

    res = redactor.redact(test_words, test_string)

    assert res == expected


def test_commas_only():
    test_words = 'fox,lazily,fence'  # ONLY commas between the words
    test_string = 'The quick brown fox jumped lazily over the fence.'
    expected = 'The quick brown XXXXXXXX jumped XXXXXXXX over the XXXXXXXX.'

    res = redactor.redact(test_words, test_string)

    assert res == expected


def test_space_then_comma():
    test_words = 'fox ,lazily ,fence'  # Spaces and then commas between the words
    test_string = 'The quick brown fox jumped lazily over the fence.'
    expected = 'The quick brown XXXXXXXX jumped XXXXXXXX over the XXXXXXXX.'

    res = redactor.redact(test_words, test_string)

    assert res == expected


def test_redact_everything():
    test_words = 'The quick brown fox jumped lazily over the fence.'
    test_string = 'The quick brown fox jumped lazily over the fence.'
    expected = 'XXXXXXXX XXXXXXXX XXXXXXXX XXXXXXXX XXXXXXXX XXXXXXXX XXXXXXXX XXXXXXXX XXXXXXXX.'

    res = redactor.redact(test_words, test_string)

    assert res == expected
