from pathlib import Path
import shutil

lab_dir = Path("assets/NOIR_GRIT_SONGS")

for lab_file in lab_dir.glob("*.lab"):

    # Create backup filename:
    # EX - GROWLS 1.lab -> EX - GROWLS 1.original
    backup_file = lab_file.with_suffix(".original")

    # Save original contents
    shutil.copy(lab_file, backup_file)

    # Read original .lab
    with open(lab_file, "r", encoding="utf8") as f:
        lines = f.readlines()

    phonemes = []

    for line in lines:
        parts = line.strip().split()

        # Expected format:
        # start end phoneme
        if len(parts) != 3:
            continue

        phoneme = parts[2]

        # Remove silence/breath tokens
        if phoneme in ["SP", "AP", "<PAD>"]:
            continue

        phonemes.append(phoneme)

    # Overwrite .lab with parsed phoneme sequence
    with open(lab_file, "w", encoding="utf8") as f:
        f.write(" ".join(phonemes))

    print(f"Parsed lab saved: {lab_file.name}")
    print(f"Original backup saved: {backup_file.name}")