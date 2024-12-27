def number_to_words(n):
    """Convert a number to its word form, including 'oh' for zero in certain cases."""
    if n == 0:
        return "zero"

    ones = [
        "", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
    ]
    teens = [
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen"
    ]
    tens = [
        "", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"
    ]

    def convert_chunk(num, use_oh=False):
        """Convert a chunk of up to 3 digits, optionally using 'oh' for zero."""
        words = []
        if num >= 100:
            words.append(ones[num // 100])
            words.append("hundred")
            num %= 100
        if num >= 10 and num < 20:
            words.append(teens[num - 10])
        else:
            if num >= 20:
                words.append(tens[num // 10])
                num %= 10
            if num > 0:
                words.append(ones[num])
            elif use_oh and num == 0:
                words.append("oh")
        return " ".join(words)

    result = []
    num_str = str(n)
    length = len(num_str)

    for i, digit in enumerate(num_str):
        # Add 'oh' if zero is in the middle of the number
        if digit == "0" and i > 0:
            result.append("oh")
        elif length - i > 2:  # Handle digits before the last two
            if digit != "0":
                result.append(ones[int(digit)])
                if length - i == 4:
                    result.append("thousand")
                elif length - i == 3:
                    result.append("hundred")
        else:
            # Handle the last two digits as a chunk
            result.append(convert_chunk(int(num_str[i:]), use_oh=True))
            break

    return " ".join(result).strip()


def number_string_to_number(s):
    """Convert a number word string to a number."""
    number_word_to_number = {
        "zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6,
        "seven": 7, "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12,
        "thirteen": 13, "fourteen": 14, "fifteen": 15, "sixteen": 16,
        "seventeen": 17, "eighteen": 18, "nineteen": 19, "twenty": 20,
        "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60, "seventy": 70,
        "eighty": 80, "ninety": 90, "hundred": 100, "thousand": 1000
    }

    words = s.lower().replace(" and ", " ").split()
    result = 0
    chunk = 0

    for word in words:
        if word == "hundred":
            chunk *= 100
        elif word == "thousand":
            chunk *= 1000
            result += chunk
            chunk = 0
        elif word in number_word_to_number:
            chunk += number_word_to_number[word]
        else:
            raise ValueError(f"Unknown word: {word}")
    result += chunk
    return result

