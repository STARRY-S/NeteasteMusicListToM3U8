import requests
import os
import sys

list_id = ''

headers = {
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
"referer": "https://music.163.com/",
"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36"
}

def GetMusicList():
    list_id = input("Playlist ID: ")
    list_url = "https://music.163.com/playlist?id=" + list_id
    req = requests.get(list_url, headers=headers)
    text = req.text.split('<li><a href="/song?id=')
    text[0] = text[0][text[0].find('title": "')+9:text[0].find('"images"')-3]
    print("List Name:", text[0])
    for i in range(1, len(text)):
        song_id = text[i][0:text[i].find('">')]
        text[i]=text[i][text[i].find('">')+2:text[i].find('</a')]
        singer = GetSingerName(song_id)
        text[i] = singer + " - " + text[i]

        # Edit Here To Replace Some Characters
        text[i] = text[i].replace(' / ', ',')
        text[i] = text[i].replace('&amp;', '&')
        text[i] = text[i].replace('*', '＊')
        text[i] = text[i].replace('/', '／')

        print(i, text[i])
    ExportList(text, list_id)
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
            if MusicName in filename:
                find = True
                break
        if find:
            return filename
    print("Error: Unable to find file: ", MusicName)
    return "Unable to find: " + MusicName

def MakeM3U8(MusicList):
    list = "#EXTM3U\n"
    for i in range(1, len(MusicList)):
        list = list + "#EXTINF:,\n"
        list = list + SearchFile(MusicList[i]) + "\n"

    filename = MusicList[0] + ".M3U8"
    try:
        file = open(filename, mode='w')
    except:
        print("Error Unable to open file: ", filename)
        exit(1)
    file.write(list)
    file.close()
    print("Successfully write your music list into {}".format(filename))

def ExportList(MusicList, list_id):
    filename = list_id + '.txt'
    file = open(filename, 'w')
    text = ''
    for i in range(0, len(MusicList)):
        text = text + MusicList[i] + '\n'
    file.write(text)
    file.close()
    print("\nExport music list txt file to {}".format(filename))

def ReadList(filename):
    try:
        file = open(filename, 'rt')
    except:
        print("Error: File", filename, "Not Found!")
        exit(0)
    list = []
    for line in file:
        line = line.strip()
        print(line)
        list.append(line)
    file.close()
    return list

def ShowHelp():
    print("Convert Neteaste MusicList To M3U8 File\n")
    print("Usage:\n\tpython3 main.py [options]\n")
    print("Default: Get music list from internet and export it to txt file and m3u8 file")
    print("\nGeneral Options:")
    print("   -f, --file\t\tImport list from txt file which is exported from this program.")
    print("   -v, --version\tShow Version.")
    print("   -h, --help\t\tShow help.")

def main():
    if len(sys.argv) == 1:
        print("Getting Music List info from internet...")
        MusicList = GetMusicList()
    elif sys.argv[1] == '-f' or sys.argv[1] == '--file':
        if len(sys.argv) == 2:
            ShowHelp()
            exit(0)
        filename = sys.argv[2]
        print("Getting Music List info from file:", filename)
        MusicList = ReadList(filename)
    elif sys.argv[1] == '-v' or sys.argv[1] == '--version':
        print("Version: 1.1.0 - 2019.09.28")
        print("By: STARRY-S")
        exit(0)
    else:
        ShowHelp()
        exit(0)

    MakeM3U8(MusicList)

if __name__ == '__main__':
    main()
