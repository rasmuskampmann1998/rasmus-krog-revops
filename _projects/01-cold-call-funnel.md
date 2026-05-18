---
layout: project
title: Cold-Call Funnel Analysis
tagline: "102,007 dials, 362 wins. The leak was not the top of the funnel. One firmographic band decided almost the entire outcome. Synthetic data, real method."
tools: [Python, SQL, Power BI]
outcome_headline: "Companies with 6 to 20 employees closed held meetings at 37.5%. Everyone else closed at 3.0%, a 12.7x gap on the single biggest lever in the dataset"
outcome_detail: "Only 12.8% of held meetings became wins, so the pipeline leaked after the first conversation, not before it. The deliverable is an additive lead score that gates the dial list."
order: 1
cover_image: /assets/images/projects/cold-call-funnel-cover.png
github_url: https://github.com/rasmuskampmann1998/rasmus-skills/tree/main/writing-case-studies/examples/full-funnel-analysis
---

Built in SQL, Python, and Power BI. Validated in DuckDB. Reproducible from a seeded synthetic generator.

An outbound team ran 102,007 dials through an auto-dialer and judged the operation on call volume. The volume was fine. Underneath it the funnel leaked in one place: only 12.8% of held meetings became wins, and a single firmographic band, companies with 6 to 20 employees, closed at 37.5% while everyone else closed at 3.0%. The decision the analysis served: a sales lead deciding which companies the dialer should call next quarter, who was buying more top-of-funnel volume to fix a problem that was not at the top of the funnel.

The figures are synthetic, generated from a seeded model that reproduces the shape of a real CRM and auto-dialer engagement whose data cannot be published. The method is the point.

Schema, scorecard rule, and Power BI model on [GitHub]({{ page.github_url }}).

## The business question

The sales lead decides which companies go on the dial list. They were judging the operation on calls made and meetings booked, the top of the funnel, and the instinct when results were thin was to dial more.

The question: across the whole funnel, where does it actually leak, who converts once they reach a real conversation, and what rule decides who to dial? The answer had to be a list the lead could act on without a data team in the room: a dial-or-skip rule they could defend to their VP and re-fit themselves each quarter. That constraint is why the deliverable is a scorecard, not a model, and why the analysis had to follow the funnel past the booked meeting, where the leak turned out to be.

## Where the data came from

The original engagement ran on a private export from a CRM and an auto-dialer at a Danish SMB accounting firm: call logs, the meetings they booked, the deals those meetings became. That export can't be published, so this version runs on a seeded synthetic generator that emits nine CSVs with the same schema and shape. Byte-stable: same script, same data every run. Everything below is the real process on that stand-in.

The raw grain mirrors how the systems store it: one row per call attempt, one per booked meeting, one per deal. Three things had to be derived before any funnel could be drawn: which call connected and booked, whether a booked meeting was actually held or cancelled, and the held-to-won outcome joined back to the company's firmographics. The held-versus-cancelled split is the column that turned a "we need more dials" story into a "we leak after the first conversation" story.

## The data model

A star schema, the funnel as three fact grains:

- `fact_calls`: one row per dial (102,007), carrying connect and meeting-booked flags. The top of the funnel.
- `fact_meetings`: one row per booked meeting, carrying held-or-cancelled status and the days-to-close clock. The middle, where the leak is.
- `fact_deals`: one row per deal, carrying won/lost and MRR. The bottom.

Seven conformed dimensions hang off those facts: date, company, rep, stage, lost reason, source, and the firmographic attributes on the company. Company is the segment axis, so its firmographics (employee band, industry) are dimension columns, not buried in a deal record. That is what lets every funnel step cut by segment without rewriting a query. Relationships are single-direction; the won and lost date relationships are inactive and activated with `USERELATIONSHIP` only where a timing measure needs them, so a measure can never silently pull the wrong date.

## Cleaning and validation

Every finding here rests on attributing each held meeting to one company segment, and on the held-versus-cancelled split being right. Three things had to be true before any chart was drawn, and a volume report skips all three.

