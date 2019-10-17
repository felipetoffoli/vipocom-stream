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
