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

- **Conditional statements**:
  - `if`, `elif`, `else` control flow. Base cases are handled with `if len(source) == 0:` and `elif len(target) == 0:`.

- **Built-in functions & conversions**:
  - `len(x)` returns length of sequence `x`.
  - `min(a, b, c)` returns the smallest of its arguments.
  - `int(True)` -> `1`, `int(False)` -> `0`; in the code, `int(source[-1] != target[-1])` converts a boolean equality check into 0/1 cost.

- **Comments**: Lines starting with `#` are ignored at runtime and explain code intent.

- **Variables & assignment**: `delta = ...` binds a value to the name `delta`. Python uses dynamic typing: a variable can hold values of any type.

- **Recursion**: The function calls itself with smaller inputs (`source[:-1]`, `target[:-1]`). Important points:
  - Every recursive function needs base cases to stop recursion, otherwise you'll get a `RecursionError`.
  - Recursion uses the call stack; deep recursion may hit recursion limits. Use iterative approaches or increase recursion limit only when necessary.

- **Standard library & modules**: To improve this function you might import `functools` and use `@functools.lru_cache(maxsize=None)` above the function to memoize results. Use `typing` for more complex type hints like `Optional[str]` or `Tuple[int, ...]`.

- **String immutability**: Strings cannot be changed in place. Slicing and concatenation produce new strings.

- **Error handling & edge cases**: This function assumes inputs are strings. In production code, you might add argument validation (e.g., `if not isinstance(source, str): raise TypeError(...)`).

- **Readability**: Use descriptive variable names and short functions. Docstrings and inline comments help others (and future you) understand intent.

**Algorithm Notes**
- Base cases: if one string is empty, cost = length of the other (all inserts/deletes).
- Recursive cases (three choices):
  - Substitute: `edit_distance(source[:-1], target[:-1]) + delta` (delta = 0 if last chars equal else 1).
  - Insert: `edit_distance(source, target[:-1]) + 1`.
  - Delete: `edit_distance(source[:-1], target) + 1`.
- Chooses `min(...)` of the three costs.
- Complexity: naive recursive version has exponential time due to overlapping subproblems. Use memoization or iterative DP for O(n*m) time.

**Improvements / Exercises**
- Add `@functools.lru_cache` to memoize recursive calls.
- Rewrite iteratively using a 2D matrix to learn dynamic programming.
- Modify operation costs (weighted edit distance) and test behavior.
- Run doctests: `python -m doctest -v strings/edit_distance.py`.

**Applications**
- Spell checking, fuzzy string matching, DNA sequence comparison, diff tools.

-- Short, focused notes to practice Python grammar and algorithmic thinking.