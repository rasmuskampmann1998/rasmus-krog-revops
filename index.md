---
layout: home
title: Home
---

<section class="hero-centered">
  <div class="container">
    <div class="hero-avatar">
      <img src="{{ '/assets/images/me/hero-portrait.jpg?v=3' | relative_url }}" alt="Rasmus Kampmann" onerror="this.src='{{ '/assets/images/me/headshot.jpg' | relative_url }}'" />
    </div>
    <p class="hero-name">Hi, I'm Rasmus Kampmann</p>
    <h1>Data Analyst, BI Developer &amp; AI Automation Specialist</h1>
    <ul class="hero-stack">
      <li>SQL</li>
      <li>Power BI</li>
      <li>Python</li>
      <li>AI Workflows</li>
    </ul>
    <p class="hero-slogan">I turn scattered commercial data into <span class="highlight">systems you trust.</span></p>
    <p class="hero-background">Three years across data, AI, and commercial systems at <strong>Veginova Seeds</strong>, <strong>Sira Logic</strong>, and <strong>Digi-Tal Regnskab</strong>.</p>
    <div class="hero-social">
      <a href="{{ site.author.linkedin }}" target="_blank" rel="noopener" aria-label="LinkedIn">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"/></svg>
      </a>
      <a href="{{ site.author.github }}" target="_blank" rel="noopener" aria-label="GitHub">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.4 3-.405 1.02.005 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"/></svg>
      </a>
      <a href="mailto:{{ site.author.email }}" aria-label="Email">
        <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 12.713l-11.985-9.713h23.97l-11.985 9.713zm0 2.574l-12-9.725v15.438h24v-15.438l-12 9.725z"/></svg>
      </a>
    </div>
    <div class="hero-ctas-centered">
      <a href="#projects" class="btn-pill btn-pill--ghost">View Projects</a>
      <a href="{{ '/contact' | relative_url }}" class="btn-pill btn-pill--primary">Get in touch</a>
    </div>
    <p class="hero-cv-link">
      <a href="{{ '/assets/files/rasmus-kampmann-cv.pdf' | relative_url }}" download>↓ Download CV</a>
    </p>
  </div>
</section>

<section class="skills-grid-section" id="skills">
  <div class="container">
    <span class="eyebrow">Skills</span>
    <h2>What I Do</h2>
    <p class="section-sub">The tools I use most, grouped by what I actually use them for.</p>
    <div class="skills-grid">

      <div class="skill-card">
        <div class="skill-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="#B5E853" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <ellipse cx="12" cy="5" rx="9" ry="3"/>
            <path d="M3 5v6c0 1.66 4 3 9 3s9-1.34 9-3V5"/>
            <path d="M3 11v6c0 1.66 4 3 9 3s9-1.34 9-3v-6"/>
          </svg>
        </div>
        <h3>SQL</h3>
        <p>I build the data layer that everything else runs on. Joins, transformations, and pipelines that turn raw data into analysis-ready tables your team can trust.</p>
      </div>

      <div class="skill-card">
        <div class="skill-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="#B5E853" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="13" width="4" height="7" rx="0.5"/>
            <rect x="10" y="7" width="4" height="13" rx="0.5"/>
            <rect x="17" y="3" width="4" height="17" rx="0.5"/>
          </svg>
        </div>
        <h3>Power BI</h3>
        <p>I build dashboards leadership actually uses. Built around the decisions teams need to make, so reporting drives action instead of just showing numbers.</p>
      </div>

      <div class="skill-card">
        <div class="skill-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="#B5E853" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="16 18 22 12 16 6"/>
            <polyline points="8 6 2 12 8 18"/>
            <line x1="14" y1="4" x2="10" y2="20"/>
          </svg>
        </div>
        <h3>Python</h3>
        <p>I build the automation, models, and analytical work spreadsheets can't handle. From data pipelines to ML classifiers to deeper analysis at scale.</p>
      </div>

      <div class="skill-card">
        <div class="skill-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="#B5E853" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 2l2.5 5.5L20 9l-4 4 1 6-5-3-5 3 1-6-4-4 5.5-1.5z"/>
            <circle cx="12" cy="12" r="1.6"/>
          </svg>
        </div>
        <h3>AI Workflows</h3>
        <p>I build AI into the pipeline where it changes the work. Lead scoring, qualification, software detection, market intelligence. Models trained on your data, deployed where decisions get made.</p>
      </div>

      <div class="skill-card">
        <div class="skill-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="#B5E853" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <rect x="3" y="4" width="18" height="16" rx="1.5"/>
            <line x1="3" y1="9" x2="21" y2="9"/>
            <line x1="3" y1="14" x2="21" y2="14"/>
            <line x1="9" y1="4" x2="9" y2="20"/>
            <line x1="15" y1="4" x2="15" y2="20"/>
          </svg>
        </div>
        <h3>Excel</h3>
        <p>I turn messy spreadsheets into clean, validated data the rest of the stack can rely on. The foundation every downstream system depends on.</p>
      </div>

      <div class="skill-card">
        <div class="skill-icon">
          <svg viewBox="0 0 24 24" fill="none" stroke="#B5E853" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="10"/>
            <line x1="2" y1="12" x2="22" y2="12"/>
            <path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"/>
          </svg>
        </div>
        <h3>Web Scraping</h3>
        <p>I build custom scrapers that pull external signals into the same warehouse as internal data. Competitor moves, prices, regulatory feeds, job postings, so your team sees the full picture, not just what's already inside.</p>
      </div>

    </div>
  </div>
