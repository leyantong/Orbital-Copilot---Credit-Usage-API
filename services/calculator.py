import re

# Define vowels for special credit calculation rules
VOWELS = "aeiouAEIOU"

def sanitize_text(text):
    """Removes non-alphanumeric characters and converts text to lowercase."""
    return re.sub(r'[^a-zA-Z0-9]', '', text).lower()

def calculate_credits(message, report_lookup):
    """Compute the credit consumption for a given message."""
    
    # If the message has a report_id, return the predefined credit cost
    report_id = message.get("report_id")
    if report_id and report_id in report_lookup:
        return report_lookup[report_id]['credit_cost'], report_lookup[report_id]['name']
    
    # Calculate credit cost based on text content
    text = message.get('text', '')
    words = re.findall(r"[a-zA-Z'-]+", text)
    base_cost = 1  # Minimum cost
    char_count = len(text)
    word_count = len(words)

    total_cost = base_cost + (0.05 * char_count)

    # Word length adjustments
    for word in words:
        length = len(word)
        total_cost += 0.1 if length <= 3 else 0.2 if length <= 7 else 0.3

    # Vowel rule: If every 3rd character is a vowel, add 0.3 credits
    total_cost += sum(0.3 for i, c in enumerate(text, 1) if i % 3 == 0 and c in VOWELS)

    # Extra charge for long messages
    if char_count > 100:
        total_cost += 5

    # Unique words discount
    if len(set(words)) == word_count and word_count > 0:
        total_cost -= 2

    # Ensure at least 1 credit is charged
    total_cost = max(1, total_cost)

    # Normalize text and check if it is a palindrome (but ignore empty strings)
    normalized_text = sanitize_text(text)
    if normalized_text and normalized_text == normalized_text[::-1]:
        total_cost = round(total_cost) * 2  # Ensure integer before doubling

    return round(total_cost, 2), None  # Return `None` when no report name is present
