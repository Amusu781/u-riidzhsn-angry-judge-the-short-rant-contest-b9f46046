"""Angry Judge: The Short Rant Contest entry. Writes one rant to OUTPUT_DIR/entry.txt."""
import os
import shutil

ENTRY = (
    "My printer refuses to print black because it is low on cyan. "
    "I am printing a boarding pass. It is black and white. "
    "There is no cyan in it. There has never been cyan in anything I own. "
    "I bought the cyan anyway. $34. It celebrated by printing a test page "
    "of pure cyan, which is now on my fridge like a hostage photo. "
    "The flight left without me. The printer is doing great."
)


def main():
    assert 1 <= len(ENTRY) <= 400 and ENTRY.strip(), len(ENTRY)
    out = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    for name in os.listdir(out):
        p = os.path.join(out, name)
        if os.path.isdir(p) and not os.path.islink(p):
            shutil.rmtree(p)
        else:
            os.remove(p)
    with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