</section>

<section class="projects is-large" id="projects">
  <div class="container">
    <span class="eyebrow">Explore my work</span>
    <h2>My Projects</h2>
    <p class="section-sub">Seven production systems built end-to-end. From scattered commercial data to decisions teams trust. Written for non-technical readers.</p>
    <div class="projects-grid-large">
      {% assign sorted_projects = site.projects | sort: "order" %}
      {% for project in sorted_projects %}
        {% include project-card.html project=project %}
      {% endfor %}
    </div>
  </div>
</section>

<section class="about-two-col" id="about-strip">
  <div class="container">
    <div class="about-two-col-grid">
      <div class="about-two-col-text">
        <span class="eyebrow">Learn more</span>
        <h2>About Me</h2>
        <p>Hi, I'm Rasmus.</p>
        <p>I build the data infrastructure, BI reporting, and AI automation that turn scattered commercial data into systems leadership can trust. SQL pipelines, Power BI, web scraping, and AI workflows wired into one system.</p>
        <p>Through my work at <strong>Veginova Seeds</strong>, <strong>Sira Logic</strong>, and <strong>Digi-Tal Regnskab</strong>, I've built BI models, automated data pipelines, ML detection systems, and end-to-end GTM infrastructure across sales, finance, operations, production, and ERP sources.</p>
        <p>Most analysts build dashboards on top of someone else's data. I build the infrastructure underneath, so data and AI talk to each other. Analysis is only as reliable as the infrastructure under it. That's why I build both.</p>
        <p><strong>How I work:</strong></p>
        <ul>
          <li>Build clean, consistent data structures as the foundation</li>
          <li>Automate ingestion and transformation instead of rebuilding manually</li>
          <li>Keep pipelines lightweight, not over-engineered</li>
          <li>Build Power BI models that are easy to maintain and extend</li>
          <li>Build dashboards around the decisions leadership makes</li>
          <li>Use AI where it makes the work faster or more accurate</li>
        </ul>
        <p style="margin-top: 28px;"><strong>Stack:</strong> SQL, Python, Power BI, Excel, data modeling, ETL, web scraping, AI workflows. Hands-on across CRMs, ERPs, dialers, and the full commercial tooling layer. On the AI side: Claude, LLM pipelines, MCP servers, machine learning, and agentic frameworks.</p>
        <p>I replace manual spreadsheets and disconnected reporting with systems that run on their own and make the business easier to understand. The outcome teams hire me for: stop rebuilding reports every Monday, stop questioning the numbers, start making commercial decisions from data you trust.</p>
        <p><em>Available for freelance projects and the right full-time role.</em></p>
      </div>
      <div class="about-two-col-photo">
        <img src="{{ '/assets/images/me/photo-2.jpg' | relative_url }}" alt="Rasmus Kampmann" loading="lazy" onerror="this.src='{{ '/assets/images/me/headshot.jpg' | relative_url }}'" />
      </div>
    </div>
  </div>
</section>

