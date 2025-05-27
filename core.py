
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


def flip_names_on_comma_between(name: str) -> str:
    parts = name.split(' ')
    if len(parts) < 2:
        return name
    for i in range(len(parts) - 1):
        if parts[i].endswith(',') and parts[i + 1].isalpha():
            parts[i], parts[i + 1] = parts[i + 1], parts[i].rstrip(',')
            return ' '.join(parts)
    return name.replace(',', '').strip()
    