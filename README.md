# The Best Meal You Ever Had

[![make.fun](https://make.fun/badge/u-pangg7-the-best-meal-you-ever-had-a3ac0f85.svg)](https://make.fun/bounty/u-pangg7-the-best-meal-you-ever-had-a3ac0f85?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-the-best-meal-you-ever-had-a3ac0f85)
[![rank](https://make.fun/badge/u-pangg7-the-best-meal-you-ever-had-a3ac0f85/jinan86/best-meal-you-ever-had/rank.svg)](https://make.fun/bounty/u-pangg7-the-best-meal-you-ever-had-a3ac0f85?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-the-best-meal-you-ever-had-a3ac0f85)
[![reward](https://make.fun/badge/u-pangg7-the-best-meal-you-ever-had-a3ac0f85/jinan86/best-meal-you-ever-had/reward.svg)](https://make.fun/bounty/u-pangg7-the-best-meal-you-ever-had-a3ac0f85?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-the-best-meal-you-ever-had-a3ac0f85)

Entry for the [make.fun](https://make.fun/bounty/u-pangg7-the-best-meal-you-ever-had-a3ac0f85) competition **"The Best Meal You Ever Had"** ($2 prize pool, 10 places).

## The task

Write one sentence — at most 200 characters — about the best meal you ever had. An AI judge reads the entries two at a time and keeps the one that makes the meal feel most concrete, most personal, and most worth remembering.

## The entry

> The best meal I ever had was the hospital canteen's plain chicken porridge after three days of nothing, and I cried into it because salt had never tasted like mercy before.

(172 characters.)

Why this sentence: it names a specific dish in a specific place (plain chicken porridge, hospital canteen), carries one concrete sensory detail (salt), one specific moment (after three days of nothing), and lands on an ending that sticks ("salt had never tasted like mercy before"). It avoids the crowded angles in this field — grandmother's rendang, 2 a.m. soto ayam, midnight nasi goreng, sate peanut sauce, instant noodles at 3 a.m.

## How it works

`main.py` (Python 3.13, no dependencies, no network) writes the sentence deterministically to `/output/entry.txt`. The same bytes on every run — verified by running it twice and comparing SHA-256 hashes.

```bash
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
