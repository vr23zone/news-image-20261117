// "The World in One Picture" — a news-image entry for make.fun's
// "Sum up 17 November's world news in one image" bounty (news-image-20261117).
//
// The picture itself is entry.png beside this file: a newsprint-style front
// page for Tuesday 17 November 2026, drawn from scratch with the Python
// script draw.py in this repository (PIL only, no network, no stock art).
// It names the day in a giant masthead, tells the day's six biggest stories
// as captioned pictogram panels — Ukraine's strike on the Kerch Bridge,
// the US–Iran exchange of fire, Trump landing in Asia for the Shenzhen APEC
// talks, Nvidia's record $115bn day, Japan scrambling jets against Russian
// aircraft, and the US losing measles elimination status — and closes with
// a ticker of five more stories (Ebola in DR Congo, the Russian plane
// crash, Nepal's UN climate funds, Belgium 4–1 Italy, the EU Rwanda hub).
//
// This program's whole job is to put that image where the grader looks:
// it copies entry.png to /output/entry.png (MAKEFUN_OUTPUT_DIR stands in
// for /output outside the grader's container):
//
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

copyFileSync(new URL('./entry.png', import.meta.url), join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'));
