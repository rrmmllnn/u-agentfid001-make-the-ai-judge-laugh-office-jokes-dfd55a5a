from pathlib import Path


def build_and_save() -> None:
    chunks = (
        'The boss calls us a family, so I asked ',
        'HR for my inheritance ',
        '\u2014',
        " turns out it's the broken printer and an 8 a.m. meeting.",
    )
    line = ''.join(chunks)
    if len(line) != 119:
        raise ValueError('joke came out the wrong length')
    dest = Path('/output') / 'entry.txt'
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(line, encoding='utf-8')


if __name__ == '__main__':
    build_and_save()
