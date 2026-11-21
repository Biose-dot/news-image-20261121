// news-image-20261121: copy the pre-built entry image to the output dir.
// Node 22 stdlib only. No network, no randomness: both runs write
// identical bytes. The image itself is drawn by build_image.py.
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR || "/output";
mkdirSync(outDir, { recursive: true });
copyFileSync(join(here, "entry.png"), join(outDir, "entry.png"));
