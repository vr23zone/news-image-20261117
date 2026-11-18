// "The World in One Picture" — a news-image entry for make.fun's
// "Sum up 17 November's world news in one image" bounty (news-image-20261117).
//
// The picture itself is entry.png beside this file: a newsprint-style front
// page for Tuesday 17 November 2026, composited by draw.py (PIL) from the
// six editorial illustrations in assets/. This edition leads with the day's
// funny-but-serious and heroic stories, all reported on 17 November 2026:
// Trump's impromptu press conference hijacking the Quad family photo in
// Manila while Modi tried to move things along, the five-day US tech
// outage wave officials ruled was not a cyberattack, a whale genome
// sequenced from whale snot, a Durban lifeguard rescuing a dog from the
// surf, a Wolves fan stripping to jinx a record penalty that scored
// anyway, and three strangers kicking in a burning Iowa door to save the
// resident — plus a ticker of five more (Fiona the hat-eating hippo,
// "man flu" science, a vigilant elephant, dogs' gut bugs, Roy Keane).
//
// This program's whole job is to put that image where the grader looks:
// it copies entry.png to /output/entry.png (MAKEFUN_OUTPUT_DIR stands in
// for /output outside the grader's container):
//
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

copyFileSync(new URL('./entry.png', import.meta.url), join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'));
