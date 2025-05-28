# Context-Free-Gramar
This program implements and tests a simple **Context-Free Grammar (CFG)** for generating strings, producing derivations, and testing membership in the language defined by the grammar.

## 📚 Grammar Definition

The CFG used is:
S → aSb | ε
This describes the language of **balanced strings of `a`s and `b`s**, such as: `ab`, `aabb`, `aaabbb`, etc.

## 🧩 Task Breakdown

### ✅ Task 1 - Define CFG
Defines the grammar:
- Start symbol: `S`
- Productions: `S → aSb | ε`
- Terminals: `a`, `b`
- Non-terminals: `S`

### ✅ Task 2 - Generate Strings
Randomly generates valid strings from the CFG using recursive expansion with a depth limit (`max_length`).
- Function: `generate_string()`
- Wrapper: `gen_strings(n=10)` generates `n` unique strings

### ✅ Task 3 - Leftmost Derivation
Builds the **leftmost derivation** for a given string from the CFG.
- Function: `leftmost_derivation(string)`
- Returns a list of steps in the derivation, or `None` if the string is not in the language.

### ✅ Task 4 - Membership Test
Checks if a string belongs to the language defined by the CFG using recursive expansion.
- Function: `membership(s)`
- Returns `True` or `False`

 ### ✅ Task 5 - Membership for {aⁿbⁿcⁿ}

Although the language L = { aⁿbⁿcⁿ | n ≥ 1 } is _not_ context-free, we simulate its recognition with a small set of productions and a direct check:

- Productions (simulating a context-sensitive process):
  ```text
  S  → aSBC
  S  → abc
  CB → BC
  aB → ab
  bB → bb
  bC → bc
  cC → cc
  ```
- Function: `membership_abc(s: str) -> bool`
  - Returns **True** if `s` has the form aⁿbⁿcⁿ, n ≥ 1.
  - Algorithm:
    1. Count the initial block of `a`'s → n.
    2. Verify the next n symbols are all `b`.
    3. Verify the next n symbols are all `c`.
    4. Ensure the string length is exactly 3·n.


## ▶️ How to Run

Make sure you have **Python 3.x** installed. Then, simply run the script in your terminal:

```bash
`python3 main.py`
```
## 🔍 Example Output
```bash
--Task 1--
S
{'S': ['aSb', '']}
    
--Task 2--
['aabb', 'ab', 'aaabbb', '', 'aaaabbbb', 'aabbb', 'abb', 'aabbbb', 'aaabb', 'aaaabb']

--Task 3--
Leftmost derivation for 'aabb':
  ⇒ S
  ⇒ aSb
  ⇒ aaSbb
  ⇒ aabb

--Task 4--
Is 'aabb' in language? -> True
Is 'abab' in language? -> False
Is 'aaabbb' in language? -> True
Is '' in language? -> True
Is 'ab' in language? -> True

--Task 5--
Is 'abc' in {aⁿbⁿcⁿ}? -> True
Is 'aabbcc' in {aⁿbⁿcⁿ}? -> True
Is 'aaabbbccc' in {aⁿbⁿcⁿ}? -> True
Is 'aabccc' in {aⁿbⁿcⁿ}? -> False
Is 'abcc' in {aⁿbⁿcⁿ}? -> False
Is '' in {aⁿbⁿcⁿ}? -> False
```