A held meeting counted as cancelled, or the reverse, would move the entire leak. The meeting status was reconciled against the deal outcome so a "held" meeting with no corresponding deal record could not silently inflate the held count, and the cancellation share (43.0% of all losses) was checked against the loss-reason mix rather than assumed.

A deal with more than one meeting must count once, not once per meeting, or a chatty segment looks like it converts more. The meeting and deal streams stay at their own grain and roll up on the deal key before they join, so revenue and win counts are counted once per deal.

The last gate catches the silent error: every analysis figure in this write-up and the dashboard is recomputed from the CSVs by one verification script, and the Power BI measures were checked by definition-equivalence against that same script. The headline measures reproduce it exactly: meeting-to-won 12.8%, the 6-20 band 37.5%, MRR won $278,449. The scorecard band coverage (its share of the universe and of historic wins) comes from applying the documented scoring rule to those same tables, not from the analysis script. If a number moves, the check fails before the chart ships.

## The approach

The unit of analysis is the held meeting, not the call. A call that never reaches a conversation tells you nothing about who converts; a held meeting does. Every held meeting is cut by the company it belonged to, and the funnel is read one step at a time so the leak has nowhere to hide.

Three cuts decide the answer. The funnel waterfall locates *where* it leaks. The segment cuts (employee band, industry) find *who* leaks and who does not. The loss mix explains *why* the rest is lost. Each cut is a single chart with a single finding, and the cuts that show no signal are reported as no signal rather than dressed up, because a flat result is itself a finding.

## The findings

**The funnel does not leak at the top. It leaks after the first conversation.**

![Full funnel, dials to closed deal]({{ '/assets/images/projects/cold-call-funnel-waterfall.png' | relative_url }})
*102,007 calls, 31,421 connected, 5,755 meetings booked, 2,829 held, 362 won. Each step loses volume as expected until the last one: only 12.8% of held meetings become wins. The drop the team could not see was the one after the meeting, not before it.*

The waterfall is the case for not buying more dials. Connect-to-booked behaves like a normal outbound funnel. The collapse is meeting-to-won: 2,829 real conversations produced 362 deals. Adding top-of-funnel volume scales the 12.8%, it does not fix it. The lever is the conversation-to-deal step, and the next chart shows the lever has a single owner.

**One employee band closes at 37.5%. Everyone else closes at 3.0%.**

![Meeting to won by employee band]({{ '/assets/images/projects/cold-call-funnel-employee-band.png' | relative_url }})
*Held-to-won by company size. The 6 to 20 band closes at 37.5% on 805 held meetings. Every other band sits between 1.4% and 6.0%. There is no gradient here, there is one spike.*

This is the single biggest result in the dataset. The win rate is not distributed across company sizes, it is concentrated in one band. The 6-20 segment closes at 37.5%; everything else combined closes at 3.0%, a 12.7x gap. A dial list that ignores employee band is spending most of its calls outside the only segment that converts, and the blended 12.8% baseline hides that completely.

**Industry is the second filter, and three industries are a hard zero.**

![Meeting to won by industry, anti-ICP in red]({{ '/assets/images/projects/cold-call-funnel-industry.png' | relative_url }})
*Held-to-won by industry. Consulting, Transport, and Marketing close at roughly zero: two wins on 502 held meetings combined. Every qualifying industry sits between 14.7% and 16.6%.*

Industry does not rank prospects on a curve; it disqualifies three of them. Consulting (0.0%), Transport (0.4%), and Marketing (1.1%) are not weak segments, they are anti-ICP: 502 held meetings, two wins. The qualifying industries are flat at 15%, which means industry is a blacklist, not a score. Two fields, employee band and an industry blacklist, do almost all the work, which is exactly what makes the deliverable a simple rule rather than a model.

**The accounting system is a non-signal, and saying so is the finding.**

