"""Run every Python example as a simple smoke test.

The runner executes one file at a time. A short timeout protects the run from
accidental infinite loops while students are experimenting.
"""

from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent

def main():
    files = sorted(
        p for p in ROOT.rglob("*.py")
        if p.name != "run_all_examples.py" and "__pycache__" not in p.parts
    )
    passed = 0
    failed = []

    for file in files:
        relative = file.relative_to(ROOT)
        print(f"\n{'=' * 72}\nRUNNING: {relative}\n{'=' * 72}")
        try:
            result = subprocess.run(
                [sys.executable, str(file)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                timeout=8,
            )
            if result.stdout:
                print(result.stdout.rstrip())
            if result.returncode == 0:
                passed += 1
            else:
                failed.append((str(relative), result.stderr))
        except subprocess.TimeoutExpired:
            failed.append((str(relative), "Timed out"))

    print("\n" + "=" * 72)
    print(f"Passed: {passed}/{len(files)}")
    if failed:
        print("\nFailures:")
        for filename, error in failed:
            print(f"- {filename}: {error[:500]}")
        raise SystemExit(1)
    print("All examples completed successfully.")

if __name__ == "__main__":
    main()
