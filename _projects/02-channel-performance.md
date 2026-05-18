---
layout: project
title: Channel Performance & Churn Analysis
tagline: "Which acquisition channel produces the most won revenue fastest, and keeps the customers it wins?"
tools: [Python, SQL, Power BI]
outcome_headline: "Win rate, dialer cost, time-to-won, and 12-month retention scored into one channel-allocation rule"
outcome_detail: "Found that the biggest channel by volume wins least, costs the most sales-dialer time, and keeps half its customers. Built an additive scorecard that routes capacity to the channels that win and stay. Reproducible end to end on synthetic data."
order: 2
cover_image: /assets/images/projects/channel-performance-cover.png
github_url: https://github.com/rasmuskampmann1998/rasmus-kampmann-case-studies/tree/main/02-channel-performance-analysis
---

> Synthetic case study. The original ran on a private Pipedrive export that cannot be redistributed. Every figure here comes from a seeded generator that reproduces the shape of the real finding. No number is a real client result. The method is the point, not the values.

## Outcome first

A sales team ran ten acquisition channels and treated them as one mix. I split the mix and scored every channel on four things: how often it wins, how much scarce sales-dialer time it costs, how fast it closes, and how many of the customers it wins are still paying a year later.

The biggest channel by volume, cold calling, was 60% of all deals, carried 91% of all dialer hours, won 8.6% of the time, and kept about half its customers at month 12. Five warm channels were 21% of deals but 69% of won revenue and 78% of revenue that survived the first year, at zero dialer cost. One channel that looked like a real motion on the org chart, re-bookings, barely won and the little it won did not stay.

The deliverable is one additive scorecard a revenue-operations lead can explain in two minutes and recompute every quarter from the same tables. It puts each channel in one of four bands: scale, maintain, cap, kill.

Technical deep-dive, generator, verification script, SQL, and the Power BI project: see the [GitHub case study]({{ page.github_url }}).

## Context

A team selling into small businesses brought in customers through ten channels: cold calling, LinkedIn outbound, referral, inbound sales, SEO, two paid social channels, cross-sell, upsell, and a re-booking queue for prospects who cancelled a first meeting.

Capacity planning treated "the channel mix" as a single number. The blended win rate looked fine. Underneath it, the channels were not one thing. They had win rates from 4.5% to 79%, time-to-won from a week to a month, and post-sale retention from roughly 50% to 96%. Averaging them hid which ones earned their cost and which ones burned it.

The scarce resource was sales-dialer time. Only two channels consumed it, and they were the two with the worst economics. That cost was invisible at the blended level.

## The problem

Most teams that run many acquisition channels judge them on win rate alone, and judge win rate at the blended level. Two failures stack:

- A channel that wins deals that churn in ninety days is not a good channel. Win rate cannot see that. The team had no post-sale view tied back to the channel that acquired the customer.
- The cost side was a single shared resource, sales-dialer hours, sitting almost entirely on the two channels that returned the least. Blended reporting averaged that away.

The question the analysis had to answer: across all ten channels, which produces the most won revenue fastest, and keeps the customers it wins, and where is dialer time being spent that does not come back?

## The approach

Channel is the unit of analysis, not the company and not the rep. Everything is cut by the channel that acquired the deal.

Four things get measured per channel, because no single one is enough on its own:

**Win rate.** The base rate. Necessary, not sufficient. A channel can win often and still lose money if those wins leave.

**Dialer cost.** Sales-dialer hours are finite. The right efficiency question is revenue returned per dialer hour, and the answer is only interesting for the two channels that spend the resource.

**Time-to-won.** A channel that closes in a week frees capacity a channel that takes a month does not. Speed is a cost in disguise.

**Retention.** The post-sale axis. Share of won customers still active at twelve months, and net revenue retention, both tied back to the acquiring channel. This is the half of the picture win rate cannot show.

These four collapse into one additive score, then into four action bands. The score is a rule, not a model. It is built so a non-technical operator can audit it and rebuild it each quarter from the dimensional tables.

## The build

**The data model.** A star schema. One fact table for deals, one for acquisition touches, one for meetings, joined to seven dimensions, with channel as the primary axis. The deal fact carries the close outcome, the sales-dialer hours attributed to it, and a post-won lifecycle: whether the customer churned, how many months they stayed, and the revenue that left when they did. Single-direction relationships, one row per deal, no double counting from the meeting grain.

**The synthetic generator.** The public version takes no private input. A seeded generator designs a per-channel win rate, a per-channel close-speed, and a per-channel twelve-month survival curve, then writes a fictional deal population that reproduces the real finding's shape. One calibration step pins the largest channel to its designed win rate so the channel ranking holds on every run. The retention model draws each won customer a lifetime from a survival curve whose monthly rate solves to the channel's designed twelve-month retention. It is deterministic and byte-stable: the same script produces the same files every time.

