# lmstudio_chinese - LM Studio 简体中文补丁

![Stars](https://img.shields.io/github/stars/HeLeiawa/lmstudio_chinese?style=flat-square&logo=github)
![Forks](https://img.shields.io/github/forks/HeLeiawa/lmstudio_chinese?style=flat-square&logo=github)
![Issues](https://img.shields.io/github/issues/HeLeiawa/lmstudio_chinese?style=flat-square&logo=github)
![License](https://img.shields.io/github/license/HeLeiawa/lmstudio_chinese?style=flat-square)
![LM Studio](https://img.shields.io/badge/LM%20Studio-0.4.26%2B4-blue?style=flat-square)
![Release](https://img.shields.io/badge/补丁版本-v1.1.0-green?style=flat-square)

LM Studio 自带的简体中文是未完成的测试版翻译，大量新功能界面仍是英文，语言列表里也挂着「简体中文 (Beta)」标记。本补丁在其官方翻译的基础上补全全部缺失内容，让 LM Studio 获得完整、可日常使用的简体中文界面。

## 功能

- 补全 92 条官方遗漏的中文翻译，覆盖 0.4.26 版全部新功能：
  推理预算、聊天模板、最大并发预测数、统一 KV 缓存、上下文检查点、
  强制置于 CPU 的 MoE 层数、自动上下文长度、远程 MCP、模型加载守卫、
  预估内存占用、默认上下文长度、预设保存流程、模型变体切换等
- 直译约 1870 处未接入翻译系统的硬编码界面文案（1500+ 组）：侧边栏导航、
  通用按钮、聊天空状态、Library 资源库页、LM Link 页面与引导弹窗、
  模型服务器与开发者文档树、转写页、插件页、权限令牌页、应用更新状态、
  新建文件夹默认名、Mermaid 图形说明等
- 额外补上 4 条连官方英文资源都缺失的文案（中文界面比英文还完整）
- 修复 1 处丢失插值变量的官方翻译 bug
- 移除语言列表中「简体中文 (Beta)」的 Beta 标记
- 打补丁后 zh_CN 全部 10 个界面模块对英文原文覆盖率 100%

注：模型卡片里的模型简介、下载量等来自 Hugging Face / 模型目录的在线数据，
不属于程序界面文案，无法通过本地补丁翻译。

## 环境要求

- Windows 系统
- Python 3.8 或更高版本（[python.org](https://www.python.org/downloads/) 下载，安装时勾选 Add python.exe to PATH）
- LM Studio 0.4.26+4（其他版本未验证；脚本内置签名校验，版本不符会拒绝写入，不会损坏程序）

## 使用方法

### 方式一：双击运行

双击 `run.bat`，看到菜单后：

```
[1] 安装中文补丁
[2] 卸载中文补丁
```

输入对应数字回车开始执行。

### 方式二：命令行

```
python lmstudio_chinese_patch.py             进入交互菜单
python lmstudio_chinese_patch.py --apply     安装补丁
python lmstudio_chinese_patch.py --restore   卸载补丁
python lmstudio_chinese_patch.py --status    查看补丁状态
python lmstudio_chinese_patch.py --dir "K:\LM Studio"   手动指定安装目录
```

脚本会自动通过注册表和常见安装路径查找 LM Studio，无需手动配置。

安装后请完全退出 LM Studio（包括托盘图标）再重新打开，在 Settings - Language 中选择「简体中文」。

## 卸载

运行脚本选择 [2]，或执行 `--restore`。补丁安装时自动备份了原始文件，卸载即恢复备份，与打补丁之前完全一致。

## 工作原理

LM Studio 是 Electron 应用，界面文案以内嵌 i18n 资源的形式打包在
`resources\app\.webpack\renderer\main_window.js` 中。本补丁：

1. 按官方中文翻译的内容签名定位各语言资源模块（不依赖打包内部 ID，小版本更新也能定位）
2. 解析资源，将缺失的中文键值合并进去，结构与官方完全一致
3. 对未接入翻译系统、写死在代码里的界面文案，按显示属性（children/label/title 等）
   锚点直译，不触碰路由标识符与程序逻辑
4. 写回前逐模块校验，任何一处异常都会中止且不落盘
5. 首次安装自动创建备份（`main_window.js.zh-patch-backup`），支持随时完整还原
6. 重复运行无副作用，只补缺失项，不会重复叠加

补丁只修改界面翻译资源与显示文案，不触碰模型、运行时和程序逻辑。

## 常见问题

**Q: 提示「未找到翻译模块」？**
LM Studio 自动更新后文件结构变化，本版本补丁不再适用。请到项目主页查看是否有适配新版本的更新。

**Q: LM Studio 更新后中文又变回英文了？**
更新会替换程序文件，补丁随之失效，重新运行一次安装即可。

**Q: 找不到安装目录？**
用 `--dir` 手动指定 LM Studio 的安装目录。

**Q: 安装后界面还是英文？**
确认已在 Settings - Language 选择「简体中文」，并完全重启过 LM Studio（含托盘进程）。

## 鸣谢

- [LM Studio](https://lmstudio.ai/) - 感谢 LM Studio 团队开发的优秀本地大模型工具。本补丁基于其内置的多语言框架与官方简体中文翻译制作，仅做缺失内容补全，不含任何官方原版翻译文件的再分发。

## 开发者

- 开发者：HeLei_awa
- 项目链接：https://github.com/HeLeiawa/lmstudio_chinese
- 酷安：https://www.coolapk.com/u/43912900
- B站：https://space.bilibili.com/397051896

## 许可证

本项目代码以 [MIT License](LICENSE) 发布。

## 免责声明

本项目为非官方的社区补丁，与 LM Studio 官方无关，仅供学习交流使用。使用本补丁产生的任何问题由使用者自行承担。
