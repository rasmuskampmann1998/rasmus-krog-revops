---
layout: project
title: Channel Performance & Churn Analysis
tagline: "Ten acquisition channels treated as one mix. Split apart, scored on win rate, dialer cost, speed, and retention, the biggest channel was the worst. Synthetic data, real method."
tools: [Python, SQL, Power BI]
outcome_headline: "Five warm channels were 21% of deals but 78% of the revenue that survived the first year, at zero dialer cost"
outcome_detail: "The largest channel by volume won 8.6% of the time, carried 91% of all sales-dialer hours, and kept half its customers. A four-factor scorecard turned that into a scale-cap-kill capacity decision."
order: 2
cover_image: /assets/images/projects/channel-performance-cover.png
github_url: https://github.com/rasmuskampmann1998/rasmus-kampmann-case-studies/tree/main/02-channel-performance-analysis
---

## What this case study demonstrates

A sales team ran ten acquisition channels and reported them as one blended number. The blend looked healthy. Underneath it the channels were not one thing: win rates from 4.5% to 79%, time-to-won from a week to a month, and post-sale retention from roughly 50% to 96%. The blend hid which channels earned their cost and which burned it.

This is a channel-level analysis with a post-sale axis most channel reporting skips. It asks two questions, not one: which channel wins, and whether the customers it wins stay. The figures here are synthetic, generated from a seeded model that reproduces the shape of a real Pipedrive engagement whose data cannot be published. The method is the point.

Want the technical detail: the star schema, the scorecard rule, the Power BI model? See the [GitHub case study]({{ page.github_url }}).

## Outcome first

One number that reframes the whole mix: five warm channels were 21% of deals but 78% of the won revenue still active twelve months later, and they spent zero sales-dialer hours doing it.

The same analysis put cold calling, the single biggest channel, in the cap band: 60% of deals, an 8.6% win rate, 91% of all dialer hours, and about half its won customers gone within a year. The deliverable was one additive scorecard a revenue-operations lead can read in two minutes and rerun every quarter from the same tables.

## Context

A team selling into small businesses acquired customers through ten channels: cold calling, LinkedIn outbound, referral, inbound sales, SEO, two paid social channels, cross-sell, upsell, and a re-booking queue for prospects who cancelled a first meeting.

Capacity planning treated "the channel mix" as a single win rate. The scarce resource was sales-dialer time, and only two channels consumed it. Both of those were near the bottom on every quality measure, but blended reporting averaged that cost away so nobody could see it.

## The problem

Most teams that run many channels judge them on win rate, blended. Two failures stack on top of each other.

A channel that wins deals which churn in ninety days is not a good channel. Win rate cannot see that. There was no post-sale view tied back to the channel that acquired the customer, so "good channel" meant "closes deals" and stopped there.

The cost side was a single shared resource. Sales-dialer hours sat almost entirely on the two channels that returned the least, and the blended report made that invisible. The question the analysis had to answer: across all ten channels, which produces the most won revenue fastest, keeps the customers it wins, and where is dialer time being spent that does not come back?

## The approach

Channel is the unit of analysis, not the company and not the rep. Every deal is cut by the channel that acquired it, and every channel is scored on four things, because no single one is enough on its own.

**Win rate** is the base rate. Necessary, not sufficient: a channel can win often and still lose money if those wins leave.

**Dialer cost** is the scarce resource. The real efficiency question is won revenue returned per dialer hour, and it only matters for the two channels that spend the resource.

**Time-to-won** is a cost in disguise. A channel that closes in a week frees capacity a channel that takes a month does not.

**Retention** is the post-sale axis: share of won customers still active at twelve months, and net revenue retention, both tied back to the acquiring channel. This is the half of the picture win rate cannot show, and it is what changed the verdict.

These four collapse into one additive score, then into four action bands. The score is a rule, not a model, deliberately, so a non-technical operator can audit every point it assigns and rebuild it next quarter from the dimensional tables.

## The build

