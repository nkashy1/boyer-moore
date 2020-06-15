import argparse
from collections import defaultdict
from typing import Dict, List, Optional, Tuple

def delta1_table(pattern: str) -> Dict[str, int]:
    delta1 = defaultdict(lambda: len(pattern))
    for i, c in enumerate(pattern):
        delta1[c] = len(pattern) - 1 - i
    return delta1

def delta2_table(pattern: str) -> Dict[int, int]:
    delta2 = defaultdict(lambda: -1)
    prefix_shift = len(pattern)-1
    for i in range(len(pattern)-1, -1, -1):
        if pattern[:len(pattern)-1-i] == pattern[i+1:len(pattern)]:
            prefix_shift = i + 1
        delta2[i] = prefix_shift + len(pattern) - 1 - i

    for i in range(len(pattern)-1):
        common_suffix_length = 0
        while (
            pattern[i-common_suffix_length] == pattern[len(pattern)-1-common_suffix_length]
            and common_suffix_length < i
        ):
            common_suffix_length += 1
        if pattern[i-common_suffix_length] != pattern[len(pattern)-1-common_suffix_length]:
            delta2[len(pattern)-1-common_suffix_length] = (
                len(pattern) - 1 - i - common_suffix_length
            )

    return delta2

def boyer_moore(pattern: str, full_string: str) -> Optional[int]:
    delta1 = delta1_table(pattern)
    delta2 = delta2_table(pattern)

    full_string_index = len(pattern) - 1
    while full_string_index < len(full_string):
        pattern_index = len(pattern) - 1
        while pattern_index >= 0 and full_string[full_string_index] == pattern[pattern_index]:
            full_string_index -= 1
            pattern_index -= 1
        if pattern_index <= 0:
            return full_string_index + 1

        shift = max(delta1[full_string[full_string_index]], delta2[pattern_index])
        full_string_index += shift

    return None

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Boyer-Moore string search')
    parser.add_argument('pattern', help='Pattern to search for')
    parser.add_argument('files', nargs='+', help='Files in which to search for pattern')
    args = parser.parse_args()
    matches: List[Tuple[str, int]] = []
    for input_file in args.files:
        with open(input_file) as ifp:
            result = boyer_moore(args.pattern, ifp.read())
        if result is not None:
            matches.append((input_file, result))

    print('Matches:')
    for filename, index in matches:
        print(f'\tFile: {filename}, index: {index}')
