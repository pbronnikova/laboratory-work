# -*- coding: utf-8 -*-
from docx import Document
from pathlib import Path

d = Document(r"c:\Users\polina\Downloads\ISTbd-13_LR2_Bronnikova.docx")
lines = []
for i, p in enumerate(d.paragraphs):
    style = p.style.name if p.style else ""
    lines.append(f"--- {i} style={style}\n{p.text}\n")
Path(r"c:\Vizitka\report_paragraphs.txt").write_text("\n".join(lines), encoding="utf-8")
print("wrote", len(lines), "blocks")
