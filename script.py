d = dict()
d["1"] = "weak_enhancer"
d["2"] = "strong_enhancer"
d["3"] = "active_promoter"
d["4"] = "inactive_promoter"
d["5"] = "weak_promoter"
d["6"] = "weak_transcribed"
d["7"] = "insulator"
d["8"] = "transcriptional_transition"
d["9"] = "polycomb_repressed"
d["10"] = "heterochromatin"
with open("ChromHMM_output/Dnd41_10_expanded.bed") as f:
    cnt = 0
    for line in f:
        cnt += 1
        if cnt <= 2:
            print(line, end='')
        else:
            els = line.split('\t')
            els[3] = d[els[3]]
            line = "\t".join(els)
            print(line, end='')

