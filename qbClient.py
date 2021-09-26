from qbittorrent import Client
import requests
import re
import os


class qbClient:
    def __init__(self, url, user, passwd):
        self.qb = Client(url)
        self.path = os.path.abspath(__file__)
        self.qb.login(user, passwd)

    def link_download(self, magnet_link, category):
        try:
            self.qb.download_from_link(magnet_link, category=category)
            return 0
        except Exception as e:
            return "qbittorrent下载错误: {e}"

    def file_download(self, file_link, category):
        try:
            r = requests.get(file_link, timeout=5)
        except Exception as e:
            return f"获取torrent文件错误: {e}"
        try:
            with open(self.path + "tmp/tmp.torrent", "ab") as f:
                f.write(r.content)
                f.seek(0, 0)
                self.qb.download_from_file(f, category=category)
                return 0
        except Exception as e:
            return f"qbittorrent下载错误: {e}"
        
    def mission_list(self):
        torrents = self.qb.torrents()
        infos = []
        for torrent in torrents:
            infos.append({
                'hash': torrent.get('hash'),
                'name': torrent.get('name'),
                'category': torrent.get('category'),
                'progress': str(int(torrent.get('progress') * 100))+"%",
                'state': torrent.get('state'),
            })
        return infos
