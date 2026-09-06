"""
Practice: Box operations

You are given a list of operations. Each operation is a tuple (op, a, b):
  - (0, a, b): create a new box of dimensions a x b
  - (1, a, b): query - does a box of dimensions a x b fit inside EVERY
               box created so far? (must fit in all of them, not just one)

A box (a, b) fits inside a box (W, H) if it fits without rotation
(a <= W and b <= H) OR with a 90-degree rotation (a <= H and b <= W).

Return a list of booleans, one per query (op == 1), in the order they appear.

Edge case: if a query happens before any box has been created, treat it as
not fitting (False) - there is nothing to fit "in all of" boxes when there
are none. (Flip this if your actual OA defines it as vacuously True.)

Example:
    ops = [
        (0, 5, 10),
        (0, 3, 3),
        (1, 2, 2),   # fits in both 5x10 (yes) and 3x3 (yes) -> True
        (0, 1, 1),
        (1, 2, 2),   # now also must fit in 1x1 -> False
    ]
    solve(ops) -> [True, False]
"""

from typing import List, Tuple


def fits(a: int, b: int, w: int, h: int) -> bool:
    return (a <= w and b <= h) or (a <= h and b <= w)


def solve(ops: List[Tuple[int, int, int]]) -> List[bool]:
    boxes: List[Tuple[int, int]] = []
    results: List[bool] = []

    for op, a, b in ops:
        if op == 0:
            boxes.append((a, b))
        elif op == 1:
            if not boxes:
                results.append(False)
                continue
            ok = all(fits(a, b, w, h) for w, h in boxes)
            results.append(ok)

    return results


if __name__ == "__main__":
    tests = [
        (
            [(0, 5, 10), (0, 3, 3), (1, 2, 2), (0, 1, 1), (1, 2, 2)],
            [True, False],
        ),
        (
            [(1, 1, 1)],
            [False],
        ),
        (
            [(0, 4, 4), (1, 4, 4), (1, 5, 4), (1, 4, 5)],
            [True, False, False],
        ),
        (
            # rotation check: 3x5 should fit into a 5x3 box
            [(0, 5, 3), (1, 3, 5)],
            [True],
        ),
    ]

    for i, (ops, expected) in enumerate(tests):
        got = solve(ops)
        status = "PASS" if got == expected else "FAIL"
        print(f"test {i}: {status}  got={got} expected={expected}")
