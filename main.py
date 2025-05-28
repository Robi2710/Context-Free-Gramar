import random

#task 1 - CFG
productions = {
    'S' : ['aSb', '']
}

terminals = {'a', 'b'}
non_terminals = {'S'}
start_symbol = 'S'

#task 2 - Generate Strings
def generate_string(symbol='S', max_length = 10):
    if len(symbol) > max_length:
        return None
    if symbol == '':
        return ''

    rule = random.choice(productions[symbol])
    result = ''
    for char in rule:
        if char in non_terminals:
            sub = generate_string(char, max_length - len(result))
            if sub is None:
                return None
            result += sub
        else:
            result += char
    return result if len(result) < max_length else None

def gen_strings(n=10, max_attempts=1000):
    attempts = 0
    strings = set()
    while len(strings) < n and attempts < max_attempts:
        s = generate_string()
        if s is not None:
            strings.add(s)
        attempts += 1
    return list(strings)

#task3 derivation
def leftmost_derivation(string, current = 'S'):
    derivation = [current]

    def derive(current, target, steps):
        if current == target:
            return steps

        term_count = sum(1 for c in current if c not in non_terminals)
        if term_count > len(target):
            return None

        for i, char in enumerate(current):
            if char in non_terminals:
                for production in productions[char]:
                    new_current = current[:i] + production + current[i+1:]
                    new_steps = steps + [new_current]
                    result = derive(new_current, target, new_steps)
                    if result:
                        return result

        return None

    return derive(current, string, derivation)

#task 4
def membership(s, current = 'S'):
    def match(current, target):
        if current == target:
            return True

        term_count = sum(1 for char in current if char not in non_terminals)

        if term_count > len(target):
            return False
        for i, char in enumerate(current):
            if char in non_terminals:
                for production in productions[char]:
                    new_current = current[:i] + production + current[i+1:]
                    if match(new_current, target):
                        return True
                return False
        return False
    return match(current, s)

# task 5

productions_cs = [
    ("S", "aSBC"),
    ("S", "abc"),
    ("CB", "BC"),
    ("aB", "ab"),
    ("bB", "bb"),
    ("bC", "bc"),
    ("cC", "cc"),
]
def membership_abc(s: str) -> bool:
    if not s or s[0] != 'a':
        return False

    n = 0
    while n < len(s) and s[n] == 'a':
        n += 1

    if s[n:2*n] != 'b' * n:
        return False

    if s[2*n:3*n] != 'c' * n:
        return False

    return 3*n == len(s)


# L = {aⁿbⁿcⁿ | n ≥ 1} nu este limbaj context-free
# deoarece necesită compararea a trei cantități egale, ceea ce nu este posibil
# cu o gramatică de tip context-free. Recunoașterea se face aici prin simulare.

if __name__ == '__main__':
    print("--Task 1--")
    print(f"Start symbol: {start_symbol}")
    print("Productions:")
    for lhs, rhss in productions.items():
        for rhs in rhss:
            rhs_display = 'ε' if rhs == '' else rhs
            print(f"  {lhs} → {rhs_display}")

    print("\n--Task 2--")
    #random.seed(42)
    generated = gen_strings(10)
    print("Generated strings:")
    for idx, s in enumerate(generated, 1):
        print(f"  {idx:2d}. {repr(s)}")

    print("\n--Task 3--")
    test_str = 'aabb'
    deriv = leftmost_derivation(test_str)
    if deriv:
        print(f"Leftmost derivation for '{test_str}':")
        for step in deriv:
            print("  ⇒", step)
    else:
        print(f"No derivation found for '{test_str}'")

    print("\n--Task 4--")
    test_cases = ['aabb', 'abab', 'aaabbb', '', 'ab']
    for case in test_cases:
        print(f"Is '{case}' in language? -> {membership(case)}")

    print("\n--Task 5--")
    tests5 = ['abc', 'aabbcc', 'aaabbbccc', 'aabccc', 'abcc', '']
    for w in tests5:
        print(f"Is '{w}' in {{aⁿbⁿcⁿ}}? -> {membership_abc(w)}")