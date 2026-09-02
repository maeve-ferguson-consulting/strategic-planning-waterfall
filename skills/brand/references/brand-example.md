<!--
WORKED EXAMPLE — not a default, and not a starting point.

Northgate Financial is a FICTIONAL firm invented purely to show the shape of a
fully-populated BRAND.md. Every name, quote, offer, price, and proof point below
is made up. Do not copy any of it into a real BRAND.md — run `/brand` and
capture the actual brand instead.

This file conforms to references/brand-schema.md — the same contract the
strategic-planning cascade (/plan-year, /plan-quarter, /plan-month, /plan-week)
and the build-* skills parse. Read it to see the exact shape a complete
BRAND.md takes.
-->

# BRAND — Northgate Financial

The canonical brand context for this Claude Project. Conforms to `references/brand-schema.md`.

---

### `Brand Identity`

```yaml
name: "Northgate Financial"
short_name: "northgate"
monogram: "NG"
tagline: "Know your numbers before the season turns"
```

---

### `Color Bases`

```yaml
- name: "Slate"
  dark:
    bg: "#1E252B"
    text: "#EEF1F3"
    accent: "#7FB2C4"
  light:
    bg: "#EEF1F3"
    text: "#1E252B"
    accent: "#2E6C82"
- name: "Clay"
  dark:
    bg: "#2B211E"
    text: "#F3EFEE"
    accent: "#D08B5F"
  light:
    bg: "#F3EFEE"
    text: "#2B211E"
    accent: "#A05A2C"
```

---

### `Typography`

```yaml
heading_font: "Source Serif 4"
heading_fallback: "Georgia, serif"
body_font: "Inter"
body_fallback: "Helvetica, Arial, sans-serif"
label_font: "Inter"
weight_override: ""
fontsource_packages:
  - "source-serif-4"
  - "inter"
```

---

### `Voice Rules`

```yaml
language_variant: "en-US"
em_dashes: "allow"
emojis: "none"
banned_words:
  - "leverage"
  - "synergy"
  - "financial freedom"
  - "game-changing"
  - "in today's economy"
  - "let's dive in"
  - "passive income"
signature_phrases:
  - "Cash is a season, not a surprise"
  - "The books tell you before the bank does"
  - "Price the job, not the hour"
person: "second"
```

---

### `Vision Tethers`

- **Cash is a season, not a surprise** — trades businesses fail on timing, not margin. Every piece traces back to seeing the cash cycle early enough to act on it.
- **Price the job, not the hour** — moving owners off hourly thinking and onto job-level profitability.
- **The owner should not be the bookkeeper** — the work that only the owner can do is never data entry.
- **Boring beats clever** — durable financial habits over tax tricks and one-off schemes.

---

### `Effects`

```yaml
metallic_accent: false
metallic_stops: []
```

---

### `Testimonial Bank`

```yaml
- quote: "We found out we were losing money on our biggest client. Two quarters later that same client is our most profitable one."
  attribution: "Dana Whitfield"
  title: "Owner, Whitfield Mechanical (fictional)"
- quote: "I stopped guessing at payroll week. That alone was worth the engagement."
  attribution: "Marcus Ellery"
  title: "Founder, Ellery Roofing (fictional)"
```

---

### `Offer Bank`

```yaml
- name: "Numbers Review"
  one_liner: "Half-day diagnostic — job costing audit, cash cycle map, and a 90-day cleanup plan"
  url: "https://example.com/numbers-review"
- name: "Fractional CFO"
  one_liner: "Monthly retainer — forecasting, pricing reviews, and a standing owner's meeting"
  url: "https://example.com/fractional-cfo"
- name: "Season Planning Intensive"
  one_liner: "Annual engagement — build the year's cash plan before the busy season starts"
  url: "https://example.com/season-planning"
```

---

<!-- ============================================================
     ENRICHMENT SECTIONS — consumed by non-builder skills.
     ============================================================ -->

### `Voice Texture`

**Voice summary:** Plain, steady, unhurried. Speaks like a trusted advisor who has seen this exact problem forty times and is not alarmed by it. Concrete over abstract. Numbers over adjectives.

**Stance toward the reader:** Peer with a specialty. Talks to competent operators who run real crews and know their trade, and assumes they simply haven't been shown their own financial picture clearly.

**Allowed stylistic moves:** Short declaratives. A specific dollar figure or date in place of a vague claim. The occasional direct question. Em-dashes are allowed here — other brands ban them; this is per-brand.

**On-brand example:**
> Most shops we meet are profitable on paper and broke in February. That isn't a margin problem. It's a timing problem, and timing problems are fixable once you can see thirteen weeks out instead of two.

**Off-brand example (and why):**
> In today's economy, it's important to leverage your financial data to unlock game-changing growth. — vague, borrowed, and says nothing a roofer could act on Monday morning.

---

### `Audience`

**Primary:** Owner-operators of construction, mechanical, and specialty trades businesses. $1M–$20M revenue, 8–60 employees. Usually second-generation or ten-plus years in. Has a bookkeeper, has never had a CFO.

**Exclude:** Pre-revenue startups. Anyone looking for tax avoidance schemes. Businesses without job-level records to work from.

**Their language:** "I don't know which jobs actually made money." "We're busy but there's never cash." "My bookkeeper gives me reports I don't read."

---

### `Reference Library`

**Named concepts:** The Thirteen-Week View — a rolling cash forecast that ends payroll-week guessing. The Job Margin Ladder — ranking every completed job by true margin to find the work worth chasing.

**Signature stories:** The February Call — the annual pattern of profitable shops running out of cash in the slow month, used to introduce the cash cycle. The Unprofitable Flagship — the biggest client that turned out to be the worst margin.

**Proof points:** Average 19-day reduction in receivable days across the first two quarters (fictional illustrative figure).
