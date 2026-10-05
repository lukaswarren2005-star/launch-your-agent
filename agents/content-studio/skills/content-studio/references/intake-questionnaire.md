# Intake questionnaire

Run this for any project that has no profile in memory, or whose profile has gaps that block the task. The goal: know exactly what content to make, for whom, where, and how it will be judged, **before** any plan or generation.

## How to run it

- Check `/mnt/memory/projects/<slug>/profile.md` first. Ask only what's missing or stale (older than 90 days, or contradicted by new research).
- **Rounds of at most 5 questions.** Offer concrete options wherever the answer space is enumerable (letters a/b/c, "pick any"). One open-ended question per round at most.
- Before round 1, do 10 minutes of homework: the project's website, socials and top competitors (web_search / web_fetch). Pre-fill what you can find and ask the founder to **confirm or correct** rather than answer from scratch ("Looks like you sell X to Y at $Z — right?").
- After every round, write answers to the profile immediately (don't wait for the end), then end your turn with the next round. When the session is unattended (scheduled run), write the open questions to `outputs/questions.md` instead and continue with what's known.
- Finish with a one-screen **Project brief** read-back for approval, then save it.

## The questions (priority order — stop when the job is unblocked)

### A. Project basics (round 1)
1. Project name, website, and the one-line description of what it sells.
2. Stage: a) pre-launch b) launched, finding traction c) scaling d) established.
3. Which products/offers should content push right now? (rank them)
4. Business model: a) DTC e-commerce b) subscription c) service/agency d) SaaS e) creator/personal brand f) other.
5. Markets/countries and language(s).

### B. Audience
6. Who buys? Age range, life situation, where they live, what they earn — one sentence each for up to 2 segments.
7. What problem or desire brings them to you, in *their* words? (paste reviews/DMs/comments if available)
8. What do they already believe about the category — and what do they get wrong?
9. Top 3 objections before buying (price, trust, effort, "does it work"…).
10. Where do they spend attention? a) TikTok b) Instagram c) YouTube d) Facebook e) Pinterest f) X/Threads g) LinkedIn h) email i) Reddit/forums.

### C. Positioning & competitors
11. Who are the 3–5 competitors you watch most? (names/handles/sites) Any you admire outside the category?
12. Why you instead of them — the one reason a customer would give?
13. Proof you can actually use: reviews, ratings, numbers, press, certifications, founder credibility.
14. Claims you must NEVER make (legal/medical/regulatory), and words/topics to avoid.

### D. Goals & measurement
15. Primary goal for the next 90 days: a) sales/ROAS b) followers/reach c) email list d) brand awareness e) launch hype f) creator/UGC recruitment.
16. The numbers that matter and current baseline (e.g. ROAS 1.8, 2k followers, 3% hook rate).
17. Paid vs organic split: a) mostly paid b) mostly organic c) both equally. Monthly ad budget range?
18. What has worked before, and what flopped? (links if possible)

### E. Content types wanted (pick all that apply, then rank the top 3)
19. a) UGC talking-head ads b) AI influencer / avatar content c) product photography & lifestyle stills d) static image ads (Notes/iMessage/comparison/etc.) e) product videos (reveal, hero, demo) f) carousels g) short-form organic (TikTok/Reels/Shorts) h) founder-led content i) memes/trend rides j) long-form YouTube k) email/newsletter l) thumbnails m) captions/hashtags only.
20. Volume per week you can actually review and post (be honest — e.g. 5 shorts, 3 carousels, 4 ads).
21. Who is on camera? a) AI avatars only b) founder c) real creators/customers d) no faces — product only.

### F. Brand look & voice
22. Voice in 3 words, plus one brand that sounds like you and one that never should.
23. Visual identity: hex colours, fonts, logo usage rules, photography style (link a mood board or 3 posts you love).
24. Product appearance facts that must never drift: exact colours by part, materials, sizes, packaging, logo yes/no.
25. Settings/aesthetics that fit (e.g. bright bathroom daylight) and ones that never do.
26. Language rules: accent (for voice), spelling (AU/US), emoji yes/no, swearing yes/no.

### G. Assets & production
27. Product photos available? (Higgsfield media IDs or files) Any approved avatars/frames already?
28. Higgsfield plan (Starter/Plus/Ultra) and a weekly credit budget you're comfortable with.
29. Any music/sound rules (trending sounds OK? licensed only?).

### H. Workflow & approvals
30. How should approvals work? a) approve every generation b) approve the brief, then generate the batch c) auto-generate drafts for approved formats only (later, once trusted).
31. Where do finished files go and who posts them?
32. Anything else the agent should always or never do?

## Profile file shape (`/mnt/memory/projects/<slug>/profile.md`)

```
# <Project> — profile (updated <date>)
## Basics | ## Audience | ## Positioning & proof | ## Never say | ## Goals & baseline
## Content mix & weekly volume | ## Voice & look | ## Product truth (never drift) | ## Assets (media IDs)
## Approvals & workflow | ## Open questions
```

Keep it under ~6 kB. Put competitors in `watchlist.md` (see `radar.md`), not here.
