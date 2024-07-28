import sys
# Description: Test the print_value function

sys.path.append("src")

def test_print_value_ten(capsys):
    from print_script import print_value
    print_value(10)
    captured = capsys.readouterr()
    assert captured.out == "Value: 10\n"
    assert captured.err == ""

def test_print_value_false(capsys):
    from print_script import print_value
    print_value(False)
    captured = capsys.readouterr()
    assert captured.out == "Value: False\n"
    assert captured.err == ""
