def find_it(seq):
    for i in range(len(seq)):
        x = seq.count(seq[i])
        if x % 2 == 1:
            return seq[i]


seq = [0, 1, 0, 1, 0]  # 1
seq1 = [1, 1, 2]  # 2
seq2 = [7]

print(find_it(seq2))
