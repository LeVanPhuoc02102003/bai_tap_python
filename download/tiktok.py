from download.parent import DownloadVideo

class TiktokVideo(DownloadVideo):
    def __init__(self, url):
        self.url = url

    def taiVideo(self):
        try:
            r = self._request.post("https://ssstik.io/abc?url=dl", {
                "id": self.url,
                "locale": "en",
                "tt": "bjVqWG9l"
            })

            data = r.html.find("a.pure-button.pure-button-primary.is-center")[0].attrs["href"]

            response = self._request.get(data)
            
            self._luuVideo("tiktok_video", response.content)
        except:
            return False

        return True
        