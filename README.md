## qbittorrent for hoshino

需要qbittorrent开启web ui
### Install
依赖库
`pip install python-qbittorrent`

文件夹放入`modules`中

`config/__bot__.py`添加`qbittorrent`

插件默认关闭，需要自行开启

### Usage

`qblist`展示qbitorrent当前所有任务的`hash,名称,分类,进度,状态`

`qblink [category] magnet:?xt=urn:btih:xxxx` 使用磁力链接下载

`qbfile [category] torrent_url` 使用torrnet文件下载（url为种子文件的下载链接）

> PS: category，webui的地址账户密码需要自行在`__init__.py中配置`，如果`category`为空，则使用qbittorrent默认下载地址等进行下载。

### TODO
临时摸出来的产物，还有很多细节需要优化
> * 种子文件判断
> * 下载feedback