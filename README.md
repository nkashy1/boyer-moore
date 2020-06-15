# boyer-moore

## Boyer-Moore example

```bash
$ python bm_pure.py "AT THAT" test_1.txt
Matches:
	File: test_1.txt, index: 25
```

## Comparing pure Python implementation to Cython build

Just did this comparison to get familiar with Cython.

Pure:
```bash
$ time for i in {1..1000}; do python bm_pure.py "AT THAT" test_1.txt>/dev/null; done

real	0m33.114s
user	0m26.745s
sys	0m6.417s
```

Cython:

First, build the C extension using:
```bash
$ python cython_setup.py build_ext --inplace
```

Then,
```bash
$ time for i in {1..1000}; do python bm_cython_cli.py "AT THAT" test_1.txt >/dev/null; done

real	0m32.663s
user	0m26.276s
sys	0m6.432s
```
