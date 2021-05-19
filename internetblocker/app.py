import os
import PIL.Image
import pystray
from . import firewall

icon_path = os.path.abspath(os.path.split(__file__)[0])
icon_stop = PIL.Image.open(os.path.join(icon_path, "assets", "stop.png"))
icon_go = PIL.Image.open(os.path.join(icon_path, "assets", "go.png"))
icon_error = PIL.Image.open(os.path.join(icon_path, "assets", "error.png"))


class App(object):
    def __init__(self):
        self.icon = pystray.Icon("internetblocker",
                                 icon=icon_go,
                                 title="Internet Blocker",
                                 menu=self.default_menu)
        print("init...")

    @property
    def default_menu(self):
        return pystray.Menu(
            pystray.MenuItem("Internet Blocker", None),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem("Block", self.block, enabled=True),
            pystray.MenuItem("Unblock", self.unblock, enabled=False),
            pystray.MenuItem("Quit", self.quit)
        )

    def run(self):
        self.icon.run()

    def quit(self):
        self.icon.stop()

    def block(self):
        blocked = firewall.enable_rules()
        if blocked:
            self.switch_to_stop()
            self.icon.notify("Internet Blocked", title=None)
        else:
            self.icon.notify("Failed to block internet", title="Error")

    def unblock(self):
        unblocked = firewall.disable_rules()
        if unblocked:
            self.switch_to_go()
            self.icon.notify("Internet Unblocked", title=None)
        else:
            self.icon.notify("Failed to unblock internet", title="Error")

    def switch_to_stop(self):
        menu = pystray.Menu(
            pystray.MenuItem("Internet Blocker", None),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem("Block", self.block, enabled=False),
            pystray.MenuItem("Unblock", self.unblock, enabled=True),
            pystray.MenuItem("Quit", self.quit)
        )
        self.icon.menu = menu
        self.icon.update_menu()
        self.icon.icon = icon_stop

    def switch_to_go(self):
        menu = pystray.Menu(
            pystray.MenuItem("Internet Blocker", None),
            pystray.Menu.SEPARATOR,
            pystray.MenuItem("Block", self.block, enabled=True),
            pystray.MenuItem("Unblock", self.unblock, enabled=False),
            pystray.MenuItem("Quit", self.quit)
        )

        self.icon.menu = menu
        self.icon.update_menu()
        self.icon.icon = icon_go