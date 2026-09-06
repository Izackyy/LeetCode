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
fitting (True) - vacuously true, since "fits in every created box" holds
trivially when there are no boxes.

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


def solve(ops: List[Tuple[int, int, int]]) -> List[bool]:
    boxes = []
    res = []

    for op, a, b in ops:
        if op == 0:
            boxes.append((a, b))
        elif op == 1:
            if not boxes:
                res.append(True)
                continue
            for box in boxes:
                if not (a <= box[0] and b <= box[1]) and not (a <= box[1] and b <= box[0]):
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
            # rotation check: 3x5 should fit into a 5x3 box
            [(0, 5, 3), (1, 3, 5)],
            [True],
        ),
    ]

    for i, (ops, expected) in enumerate(tests):
        got = solve(ops)
        status = "PASS" if got == expected else "FAIL"
        print(f"test {i}: {status}  got={got} expected={expected}")