**The verification script.** A single script recomputes every number quoted in the write-up, the deck, and the dashboard, straight from the generated tables. It is the source of truth. The narrative quotes it. It also computes the scorecard itself, so the rule in the deck is reproduced from data, not asserted over it. The SQL queries were cross-checked against it in DuckDB with zero foreign-key orphans.

**The Power BI dashboard.** Four pages on the star schema, twenty measures, themed in one calm palette with red reserved for the worst channels so the colour carries the story. The retention measures read the post-won columns directly and never traverse an inactive relationship, which is a class of bug that file validation cannot catch. Every chart is a bar, a line on a real ordered axis, a card, or a matrix. No pie, no scatter, no decoration that does not carry information.

The charts below are generated by the analysis script straight from the same tables, not screenshots. They are the figures the dashboard renders.

![Win rate against net revenue retention, every channel]({{ '/assets/images/projects/channel-performance-economics.png' | relative_url }})
*The channel-economics view. Win rate on the x-axis, net revenue retention on the y, bubble sized by won revenue. Warm channels cluster top-right: they win and they stay. Cold calling is the large bubble bottom-left, real revenue but a low win rate and half of it gone within a year. This one chart is the whole argument.*

![Logo survival by channel group, months zero to twelve]({{ '/assets/images/projects/channel-performance-retention-curve.png' | relative_url }})
*Do the wins stay? Share of won customers still active by month since the deal closed. Expansion holds near the top across all twelve months. The outbound dialer line drops away early. The x-axis is months retained, a real ordered axis, not a calendar trend, which is why a line is honest here.*

![Win rate against deal volume by channel]({{ '/assets/images/projects/channel-performance-winrate-volume.png' | relative_url }})
*Win rate against deal volume, bubble sized by won revenue. The largest channel by volume sits near the bottom on win rate. The axis is linear, so cold calling's volume dominance is shown plainly with a callout rather than hidden behind a log scale.*

## The outcome

The numbers, all synthetic and recomputed by the verification script:

- Cold calling: 60.4% of deals, 8.6% win rate, 91% of all dialer hours, about 51% of its won customers retained at twelve months. Its 23.5% share of won revenue shrinks to 15.7% once churn is taken out.
- Five warm channels (LinkedIn, referral, inbound, cross-sell, upsell): 21.1% of deals, 69.0% of won revenue, 77.6% of net revenue, 83% retained at twelve months, zero dialer cost.
- Re-bookings: 4.5% win rate on 312 deals. The few it won did not stay, on a sample too small to lean on, so the kill verdict rests on the win rate, not the retention.
- Blended twelve-month retention 74%, net revenue retention 74%.

The scorecard puts the five warm channels in **scale**, the three paid and search channels in **maintain**, cold calling in **cap** (it still books real volume, so freeze it, do not grow it), and re-bookings in **kill** as a standalone motion. The retention factor in the score is a bonus, not a penalty, on purpose: win rate and dialer cost already separate the channels, and retention should confirm that split, not be able to flip a band on its own.

The recommendation is concrete. Move a third of cold-call dialer hours to the warm follow-up motions. Retire the standalone re-booking queue and fold confirmed reschedules back into their source channel. Recompute the scorecard monthly from the same tables.

## What I'd do differently

The first version had no post-sale view at all. The word "churn" was in the write-up, but it was standing in for "low win rate," which is not churn. A channel that wins and then loses the customer in two months is a different and worse problem than a channel that wins less often, and the analysis could not tell them apart until the retention axis went in. That was the real gap, and it was the second pass that caught it, not the first.

Two of the original five charts did not survive review. One plotted a monthly trend on data with no designed trend, so it was noise dressed as a finding. One showed dialer efficiency for ten channels when only two channels spend dialer time, so eight of its bars were empty. Both were replaced with charts backed by a real signal. The lesson held: a chart that looks busy is not the same as a chart that says something.

The smallest channel, re-bookings, has only fourteen won deals. Its retention reads directionally and nothing load-bearing leans on it. I flagged it as small-sample everywhere it appears rather than letting a fourteen-row number carry a recommendation. The kill call stands on the 312-deal win rate instead.

## Tools

Python with pandas and numpy for the generator and the verification script. Faker for the fictional company names. matplotlib for the charts. SQL for the schema and the analytical queries, cross-checked in DuckDB. Power BI on a PBIP/TMDL project for the dashboard, validated with pbi-cli. The whole thing reproduces from one generator script with no real client data.
