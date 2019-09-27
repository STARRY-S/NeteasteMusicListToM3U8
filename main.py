#!/bin/env python3
#-*-coding:utf-8-*-
import requests
import os

list_id = input("Playlist ID: ")

headers = {
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"accept-encoding": "gzip, deflate, br",
"accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
"cookie": "",
"referer": "https://music.163.com/",
"sec-fetch-mode": "nested-navigate",
"sec-fetch-site": "same-origin",
"upgrade-insecure-requests": "1",
"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}

def GetMusicList():
    list_url = "https://music.163.com/playlist?id=" + list_id
    req = requests.get(list_url, headers=headers)
    text = req.text.split('<li><a href="/song?id=')
    text[0] = text[0][text[0].find('title": "')+9:text[0].find('"images"')-3]
    print("Music List Name:", text[0])
    for i in range(1, len(text)):
        song_id = text[i][0:text[i].find('">')]
        text[i]=text[i][text[i].find('">')+2:text[i].find('</a')]
        singer = GetSingerName(song_id)
        text[i] = singer + " - " + text[i]
        print(i, text[i])
    return text

def GetSingerName(song_id):
    song_url = "https://music.163.com/song?id=" + song_id;
    req = requests.get(song_url, headers=headers)
    text = req.text
    name = text[text.find('''歌手'''):text.find('''所属专辑''')]
    name = name[name.find('''<span title="''')+13:name.find('''"><a class=''')]
    if ('''"><span class="s-fc7">''' in name):
        name = name[:name.find('''"><span class="s-fc7">''')]
    return name

def SearchFile(MusicName):
    # os.chdir(".")
    for fpath, dirname, fnames in os.walk("."):
        find = False
        for name in fnames:
            filename = os.path.join(fpath, name)
            filename = filename[2:]
            if (MusicName in filename):
                find = True
                break
        if (find):
            return filename

    print("Error: Unable to find file: ", MusicName)
    return ""

def MakeM3U8(MusicList):
    list = "#EXTM3U\n"
    for i in range(1, len(MusicList)):
        list = list + "#EXTINF:,\n"
        list = list + SearchFile(MusicList[i]) + "\n"

    filename = MusicList[0] + ".M3U8"
    file = open(filename, 'w')
    file.write(list)
    file.close
    print("Successfully write your music list into {}".format(filename))

def main():
    print("Getting Music List info...")
    MusicList = GetMusicList()
    MakeM3U8(MusicList)

if __name__ == '__main__':
    main()
