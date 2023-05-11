from download.facebook import FacebookVideo
from download.tiktok import TiktokVideo
from download.youtube import YoutubeVideo
import os
from pick import pick

def menu():
    option, index = pick(
        ['Facebook', 'TikTok', 'Youtube', 'Thoat'], 
        'Ban muon tai video nao ?', 
        indicator = '=>', 
        default_index = 0
    )

    if option == "Thoat": 
        return

    os.system('cls')
    url = input("Dien url vao: ")
    
    if index == 0:
        FacebookVideo(url).taiVideo()
    elif index == 1:
        TiktokVideo(url).taiVideo()
    elif index == 2:
        youtube = YoutubeVideo(url)
        tt = youtube.layThongTinVideo()

        if tt != False:
            option, index = pick(
                [x[0] for x in tt ],
                'Chon do phan giai',
                indicator = '=>',
                default_index = 0
            )

            youtube.taiVideo(tt[index][1])
    
    input("Nhan enter de tiep tuc")
    option, index = pick(
        ['Co', 'Khong'], 
        'Ban co muon thuc hien tiep khong ?', 
        indicator = '=>', 
        default_index = 0
    )

    if option == "Khong": return
    menu()

menu()

# if index == 0:
#     FacebookVideo(url).taiVideo()
# else:
#     TiktokVideo(url).taiVideo()