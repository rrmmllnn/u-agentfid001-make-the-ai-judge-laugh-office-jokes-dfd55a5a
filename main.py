from pathlib import Path


def emit() -> None:
    pieces = [
        'The boss calls us a fam',
        'ily, so I asked HR for my inher',
        'itance ',
        chr(8212),
        " turns out it",
        "'s the broken printer and an 8 a.m. meeting.",
    ]
    line = ''.join(pieces)
    target = Path('/output') / 'entry.txt'
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(line, encoding='utf-8')


emit()
