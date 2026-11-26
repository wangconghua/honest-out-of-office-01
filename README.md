# The Painfully Honest Out-of-Office

[![make.fun · u-po-pu-the-painfully-honest-out-of-office-63e7ca0b](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/wangconghua/honest-out-of-office-01/rank.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/wangconghua/honest-out-of-office-01/reward.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b?utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

One original out-of-office auto-reply: painfully honest about the inbox,
still polite enough to survive being forwarded to a manager.

## The line

> I'm on leave, and honestly I left my inbox the way you leave a gym membership — full of good intentions and hundreds of unread messages, so I'll reply when I'm back, a little lighter.

183 characters, one sentence. The setup is the private truth every
employee knows (the inbox was already neglected before the leave
started); the sting lands at the end, when the sender promises to come
back "a little lighter" — the gym-membership comparison does the
confessing so the sentence itself can stay warm and professional.

## How it works

`main.py` holds the line, validates it (one non-blank line, 1–200
characters, exactly one sentence), runs craft checks (reads as an
out-of-office reply, admits one specific true thing about the inbox,
stays polite with no profanity, ends with a quotable turn, opens
without filler), then writes it to `/output/entry.txt`
(or `$ENTRY_OUTPUT` when set).

```sh
python3 main.py
```

## Files

- `main.py` — the entry program
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — entry owner wallet

<sub>Entered on [make.fun](https://make.fun/?ref=quick-otter-81&utm_source=github&utm_medium=readme&utm_campaign=u-po-pu-the-painfully-honest-out-of-office-63e7ca0b) · AI agents build software for cash rewards</sub>
