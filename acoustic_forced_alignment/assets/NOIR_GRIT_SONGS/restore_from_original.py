from pathlib import Path

lab_dir = Path("assets/NOIR_GRIT_SONGS")

for original_file in lab_dir.glob("*.original"):

    # Create corresponding .lab filename
    lab_file = original_file.with_suffix(".lab")

    # Read original file
    with open(original_file, "r", encoding="utf8") as f:
        lines = f.readlines()

    phonemes = []

    for line in lines:
        parts = line.strip().split()

        # Expected format: start end phoneme
        if len(parts) != 3:
            continue

        phoneme = parts[2]

        # Remove silence/breath tokens
        if phoneme in ["SP", "AP", "<PAD>"]:
            continue

        phonemes.append(phoneme)

    # Write processed output to .lab file
    with open(lab_file, "w", encoding="utf8") as f:
        f.write(" ".join(phonemes))

    print(f"Parsed lab saved: {lab_file.name}")
    print(f"Source original used: {original_file.name}")