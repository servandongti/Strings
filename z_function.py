
def z_function(input_str: str) -> list[int]:
    """
    >>> z_function("abracadabra")
    [0, 0, 0, 1, 0, 1, 0, 4, 0, 0, 1]
    >>> z_function("aaaa")
    [0, 3, 2, 1]
    >>> z_function("zxxzxxz")
    [0, 0, 0, 4, 0, 0, 1]
    """
    z_result = [0 for i in range(len(input_str))]

    left_pointer, right_pointer = 0, 0

    for i in range(1, len(input_str)):
        if i <= right_pointer:
            min_edge = min(right_pointer - i + 1, z_result[i - left_pointer])
            z_result[i] = min_edge

        while go_next(i, z_result, input_str):
            z_result[i] += 1

        if i + z_result[i] - 1 > right_pointer:
            left_pointer, right_pointer = i, i + z_result[i] - 1

    return z_result


def go_next(i: int, z_result: list[int], s: str) -> bool:
    """
    Check if we have to move forward to the next characters or not
    """
    return i + z_result[i] < len(s) and s[z_result[i]] == s[i + z_result[i]]


def find_pattern(pattern: str, input_str: str) -> int:
    """
    Example of using z-function for pattern occurrence
    Given function returns the number of times 'pattern'
    appears in 'input_str' as a substring

    >>> find_pattern("abr", "abracadabra")
    2
    >>> find_pattern("a", "aaaa")
    4
    >>> find_pattern("xz", "zxxzxxz")
    2
    """
    answer = 0
    z_result = z_function(pattern + input_str)

    for val in z_result:
        if val >= len(pattern):
            answer += 1

    return answer


if __name__ == "__main__":
    import doctest

    doctest.testmod()
