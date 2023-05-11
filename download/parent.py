from requests_html import HTMLSession
from abc import abstractmethod

class DownloadVideo:
    _request = HTMLSession()

    def __init__(self, url):
        self.url = url
        self.videoURL = ""
        self.message = ""

    @abstractmethod
    def taiVideo(self):
        pass

    def _luuVideo(self, name, data):
        try:
            with open("./result/" + name + ".mp4", "wb") as f:
                f.write(data)
        except:
            return False
        return True