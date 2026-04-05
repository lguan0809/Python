Name: generate_takeout_notes

# Skill: generate_takeout_notes

Description
- Create beginner-focused "takeout" notes for a given Python file. The notes must explain Python grammar used in the file, give a clear, step-by-step explanation of any algorithmic logic (recurrence/DP/complexity), provide small runnable code examples (memoized and iterative where relevant), and include commands to run and test the code. Tone: beginner-friendly, concise, and actionable.

Inputs
- `file_path` (required): workspace-relative path to the Python file to analyze (e.g., `strings/edit_distance.py`).
- `target_folder` (optional): where to save notes; default: same directory as the source under `.../notes/`.
- `beginner` (optional, default true): when true, use extra explanation and simple examples.

Behavior / Steps the agent must follow
1. Read the entire source file. If the file is not valid Python, return an error message.
2. Extract high-level purpose: from module docstring, function/class docstrings, or file-level comments.
2.1. Read the repository contribution guidelines located at `CONTRIBUTING.md` (prefer the `notes` branch when present). Parse the document for any coding style or contribution rules that apply to Python files (for example: naming conventions, testing requirements, formatting, licensing notices). If the source file violates any of these rules, record each violation in a dedicated **Contributing Violations** section in the notes (include rule text and a short explanation of why the file violates it).
3. Identify functions/classes and the primary algorithmic entrypoint (heuristic: largest function, or function called in `if __name__ == "__main__"`).
4. Produce a notes document with these sections:
   - Header with file name and short purpose.
   - **Python Grammar (detailed)**: provide a thorough, beginner-friendly breakdown of all Python language features and idioms used in the file. For each feature that appears in the source, include:
      - A short explanation in plain language aimed at beginners.
      - A 1–3 line runnable code snippet showing the feature in general.
      - A note explaining how the feature is used in the source file and why it matters for understanding the code.

      Required grammar topics to check for and document when present (non-exhaustive):
      - **Function definitions & signatures**: `def`, positional/keyword args, default values, `*args`, `**kwargs`.
      - **Type hints / annotations**: parameter and return annotations (what they mean and compatibility notes).
      - **Docstrings & doctests**: module/function docstrings and `>>>` examples — how to run doctests.
      - **Imports & modules**: `import`, `from ... import ...`, and when external packages require installation.
      - **Basic data types & literals**: `str`, `int`, `float`, `bool`, `None`, lists, tuples, dicts, sets.
      - **Indexing & slicing**: e.g., `s[-1]`, `s[:-1]` and how slices produce new objects.
      - **Control flow**: `if` / `elif` / `else`, `for` / `while`, `break` / `continue`.
      - **Comprehensions**: list/dict/set comprehensions and generator expressions (if used).
      - **Built-ins & common functions**: `len()`, `min()`, `int()`, `range()`, etc.; show return types and examples.
      - **Strings & formatting**: string methods, f-strings, `.format()`, and case sensitivity.
      - **Mutability vs immutability**: which types are mutable and implications (e.g., slicing strings returns new strings).
      - **Recursion**: base cases, stack limits, and when to prefer iterative or memoized approaches.
      - **Error handling**: `try` / `except` and raising exceptions; input validation patterns.
      - **Context managers & file I/O**: `with open(...) as f:` if present.
      - **Generators & iterators**: `yield`, iterator protocols (if present).
      - **Decorators & higher-order functions**: `@decorator`, `functools` usage (if present).
      - **Standard library utilities**: `functools.lru_cache`, `typing`, `collections`, etc. — mention introduced versions where relevant.

      Format requirement: show a short code example for each documented feature and a clear one-sentence mapping to the code under analysis. When the file is short, include the snippet inline; for longer examples use a separate fenced code block. Always include a one-line "why this matters" for beginners.

      Compatibility: note the minimum recommended Python version required for any feature used (e.g., type hint forms, f-strings require 3.6+, `functools.lru_cache` exists since 3.2). If the file uses modern features (3.8+), state that explicitly.
   - **Algorithm Notes (detailed)**: state the algorithm, formal recurrence or pseudocode, trace a small example step-by-step, prove/justify correctness intuitively, list complexity (time/space) and discuss optimizations (memoization, iterative DP, space-optimized DP), and provide concrete code examples (a memoized version and an iterative version when applicable).
   - **Improvements / Exercises**: practical next steps and small exercises to practice.
   - **How to Run & Test**: commands to execute the file and run doctests or example snippets.
   - **Files Created**: path where the notes will be saved.
5. Save the notes as `<source_basename>_takeout.md` under `target_folder` (create folder if needed). Use concise Markdown with headings and bullet lists.
   - If any contributing-guideline violations were detected, append a **Contributing Violations** section at the end of the notes describing each violation and suggesting a fix.
6. Optionally (prompt the user), create a `notes` git branch, commit and push the note file.

Output format
- Save as a Markdown file with the sections above. Use simple examples and beginner-friendly language.
- When returning a short response to the user, include the path to the generated notes document using a workspace-relative link.

Examples
- Input `strings/edit_distance.py` → create `strings/notes/edit_distance_takeout.md` containing purpose, detailed grammar section, detailed algorithm section (recurrence, DP, memoized and iterative examples), run commands, and exercises.

Constraints & Safety
- Do not modify the original source file unless the user explicitly asks.
- If the file imports external packages not installed, note that the user may need to install dependencies.

Developer notes
- Prefer small, clear code examples. Keep explanations short but thorough for beginners.
- When analyzing algorithms, include both top-down (memoized) and bottom-up (iterative) patterns if relevant.
- Keep default Python version compatibility to 3.6+ unless file uses newer features; mention minimum recommended Python version in the notes.

End of SKILL.md
