import re

with open('scratch/TELUGU_COMPLEX_PARAS_INPUT.txt', 'r', encoding='utf-8') as f:
    in_text = f.read()

with open('scratch/TELUGU_COMPLEX_PARAS_OUTPUT.txt', 'r', encoding='utf-8') as f:
    out_text = f.read()

words_in = in_text.split()
words_out = out_text.split()

for win, wout in zip(words_in, words_out):
    if win in ['ప్రకృతి', 'తెలుగు', 'భాష', 'ద్రావిడ', 'దక్షిణ', 'శ్రీశైల', 'మహాక్షేత్రంలో', 'సమసమాజ']:
        print(f"{win} -> {wout}")

