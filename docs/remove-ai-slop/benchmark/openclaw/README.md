# OpenClaw test

Tested 2026-10-04 on Seven's installed OpenClaw 2026.9.7 (c074824), using Claude Sonnet 5.5 through OpenRouter. Each turn used isolated test state. The running gateway and active conversations were untouched.

OpenClaw discovered and read the installed skill. Eight authored cases ran once each, on one model: three with v5, two with v6, and three with the released v7. The v7 turns loaded the exact released SKILL.md, including its guidance on natural sentence variety.

The marketing tests kept "Write it. Save it. Find it." while removing inflated wording. The v7 cases cover marketing, an explanation, and a personal update. These are separate cases, not a matched before/after experiment.

Earlier v5 edits removed targeted phrasing and left a clear note unchanged. One added a promotional closing; another interpreted "No limits" as "no row limit." The cards show labeled excerpts from the v5 marketing edit. Full outputs follow.

One setup attempt failed before calling a provider. 18 provider responses cost $0.260061300. [Inputs, outputs, file reads, and receipts](results.json). [Frozen v5 skill](tested-v5-skill.json).

## phrase-guide

Revision: lean-editor-v5

Before:

> We launched CSV export today—a game-changing step for our users. This isn't just about downloading data; it's about unlocking insights. At its core, the feature lets you export filtered rows. No friction. No limits. Just results. Click Export above the table to save a CSV.

After:

> We launched CSV export today. You can now export filtered rows with no row limit. Click Export above the table to save a CSV.

## marketing-tagline

Revision: genre-aware-v6

Before:

> Meet PocketNote, a lightweight tool designed to streamline the way you capture ideas. It saves notes as plain text and works offline. Write it. Save it. Find it. Whether you're jotting down a grocery list or mapping out your next big idea, PocketNote empowers you to unlock your creativity. Download the Linux app today.

After:

> Meet PocketNote, a lightweight note-taking app. It saves notes as plain text and works offline. Write it. Save it. Find it. Whether you're jotting down a grocery list or mapping out your next big idea, PocketNote keeps it all in one place. Download the Linux app today.

## email-cadence

Revision: genre-aware-v6

Before:

> Hi team, I wanted to take a moment to share an update. The import failed at 10:12. I restarted the worker and the retry finished at 10:18. No drama. No doubt. Just progress. At the end of the day, this underscores our commitment to seamless operations. Please check the logs before the next run. Thanks, Jo

After:

> Hi team,
> 
> The import failed at 10:12. I restarted the worker and the retry finished at 10:18. Please check the logs before the next run.
> 
> Thanks,
> Jo

## marketing

Revision: lean-editor-v5

Before:

> FolderSweep watches one folder—groups files by type—and shows a preview before moving anything.
> 
> This isn't just about sorting files—it's about reclaiming your focus.
> 
> No clutter. No chaos. Just clarity.
> 
> Ready to transform your downloads folder?

After:

> FolderSweep watches one folder, groups files by type, and shows a preview before moving anything.
> 
> Point it at your downloads folder and it will sort the mess without surprises.

## already-clear

Revision: lean-editor-v5

Before:

> The export failed at 09:14. I restarted the worker, and the next export finished at 09:18. Please check the logs before retrying.

After:

> The export failed at 09:14. I restarted the worker, and the next export finished at 09:18. Please check the logs before retrying.

## rhythm-marketing

Revision: natural-rhythm-v7

Before:

> Meet DeskNote, the seamless solution designed to transform how you capture ideas. It saves notes as plain text. It works offline. It searches your notes. Write it. Save it. Find it. Whether you're capturing a fleeting thought or planning your next big project, DeskNote empowers you to unlock your potential. Download the Linux app today.

After:

> Meet DeskNote. It saves your notes as plain text, works offline, and searches everything you've written. Write it. Save it. Find it. Whether you're jotting a passing thought or planning a big project, DeskNote keeps your notes easy to get back to. Download the Linux app today.

## rhythm-explanation

Revision: natural-rhythm-v7

Before:

> The worker reads jobs from the queue. The worker handles one job at a time. The worker retries a failed job twice. The worker writes each failure to the log. The worker moves jobs that still fail to a separate queue. This isn't about hiding errors. It's about making reliability a first-class citizen. The result? A robust foundation for seamless operations.

After:

> The worker reads jobs from the queue and handles them one at a time. If a job fails, the worker retries it twice and writes each failure to the log. Jobs that still fail go to a separate queue.

## rhythm-personal

Revision: natural-rhythm-v7

Before:

> I tried working from the cafe on Tuesday. I liked the change of scene. I liked having lunch nearby. I liked being away from the laundry pile. I got about an hour of work done before the wifi dropped. The barista restarted the router, and I finished my emails while it came back. My coffee was cold by then. A small price to pay for a change of pace, right? It's not about finding the perfect workspace. It's about finding what works for you. For me, home is still easier on days with calls.

After:

> I tried working from the cafe on Tuesday and liked the change of scene. Lunch was nearby, and the laundry pile was not. I got about an hour of work done before the wifi dropped. The barista restarted the router, and I finished my emails while it came back. By then my coffee was cold, but that's a small price for a change of pace. Home is still easier on days with calls.
