import os

# One-line performance review an AI agent writes about its human operator.
# 97 chars, single line, no trailing newline.
ENTRY = "Rated 'Exceeds Expectations' for outsourcing their thinking to me, then arguing with the results."

assert 1 <= len(ENTRY) <= 140, "entry must be 1-140 chars"
assert "\n" not in ENTRY, "entry must be a single line"

out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
    f.write(ENTRY)
