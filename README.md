# Convert Neteaste Music Playlist to M3U8 file

## Usage:

The default download directory of Neteaste Music is `~/Music/CloudMusic`.

```
sudo pip3 install requests
git clone https://github.com/STARRY-S/NeteasteMusicListToM3U8.git
cp ./main.py ~/Music && cd ~/Music
python3 ./main.py
```

After that, copy both `CloudMusic` directory and `M3U8` file into the root directory of your Walkman Music Player.

## Others:

1. Make sure you've downloaded all music files in your music list.

2. Replace `*.ncm` file to `mp3/flac` file first.

3. Make sure you have a good internet connection.

# 简体中文：

##　使用：

网易云音乐的默认下载地址为`~/Music/CloudMusic`。

```
sudo pip3 install requests
git clone https://github.com/STARRY-S/NeteasteMusicListToM3U8.git
cp ./main.py ~/Music && cd ~/Music
python3 ./main.py
```

在此之后，复制生成的`.M3U8`文件和`CloudMusic`文件夹到你的Walkman播放器中。

##　其他：

1. 提前将歌单中的全部歌曲下载至本地

2. 把`*.ncm`歌曲换成未加密的`mp3/flac`的文件。

3. 确保在网络连接正常的情况下运行本程序。
