#!/usr/bin/env python3
"""news-image-20261119 entry: copy the built front page to /output/entry.png.

The image was built during the build session (three original diffusion
hero panels composited with PIL; every word, number, map and pictogram
drawn in code) and ships in this repository as entry.png. This program
only copies it, so the two grader runs are byte-identical. After copying,
the output is verified against the source (byte size and SHA-256); any
mismatch aborts with a non-zero exit and a clear message.
Standard library only; no network.
"""
import hashlib
import os
import shutil
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    sys.exit(1)


def main():
    source = HERE / "entry.png"
    if not source.is_file():
        fail(f"source image missing: {source}")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    if target.stat().st_size != source.stat().st_size:
        fail(
            f"copied entry size mismatch: source "
            f"{source.stat().st_size} bytes, output "
            f"{target.stat().st_size} bytes"
        )
    source_hash = sha256(source)
    target_hash = sha256(target)
    if target_hash != source_hash:
        fail(
            f"copied entry hash mismatch: source sha256 {source_hash}, "
            f"output sha256 {target_hash}"
        )


if __name__ == "__main__":
    main()
