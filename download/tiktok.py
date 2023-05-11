from download.parent import DownloadVideo
import re

class TiktokVideo(DownloadVideo):
    def __init__(self, url):
        self.url = url

    def getToken(self):
        response = self._request.get('https://ssstik.io/en')
        return re.findall("tt:'(.*?)'", response.text)[0]

    def taiVideo(self):
        try:
            token = self.getToken() #lay token :3

            r = self._request.post("https://ssstik.io/abc?url=dl", {
                "id": self.url,
                "locale": "en",
                "tt": token
            })

            data = r.html.find("a.pure-button.pure-button-primary.is-center")[0].attrs["href"]

            response = self._request.get(data)
            self._luuVideo("tiktok_video", response.content)
        except:
            print('Tai video tiktok that bai!')
            return False

        print('Tai video tiktok thanh cong!')
        return True
        