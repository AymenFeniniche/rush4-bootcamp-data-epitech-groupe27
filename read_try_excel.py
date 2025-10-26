from pathlib import Path
import pandas as pd
p = Path('Camp_Market.csv')
print('Exists:', p.exists(), '->', p.resolve())
if not p.exists():
    raise SystemExit(1)

# Try with read_excel
try:
    df = pd.read_excel(p)
    print('read_excel SUCCESS, shape:', df.shape)
    print(df.head().to_string())
except Exception as e:
    print('read_excel failed:', repr(e))
    # try read_csv with some encodings
    for enc in ['latin-1','cp1252','utf-8','utf-8-sig']:
        try:
            print('Trying read_csv with', enc)
            df = pd.read_csv(p, sep=';', encoding=enc, engine='python')
            print('read_csv SUCCESS with', enc, 'shape:', df.shape)
            print(df.head().to_string())
            break
        except Exception as e2:
            print('read_csv failed with', enc, ':', repr(e2))
