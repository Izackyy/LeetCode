"""
Optimal solution for box-fit-queries: O(1) per operation, O(n) overall.

Key insight: (a, b) fits in (W, H) with optional 90-degree rotation iff
min(a, b) <= min(W, H) AND max(a, b) <= max(W, H). So normalizing every
box (and every query) to (small, large) turns "fits in every box created
so far" into two running minimums: the smallest "small" side and the
smallest "large" side seen across all boxes. A query just compares
against those two numbers - no per-box loop needed.

See box-fit-queries.py for the brute-force O(queries * boxes) version
and the full problem statement in README.md.
"""

import random
from typing import List, Tuple


def solve_optimal(ops: List[Tuple[int, int, int]]) -> List[bool]:
    min_small = float('inf')
    min_large = float('inf')
    has_box = False
    res = []

    for op, a, b in ops:
        if op == 0:
            s, l = (a, b) if a <= b else (b, a)
            min_small = min(min_small, s)
            min_large = min(min_large, l)
            has_box = True
        elif op == 1:
            if not has_box:
                res.append(True)
                continue
            qs, ql = (a, b) if a <= b else (b, a)
            res.append(qs <= min_small and ql <= min_large)

    return res


def solve_brute(ops: List[Tuple[int, int, int]]) -> List[bool]:
    boxes = []
    res = []
    for op, a, b in ops:
        if op == 0:
            boxes.append((a, b))
        elif op == 1:
            if not boxes:
                res.append(True)
                continue
            for w, h in boxes:
                if not (a <= w and b <= h) and not (a <= h and b <= w):
                    res.append(False)
                    break
            else:
                res.append(True)
    return res


if __name__ == "__main__":
    tests = [
        (
            [(0, 5, 10), (0, 3, 3), (1, 2, 2), (0, 1, 1), (1, 2, 2)],
            [True, False],
        ),
        (
            [(1, 1, 1)],
            [True],
        ),
        (
            [(0, 4, 4), (1, 4, 4), (1, 5, 4), (1, 4, 5)],
            [True, False, False],
        ),
        (
            [(0, 5, 3), (1, 3, 5)],
            [True],
        ),
    ]

    for i, (ops, expected) in enumerate(tests):
        got = solve_optimal(ops)
        status = "PASS" if got == expected else "FAIL"
        print(f"test {i}: {status}  got={got} expected={expected}")

    random.seed(0)
    mismatches = 0
    for _ in range(2000):
        n = random.randint(1, 15)
        ops = [(random.randint(0, 1), random.randint(1, 10), random.randint(1, 10)) for _ in range(n)]
        if solve_brute(ops) != solve_optimal(ops):
            mismatches += 1
            print("MISMATCH", ops)
    print("random trials:", "all match" if mismatches == 0 else f"{mismatches} mismatches")
