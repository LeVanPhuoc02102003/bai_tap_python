from download.parent import DownloadVideo
import json

class YoutubeVideo(DownloadVideo):
    def __init__(self, url):
        self.url = url
        self.videoID = ""

    def layThongTinVideo(self):
        response = self._request.post("https://www.y2mate.com/mates/analyzeV2/ajax", {
            "k_query": self.url,
            "k_page": "home",
            "hl": "en",
            "q_auto": 1
        })

        data = response.json()
        if(data['status'] != 'ok'):
            self.message = "Khong the lay thong tin video"
            return False

        self.videoID = data["vid"]
        return [(value['q'], value['k']) for _, value in data["links"]["mp4"].items()]

    def taiVideo(self, key):
        response = self._request.post("https://www.y2mate.com/mates/convertV2/index", {
            "vid": self.videoID,
            "k": key
        })

        tai = self._request.get(response.json()["dlink"])

        print(self._luuVideo("video_youtube", tai.content) and "Tai Thanh Cong" or "Tai That Bai")
