# nfslm
「你服死了没？」 简单的 Minecraft 服务器在线状态图

## 部署
``` shell
$ git clone https://github.com/jinzhijie/nfslm.git
$ pip3 install -r requirements.txt
$ python3 main.py
```

> nfslm 将会在 ｀85｀ 端口运行

## APIs
### /status-icon
获取 Minecraft 服务器是否在线的图标，可在 `<img />` 标签内使用

| method | GET |
| params `addr` | Minecraft 服务器地址，支持 SRV 记录 |
| response | svg+xml |
