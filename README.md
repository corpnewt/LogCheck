# LogCheck
Py script to scrape high level info from an opencore log

```
usage: LogCheck [-h] [-o OUTPUT] [-m MATCH_KEYS] [-s SKIP_KEYS] [input_file ...]

Py script to scrape high level info from an opencore log

positional arguments:
  input_file            path to the input opencore-[timestamp].txt log file

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        path to the output json file - omit for stdout (requires an input_file)
  -m MATCH_KEYS, --match-keys MATCH_KEYS
                        regex pattern for top level keys to include (cli only)
  -s SKIP_KEYS, --skip-keys SKIP_KEYS
                        regex pattern for top level keys to exclude (cli only)
```
