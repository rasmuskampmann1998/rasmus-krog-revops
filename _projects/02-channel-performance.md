---
layout: project
title: Channel Performance & Churn Analysis
tagline: "Ten acquisition channels treated as one mix. Split apart, scored on win rate, dialer cost, speed, and churn, the biggest channel was the worst. Synthetic data, real method."
tools: [Python, SQL, Power BI]
outcome_headline: "Five warm channels were 21% of deals but 78% of the revenue that survived the first year, at zero dialer cost"
outcome_detail: "The largest channel by volume won 8.6% of the time, carried 91% of all sales-dialer hours, and churned half its customers within twelve months."
order: 2
cover_image: /assets/images/projects/channel-performance-cover.png
github_url: https://github.com/rasmuskampmann1998/rasmus-skills/tree/main/writing-case-studies/examples/channel-performance-analysis
---

Built in SQL, Python, and Power BI. Validated in DuckDB. Reproducible from a seeded synthetic generator.

A sales team ran ten acquisition channels and reported them as one blended win rate. Underneath: win rates from 4.5% to 79%, twelve-month churn from 4% to 50%, time-to-won from a week to a month. The blend hid which channels earned their cost and which burned it. The deliverable is a four-factor scorecard a revenue-operations lead reruns each quarter to decide where dialer hours and budget go next.

The figures are synthetic, generated from a seeded model that reproduces the shape of a real CRM engagement whose data cannot be published. The method is the point.

Schema, scorecard rule, and Power BI model on [GitHub]({{ page.github_url }}).

## The business question

The revenue-operations lead decides every quarter where dialer hours and budget go. They were deciding it on a single blended win rate that hid which channels actually earned the spend. The brief was a quarterly cadence: bands reviewed together, the lead reruns the scorecard themselves between reviews, no data team in the loop.

The question: across ten channels, which produces the most won revenue fastest, retains the customers it wins, and where is dialer time being spent that does not come back? The answer had to be something the lead could act on without a data team in the room: a ranking they could defend to a CFO and rerun themselves each quarter. That constraint is why the deliverable is a scorecard, not a model, and why churn had to be in scope alongside win rate.

## Where the data came from

The original engagement ran on a private CRM export from a Danish SMB accounting firm: deals, the activities behind them, the meetings they produced. That export can't be published, so this version runs on a seeded synthetic generator that emits ten CSVs with the same schema and shape. Byte-stable: same script, same data every run. Everything below is the real process on that stand-in.

The raw grain mirrors how a CRM stores it: one record per deal, separate streams for the touches that created it and the meetings it generated. Three things were not in the raw export and had to be derived: the channel attributed to each deal (first-touch), the sales-dialer hours consumed per deal, and the post-won lifecycle (whether and when a won customer churned). The post-won lifecycle is the column the original reporting never had, and the one that changed the answer.

## The data model

A star schema, channel as the primary dimension, three fact grains:

- `fact_deals`: one row per deal, channel-attributed, carrying the close outcome, the dialer hours spent on it, and the post-won columns (`is_churned`, `retained_months`, `churned_mrr`).
- `fact_touches`: one row per acquisition touch, used for first-touch attribution and the dialer-cost rollup.
- `fact_meetings`: one row per booked meeting, used for the show-rate and cancellation cuts.

Seven conformed dimensions hang off those facts: date, channel, campaign, company, rep, stage, lost reason. Channel is a dimension, not a column on the deal, so every measure cuts by channel without rewriting a query. Relationships are single-direction, one row per deal. `dim_campaign` deliberately doesn't join `dim_channel`; channel context arrives through `fact_deals`, keeping the schema a clean star. Small choices like that are the difference between a model a revenue lead can extend and one only its author can.

## Cleaning and validation

Every finding here rests on attributing each deal to one channel. Three things had to be true before any chart was drawn, and a findings report skips all three.

A dangling channel key would silently drop deals from a rollup and bias the ranking toward whichever channel kept its keys clean, so I joined every foreign key in the fact tables back to its dimension in DuckDB and required zero orphans, including the post-won `churn_date_key`. It came back clean; if it had not, the win-rate cliff could have been an artefact of lost rows rather than a real split.

A deal with three meetings must count as one deal, not three, or every channel that books more meetings looks like it wins more revenue. The touch and meeting streams stay at their own grain and roll up before they reach the deal grain, so revenue is counted once per deal and the dialer-cost rollup is not inflated by chatty channels.

