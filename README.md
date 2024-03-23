# mission tools

POC of DCS mission tools.

Will transform a DCS mission (lua file) into an ordered Yaml file.

Ordered collections:
- country (by name)
- helicopter (by name)
- plane (by name)
- static (by name)
- ship (by name)
- vehicle (by name)

## work on this project

```shell
python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
```

launch tests:

```shell
pytest
```



coalition / blue / country / <id> / name
coalition / blue / country / <id> / helicopter / group / <id> / name
coalition / blue / country / <id> / plane / group / <id> / name
coalition / blue / country / <id> / ship / group / <id> / name
coalition / blue / country / <id> / static / group / <id> / name
coalition / blue / country / <id> / vehicle / group / <id> / name