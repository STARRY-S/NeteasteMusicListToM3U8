# Convert Neteaste Music Playlist to M3U8 file

> 2020年6月补充： 因为网易不知啥时候更新了网页版，获取播放列表只能依靠cookie登录，且只能获取你自己创建的播放列表。

结合已下载好的本地音乐导出网易云音乐的歌单为m3u8格式的播放列表文件。

可用于播放列表的备份和迁移。

## Usage：

网易云音乐的默认下载地址为`~/Music/CloudMusic`。

```
sudo pip3 install requests
git clone https://github.com/STARRY-S/NeteasteMusicListToM3U8.git
cp ./NeteasteMusicListToM3U8/main.py ~/Music && cd ~/Music
```

浏览器打开[网易云音乐](https://music.163.com)并登录后打开需要转换的播放列表，按F12找到cookie，复制。

编辑`main.py`，粘贴cookie。

 **为了帐号安全，不要将你的cookie告诉其他人**

运行`python3 main.py`, 这将会生成一个`txt`文件和一个`m3u8`文件，如果你需要再次重新生成`m3u8`文件，你可以指定`-f/--file`参数选择已生成的`txt`文本文件来加载之前生成的`txt`文件以节省网上抓包的时间。

然后检查一下生成的M3U8文件是否正确，搜索关键字`Unable`将不正确的文件目录更改为正确的文件目录。

 **`ncm`文件和那些目录不正确的文件将无法被播放器识别播放。**

最后将生成的`m3u8`文件连同你的本地音乐`CloudMusic`文件夹一同复制到你的Walkman播放器/内存卡根目录中，要确保不要修改本地音乐文件路径。

## 其他：

1. 提前将歌单中的全部歌曲下载至本地。

2. 把`*.ncm`歌曲换成文件名相同且未加密的`mp3/flac`的文件。

3. 确保在网络连接正常的情况下运行本程序。

4. 能力有限，程序写得简陋，勉强够用，有更好的意见/建议欢迎提issue。
