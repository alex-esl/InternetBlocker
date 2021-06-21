"""
Reads and edits Windows Firewall using netsh. May switch over to
registry based changes to avoid excess console windows.
"""

import subprocess


RULE_IN = "Block Internet In"
RULE_OUT = "Block Internet Out"


def rule_enabled(rule_name):
    process = subprocess.run(["netsh", "advfirewall", "firewall", "show", "rule", f"name={rule_name}"],
                             universal_newlines=True,
                             stdout=subprocess.PIPE)
    output = process.stdout.splitlines()
    try:
        return parse_check_output(output)
    except ValueError as e:
        raise e


def toggle_rule(rule_name, toggle):
    toggle_arg = "yes" if toggle else "no"
    subprocess.run(
        ["netsh", "advfirewall", "firewall", "set", "rule", f"name={rule_name}", "new", f"enable={toggle_arg}"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL)


def parse_check_output(output):
    for line in output:
        if line.find("Enabled:") > -1:
            if line.find("Yes") > -1:
                return True
            if line.find("No") > -1:
                return False
            else:
                raise ValueError("Unexpected console output")


def enable_rules():
    try:
        toggle_rule(RULE_IN, True)
        toggle_rule(RULE_OUT, True)
        enabled_in = rule_enabled(RULE_IN)
        enabled_out = rule_enabled(RULE_OUT)
        return enabled_in and enabled_out
    except ValueError as e:
        print(e)
        return False


def disable_rules():
    try:
        toggle_rule(RULE_IN, False)
        toggle_rule(RULE_OUT, False)
        enabled_in = rule_enabled(RULE_IN)
        enabled_out = rule_enabled(RULE_OUT)
        return not enabled_in and not enabled_out
    except ValueError as e:
        print(e)
        return False
