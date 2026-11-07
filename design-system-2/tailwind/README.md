# Red Thread in Next.js, Tailwind CSS v4 and shadcn/ui

This folder holds the design system for the app stack: **Next.js (App Router), Tailwind CSS v4 and shadcn/ui**. It was checked against Next 16.4, Tailwind 4.3 and the shadcn CLI 4.x.

| File | What it is |
| --- | --- |
| `theme.css` | Every token as Tailwind theme variables and utilities, plus the shadcn/ui colour roles, for both themes. **Generated** from `../tokens.json` by `python3 design-system-2/scripts/build_preview.py`. Don't edit it by hand. |
| `fonts.ts` | The six fonts, self-hosted with `next/font`: Newsreader, Atkinson Hyperlegible Next and IBM Plex Mono for the game, then Share Tech Mono, Arimo and Caveat for evidence. |

## Set up

1. **Copy both files into the app.** Rerun the build after any token change and copy `theme.css` again.
   - `theme.css` goes to `src/app/red-thread-theme.css`.
   - `fonts.ts` goes to `src/lib/fonts.ts`.
2. **Run `npx shadcn@latest init`** and accept CSS variables. It writes colour variables into `globals.css`.
3. **Replace `globals.css`** with the lines below. Delete everything shadcn generated after its imports: the `@custom-variant dark` line, the `:root` and `.dark` blocks, its `@theme inline` block and its `@layer base` block. `theme.css` provides all of them, in Red Thread's colours.

   ```css
   @import "tailwindcss";
   @import "tw-animate-css";
   @import "./red-thread-theme.css";
   ```

4. **Fonts and theme in the root layout.** Themes switch on `data-theme`, not a `.dark` class. Night is the default and Paper is for daylight. Use [next-themes](https://github.com/pacocoursey/next-themes) for the switch. Wrap its `ThemeProvider` in a file marked `"use client"` if your setup needs it.

   ```tsx
   // src/app/layout.tsx
   import { ThemeProvider } from "next-themes";
   import { fontVariables } from "@/lib/fonts";
   import "./globals.css";

   export default function RootLayout({ children }: { children: React.ReactNode }) {
     return (
       <html lang="en-NZ" className={fontVariables} data-theme="night" suppressHydrationWarning>
         <body>
           <ThemeProvider attribute="data-theme" themes={["night", "paper"]} defaultTheme="night" enableSystem={false}>
             {children}
           </ThemeProvider>
         </body>
       </html>
     );
   }
   ```

   shadcn components carry `dark:` classes. In `theme.css`, `dark:` means the Night theme, so those classes behave as their authors intended. Use `paper:` for anything specific to daylight.

## Five edits to the shadcn components

These bring the stock components in line with the brand book. Make them once, after `shadcn add`, in `src/components/ui/`.

1. **Button sizes in `button.tsx`.** Change the default size from `h-9` to `h-11`, so buttons are 44px for cold fingers. Make `sm` `h-9` at the smallest.
2. **Destructive buttons in `button.tsx`.** In the `destructive` variant, change `text-white` to `text-background`. `destructive` maps to `ink`, not red, because the thread is the only red. Never use it for a wrong answer: a wrong answer is said in words ("That doesn't hold. Look at the timestamp again.").
3. **Inputs in `input.tsx` and `select.tsx`.** Change `h-9` to `h-11`, for the same 44px.
4. **Game panels.** Add `surface-note` to a `Card`, `Dialog` or `Sheet` when the game is talking: off-white, rounded, flat. Leave dashboards and menus on the default `bg-card`.
5. **Don't put evidence in shadcn components.** Receipts, statements, screenshots and notes are objects from the story: square, white and shadowed. Use the Red Thread evidence components from `../components/`, or `surface-evidence` until they're ported to TSX.

Some things are already handled in `theme.css`:
- **Radii.** shadcn's radius scale matches the system: `rounded-sm` is the tag radius (6px), `rounded-md` the control radius (10px) for buttons and inputs, and `rounded-lg` and `rounded-xl` the note radius (16px) for cards and dialogs.
- **Flat game layer.** `shadow-xs` and `shadow-sm` are transparent, so shadcn cards and inputs stay flat. Larger shadows remain for menus and dialogs, which float above the page.
- **Browser defaults.** Text selection, the text cursor, the focus ring and `color-scheme` are themed.

## Classes you'll use

| Need | Classes |
| --- | --- |
| Case title | `type-display-l` (or `font-serif text-display-l`) |
| Evidence title | `type-heading`; one phrase of emphasis in `type-heading-italic` |
| Instruction heading / body / caption | `type-title` · `type-body` · `type-small` |
| File label ("CASE 001 · OPEN") | `type-label text-brass`. It's uppercase already. Use sparingly: these labels are the quickest way to look templated |
| Times, coordinates, transcripts | `type-evidence` (tabular figures) |
| Game note | `surface-note p-6` |
| Evidence object | `surface-evidence` (square, white, `shadow-object`) |
| Evidence with a torn edge or other cut-out shape | `drop-object` (a filter shadow that follows the shape) |
| Manila evidence tag | `surface-manila` |
| Thermal print / printout / handwriting | `type-receipt` · `type-doc-body` · `type-hand text-evidence-pen` |
| Every colour token | `bg-ground`, `text-ink`, `text-ink-muted`, `bg-note`, `text-note-ink`, `bg-thread`, `text-thread-text`, `bg-manila`, `text-evidence-ink`, `border-line` … |
| shadcn roles | `bg-background`, `text-foreground`, `bg-primary` (the thread), `text-muted-foreground`, `border-border`, `ring-ring` … |
| Radii by meaning | `rounded-evidence` (0) · `rounded-tag` · `rounded-control` · `rounded-note` · `rounded-device` · `rounded-pill` (pins only) |

Spacing needs nothing extra. The system's 4px grid is Tailwind's default spacing scale, so `p-4` is 16px, the same as `space-4`.

## How shadcn's colour roles map

| shadcn role | Red Thread token |
| --- | --- |
| background / foreground | `ground` / `ink` |
| card · muted | `surface` |
| popover · secondary · accent | `surface-raised` |
| primary / primary-foreground | `thread` / `on-thread` (one primary button per screen) |
| muted-foreground | `ink-muted` |
| destructive | `ink` (see edit 2) |
| border / input / ring | `line` / `line-strong` / `focus` |
| chart-1 to chart-5 | `thread`, `brass`, `solved`, `ink-muted`, `manila` |
