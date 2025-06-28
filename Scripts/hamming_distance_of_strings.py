def HammingDistance(p, q,md):
    HD = 0
    for i in range(len(p)):
        if p[i] != q[i]:
            HD += 1
            md[i] = [p[i], 'to', q[i]]
        else:
            continue
    return HD

MutationDictionary = {}

while True:
    Sequence_1 = input("Please enter your sequence, or '/' to exit:").upper()
    if Sequence_1 == "/":
        break
    Sequence_2 = input("Please enter your sequence, or '/' to exit:").upper()
    if Sequence_2 == "/":
        break
    print(HammingDistance(Sequence_1,Sequence_2,MutationDictionary))
    print(MutationDictionary)
    MutationDictionary = {}