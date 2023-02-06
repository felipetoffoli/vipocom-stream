import os
import re
import glob


class Stream:
    @staticmethod
    def check_on(key_stream):
        check = False
        folder_files = os.listdir(r'/home/stream')

        print(folder_files)
        for filename in folder_files:
            stremer_name = filename.replace('.m3u8', '')
            if re.fullmatch(key_stream, stremer_name):
                check = True
        return check

    @staticmethod
    def stremer_all():
        # folder_files = os.listdir(r'/home/stream/hls')
        folder_files = glob.glob(r'/home/stream/*.m3u8')
        key_stremers = []
        if folder_files:
            for file in folder_files:
                bar_split = file.split('/')
                name_with_m3u8 = bar_split[len(bar_split) -1]
                m3u8_split = name_with_m3u8.split('.m3u8')
                key = m3u8_split[0]
                key_stremers.append(key)

        return {'stremers': key_stremers}
