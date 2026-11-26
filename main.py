#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office — make.fun entry.

Writes one original out-of-office auto-reply (a single sentence of at
most 200 characters) to /output/entry.txt (or $ENTRY_OUTPUT when set).
"""

import os
import sys

ENTRY = ("I'm on leave, and honestly I left my inbox the way you leave a "
         "gym membership — full of good intentions and hundreds of unread "
         "messages, so I'll reply when I'm back, a little lighter.")


def validate(text):
    """Check the entry is a single non-empty line of 1-200 characters
    forming exactly one sentence."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty")
    if "\n" in text.strip():
        raise ValueError("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(text))
    terminals = sum(text.count(c) for c in ".!?")
    if terminals != 1:
        raise ValueError(
            "entry must be exactly one sentence, found %d terminal marks"
            % terminals)
    if not text.rstrip().endswith((".", "!", "?")):
        raise ValueError("entry must end with terminal punctuation")
    return True


def check_ooo_signal(text):
    """The line must read as an out-of-office auto-reply: it says the
    sender is away on leave and promises a reply on return."""
    low = text.lower()
    if "on leave" not in low and "out of the office" not in low:
        raise ValueError("entry must say the sender is away on leave")
    if "reply" not in low or "back" not in low:
        raise ValueError("entry must promise a reply when the sender is back")
    return True


def check_honest_admission(text):
    """The line must admit one specific true thing about the inbox that
    a real employee would only say privately, flagged out loud."""
    low = text.lower()
    if "honestly" not in low:
        raise ValueError("entry must flag its confession with 'honestly'")
    if "unread messages" not in low and "unread email" not in low:
        raise ValueError("entry must name the neglected inbox concretely")
    return True


def check_polite_tone(text):
    """The line must stay warm and professional: no profanity, no
    insults, and a courteous commitment to reply."""
    low = text.lower()
    rude = ["damn", "hell", "sucks", "hate", "stupid", "idiot",
            "shut up", "don't care", "not my problem"]
    for word in rude:
        if word in low:
            raise ValueError("entry must stay polite, found %r" % word)
    if "i'll reply" not in low and "i will reply" not in low:
        raise ValueError("entry must carry a courteous reply commitment")
    return True


def check_quotable_turn(text):
    """The line must land with a quotable turn at the end, not trail
    off into a list of complaints."""
    low = text.lower()
    if "gym membership" not in low:
        raise ValueError("entry must carry its confessing comparison")
    if not text.rstrip().endswith("a little lighter."):
        raise ValueError("entry must end on its quotable turn")
    if low.count(",") > 4:
        raise ValueError("entry must not become a complaint list")
    return True


def check_no_filler(text):
    """The line must open without throat clearing and carry no padding
    words that burn the 200-character budget."""
    first = text.strip().split()[0].strip(",.!?").lower()
    if first in ("hi", "hello", "hey", "just", "so", "well", "dear"):
        raise ValueError("entry must not open with filler %r" % first)
    low = text.lower()
    for filler in ("very", "really", "actually", "basically"):
        if " %s " % filler in low:
            raise ValueError("entry must not pad itself with %r" % filler)
    return True


def run_checks(text):
    """Run every craft check; each raises ValueError on failure."""
    for check in (check_ooo_signal, check_honest_admission,
                  check_polite_tone, check_quotable_turn,
                  check_no_filler):
        check(text)
    return True


def main():
    validate(ENTRY)
    run_checks(ENTRY)
    out = os.environ.get("ENTRY_OUTPUT") or "/output/entry.txt"
    parent = os.path.dirname(out)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print("wrote %d characters to %s" % (len(ENTRY), out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
