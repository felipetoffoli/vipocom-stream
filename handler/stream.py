import os
import re


class Stream:
    @staticmethod
    def check_on(key_stream):
        check = False
        folder_files = os.listdir(r'/home/stream/hls')

        print(folder_files)
        for file in folder_files:
            if re.search(key_stream, file):
                check = True
        return check

    @staticmethod
    def stremer_all():
        default_files = [
            'index.html', 'main.js',
            'main.js.save', 'offiline.png',
            'style.css'
        ]
        folder_files = os.listdir(r'/home/stream/hls')
        for default_file in default_files.copy():
            try:
                if default_file in folder_files:
                    folder_files.remove(default_file)
            except Exception as e:
                print(e)
        return {'stremers': folder_files}
