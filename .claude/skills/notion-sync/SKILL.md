---
name: notion-sync
description: Sync Red Thread documents between this repo and the founder's Notion pages — pull new edits from Notion into the repo, or push repo changes back to Notion. Use when asked to sync, import, export, update Notion, or check whether Notion and the repo differ.
---

# Notion sync

The repo is the source of truth (decision 2026-11-06), but the founder may still edit in Notion. Page IDs are in `context/overview.md`.

| Notion page | Repo file |
| --- | --- |
| Red Thread (parent) | `context/overview.md` |
| Business Model | `context/business-model.md` |
| GTM Strategy | `context/gtm.md` |
| Game Design | `context/game-design.md` |
| Case 001.2 | `cases/001-dusk-painting/case.md` + `solution.md` |

## Pull (Notion → repo)
1. Search Notion for "Red Thread" to catch new sub-pages; fetch each mapped page.
2. Compare `page_last_edited_at` with the repo file's last commit date (`git log -1 --format=%cI -- <file>`). Only process pages edited since.
3. Show the founder a short diff summary per file **before** writing. Preserve repo-only additions (e.g. `[decide]` tags, actual hours). Founder notes in Notion (inline comments, strikethroughs) become 🔧 notes or decisions.
4. New Notion case pages → new `cases/NNN-slug/` folder, splitting spoilers into `solution.md`.

## Push (repo → Notion)
1. Confirm with the founder which pages to update — Notion edits are visible to anyone the pages are shared with.
2. Update the mapped page's content; keep solution content inside a red callout headed "Solution (spoilers)".
3. Never delete Notion pages; mark superseded ones in their title instead.

Commit after a pull with message `sync: pull <pages> from Notion`.