The last gate catches the silent error: the scorecard quotes a number, and the rule that produces the band has to agree with it. One verification script recomputes every figure in this write-up, the dashboard, and the scorecard from the CSVs, and reassigns the bands from the same rule. If a measure moves, the script fails before the chart ships.

## The approach

Channel is the unit of analysis. Every deal is cut by the channel that acquired it, scored on four things, because no single one is enough.

**Win rate.** The base rate. A channel can win often and still lose money if those wins leave.

**Dialer cost.** The scarce resource: won revenue returned per dialer hour. It only matters for the two channels that spend it. Everything else returns revenue at zero dialer cost, which is itself the finding.

**Time-to-won.** A cost in disguise. A channel that closes in a week frees a rep's capacity that a channel taking a month does not.

**Churn.** The post-sale axis, and the one that changed the verdict. Measured through twelve-month retention and net revenue retention, tied back to the acquiring channel. The half of the picture win rate cannot show.

These collapse into one additive score, then four bands: scale, maintain, cap, kill. A rule, not a model, deliberately. A model would be more precise and useless here, because nobody on the revenue team could audit it or rebuild it next quarter. Every point is traceable to a number in the tables.

## The findings

**Win rate splits the channels into two populations, and the biggest one is in the wrong half.**

![Win rate by channel]({{ '/assets/images/projects/channel-performance-winrate.png' | relative_url }})
*Win rate per channel, sorted, sales-dialer channels in red. There is no gradient here, there is a cliff. Referral, cross-sell, upsell, inbound, and LinkedIn all clear 61%. Everything else is under 15%. Cold calling, the channel that books the most deals, sits at 8.6%, third from the bottom.*

The win-rate chart is the case for abandoning the blend in one image. The channels do not sit on a smooth curve from good to bad. They form two clusters with nothing in between: five warm channels above 61%, five channels below 15%. A blended average of those two populations describes none of them. Cold calling at 8.6% is not "a bit below average", it is in the bottom cluster, and it is the largest channel the team runs.

**Volume is concentrated exactly where win rate is weakest.**

![Deal volume by channel]({{ '/assets/images/projects/channel-performance-volume.png' | relative_url }})
*Deals created per channel. Cold calling is roughly ten times the next-biggest channel. The single bar that dominates the volume chart is the same channel sitting third from the bottom on win rate.*

Put the two bar charts next to each other and the structural problem is obvious. The channel with the most deals has nearly the worst win rate. The team's capacity was being spent in proportion to volume, and volume was inversely related to quality. This is the dilution trap: a high-volume, low-conversion channel makes the pipeline look busy and the blended number look stable while consuming the capacity that the high-conversion channels needed.

**Churn is the second axis, and it punishes the same channels again.**

![Net revenue retention by channel]({{ '/assets/images/projects/channel-performance-nrr.png' | relative_url }})
*Net revenue retention at twelve months, per channel. Expansion and referral channels keep 87% to 94% of the revenue they win. Cold calling keeps 50%. The dialer channels are red, at the bottom, again.*

This is the chart the original reporting could not produce. Win rate stops at the signature; this starts there. Cold calling wins less often and then loses half of what it does win within a year. Its 23.5% share of won revenue shrinks to 15.7% once churn is taken out. The warm channels are the mirror image: they win more often and the revenue stays. Win rate and twelve-month retention rank the channels in nearly the same order. On a real dataset, two independent measures agreeing tells you the conclusion isn't a single-metric artefact. In this synthetic version the agreement is built into the model, so the takeaway is the method of cross-checking one axis against a second, not the figures themselves.

**The wins that stay, stay from day one.**

![Logo survival by channel group]({{ '/assets/images/projects/channel-performance-retention-curve.png' | relative_url }})
*Share of won customers still active by month since the deal closed, grouped by channel type. The x-axis is months retained, a real ordered axis. Expansion holds near the top across all twelve months. The outbound dialer line bleeds from the first month and never recovers.*

The survival curve shows the churn gap is not a late-life cliff that better onboarding could fix. The outbound line separates from the others in month one and the gap only widens. When churn starts that early and never recovers, the reading is that the channel is selecting weaker-fit customers rather than serving the same customers worse, which is the difference between "improve retention on this channel" and "stop scaling this channel". On a real dataset that distinction is what the survival shape would tell you; here the shape is generated to demonstrate the method, so treat the conclusion as the method, not as an observed result.

