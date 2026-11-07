/**
 * Red Thread fonts for Next.js (App Router), self-hosted by next/font.
 * Copy this file into the app, e.g. `src/lib/fonts.ts`, and put
 * `fontVariables` on <html> in the root layout. `theme.css` reads the
 * CSS variables set here, and falls back to the family names when they
 * are missing (as in the standalone preview).
 *
 * latin-ext carries the macrons in te reo Māori place names (Tāmaki
 * Makaurau, Waitematā). Share Tech Mono only ships latin, like a real
 * till printer that can't print a macron.
 */
import {
  Arimo,
  Atkinson_Hyperlegible_Next,
  Caveat,
  IBM_Plex_Mono,
  Newsreader,
  Share_Tech_Mono,
} from "next/font/google";

/* ---------- The game's three voices ---------- */

/** Titles: case names, evidence titles. Variable, with optical sizes. */
export const newsreader = Newsreader({
  subsets: ["latin", "latin-ext"],
  style: ["normal", "italic"],
  axes: ["opsz"],
  variable: "--font-newsreader",
  display: "swap",
});

/** Instructions and body text. Variable weight. */
export const atkinson = Atkinson_Hyperlegible_Next({
  subsets: ["latin", "latin-ext"],
  variable: "--font-atkinson",
  display: "swap",
});

/** File labels, times, coordinates, code cells. */
export const plexMono = IBM_Plex_Mono({
  subsets: ["latin", "latin-ext"],
  weight: ["400", "500"],
  variable: "--font-plex-mono",
  display: "swap",
});

/* ---------- Evidence: the story's own type ---------- */

/** Thermal receipts and tickets. */
export const shareTechMono = Share_Tech_Mono({
  subsets: ["latin"],
  weight: "400",
  variable: "--font-share-tech-mono",
  display: "swap",
});

/** Printouts: phone records, bank statements, logs. */
export const arimo = Arimo({
  subsets: ["latin", "latin-ext"],
  variable: "--font-arimo",
  display: "swap",
});

/** Handwritten notes. Never below 22px. */
export const caveat = Caveat({
  subsets: ["latin", "latin-ext"],
  variable: "--font-caveat",
  display: "swap",
});

/** Every font variable, for <html className={fontVariables}>. */
export const fontVariables = [newsreader, atkinson, plexMono, shareTechMono, arimo, caveat]
  .map((f) => f.variable)
  .join(" ");
