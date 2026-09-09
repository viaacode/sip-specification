#!/usr/bin/env python3

import csv
import json
import sys
from pathlib import Path


def main():
    if len(sys.argv) not in (3,):
        sys.exit("Usage: python3 scripts/json_to_google_sheet_csv.py <input.json|input_dir> <output.csv|output_dir>")

    source = Path(sys.argv[1])
    target = Path(sys.argv[2])

    if source.is_dir():
        target.mkdir(parents=True, exist_ok=True)
        for path in sorted(source.glob("*.json")):
            write_csv(path, target / f"{path.stem}.csv")
    else:
        write_csv(source, target)


def write_csv(source, target):
    rows = json.loads(source.read_text(encoding="utf-8"))

    if not isinstance(rows, list) or any(not isinstance(row, dict) for row in rows):
        sys.exit(f"{source}: expected a JSON array of objects")

    columns = list(dict.fromkeys(key for row in rows for key in row))
    target.parent.mkdir(parents=True, exist_ok=True)

    with target.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows({key: csv_cell(value) for key, value in row.items()} for row in rows)


def csv_cell(value):
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False)
    return value


if __name__ == "__main__":
    main()
