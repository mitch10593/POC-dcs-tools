# Mission Tools

POC of DCS mission tools.

Will transform a DCS mission (lua file) into an ordered Yaml file.

Ordered collections:
- country (by name)
- helicopter (by name)
- plane (by name)
- static (by name)
- ship (by name)
- vehicle (by name)

## Usage

### Convert a DCS Lua Mission to YAML

```shell
python lua2yml.py src/mission/mission src/mission/mission.yml
```

### Convert a YAML Mission to DCS Lua

```shell
python yml2lua.py src/mission/mission.yml src/mission/mission
```

## work on this project

### virtual environment

**Linux**:

```shell
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**:

```shell
@todo
```

### install requirements

```shell
pip install -r requirements.txt
```

### launch tests

```shell
pytest
```