**Speed tells the same story a third time.**

![Time to won by channel]({{ '/assets/images/projects/channel-performance-time-to-won.png' | relative_url }})
*Median and 90th-percentile days from first touch to won, per channel. Expansion closes in under a week at the median. Cold calling takes 20 days, re-bookings 31, with long tails behind both.*

Every axis points the same way. The channels that win more and retain more also close faster, which means they return capacity to the team sooner and can be worked again within the quarter. The channels that win least and churn most are also the slowest, so the same dialer hour buys fewer attempts. There is no axis on which the dialer channels are the better investment.

## The deliverable

The four factors collapse into one additive scorecard. Each channel earns points on win rate, dialer cost, time-to-won, and twelve-month retention, and the total drops it into one of four bands.

- **Scale** (LinkedIn, referral, inbound, cross-sell, upsell): 21% of deals, 69% of won revenue, **78% of the revenue that survived the first year**, 83% retained at twelve months, zero dialer cost. Move budget and capacity here first.
- **Maintain** (Facebook, SEO, Instagram): 14% of deals, 7% of won revenue, mid retention. Hold spend, no new investment.
- **Cap** (cold calling): 60% of deals, 23.5% of won revenue that shrinks to 15.7% net of churn, 91% of dialer hours, 51% retained. It still books real volume, so the call is freeze it, do not grow it. Capping, not killing, because the volume is real even though the quality is not.
- **Kill** (re-bookings): a 4.5% win rate on 312 deals. Stop it as a standalone motion and fold confirmed reschedules back into the channel that originally booked the meeting.

The retention factor is a non-negative bonus by design, not a penalty. Win rate and dialer cost already separate the channels cleanly; retention is there to confirm that split, not to be powerful enough to flip a band on its own. That keeps the rule honest: it cannot be gamed by one strong quarter on a single axis, and a revenue lead can defend every band assignment by pointing at the underlying numbers.

The scorecard is built so a revenue-operations lead can rerun it each quarter, defend each band to a CFO from the underlying numbers, and reassign channels as the mix shifts. The recommendation it points to is concrete: move a third of cold-call dialer hours to the warm follow-up motions, retire the standalone re-booking queue, rerun monthly from the same tables so the bands track reality instead of last quarter's assumptions.

## What I'd do differently

The first pass had no post-sale axis at all. The word "churn" was in the write-up, but it was standing in for "low win rate", which is not churn. A channel that wins and then loses the customer in two months is a different and worse problem than a channel that wins less often, and the analysis could not tell them apart until retention went in. Adding it changed which channels looked safe. A channel can clear a respectable win rate and still belong in the cap band once you can see what happens after the signature. I should have built the post-sale view from the start instead of treating the contract as the finish line.

The smallest channel, re-bookings, has only fourteen won customers. Its retention number is too thin to carry a recommendation, so the kill verdict rests on its 4.5% win rate over 312 deals, not on the fourteen-row retention figure, and it is flagged as small-sample everywhere it appears. A real engagement would run the window longer to give that channel a sample worth a decision rather than a direction.

## Tools, by step

The same tools most analysts list, but used at a specific step for a specific reason:

| Step | Tool | What it did here |
|---|---|---|
| Sourcing | CRM export (synthetic stand-in via a seeded Python generator) | Deals, touches, and meetings at CRM grain; no private data leaves the original engagement |
| Modelling | SQL (Postgres-style DDL) | The star schema: three fact grains, seven conformed dimensions, channel as the primary axis |
| Cleaning and validation | DuckDB | Referential-integrity checks (zero FK orphans), grain dedupe, query validation before any finding |
| Churn analysis | Python (pandas) | Twelve-month retention curves, net revenue retention, and survival shape by channel group |
| Analysis | Python (pandas, numpy) | The four-factor scoring and a verification script that recomputes every quoted number |
| Dashboard | Power BI (PBIP/TMDL, validated headless with pbi-cli) | The channel scorecard as something the revenue lead reruns each quarter |
| Reproduction | One seeded script | The whole pipeline regenerates byte-identically from source with no real client data |

Every chart in this case study is a bar or a line, one comparison grammar, nothing that needs a second encoding to decode.
