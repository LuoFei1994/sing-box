# StevenBlack Hosts for Loon

本仓库通过 GitHub Actions 定期抓取 [StevenBlack/hosts](https://github.com/StevenBlack/hosts) 项目，自动转换为 **Loon** 支持的 `[Host]` 格式，并存放在 `main` 分支的 `StevenBlack-hosts/` 文件夹下。

## 📥 订阅地址

在 Loon 配置文件中添加以下远程 Host：

```ini
[Remote Host]
https://raw.githubusercontent.com/LuoFei1994/sing-box/main/StevenBlack-hosts/loon-hosts.conf, tag=StevenBlack, update-interval=86400
