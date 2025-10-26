from pathlib import Path
import pandas as pd
try:
    import chardet
except ImportError:
    chardet = None

csv_path = Path('Camp_Market.csv')
if not csv_path.exists():
    print(f'Fichier non trouvé: {csv_path.resolve()}')
    raise SystemExit(1)

# detect encoding
detected = None
if chardet:
    with open(csv_path, 'rb') as f:
        raw = f.read(200000)
    res = chardet.detect(raw)
    detected = res.get('encoding')
    print('chardet detected encoding:', detected, 'confidence:', res.get('confidence'))
else:
    print('chardet non installé, on essaiera des encodages courants')

candidates = ([detected] if detected else []) + ['utf-8', 'utf-8-sig', 'cp1252', 'latin-1', 'iso-8859-1', 'utf-16']
for enc in candidates:
    if not enc:
        continue
    try:
        print('Trying encoding', enc)
        df = pd.read_csv(csv_path, sep=';', encoding=enc, engine='python')
        print('Read OK with', enc)
        used = enc
        break
    except Exception as e:
        print('Fail with', enc, ':', e)
else:
    print('Failed to read CSV with tested encodings')
    raise SystemExit(2)

out = csv_path.with_name(csv_path.stem + '_utf8.csv')
df.to_csv(out, index=False, sep=';', encoding='utf-8')
print('Saved UTF-8 file:', out)
