"""Make the Judge Smile — entry program.

Writes one line (at most 200 characters) about a small good thing that
happened today to /output/entry.txt. Pure standard library.
"""

LINE = (
    "Today the auto driver turned the meter off at the last signal and said "
    "the ride was free \u2014 his daughter had passed her exam this morning."
)


def main() -> None:
    line = LINE
    if not line or not line.strip():
        raise ValueError("entry line must not be empty")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if len(line) > 200:
        raise ValueError(f"entry is {len(line)} characters, over the 200 limit")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)


if __name__ == "__main__":
    main()
