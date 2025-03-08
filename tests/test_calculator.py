import pytest
from services.calculator import calculate_credits

def test_calculate_credits():
    """Test credit calculation logic for various message types."""

    # Test a normal text message
    message = {"text": "Hello world!"}
    credits, _ = calculate_credits(message, {})
    assert credits >= 1  # Basic messages should have at least 1 credit

    # Test a message that generates a report
    report_lookup = {1234: {"name": "Sample Report", "credit_cost": 50}}
    message_with_report = {"report_id": 1234}
    credits, name = calculate_credits(message_with_report, report_lookup)
    assert credits == 50  # The credit cost should match the report's predefined value
    assert name == "Sample Report"

    # Test a palindrome message (should double the credits)
    palindrome_message = {"text": "Madam, in Eden, I'm Adam"}
    credits, _ = calculate_credits(palindrome_message, {})
    assert credits % 2 == 0  # The credit value should be an even number

    # Test a message with an empty string (should return minimum credit)
    empty_message = {"text": ""}
    credits, _ = calculate_credits(empty_message, {})
    assert credits == 1  # Should return the minimum 1 credit

    # Test a long message (should trigger additional credits)
    long_text = "a" * 101
    long_message = {"text": long_text}
    credits, _ = calculate_credits(long_message, {})
    assert credits > 5  # Should apply the long text penalty

