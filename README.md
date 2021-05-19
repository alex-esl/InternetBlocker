# InternetBlocker
System tray app for enabling and disabling firewall rules. The "Block Internet In" and "Block Internet Out" rules must already be defined in windows firewall.

Distributed using Nuitka

build with:
```
python -m nuitka --windows-icon-from-ico=./internetblocker/assets/shortcut.ico internet_blocker.py
```

TODO: hide netsh console windows, better distribution needed.