# Takeout Notes — `edit_distance.py`

- **Purpose**: Computes the Levenshtein (edit) distance between two strings — minimum number of insertions, deletions, or substitutions (cost 1).

**Python Grammar (detailed)**

- **Function definition & type hints**: `def edit_distance(source: str, target: str) -> int:` defines a function named `edit_distance` that takes two `str` arguments and returns an `int`. Type hints are optional metadata that help editors and linters; they do not change runtime behavior.

- **Docstrings & doctests**: The triple-quoted string directly under the function is a docstring. It documents purpose, parameters, and includes example usage lines starting with `>>>` (doctests). Run with `python -m doctest -v strings/edit_distance.py` to validate examples.

- **Main guard**: `if __name__ == "__main__":` runs code only when the file is executed as a script, not when imported as a module. Useful for simple tests or demo code.

- **Indexing & slicing**:
  - `source[-1]` accesses the last character (negative indices count from the end).
  - `source[:-1]` returns all characters except the last one (slice up to but not including index -1).
  - Slices create new strings; they do not modify the original string (strings are immutable).

**Algorithm Notes (detailed)**

- **What the algorithm computes**: the Levenshtein (edit) distance is the minimum number of single-character insertions, deletions, or substitutions required to transform `source` into `target`. Each operation here costs `1`.

- **Recurrence relation**: let `ED(i, j)` be the edit distance between the prefixes `source[:i]` and `target[:j]` (i.e., first `i` and `j` characters).
  - Base cases:
    - `ED(0, j) = j` (transform empty source into `j` characters by `j` insertions).
    - `ED(i, 0) = i` (transform `i` characters into empty target by `i` deletions).
  - Recursive step (for i, j > 0):
    - `cost = 0 if source[i-1] == target[j-1] else 1`
    - `ED(i, j) = min(ED(i-1, j-1) + cost, ED(i, j-1) + 1, ED(i-1, j) + 1)`
      - `ED(i-1, j-1) + cost` → substitute or match last character
      - `ED(i, j-1) + 1` → insert into `source` (or delete from `target`)
      - `ED(i-1, j) + 1` → delete from `source`

- **How the recursive code maps to the relation**: the implementation uses full strings and slices instead of indices:
  - `edit_distance(source[:-1], target[:-1]) + delta` corresponds to `ED(i-1, j-1) + cost`.
  - `edit_distance(source, target[:-1]) + 1` corresponds to `ED(i, j-1) + 1` (insert).
  - `edit_distance(source[:-1], target) + 1` corresponds to `ED(i-1, j) + 1` (delete).

- **Trace example (small)**: compute `edit_distance('ab', 'ac')`:
  1. Compare last chars: `'b'` vs `'c'` → `cost = 1`.
  2. Evaluate three options:
     - substitute: `ED('a','a') + 1` → `0 + 1 = 1`
     - insert: `ED('ab','a') + 1` → `1 + 1 = 2`
     - delete: `ED('a','ac') + 1` → `1 + 1 = 2`
  3. Minimum is `1` → one substitution.

- **Correctness (intuition)**: any optimal edit sequence that transforms the full strings must perform one of the three last operations affecting the final character(s): match/substitute, insert, or delete. Considering all three and taking the minimum recursively yields the optimal value.

- **Complexity**:
  - Naive recursion: exponential time due to overlapping subproblems (many repeated calls), roughly O(3^(max(n,m))).
  - With memoization (top-down DP): O(n*m) time and O(n*m) space, where `n = len(source)`, `m = len(target)`.
  - Iterative DP (bottom-up): also O(n*m) time and O(n*m) space; with optimized row-wise implementation you can reduce space to O(min(n,m)).

- **Memoization (practical fix)**: use `functools.lru_cache` to cache results of calls. Example:

```py
from functools import lru_cache

@lru_cache(maxsize=None)
def edit_distance_cached(s: str, t: str) -> int:
    if not s: return len(t)
    if not t: return len(s)
    delta = int(s[-1] != t[-1])
    return min(
        edit_distance_cached(s[:-1], t[:-1]) + delta,
        edit_distance_cached(s, t[:-1]) + 1,
        edit_distance_cached(s[:-1], t) + 1,
    )
```

- **Iterative DP (bottom-up)**: build a (n+1) x (m+1) matrix `dp` where `dp[i][j] = ED(i, j)`; fill base rows/columns then compute row-by-row using the recurrence. Pseudocode:

```text
initialize dp matrix of size (n+1) x (m+1)
for i in 0..n: dp[i][0] = i
for j in 0..m: dp[0][j] = j
for i in 1..n:
  for j in 1..m:
    cost = 0 if source[i-1] == target[j-1] else 1
    dp[i][j] = min(dp[i-1][j-1] + cost, dp[i][j-1] + 1, dp[i-1][j] + 1)
return dp[n][m]
```

- **Testing & edge cases**:
  - Empty strings, identical strings, case sensitivity (`'a'` vs `'A'`).
  - Non-string inputs: consider input validation in production code.

- **Practical tips**:
  - For long strings, prefer the iterative DP or memoized version.
  - For space optimization, compute only two rows at a time (previous and current), giving O(min(n,m)) space.
  - Use doctests and small traced examples to build intuition.