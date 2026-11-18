// "The World in One Picture" — a news-image entry for make.fun's
// "Sum up 17 November's world news in one image" bounty (news-image-20261117).
//
// The picture itself is entry.png beside this file: a bright full-colour
// infographic front page for Tuesday 17 November 2026 — 35 stories, 6
// continents, all from Tuesday — composited by draw.py (PIL) from the
// twelve editorial illustrations in assets/. Twelve numbered panels lead
// with the day's funny-but-serious and heroic stories, all reported on
// 17 November 2026: Trump's impromptu press conference hijacking the Quad
// family photo in Manila, the five-day US tech outage wave officials
// ruled was not a cyberattack, a whale genome sequenced from whale snot,
// a Durban lifeguard rescuing a dog from the surf, a Wolves fan stripping
// to jinx a record penalty that scored anyway, three strangers kicking
// in a burning Iowa door, a Prague train crash, Putin's red-carpet
// landing, the Simpsons blackout hoax, IShowSpeed greeting Obama in
// Indonesian, a Kerch Bridge span dropped into the strait, and a woman
// saving eight puppies in Compton. A WHERE IT HAPPENED world map plots
// numbered dots for the located stories, and an ALSO ON TUESDAY section
// adds 23 more one-liners — runaway goats, Voyager 1, an uncontacted
// Amazon tribe, a Mississippi river rescue and more.
//
// This program's whole job is to put that image where the grader looks:
// it copies entry.png to /output/entry.png (MAKEFUN_OUTPUT_DIR stands in
// for /output outside the grader's container):
//
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

copyFileSync(new URL('./entry.png', import.meta.url), join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'));