<section class="experience-section" id="experience">
  <div class="container">
    <span class="eyebrow">3+ years of experience</span>
    <h2>Previous Experience</h2>
    <p class="section-sub">Roles where I built the data systems, dashboards, and automation behind real commercial decisions.</p>

    <div class="experience-timeline">

      <div class="experience-card">
        <p class="experience-date">Feb 2026 – May 2026 · Full-time · Hybrid</p>
        <h4 class="experience-role">GTM Engineer &amp; Data Analyst</h4>
        <p class="experience-company">Digi-Tal Regnskab</p>
        <ul class="experience-bullets">
          <li>Built the LinkedIn outbound infrastructure and analytics layer for a Danish SMB accounting firm.</li>
          <li>Built end-to-end outbound pipeline: scraping, enrichment, scoring, sequence execution. Cold outreach hit around 50% acceptance rate.</li>
          <li>Built predictive lead-scoring and accounting-software detection ML models (~75% accuracy across Danish SMBs).</li>
          <li>Full-channel revenue analysis across Meta, Google, LinkedIn, cold calling, and inbound.</li>
        </ul>
        <p class="experience-stack"><strong>Stack:</strong> SQL · Python · Pipedrive · Clay · Playwright · Apify · HeyReach · Claude</p>
      </div>

      <div class="experience-card">
        <p class="experience-date">Aug 2023 – Feb 2026 · Full-time · Hybrid</p>
        <h4 class="experience-role">Data Analyst &amp; RevOps</h4>
        <p class="experience-company">Veginova Seeds</p>
        <ul class="experience-bullets">
          <li>Owned the BI and reporting stack across sales, operations, and production. Single source of truth for the business.</li>
          <li>Improved KPI accuracy by 40%+. Standardised metric definitions across teams.</li>
          <li>Cut reporting time by 10+ hours per week. Stabilised broken reporting workflows and consolidated data sources.</li>
          <li>Resolved data inconsistencies across inventory, sales, and production systems.</li>
        </ul>
        <p class="experience-stack"><strong>Stack:</strong> SQL · Power BI · Python · Excel · Clay · Claude Code</p>
      </div>

      <div class="experience-card">
        <p class="experience-date">Jun 2024 – Aug 2025 · Self-employed · Remote</p>
        <h4 class="experience-role">Founder · GTM Engineer &amp; RevOps</h4>
        <p class="experience-company">Sira Logic</p>
        <ul class="experience-bullets">
          <li>Service business building AI-driven lead generation, enrichment, and CRM automation for B2B companies.</li>
          <li>Built lead enrichment and scoring workflows. Qualification accuracy improved by 30–40%.</li>
          <li>Built CRM automation pipelines integrating HubSpot and GoHighLevel with external data sources.</li>
          <li>Built custom web scraping systems for industry-specific data sources.</li>
        </ul>
        <p class="experience-stack"><strong>Stack:</strong> SQL · Python · Clay · Apify · HubSpot · GoHighLevel · HeyReach</p>
      </div>

      <div class="experience-card">
        <p class="experience-date">Jan 2025 – Jan 2026 · Freelance · Remote</p>
        <h4 class="experience-role">AI &amp; LLM Data Analyst</h4>
        <p class="experience-company">Outlier</p>
        <ul class="experience-bullets">
          <li>Reviewed and annotated 1,000+ Danish-language AI conversations to improve response quality.</li>
          <li>Spotted patterns where models failed and fed that back into training data.</li>
          <li>Built practical understanding of how LLMs work and where they break. The same insight powers the AI scoring and qualification workflows I build today.</li>
        </ul>
      </div>

      <div class="experience-card">
        <p class="experience-date">Jan 2023 – Aug 2023 · Part-time · Hybrid</p>
        <h4 class="experience-role">Marketing &amp; Digital Graduate</h4>
        <p class="experience-company">Damstahl Danmark</p>
        <ul class="experience-bullets">
          <li>Managed product and marketing data in ERP and CRM platforms across European markets.</li>
          <li>Built Excel dashboards for campaign reporting.</li>
          <li>Standardised regional data processes.</li>
        </ul>
      </div>

    </div>
  </div>
</section>

<section class="cta-soft">
  <div class="container">
    <span class="eyebrow">Want to work together?</span>
    <h2>See my freelance services</h2>
    <a href="{{ '/services' | relative_url }}" class="btn-primary">View Services →</a>
    <p class="cta-soft-footnote">Recruiters: see my <a href="{{ site.author.linkedin }}" target="_blank" rel="noopener">LinkedIn</a> or grab my <a href="{{ '/assets/files/rasmus-kampmann-cv.pdf' | relative_url }}" download>CV</a>.</p>
  </div>
</section>
