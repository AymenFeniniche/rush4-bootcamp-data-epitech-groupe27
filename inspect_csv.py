from pathlib import Path
csv_path = Path('Camp_Market.csv')
if not csv_path.exists():
    print('File not found:', csv_path.resolve())
    raise SystemExit(1)

with open(csv_path, 'rb') as f:
    head = f.read(1024)

print('--- First 512 bytes (hex) ---')
print(head[:512].hex())
print('\n--- First 512 bytes (repr decoded with errors=replace) ---')
print(head[:512].decode('utf-8', errors='replace'))
print('\n--- Sample lines using latin-1 decoding (errors=replace) ---')
print(head[:512].decode('latin-1', errors='replace'))
