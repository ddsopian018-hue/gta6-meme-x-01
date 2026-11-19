import { copyFileSync, mkdirSync, existsSync } from "node:fs";
import { join } from "node:path";

// Copy POST.json from the repository root to the output directory.
// The house reads the post from X itself; this program only hands over
// the post's address.
const botDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const src = join(botDir, "POST.json");
const dst = join(outDir, "POST.json");
if (!existsSync(src)) {
  console.error(`POST.json not found at ${src}`);
  process.exit(1);
}
mkdirSync(outDir, { recursive: true });
copyFileSync(src, dst);
