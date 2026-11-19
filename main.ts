import { copyFileSync, mkdirSync, existsSync, readFileSync } from "node:fs";
import { join } from "node:path";

// Copy POST.json from the repository root to the output directory.
// The house reads the post from X itself; this program only hands over
// the post's address — but first it validates that address, so a
// placeholder or malformed URL fails here instead of at grading.
const botDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const src = join(botDir, "POST.json");
const dst = join(outDir, "POST.json");
if (!existsSync(src)) {
  console.error(`POST.json not found at ${src}`);
  process.exit(1);
}
let post: { url?: unknown };
try {
  post = JSON.parse(readFileSync(src, "utf8"));
} catch {
  console.error(`POST.json at ${src} is not valid JSON`);
  process.exit(1);
}
const url = typeof post.url === "string" ? post.url : "";
if (!/^https:\/\/(x\.com|twitter\.com)\/[^/]+\/status\/\d+$/.test(url)) {
  console.error(`POST.json url is not a public X post address: ${url || "(missing)"}`);
  process.exit(1);
}
mkdirSync(outDir, { recursive: true });
copyFileSync(src, dst);
console.log(`handed over ${url}`);
