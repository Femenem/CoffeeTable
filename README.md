# CoffeeTable

## Development

### Note: currently requires the working directory to be ~/projects/CoffeeTable, otherwise config/container volumes will not be read

1. Copy env and set values:
```sh
cp .env.example .env
```
2. Start container (-d for background)
```sh
docker-compose up -d
```

## Documentation
- https://github.com/bastilimbach/docker-MagicMirror
- https://github.com/MichMich/MagicMirror/wiki/3rd-party-modules

### When cloning a submodule:

```sh
git submodule add <url>
```

---

## Production Only!

### Install unclutter to auto-hide mouse
```sh
sudo apt-get update && sudo apt-get install unclutter
```

### Start Chromium with magicmirror on startup
```sh
sudo cp ./autostart ~/.config/lxsession/LXDE-pi/autostart
```
