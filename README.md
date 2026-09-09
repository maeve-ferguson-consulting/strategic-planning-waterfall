# The Strategic Planning Waterfall

A connected set of planning sessions that cascades from your three-year 10x vision all the way down to what you do this week — so every quarter, month, and week ladders up to the same north star instead of drifting on its own.

Draws on the ideas in Dan Sullivan and Benjamin Hardy's **10x Is Easier Than 2x** and on the monthly and weekly planning approach popularised by Michael Hyatt's **Full Focus** work. You're guided one question at a time; each level reads the one above it. You walk away with a branded, interactive strategic plan and a spreadsheet tracker at every level.

**About 10 minutes to set up.**

---

## Step 1 — Install in Claude Cowork

1. Open **Cowork** in Claude, then open **Customize → Plugins**.
2. Under **Personal plugins**, click **+ → Add marketplace → Add from a repository**.
3. Paste `https://github.com/maeve-ferguson-consulting/strategic-planning-waterfall`.
4. Click **Sync**, then find **The Strategic Planning Waterfall** and click **Add** or **Install**, depending on your Claude version.

This repository is public, so you do not need to connect a GitHub account. To pick up later improvements, open the marketplace in **Customize → Plugins** and click **Update**.

> If Cowork says `Unknown skill: plugin`, you pasted a Claude Code command into a Cowork conversation. Use **Customize → Plugins** instead.

<details>
<summary>Using Claude Code instead?</summary>

Run these two commands in Claude Code:

```
/plugin marketplace add maeve-ferguson-consulting/strategic-planning-waterfall
/plugin install strategic-planning-waterfall@strategic-planning-waterfall
```

</details>

### Check the installation

Start a new conversation and type `/`. You should see all five skills: `/brand`, `/plan-year`, `/plan-quarter`, `/plan-month`, and `/plan-week`. If you installed an earlier version, update the marketplace first and then start a new conversation.

## Step 2 — Set up your brand context (first time only)

Start a new conversation, type `/`, and select:

```
/brand
```

This is a short, one-question-at-a-time interview that captures your company name, voice, colors, and audience into a `BRAND.md` file. Every planning session below reads from it, so your plans come back branded to you, not to us.

## Step 3 — Run the cascade

Work top-down, in this order:

| Command | What it does |
|---|---|
| `/plan-year` | Your 3-year 10x vision, the 80% to eliminate and 20% to amplify, and this year's three initiatives |
| `/plan-quarter` | The ONE 10x outcome for the next 90 days, with monthly milestones |
| `/plan-month` | This month's Big 3 goals, tied to the quarterly outcome, plus your ideal week |
| `/plan-week` | A fast Friday review-and-plan against the monthly Big 3 |

Each one produces a branded, interactive HTML plan plus a spreadsheet tracker (except the weekly check-in, which is a fast conversational session with no file output). Run `/plan-year` and `/plan-quarter` once each; `/plan-month` monthly; `/plan-week` every week.

## What's inside

- `/brand` — the one-time brand intake that every other skill reads from
- `/plan-year` — the 3-year 10x vision and annual initiatives
- `/plan-quarter` — the 90-day 10x outcome
- `/plan-month` — the Big 3 and ideal week
- `/plan-week` — the Friday review-and-plan rhythm

## Questions

Reply to the email this came from, or reach out at [hello@maeveferguson.com](mailto:hello@maeveferguson.com).

---

<sub>These skills are an independent implementation of publicly published planning ideas. They are not affiliated with, endorsed by, or licensed from Michael Hyatt & Co. or The Strategic Coach, Inc. *Full Focus* and *10x Is Easier Than 2x* are the work of their respective authors and publishers.</sub>
