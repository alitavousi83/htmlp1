import  sys
import os

def collect_file_stats(filename):
    lines = 0
    words = 0
    chars = 0
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                lines += 1
                words += len(line.split())
                chars += len(line)
        return {
            "filename": filename,
            "lines": lines,
            "words": words,
            "characters": chars,
        }
    except Exception as e:
        print(f"Could not open file: {filename} ({e})")
        return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python stats.py <file1> [file2 ...]")
        return
    for filepath in sys.argv[1:]:
        if not os.path.isfile(filepath):
            print(f"File not found: {filepath}")
            continue
        stats = collect_file_stats(filepath)
        if stats:
            print(f"File: {stats['filename']}")
            print(f"Lines: {stats['lines']}")
            print(f"Words: {stats['words']}")
            print(f"Characters: {stats['characters']}")

if __name__ == "__main__":
    main()
