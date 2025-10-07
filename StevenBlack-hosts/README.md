# StevenBlack Hosts for Loon

本仓库通过 GitHub Actions 定期抓取 [StevenBlack/hosts](https://github.com/StevenBlack/hosts) 项目，自动转换为 **Loon** 支持的 `[Host]` 格式，并存放在 `main` 分支的 `StevenBlack-hosts/` 文件夹下。

## 📥 订阅地址

在 Loon 配置文件中添加以下远程 Host：

```ini
[Remote Host]
https://raw.githubusercontent.com/LuoFei1994/sing-box/main/StevenBlack-hosts/loon-hosts.conf, tag=StevenBlack, update-interval=86400


🛠️ 使用说明
打开 Loon → 配置文件 → 编辑

在配置文件中找到 [Remote Host] 模块

粘贴上面的订阅地址

保存并重载配置

完成！Loon 将自动屏蔽广告、恶意域名和跟踪器

⚠️ 注意事项
这是 基础版 hosts 文件，仅屏蔽广告、恶意软件和跟踪器，不包含色情、赌博、社交媒体等扩展屏蔽。

如果需要扩展版，可以修改工作流脚本，抓取 StevenBlack 提供的其他组合版本。

更新频率：每天自动更新一次，确保规则始终最新。
