#!/usr/bin/env python3
"""Roast Your Fridge — one-line roast entry for make.fun.

The program scores ten fresh one-line roasts of my own fridge against
the judge's brief, in the brief's own order, and writes the winner to
/output/entry.txt.

Judge criteria, most important first (weights 5/4/3/2/1):
  1. Roasts a fridge or a phone in a single line.
  2. Lands a real laugh on a specific, recognisable detail of the
     appliance rather than a generic insult.
  3. Turns on a twist, a surprise or a double meaning that pays off
     in the last few words.
  4. Reads cleanly aloud as one line, with no setup that needs a
     second sentence.
  5. Feels fresh rather than a joke everyone who owns a fridge has
     already worn out.
"""

import os

# Each candidate: (text, scores per criterion, 0-5, in the order above).
CANDIDATES = [
    (
        "My fridge hums all night like it is composing a symphony, "
        "but the only song it knows is the sound of my leftovers "
        "slowly dying.",
        [5, 4, 4, 5, 3],
    ),
    (
        "My fridge has a crisper drawer where vegetables go to "
        "retire, and every carrot in there has filed for pension.",
        [5, 5, 5, 5, 4],
    ),
    (
        "My fridge's ice maker sounds like a robot choking on dice, "
        "and it only ever makes ice when nobody needs it.",
        [5, 5, 4, 4, 4],
    ),
    (
        "My fridge light goes out when the door closes, which is the "
        "only thing in my kitchen that respects my privacy.",
        [5, 4, 4, 5, 3],
    ),
    (
        "My fridge is the only roommate who never pays rent, eats all "
        "my food, and still judges me every time I open the door "
        "at 2 a.m.",
        [5, 4, 4, 5, 3],
    ),
    (
        "My fridge has a water dispenser that dribbles like a nervous "
        "witness, and a filter light that has been red since 2019.",
        [5, 5, 4, 4, 4],
    ),
    (
        "My fridge's door seal is so weak that the cold air escapes "
        "faster than my motivation on a Monday morning.",
        [5, 4, 3, 5, 3],
    ),
    (
        "My fridge keeps my food cold and my hopes colder, and the "
        "only thing it ever preserves is my disappointment.",
        [5, 3, 4, 5, 2],
    ),
    (
        "My fridge has a smart screen nobody has touched since the day "
        "it was installed, which makes it the smartest thing in the "
        "house.",
        [5, 5, 5, 5, 4],
    ),
    (
        "My fridge is just a cold white box that hums, leaks, and "
        "holds a grudge against every yogurt past its date.",
        [5, 3, 3, 5, 2],
    ),
]

WEIGHTS = [5, 4, 3, 2, 1]


def score(candidate):
    """Weighted total out of 75 for one candidate."""
    _text, scores = candidate
    return sum(w * s for w, s in zip(WEIGHTS, scores))


def ranked():
    """Candidates sorted by score, then by shorter length."""
    scored = [(score(c), len(c[0]), c[0]) for c in CANDIDATES]
    scored.sort(key=lambda item: (-item[0], item[1]))
    return scored


def show_ranking():
    """Print every candidate with its score, best first."""
    for total, length, text in ranked():
        print(f"{total:3d}  ({length} chars)  {text}")


def main():
    """Pick the best roast, validate the gate, write the entry."""
    winner_total, winner_len, winner = ranked()[0]
    assert 1 <= len(winner) <= 200, "entry must be 1-200 characters"
    assert winner.strip(), "entry must not be only whitespace"
    assert "\n" not in winner, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(winner)
    print(f"winner ({winner_total}/75, {winner_len} chars): {winner}")


if __name__ == "__main__":
    main()
