#!/usr/bin/env python3
from glob import glob
from collections import defaultdict
import subprocess
import sys


def main():
    keymaps = defaultdict(set)

    for filename in glob("keyboards/**/vial.json", recursive=True):
        filename = filename[10:-10]
        keyboard, keymap = filename.split("/keymaps/")
        keymaps[keyboard].add("default")
        keymaps[keyboard].add(keymap)

    failed = False
    for keyboard, keymaps in keymaps.items():
        for keymap in keymaps:
            sys.stdout.write(f"==> Compiling {keyboard}:{keymap}\n")
            sys.stdout.flush()
            if subprocess.call(["make", f"{keyboard}:{keymap}", "-j4"]) != 0:
                failed = True

    if failed:
        sys.exit(1)


if __name__ == "__main__":
    main()
