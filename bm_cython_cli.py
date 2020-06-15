import argparse
from typing import List, Tuple

from bm_cython import boyer_moore

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
