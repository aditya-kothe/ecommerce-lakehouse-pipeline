
import csv
from pathlib import Path

DATA_DIR = Path("data/olist")

for file_path in sorted(DATA_DIR.glob("*.csv")):
    with file_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.reader(file)
        header = next(reader, None)
        row_count = sum(1 for _ in reader)

    print(f"\nFile: {file_path.name}")
    print(f"Columns: {len(header) if header else 0}")
    print(f"Rows: {row_count}")
    print(f"Headers: {header}")

