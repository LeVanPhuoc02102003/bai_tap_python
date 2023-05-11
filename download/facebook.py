from download.parent import DownloadVideo
import json
import re

class FacebookVideo(DownloadVideo):
    def __init__(self, url):
        self.url = url

    def __xuLyLienKet(self, url):
        result = url.replace("www", "m")
        return result

    def laySourceVideo(self, url, request):
        if url.find("watch") == -1:
            data = json.dumps(re.findall('data-store="(.*?)"', request.text)[1]
            .replace("&quot;", "'")
            .replace("&amp;", "&")
            .replace("&#123;", "{")
            .replace("&#125;", "}")
            .replace("\\\\", ""))

            return re.findall("'src':'(.*?)'", data)[0]
        else:
            dataStore = request.html.find('[data-store]')[0].attrs["data-store"]
            return json.loads(dataStore)["src"]

        return "error"

    def taiVideo(self):
        if self.url == '':
            print('Dua link fb vao')
            return
        
        url = self.__xuLyLienKet(self.url)

        try:
            r = self._request.get(url)
        except:
            print('Liên kết không hợp lệ')
            return
        
        try:
            videoSRC = self.laySourceVideo(url, r)
            response = self._request.get(videoSRC)
            self._luuVideo("video_fb", response.content)
        except:
            print('Tai video that bai!')
            return False
        
        print('Tai video thanh cong!')
        return True