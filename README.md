# hse25_hw3

ноутбук лежит в репозитории

клеточная линия DND-41

H3k04me1,
H3k27ac,
H3k09ac,
H3k04me3,
H3k04me2,
H3k79me2,
H4K20me1,
H3k36me3,
H3k09me3,
H3K27me3

Имена файлов:
```bash
filenames=(
    "wgEncodeBroadHistoneDnd41H3k04me1AlnRep1.bam"
    "wgEncodeBroadHistoneDnd41H3k04me2AlnRep1.bam"
    "wgEncodeBroadHistoneDnd41H3k04me3AlnRep1.bam"
    "wgEncodeBroadHistoneDnd41H3k09acAlnRep1.bam"
    "wgEncodeBroadHistoneDnd41H3k09me3AlnRep1.bam"
    "wgEncodeBroadHistoneDnd41H3k27acAlnRep1.bam"
    "wgEncodeBroadHistoneDnd41H3k27me3AlnRep1.bam"
    "wgEncodeBroadHistoneDnd41H3k36me3AlnRep1.bam"
    "wgEncodeBroadHistoneDnd41H3k79me2AlnRep1.bam"
    "wgEncodeBroadHistoneDnd41H4k20me1AlnRep1.bam"
)
```

Картинки из отчета ChromHMM:

![image](https://github.com/user-attachments/assets/21c5f52c-0e9e-484c-aee3-811c43efac7c)
![image](https://github.com/user-attachments/assets/0aaa1546-09c6-40d4-a4f6-91ff1b30a4c8)
![image](https://github.com/user-attachments/assets/6ecda353-e56f-49f5-bd7d-19fda57a0de5)
![image](https://github.com/user-attachments/assets/a328eb69-69ef-47d4-9cb8-912ad55a3f2c)
![image](https://github.com/user-attachments/assets/ea3069da-a5ab-488b-a232-c7384a446d65)

Таблица состояний:
| State | Name | Характерные гистоновые модификации | Расположение относительно CpG островков |
| - | - | - | - |
| 1 | weak enhancer | H3k04me1, H3k27ac, H3k09ac, H3k04me3, H3k04me2, H3k79me2 | CpGIsland, RefseqExon, RefSeqTES, RefSeqTSS, RefSeqTSS2kb |
| 2 | strong enhancer | H3k04me1, H3k27ac | laminB1lads |
| 3 | active promoter | H3k04me1, H3k04me2, H3k79me2, H4K20me1, H3k36me3 | RefseqExon, RefSeqGene, RefSeqTES |
| 4 | inactive promoter | H3k79me2 | RefSeqGene |
| 5 | weak promoter | H3k79me2, H4K20me1, H3k36me3 | RefseqExon, RefSeqGene, RefSeqTES |
| 6 | weak transcribed | - | RefSeqGene, RefSeqTES |
| 7 | insulator | H3k36me3 | RefseqExon, RefSeqGene, RefSeqTES |
| 8 | transcriptional transition | H3k09me3 | laminB1lads |
| 9 | polycomb repressed | - | laminB1lads |
| 10 | heterochromatin | H3K27me3 | laminB1lads |

![](https://github.com/user-attachments/assets/edfeb690-c38c-401c-b8ee-2d6057bfac4e)

![](https://github.com/user-attachments/assets/0f9dad53-648c-476e-9915-bc9f5434e628)

Для получения bed-файла с названиями использовался скрипт:
```python
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
```

Запускался с помощью
```bash
python3 script.py > edited.bed
```
