import winreg
from winreg import *
from contextlib import suppress
import itertools

RULES_PATH = "SYSTEM\\CurrentControlSet\\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\FirewallRules"
RULE_IN = "Block Internet In"
RULE_OUT = "Block Internet Out"

def check_for_rule(rule_name):
    try:
        rules = winreg.OpenKey(
            winreg.HKEY_LOCAL_MACHINE,
            "SYSTEM\\CurrentControlSet\\\Services\\SharedAccess\\Parameters\\FirewallPolicy\\FirewallRules",
            0,
            winreg.KEY_READ)
        rules_info = winreg.QueryInfoKey(rules)
        num_of_keys = rules_info[1]
        print(f"found {num_of_keys} keys")
        for i in range(num_of_keys):
            key = winreg.EnumValue(rules, i)
            if "Block Internet" in key[1]:
                print(key)

    except (FileNotFoundError, TypeError, OSError) as e:
        print(e)


def find_rule_by_name(name):
    for key in subkeys(RULES_PATH):
        if name in key[1]:
            print(key[1].split("|"))


def subkeys(path):
    with suppress(WindowsError), OpenKey(HKEY_LOCAL_MACHINE, path, 0, KEY_READ) as key:
        for i in itertools.count():
            yield EnumValue(key, i)


if __name__ == "__main__":
    find_rule_by_name(RULE_IN)