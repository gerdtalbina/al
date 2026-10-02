#!/usr/bin/env python3

dna = input("DNA: ").strip().upper()

valid_nucleotides = set("ACGT")
if not set(dna).issubset(valid_nucleotides) or len(dna) == 0:
    print("error")
else:
    print("\n1. L:")
    for nuc in "ACGT":
        print(f" {nuc}: {dna.count(nuc)}")

    trans_table = str.maketrans("ACGT", "TGCA")
    complementary = dna.translate(trans_table)
    print(f"\n2. COMPLEMENTARY:\n   {complementary}")

    subseq = input("\n3. dna: ").strip().upper()

    indices = []
    pos = dna.find(subseq)
    while pos != -1:
        indices.append(pos + 1)
        pos = dna.find(subseq, pos + 1)

    if indices:
        print(f" index'{subseq}': {indices}")
    else:
        print(f"error")
