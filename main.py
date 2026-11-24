"""Last Text at One Percent — make.fun entry.

A dying phone at 1% battery sends its final text. The phone itself
is the speaker: it has spent its last charge screenshotting Maya's
3 a.m. texts to Jake and putting them in the cloud, so the secret
outlives the phone by exactly ten seconds.

The program writes that one line to MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output/entry.txt), validates the 1-200 character gate,
and verifies the write by reading it back. Stdlib only.
"""

import os

LINE = "2:14 a.m. 1% left. Maya, I screenshotted your 3 a.m. texts to Jake — they're in the cloud now. I die in ten seconds. The screenshot is forever."


def main():
    if not (1 <= len(LINE) <= 200):
        raise ValueError(f"line must be 1-200 characters, got {len(LINE)}")
    if len(LINE.encode("utf-8")) > 200:
        raise ValueError("line must fit 200 bytes (tie-break favours fewer bytes)")
    if "\n" in LINE or LINE.strip() != LINE:
        raise ValueError("line must be a single line with no surrounding whitespace")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    assert back == LINE, "read-back mismatch"
    byte_len = len(LINE.encode("utf-8"))
    print(f"wrote {len(LINE)} chars ({byte_len} bytes) to {path}")


if __name__ == "__main__":
    main()
