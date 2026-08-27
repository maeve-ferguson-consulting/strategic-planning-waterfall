# The Strategic Planning Waterfall

A connected set of planning sessions that cascades from your three-year 10x vision all the way down to what you do this week — so every quarter, month, and week ladders up to the same north star instead of drifting on its own.

Draws on the ideas in Dan Sullivan and Benjamin Hardy's **10x Is Easier Than 2x** and on the monthly and weekly planning approach popularised by Michael Hyatt's **Full Focus** work. You're guided one question at a time; each level reads the one above it. You walk away with a branded, interactive strategic plan and a spreadsheet tracker at every level.

**About 10 minutes to set up.**

---

## Step 1 — Connect Claude to GitHub (one-time)

1. Open Claude Code (or Claude Cowork)
2. Click your profile icon → **Settings**
3. Scroll to **Integrations** → click **Connect GitHub** and authorize

If you've connected GitHub before, skip to Step 2.

## Step 2 — Install the plugin

In any Claude Code / Cowork conversation, run:

```
/plugin marketplace add github:maeve-ferguson-consulting/strategic-planning-waterfall
```

Select **Install** when prompted, and keep **Auto-update** on — future improvements reach you automatically.

## Step 3 — Set up your brand context (first time only)

Run:

```
/brand
```

This is a short, one-question-at-a-time interview that captures your company name, voice, colors, and audience into a `BRAND.md` file. Every planning session below reads from it, so your plans come back branded to you, not to us.

## Step 4 — Run the cascade

Work top-down, in this order:

| Command | What it does |
|---|---|
| `/plan-year` | Your 3-year 10x vision, the 80% to eliminate and 20% to amplify, and this year's three initiatives |
| `/plan-quarter` | The ONE 10x outcome for the next 90 days, with monthly milestones |
| `/plan-month` | This month's Big 3 goals, tied to the quarterly outcome, plus your ideal week |
| `/plan-week` | A fast Friday review-and-plan against the monthly Big 3 |

Each one produces a branded, interactive HTML plan plus a spreadsheet tracker (except the weekly check-in, which is a fast conversational session with no file output). Run `/plan-year` and `/plan-quarter` once each; `/plan-month` monthly; `/plan-week` every week.

## What's inside

- `define-brand-voice` — the one-time brand intake that every other skill reads from
- `annual-strategic-planner` — the 3-year 10x vision and annual initiatives
- `quarterly-strategic-planner` — the 90-day 10x outcome
- `monthly-gameplan` — the Big 3 and ideal week
- `weekly-plan` — the Friday review-and-plan rhythm

## Questions

Reply to the email this came from, or reach out at [hello@maeveferguson.com](mailto:hello@maeveferguson.com).

---

<sub>These skills are an independent implementation of publicly published planning ideas. They are not affiliated with, endorsed by, or licensed from Michael Hyatt & Co. or The Strategic Coach, Inc. *Full Focus* and *10x Is Easier Than 2x* are the work of their respective authors and publishers.</sub>
