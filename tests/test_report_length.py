from lib.report_length import report_length

def test_report_length():
    assert report_length("") == "This string was 0 characters long."
    assert report_length("A") == "This string was 1 characters long."  # Updated expected output
    assert report_length("Hello, World!") == "This string was 13 characters long."
    assert report_length("!@#$%^&*()") == "This string was 10 characters long."
    assert report_length("   ") == "This string was 3 characters long."

    print("All test cases pass.")
