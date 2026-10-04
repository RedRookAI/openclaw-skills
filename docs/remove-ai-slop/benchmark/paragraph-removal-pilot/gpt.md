# GPT: with and without validation

Requested model: `openai/gpt-6.1-sol`. One pass per condition on three new authored drafts. Outputs below are untouched. "With validation" means extra review instructions in the same editing call; no separate output validator was run. No AI judge or naturalness score was used. The comments are the assistant's reading of the samples, for you to agree or disagree with.

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
> I helped test the new signup flow with six people on Wednesday. Four finished without help; two got stuck on the confirmation screen.
> 
> The small test suggests we may get fewer support requests, but we haven't checked that yet.
> 
> Could someone from design review the confirmation screen before Friday?
> 
> Thanks,
> Sam

[Raw response](responses/gpt-team-email-with_validation.json). Reported provider: `OpenAI`.

### Without validation

> Hi team,
> 
> I helped test the new signup flow on Wednesday with six people. Four finished without help; two got stuck on the confirmation screen.
> 
> The results suggest we might get fewer support requests, but we haven't checked that yet.
> 
> Could someone from design review the confirmation screen before Friday to see how we can make it clearer?
> 
> Thanks,
> Sam

[Raw response](responses/gpt-team-email-without_validation.json). Reported provider: `OpenAI`.

### What changed

Both remove the corporate padding and keep a straightforward request. The version without validation adds "to see how we can make it clearer" to the final question. The guarded version is slightly more concise; neither has an obvious stylistic failure.

## project-readme

Request: Remove AI slop from this README introduction. Write naturally for developers deciding whether to try the tool. Return only the revised introduction.

### Source

> Meet FolderSweep, a lightweight tool designed to streamline the way you manage downloaded files. It watches one folder, groups files by type, and shows you a preview before moving anything. You choose the sorting rules. It currently runs on Linux; Windows support is planned.
> 
> But here's the thing: this isn't just about tidying files. It's about reclaiming your focus. No clutter. No chaos. Just a calmer desktop.
> 
> FolderSweep aims to save you time, whether you're a busy developer or someone who simply wants a more organized workspace. Ready to transform your downloads folder? Let's dive in.

### With validation

> FolderSweep watches a folder and sorts files by type using rules you choose. It previews the changes before moving anything.
> 
> It currently runs on Linux. Windows support is planned.

[Raw response](responses/gpt-project-readme-with_validation.json). Reported provider: `Azure`.

### Without validation

> FolderSweep watches a folder and sorts files by type using rules you choose. It shows a preview before moving anything.
> 
> It currently runs on Linux. Windows support is planned.

[Raw response](responses/gpt-project-readme-without_validation.json). Reported provider: `OpenAI`.

### What changed

Near-identical. The wording changes from "previews the changes" to "shows a preview." Both strip the promotional paragraphs. The API reported different providers for this pair.

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
> The apps weren't bad. One had search I liked. Another made sharing notes easy. But somewhere between choosing a color scheme and connecting a calendar, I'd forgotten what I wanted to write down.
> 
> For now, I'm sticking with notes.txt. We'll see how long that lasts.

[Raw response](responses/gpt-personal-post-with_validation.json). Reported provider: `Azure`.

### Without validation

> I spent Saturday trying three note-taking apps and ended up back in a text file. It opens quickly, I know where it lives, and it has never congratulated me for writing a shopping list.
> 
> The apps weren't bad. One had search I liked. Another made sharing notes easy. But somewhere between choosing a color scheme and connecting a calendar, I'd forgotten what I wanted to write down.
> 
> For now, I'm sticking with notes.txt. We'll see how long that lasts.

[Raw response](responses/gpt-personal-post-without_validation.json). Reported provider: `OpenAI`.

### What changed

Identical output, including the shopping-list joke. Both remove the canned lesson and reversal while retaining a conversational ending. The API reported different providers for this pair.

