from progressreader import ProgressReader
from preferences import Preferences
import rumps, json, requests


class PreferencePane(rumps.Window):

    def __init__(self):
        super(PreferencePane, self).__init__(title="Preferences")
        self.message = "You can modify the below configuration using JSON."
        self.default_text = str(json.dumps(Preferences().config,
                                           sort_keys=True,
                                           indent=4,
                                           separators=(',', ': ')
                                           ))
        self.add_button("Cancel")


class About(rumps.Window):

    def __init__(self):
        super(About, self).__init__(title="About")
        self.default_text = str("Version: 0.1.1\nAuthor: Christian D. Tuen")


class StatusBarApp(rumps.App):

    def __init__(self):
        super(StatusBarApp, self).__init__("-- %")
        try:
            self.preferences = Preferences()
            self.progress_reader = ProgressReader(self.preferences.ip, self.preferences.port)
        except requests.exceptions.ReadTimeout:
            rumps.alert("Not able to connect to 3D printer, please check the application preferences.")
        except Exception as e:
            rumps.alert(str(e))

    @rumps.clicked("Preferences")
    def prefs(self, _):
        response = PreferencePane().run()
        requirements = ['ip', 'interval']
        if response.clicked == 1:
            try:
                user_configuration = json.loads(str(response.text))
                if not all(requirement in user_configuration for requirement in requirements):
                    raise ValueError('You are missing required properties in the JSON configuration.')
                self.preferences.configuration = user_configuration
                self.preferences.write_config()
                self.refresh(_)
            except Exception as e:
                rumps.alert(str(e))

    @rumps.clicked("Refresh")
    def refresh(self, _):
        self.preferences = Preferences()
        self.progress_reader = ProgressReader(self.preferences.ip, self.preferences.port)
        self.progress_updater(_)

    @rumps.clicked("About")
    def about(self, _):
        About().run()

    @rumps.timer(Preferences().interval)
    def progress_updater(self, _):
        self.progress_reader.update_progress()
        usage = self.progress_reader.get_progress()
        if usage == -1:
            usage = "--"
        self.title = f"{usage}%"


if __name__ == "__main__":
    StatusBarApp().run()
