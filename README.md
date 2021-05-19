# InternetBlocker
System tray app for enabling and disabling firewall rules. The "Block Internet In" and "Block Internet Out" rules must already be defined in windows firewall.

Distributed using PyInstaller

build with:
```
pyinstaller --additional-hooks-dir=. --noconsole  internet_blocker.py
```

TODO: hide netsh console windows, better distribution needed, pretty gross atm (Pyinstaller binary detected as trojan)

