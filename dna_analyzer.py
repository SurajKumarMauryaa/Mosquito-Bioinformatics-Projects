from Bio import SeqIO

file = "sequence.fasta"

try:
    for record in SeqIO.parse(file, "fasta"):
        seq = record.seq
        length = len(seq)
        gc = (seq.count("G") + seq.count("C")) / length * 100

        print("ID:", record.id)
        print("Length:", length)
        print("GC Content:", round(gc, 2), "%")
        print("-" * 30)

except FileNotFoundError:
    print("Error: FASTA file not found. Check file path.")
