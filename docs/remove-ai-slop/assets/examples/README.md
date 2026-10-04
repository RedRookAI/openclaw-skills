# Remove AI slop: before and after

Approved marketing examples, tested 2026-10-04. The input is deliberately flawed copy about a fictional product. Both models used the same released editing instructions. Outputs are unchanged.

## Before

> In today's fast-paced digital landscape, managing your downloads can feel like navigating a labyrinth. Meet FolderSweep—a seamless, game-changing solution designed to elevate your workflow.
> 
> FolderSweep watches one folder. FolderSweep groups files by type. FolderSweep shows a preview before moving anything. It works on Linux and macOS – and you can undo the last move. This isn't just about organizing files—it's about unlocking your potential. Your downloads folder called. It wants its dignity back.
> 
> Why does this matter? Here's the kicker: you stay in control—every step of the journey. No clutter. No chaos. Just clarity. The preview reflects our unwavering commitment to transparency, empowering you to navigate your files with confidence.
> 
> It's worth noting that you decide when to move the files—nothing moves until you confirm. Preview first. Move when ready. At the end of the day, FolderSweep is more than a tool—it's your partner in productivity. Try it today.

## GPT-6.1-Sol

> FolderSweep helps organize your downloads by watching one folder and grouping files by type. It works on Linux and macOS.
> 
> You can preview the changes before moving anything. Nothing moves until you confirm, and you can undo the last move.
> 
> Preview first. Move when ready. Try FolderSweep today.

## Claude Sonnet 5.5

> FolderSweep keeps your downloads folder tidy without moving anything behind your back.
> 
> It watches one folder and groups files by type. Before it moves anything, it shows a preview, and nothing moves until you confirm. If you change your mind, you can undo the last move. It runs on Linux and macOS.
> 
> Preview first. Move when ready.
> 
> Try FolderSweep today.

Both edits remove all five em dashes and the en dash, along with canned humor, inflated claims, negation framing, and repetitive phrasing. Both keep "Preview first. Move when ready."

Copy the plain text from [before.txt](before.txt), [gpt-after.txt](gpt-after.txt), or [claude-after.txt](claude-after.txt). Use these for side-by-side cards or social posts. Label the outputs with their model names.

[GPT request and response](../../benchmark/marketing-demo/gpt-record.json). [Claude request and response](../../benchmark/marketing-demo/claude-record.json).
