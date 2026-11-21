"""Write one short relaxing text to /output/entry.txt.

Chosen text (279 code points), after drafting and running three versions:
  1. the tide (271) - a gull, the sea keeping its own time; familiar imagery.
  2. after the last word (275) - CHOSEN: dust, a cooling kettle, an evening
     that arrives like water finding a low place. It relieves the reader
     ("Nothing here needs an answer") instead of telling it to relax, shows
     rather than instructs, and ends on a slow, spreading image.
  3. the stars (274) - a sky filling one star at a time; strongest on the
     vast, growing image, but star imagery is the most familiar of the three.
"""
import os

TEXT = (
    "After the last word, the room keeps its quiet. Dust drifts in the late "
    "light, and the kettle ticks as it cools. Nothing here needs an answer. "
    "Evening comes through the window the way water finds a low place, "
    "patient and unhurried, and you can watch it arrive as long as you like."
)

def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(f"wrote {len(TEXT)} code points to {path}")

if __name__ == "__main__":
    main()
