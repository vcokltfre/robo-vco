from pathlib import Path

def copy(origin, dest):
    with Path(origin).open() as f:
        data = f.read()
    with Path(dest).open('w') as f:
        f.write(data)

dirs = ["./data", "./data/config", "./data/persist", "./data/temp"]

for directory in dirs:
    data_path = Path(directory)

    if not data_path.exists():
        data_path.mkdir(parents=True)

config_path = Path("./data/config/main.json")

if not config_path.exists():
    copy("./templates/config.json", "./data/config/main.json")

perms_path = Path("./data/persist/perms.json")

if not perms_path.exists():
    copy("./templates/perms.json", "./data/persist/perms.json")
