# sip-specification

## JSON to Google Sheets

Convert one of the profile JSON files to CSV, then import the CSV in Google Sheets:

```sh
python3 scripts/constraints_json_to_csv.py.py _data/BASIC_PROFILE.json basic-profile.csv
```

The `Export CSV` GitHub Actions workflow also generates CSV files for all files in `_data/`
whenever that folder changes, and uploads them as a `constraints-csv` artifact.
