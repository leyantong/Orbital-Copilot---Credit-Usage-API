import re

# Define vowels for special credit calculation rules
VOWELS = "aeiouAEIOU"

def sanitize_text(text):
    """Removes non-alphanumeric characters and converts text to lowercase."""
    return re.sub(r'[^a-zA-Z0-9]', '', text).lower()

def calculate_credits(message, report_lookup):
    """Compute the credit consumption for a given message."""
    report_id = message.get("report_id")
    if report_id and report_id in report_lookup:
        return report_lookup[report_id]['credit_cost'], report_lookup[report_id]['name']
    
    # Calculate credit cost based on text content
    text = message['text']
    words = re.findall(r"[a-zA-Z'-]+", text)
    base_cost = 1
    char_count = len(text)
    word_count = len(words)

    total_cost = base_cost + (0.05 * char_count)

    for word in words:
        length = len(word)
        total_cost += 0.1 if length <= 3 else 0.2 if length <= 7 else 0.3

    total_cost += sum(0.3 for i, c in enumerate(text, 1) if i % 3 == 0 and c in "aeiouAEIOU")

    if char_count > 100:
        total_cost += 5

    if len(set(words)) == word_count and word_count > 0:
        total_cost -= 2

    total_cost = max(1, total_cost)

    normalized_text = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    if normalized_text == normalized_text[::-1]:
        total_cost *= 2

    return round(total_cost, 2), None  # Return `None` when there is no report name
