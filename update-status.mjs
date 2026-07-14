// Rotates the "status" line in README.md.
// Runs on a schedule via .github/workflows/update-status.yml, no server needed.

import { readFileSync, writeFileSync } from "node:fs";

const README_PATH = new URL("../README.md", import.meta.url);
const POOL_PATH = new URL("./status-pool.json", import.meta.url);

const pool = JSON.parse(readFileSync(POOL_PATH, "utf8"));

// Deterministic pick based on day of year, so it changes once a day
// instead of jumping around every time the workflow happens to run.
const dayOfYear = Math.floor(
  (Date.now() - new Date(new Date().getFullYear(), 0, 0)) / 86_400_000
);
const status = pool[dayOfYear % pool.length];

const readme = readFileSync(README_PATH, "utf8");

const START = "<!--STATUS:START-->";
const END = "<!--STATUS:END-->";
const startIdx = readme.indexOf(START);
const endIdx = readme.indexOf(END);

if (startIdx === -1 || endIdx === -1) {
  console.error(`Could not find ${START} / ${END} markers in README.md`);
  process.exit(1);
}

const updated =
  readme.slice(0, startIdx + START.length) +
  status +
  readme.slice(endIdx);

if (updated !== readme) {
  writeFileSync(README_PATH, updated);
  console.log(`status updated -> "${status}"`);
} else {
  console.log("status unchanged, nothing to commit");
}
