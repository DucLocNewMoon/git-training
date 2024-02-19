import sys

from PySide6.QtWidgets import QApplication, QMessageBox

from version import AppVersion
from version_restriction import check_version_restriction
from sentry import excepthook, initialize_sentry
from src.windows import HotmailListWindow


# check if this app is running in a "frozen" environment, i.e. it has been packaged into an executable using tools like PyInstaller
# if yes, i.e. production environment, initialize sentry logging
if getattr(sys, 'frozen', False):
    initialize_sentry()

# check for app version restriction
app_version = '1.0.1'
is_active_or_none = check_version_restriction(app_version)

app_version = AppVersion.VERSION.value
is_active_or_none = check_version_restriction(app_version)

if __name__ == '__main__':
    if is_active_or_none is None:
        app = QApplication(sys.argv)
        QMessageBox.critical(None, "Error", f"The version {app_version} does not exist or is not yet launched.<br>Please, contact TNM DEV team for support.")
        sys.exit(1)
    elif not is_active_or_none:
        app = QApplication(sys.argv)
        QMessageBox.critical(None, "Error", f"The version {app_version} is not currently in use anymore.<br>Please, update to the latest version.")
        sys.exit(1)
    else:
        app = QApplication(sys.argv)
        sys.excepthook = excepthook

        window = HotmailListWindow()
        window.show()
        sys.exit(app.exec())