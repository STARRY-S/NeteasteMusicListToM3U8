# Convert Neteaste Music Playlist to M3U8 file

## Usage:

The default download directory of Neteaste Music is `~/Music/CloudMusic`.

```
sudo pip3 install requests
git clone https://github.com/STARRY-S/NeteasteMusicListToM3U8.git
cp ./NeteasteMusicListToM3U8/main.py ~/Music && cd ~/Music
python3 ./main.py
```

It will generate a `txt` file and a `m3u8` file, you can use `-f/--file` option to load `txt` file if you want to regenerate the`M3U8`file.

After that, checkout the `m3u8` file generated and correct the `Unable to find` file directory.

The `ncm` file and "Unabel to find directory" file can't be play in Music player.

Then, copy both `CloudMusic` directory and `M3U8` file into the root directory of your Walkman Music Player.

Enjoy.

## Others:

1. Make sure you've downloaded all music files in your music list.

2. Replace `*.ncm` file to `mp3/flac` file before execute this program.

3. Make sure you have a good internet connection.

# 简体中文：
使用播放列表id导出网易云音乐的歌单为M3U8文件

## 使用：

网易云音乐的默认下载地址为`~/Music/CloudMusic`。

```
sudo pip3 install requests
git clone https://github.com/STARRY-S/NeteasteMusicListToM3U8.git
cp ./NeteasteMusicListToM3U8/main.py ~/Music && cd ~/Music
python3 ./main.py
```

这将会生成一个`txt`文件和一个`m3u8`文件，如果你需要重新生成`m3u8`文件，你可以指定`-f/--file`参数来加载之前生成的`txt`文件。

然后检查一下生成的M3U8文件是否正确，将里面`Unable to find`的文件目录替换为正确的文件目录。

`ncm`文件和那些目录不正确的文件将无法被播放器识别播放。

最后将生成的`m3u8`文件和`CloudMusic`文件夹一同复制到你的Walkman播放器/内存卡根目录中。

## 其他：

1. 提前将歌单中的全部歌曲下载至本地

2. 把`*.ncm`歌曲换成未加密的`mp3/flac`的文件。

3. 确保在网络连接正常的情况下运行本程序。
