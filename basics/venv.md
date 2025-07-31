# Virtual python environments

## Advantages of venvs
- No mix of dependencies from different projects
- No mix up of system modules (macOS/Linux where Python comes preinstalled & is used by the OS)

## Create new python venv
macOS/Linux:
```shell
python3 -m venv venv/
```

Windows:
```shell
py -m venv venv\
```

## Activate venv

macOS/Linux:
```shell
source venv/bin/activate
```

Windows:
```shell
venv\Scripts\activate
```

## Deactivate venv
All operating systems:
```shell
deactivate
```