**A star schema, channel-first.** One fact table for deals, one for acquisition touches, one for meetings, joined to seven dimensions, with channel as the primary axis. The deal fact carries the close outcome, the sales-dialer hours attributed to it, and a post-won lifecycle: whether the customer churned, how many months they stayed, and the revenue that left when they did. Single-direction relationships, one row per deal, no double counting from the meeting grain. It reproduces from a seeded generator with no private data.

**A scorecard that reproduces its own bands.** Each channel scores on the four factors and lands in scale, maintain, cap, or kill. The rule is not asserted over the data; a verification step recomputes every channel's score and band straight from the tables, so the numbers in the deck and the rule that produced them cannot drift apart. The retention factor is a non-negative bonus by design: win rate and dialer cost already separate the channels, and retention should confirm that split rather than be able to flip a band on its own.

**A four-page Power BI model.** Twenty measures on the star schema. The retention measures read the post-won columns directly and never traverse an inactive relationship, which is a class of filter-context bug that file validation cannot catch. Every visual is a bar, a line on a genuinely ordered axis, a card, or a matrix. No chart that does not carry information.

![Channel economics: win rate against net revenue retention]({{ '/assets/images/projects/channel-performance-economics.png' | relative_url }})
*The whole argument in one chart. Win rate on the x-axis, net revenue retention on the y, bubble sized by won revenue. The warm channels cluster top-right: they win and they stay. Cold calling is the large red bubble bottom-left, real revenue but a low win rate and half of it gone within a year.*

![Logo survival by channel group, months zero to twelve]({{ '/assets/images/projects/channel-performance-retention-curve.png' | relative_url }})
*Do the wins stay? Share of won customers still active by month since the deal closed. Expansion holds near the top across twelve months. The outbound dialer line is the one that bleeds. The x-axis is months retained, a real ordered axis, which is why a line is honest here.*

![Win rate against deal volume by channel]({{ '/assets/images/projects/channel-performance-winrate-volume.png' | relative_url }})
*Win rate against deal volume, bubble sized by won revenue. The largest channel by volume sits near the bottom on win rate. The axis is linear, so cold calling's volume dominance is shown plainly rather than hidden behind a log scale.*

## The outcome

The bands, with coverage recomputed from the data:

- **Scale** (LinkedIn, referral, inbound, cross-sell, upsell): 21% of deals, 69% of won revenue, 78% of revenue that survived the first year, 83% retained at twelve months, zero dialer cost.
- **Maintain** (Facebook, SEO, Instagram): 14% of deals, 7% of won revenue, mid retention. Hold spend, no new investment.
- **Cap** (cold calling): 60% of deals, 23.5% of won revenue that shrinks to 15.7% once churn is taken out, 91% of dialer hours, 51% retained. It still books real volume, so freeze it, do not grow it.
- **Kill** (re-bookings): a 4.5% win rate. Stop it as a standalone motion and fold confirmed reschedules back into the source channel.

The recommendation was concrete: move a third of cold-call dialer hours to the warm follow-up motions, retire the standalone re-booking queue, and rerun the scorecard monthly from the same tables.

## What I'd do differently

The first pass had no post-sale axis at all. The word "churn" was in the write-up, but it was standing in for "low win rate", which is not churn. A channel that wins and then loses the customer in two months is a different and worse problem than a channel that wins less often, and the analysis could not tell them apart until retention went in. Adding it changed which channels looked safe. I should have built the post-sale view from the start instead of treating win rate as the whole story.

The smallest channel, re-bookings, has only fourteen won customers. Its retention number is too thin to lean on, so the kill verdict rests on its win rate over 312 deals, not on the fourteen-row retention figure, and it is flagged as small-sample everywhere it appears. A real engagement would run longer to get that channel a sample worth a recommendation.

## Tools

Python with pandas and numpy for the analysis and the verification step. SQL for the schema and the analytical queries, cross-checked in DuckDB. Power BI on a PBIP/TMDL project for the dashboard, validated headless with pbi-cli. The whole thing reproduces from one script with no real client data.
