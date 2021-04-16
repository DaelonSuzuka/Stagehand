from qtstrap import *
from qtpy.QtNetwork import *
import json


class ApplicationUpdater(QObject):
    def __init__(self) -> None:
        super().__init__()

        self.request_manager = QNetworkAccessManager(self)
        self.request_manager.finished.connect(self.replyRecieved)

    def check_latest(self):
        url = OPTIONS.app_info.AppReleaseUrl
        self.request_manager.get(QNetworkRequest(QUrl(url)))

    def replyRecieved(self, reply: QNetworkReply):
        if reply.error() == QNetworkReply.NoError:
            response = reply.readAll()
            d = json.loads(str(response, 'utf-8'))
            remote_version = float(d['tag_name'])
            current_version = float(OPTIONS.app_info.AppVersion)

            if remote_version > current_version:
                print('There is an update available')

