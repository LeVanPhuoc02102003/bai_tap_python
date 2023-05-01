from download.facebook import FacebookVideo
from download.tiktok import TiktokVideo
from pick import pick

option, index = pick(
    ['Facebook', 'TikTok'], 
    'Bạn muốn tải video nền tảng nào ?', 
    indicator = '=>', 
    default_index = 0
)


url = input("Điền url video vào: ")

if index == 0:
    FacebookVideo(url).taiVideo()
else:
    TiktokVideo(url).taiVideo()