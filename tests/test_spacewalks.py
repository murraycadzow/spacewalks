from eva_data_analysis import text_to_duration

def test_text_to_duration_integer_no_minutes():
    actual = text_to_duration("10:00") 
    expected = 10.00
    assert(actual == expected)

def test_text_to_duration_integer_with_minutes():
    actual = text_to_duration("10:20") 
    expected = 10.333333
    assert( (abs(actual) - expected) < 1e-5)


