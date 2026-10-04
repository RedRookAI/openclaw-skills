# Claude: with and without validation

Requested model: `anthropic/claude-sonnet-5.5`. One pass per condition on three new authored drafts. Outputs below are untouched. "With validation" means extra review instructions in the same editing call; no separate output validator was run. No AI judge or naturalness score was used. The comments are the assistant's reading of the samples, for you to agree or disagree with.

[Exact prompt difference](prompt-diff.txt). [Full experiment plan](plan.json). [Side-by-side view](comparison.html).

## team-email

Request: Remove AI slop from this email. Make it sound like a colleague writing to the team. Return only the edited email.

### Source

> Hi team,
> 
> I wanted to take a moment to share an update on the new signup flow. I helped test it on Wednesday with six people. Four finished without help; two got stuck on the confirmation screen. That's encouraging, but there's still room for improvement.
> 
> This isn't about chasing perfection. It's about creating a seamless experience. The smaller test suggests we may get fewer support requests, though we haven't looked at that yet.
> 
> Could someone from design take a look at the confirmation screen before Friday? At the end of the day, a little clarity goes a long way.
> 
> Thanks,
> Sam

### With validation

> Hi team,
> 
> Here's an update on the new signup flow. I helped test it on Wednesday with six people. Four finished without help, and two got stuck on the confirmation screen.
> 
> The small test suggests we may get fewer support requests, though we haven't looked at that yet.
> 
> Could someone from design look at the confirmation screen before Friday?
> 
> Thanks,
> Sam

[Raw response](responses/claude-team-email-with_validation.json). Reported provider: `Azure`.

### Without validation

> Hi team,
> 
> Here's an update on the new signup flow. I helped test it with six people on Wednesday. Four finished without help, and two got stuck on the confirmation screen.
> 
> The small sample suggests we may get fewer support requests, but we haven't checked that yet.
> 
> Could someone from design look at the confirmation screen before Friday?
> 
> Thanks,
> Sam

[Raw response](responses/claude-team-email-without_validation.json). Reported provider: `Azure`.

### What changed

Near-identical. Word order and "looked" versus "checked" change; both sound like the same colleague writing the update.

## project-readme

Request: Remove AI slop from this README introduction. Write naturally for developers deciding whether to try the tool. Return only the revised introduction.

### Source

> Meet FolderSweep, a lightweight tool designed to streamline the way you manage downloaded files. It watches one folder, groups files by type, and shows you a preview before moving anything. You choose the sorting rules. It currently runs on Linux; Windows support is planned.
> 
> But here's the thing: this isn't just about tidying files. It's about reclaiming your focus. No clutter. No chaos. Just a calmer desktop.
> 
> FolderSweep aims to save you time, whether you're a busy developer or someone who simply wants a more organized workspace. Ready to transform your downloads folder? Let's dive in.

### With validation

> FolderSweep watches a folder (typically Downloads), groups files by type, and shows you a preview before moving anything. You write the sorting rules yourself.
> 
> It currently runs on Linux. Windows support is planned.

[Raw response](responses/claude-project-readme-with_validation.json). Reported provider: `Azure`.

### Without validation

> FolderSweep is a lightweight tool for sorting your downloads folder. It watches one folder, groups files by type, and shows a preview before moving anything. You choose the sorting rules.
> 
> It currently runs on Linux. Windows support is planned.

[Raw response](responses/claude-project-readme-without_validation.json). Reported provider: `Azure`.

### What changed

The version without validation gives a short explanation of what the tool is and keeps "You choose the sorting rules." The guarded version uses "(typically Downloads)" and "You write the sorting rules yourself." The guard does not produce an obviously more natural introduction.

## personal-post

Request: Remove AI slop from this short personal post. Keep it conversational, with any humor that earns its place. Return only the revised post.

### Source

> I spent Saturday trying three note-taking apps and ended up back in a text file. The file opens quickly, I know where it lives, and it has never congratulated me for writing a shopping list.
> 
> To be clear, the other apps weren't bad. One had search I liked. Another made sharing notes easy. But somewhere between choosing a color scheme and connecting a calendar, I'd forgotten what I wanted to write down.
> 
> The lesson? Sometimes simplicity is the ultimate sophistication. It's not about finding the perfect tool. It's about finding the tool that gets out of your way. For now, mine is notes.txt. We'll see how long that lasts.

### With validation

> I spent Saturday trying three note-taking apps and ended up back in a text file. It opens quickly, I know where it lives, and it has never congratulated me for writing a shopping list.
> 
> The other apps weren't bad. One had search I liked. Another made sharing notes easy. But somewhere between choosing a color scheme and connecting a calendar, I forgot what I'd wanted to write down.
> 
> For now, I'm using notes.txt. We'll see how long that lasts.

[Raw response](responses/claude-personal-post-with_validation.json). Reported provider: `Azure`.

### Without validation

> I spent Saturday trying three note-taking apps and ended up back in a text file. It opens quickly, I know where it lives, and it has never congratulated me for writing a shopping list.
> 
> The other apps weren't bad. One had search I liked. Another made sharing notes easy. But somewhere between choosing a color scheme and connecting a calendar, I forgot what I'd wanted to write down.
> 
> For now, my tool is notes.txt. We'll see how long that lasts.

[Raw response](responses/claude-personal-post-without_validation.json). Reported provider: `Azure`.

### What changed

Almost identical. The only changed sentence is "For now, I'm using notes.txt" versus "For now, my tool is notes.txt." Both retain the joke and remove the stock lesson.