The same cut by accounting software was flat: every system between 12.1% and 13.4%, sitting on the 12.8% baseline. It would have been easy to present a "best-converting accounting system" chart; the honest result is that there is no signal there, so it is not a chart. Reporting the null keeps the two real signals credible.

**Most losses never reach a real conversation.**

![Lost-reason Pareto]({{ '/assets/images/projects/cold-call-funnel-loss.png' | relative_url }})
*Loss mix. 43.0% of all losses are meeting cancellations, and No-response is 57.3% of the categorised reasons. Most lost deals were lost before a salesperson ever spoke to them.*

The leak has a second mechanism. Of 4,329 losses, 1,862 (43.0%) are meeting cancellations, deals that died between booking and the conversation. That is a confirmation-cadence problem, not a sales-skill problem, and it is fixable without touching the dial list. It also explains why top-of-funnel volume felt unproductive: a large share of booked meetings never became conversations at all.

**Speed is not the constraint.**

![Meeting to won cycle]({{ '/assets/images/projects/cold-call-funnel-cycle.png' | relative_url }})
*Days from held meeting to won. Median 11 days, p90 24 days. Deals that close, close fast.*

The cycle is short and tight: median 11 days, 90th percentile 24. Deals that close do not drag. Closing speed is not where to spend effort; the prior charts already named where to spend it. Reporting the cycle confirms there is no hidden slow-deal problem masking the real story.

## The deliverable

The findings collapse into one additive lead score that gates the dial list. Each company earns points on the two fields that carry the signal, employee band and industry, and the total decides dial or skip.

- Employee band 6-20: the heavy positive weight. It is the 37.5%-vs-3.0% lever.
- Anti-ICP industry (Consulting, Transport, Marketing): a hard negative that zeroes the score regardless of size.
- Everything else: small or zero weight, because the data showed no other field carries signal.

There is no "maybe" tier. The data has one decisive split, not a gradient, so the scorecard has two outcomes, not three. On the historic data the Dial band is 22.7% of the universe and covers 83% of the wins: skip three-quarters of the list, keep most of the revenue. The scorecard is built so a sales lead can re-fit the weights each quarter from the same tables and defend every point of the score to a VP from the underlying segment lift, not a model coefficient. Alongside it: a meeting-confirmation cadence to attack the 43% cancellation loss, and an industry blacklist that removes the three anti-ICP industries from active dialing.

## What I'd do differently

The first pass read this as a top-of-funnel problem because that is what the team measured and what the call volume invited. The funnel waterfall is what reframed it: the leak was the meeting-to-won step the whole time, and no amount of connect-rate optimisation touches it. I should have drawn the full funnel before looking at any single step, because the step everyone watches is rarely the step that leaks.

The anti-ICP industries are a hard zero on this synthetic population, which is cleaner than reality. A real engagement would show a low but non-zero rate there, and the honest call would be to set the blacklist threshold from a confidence interval on the real conversion rate, not from an exact zero. The method is the same; the threshold would need a real sample behind it.

## Tools, by step

The same tools most analysts list, used at a specific step for a specific reason:

| Step | Tool | What it did here |
|---|---|---|
| Sourcing | CRM + auto-dialer export (synthetic stand-in via a seeded Python generator) | Call logs, meetings, and deals at system grain; no private data leaves the original engagement |
| Modelling | SQL (Postgres-style DDL) | The star schema: three funnel fact grains, seven conformed dimensions, company as the segment axis |
| Cleaning and validation | DuckDB | Held-vs-cancelled reconciliation, grain dedupe on the deal key, query validation before any finding |
| Analysis | Python (pandas, numpy) | The funnel and segment cuts, the loss mix, and a verification script that recomputes every quoted number |
| Dashboard | Power BI (PBIP/TMDL, validated headless with pbi-cli) | The funnel and the scorecard as something the sales lead reruns each quarter |
| Reproduction | One seeded script | The whole pipeline regenerates byte-identically from source with no real client data |

Every chart in this case study is a bar, a line, or a histogram, one comparison grammar, nothing that needs a second encoding to decode.
