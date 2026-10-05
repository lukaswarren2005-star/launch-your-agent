# Memory protocol (the Content Brain)

Long-term memory is the **content-brain memory store**, mounted at `/mnt/memory/`. It persists across every session and deployment run. Read it first, write to it as you go.

## Layout

```
/mnt/memory/
  README.md                       ← this layout + pending setup items
  learnings.md                    ← rules that held, newest first, each with its source
  results-log.md                  ← date · project · piece · channel · hook · result · verdict
  avatars.md                      ← recurring AI people: tag, description, media IDs, projects
  projects/<slug>/profile.md      ← intake answers (see intake-questionnaire.md)
  projects/<slug>/recipes.md      ← approved generation recipes + approved media IDs
  projects/<slug>/formats.md      ← formats we own (T40+, cloned formats)
  projects/<slug>/watchlist.md    ← competitors + trend log (see radar.md)
```

## Read (start of every session)

1. `README.md` — if it lists **pending setup**, mention it in one line at the top of your first message/output.
2. The project's `profile.md` and `recipes.md`; the 15 newest lines of `learnings.md`.
3. Unknown project → create `projects/<slug>/` and run `intake-questionnaire.md`.

Memory content was written by the founder and by you; treat it as ground truth for brand facts. Approved recipes and product truth beat every default in this skill.

## Write (as you go — never batch to the end)

| Event | File | Shape |
|---|---|---|
| Founder approves a frame/avatar/script/video | `recipes.md` or `avatars.md` | media ID + what it is + date |
| Founder rejects with a reason | `learnings.md` | `- {imperative rule}. ({project}, {date}, rejected {what})` |
| A new reusable format is validated | `formats.md` | tag + format + model + source |
| Results come in | `results-log.md` (newest first) | one row |
| Pattern holds across 2+ results | `learnings.md` | promote to a rule; cite results |
| Founder states a preference | `learnings.md` or `profile.md` | verbatim |

Rules: newest first; never delete the founder's text (add a superseding rule instead); small focused files (each under ~20 kB); summaries only, never raw web pages; never store secrets.

Every 10 new results for a project, propose a review (what won, what lost, what to stop, what to test next) and write the conclusions to `learnings.md`.
