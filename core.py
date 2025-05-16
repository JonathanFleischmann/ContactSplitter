
def get_longest_of_values_contained(string: str, values: list[str]) -> str | None:
    longest_found_value: str | None = None

    for value in values:
        if string.startswith(value):
            if longest_found_value is None or len(value) > len(longest_found_value):
                longest_found_value = value

    return longest_found_value

def pop_first_word(text: str) -> tuple[str, str]:
    parts = text.strip().split(' ', 1)
    if len(parts) == 1:
        return parts[0], ''
    return parts[0], parts[1]