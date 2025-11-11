import logging

from ulauncher.api.client.Extension import Extension
from ulauncher.api.client.EventListener import EventListener
from ulauncher.api.shared.event import KeywordQueryEvent, ItemEnterEvent
from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.RenderResultListAction import RenderResultListAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.ExtensionCustomAction import ExtensionCustomAction

log = logging.getLogger(__name__)


class UlauncherBrightnessExtension(Extension):

    def __init__(self):
        super().__init__()
        self.subscribe(KeywordQueryEvent, KeywordQueryEventListener())
        self.subscribe(ItemEnterEvent, ItemEnterEventListener())


class KeywordQueryEventListener(EventListener):
    def on_event(self, event, extension):
        """
        Listen to user input and return brightness setting options.
        The first setting is the value entered by the user if valid,
        followed by preset values from 10 to 100 in steps of 10.
        """
        argument = event.get_argument()
        items = []
        if argument and argument.isdigit() and 1 <= int(argument) <= 100:
            items.append(
                ExtensionResultItem(
                    icon="images/icon.png",
                    name=f'Set brightness to {argument}% on screens {extension.preferences["displays"]}',
                    on_enter=ExtensionCustomAction(argument, keep_app_open=False),
                )
            )

        for i in range(10, 101, 10):
            items.append(
                ExtensionResultItem(
                    icon=f"images/icon_{i:03d}.png",
                    name=f'Set brightness to {i}% on screens {extension.preferences["displays"]}',
                    on_enter=ExtensionCustomAction(str(i), keep_app_open=False),
                )
            )

        return RenderResultListAction(items)


class ItemEnterEventListener(EventListener):
    def on_event(self, event, extension):
        argument = event.get_data()
        displays = extension.preferences["displays"].split(",")
        for display in displays:
            if not display.isdigit() or int(display) < 0:
                log.error(f"Invalid display number: {display}")
                log.error(f"Provided displays: {displays}")
                log.error(
                    "Displays should be a comma-separated list of non-negative integers."
                )
                return ExtensionResultItem(
                    name=f'Cannot parse display setting: "{displays}". Make sure it is a comma separated list of non-negative integers.',
                    description="Item description %s" % i,
                    on_enter=ExtensionCustomAction(str(i), keep_app_open=False),
                )
        # Run DDCutil to set the brightness of screen 0 and 1 using the user input from the event
        import subprocess

        for display in displays:
            subprocess.run(["ddcutil", "setvcp", "10", argument, "--display", display])


if __name__ == "__main__":
    UlauncherBrightnessExtension().run()
