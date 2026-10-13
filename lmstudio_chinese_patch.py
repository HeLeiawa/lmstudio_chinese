#!/usr/bin/env python3
# -*- coding: utf-8 -*-
r"""LM Studio 简体中文补丁

项目: https://github.com/HeLeiawa/lmstudio_chinese
开发者: HeLei_awa

直接运行进入交互菜单:
    [1] 安装中文补丁
    [2] 卸载中文补丁

命令行模式:
    python lmstudio_chinese_patch.py --apply                 安装补丁
    python lmstudio_chinese_patch.py --restore              卸载补丁（恢复备份）
    python lmstudio_chinese_patch.py --status               查看补丁状态
    python lmstudio_chinese_patch.py --dir "K:\LM Studio"   手动指定安装目录

已验证版本: LM Studio 0.4.26+4 (Windows)
"""
import sys, os, json, shutil, subprocess

VERSION = '1.0.0'
BACKUP_SUFFIX = '.zh-patch-backup'

PATCH_DATA = json.loads(
    r"""{"namespaces":{"sidebar":{"sigs":[["chat","聊天"],["discover","发现"],["myModels","我的模型"]],"ops":[]},"chat":{"sigs":[["modelLoaderPlaceholder","选择要加载的模型"],["systemPromptPlaceholder","设置系统提示"],["userRoleText","用户"]],"ops":[{"c":[],"k":"actions/clearLastUsedModel","v":"清除最近使用的模型","f":false},{"c":[],"k":"actions/clearLastUsedModel/error","v":"清除最近使用的模型失败。","f":false},{"c":["plugins","pluginSelect"],"k":"signOutMcpPlugin/error","v":"退出插件登录失败","f":false},{"c":["plugins","pluginSelect"],"k":"cancelMcpAuthentication/error","v":"取消插件认证失败","f":false},{"c":["genInfo"],"k":"speculativeDecodingAcceptedPercentage","v":"{{percentage}}% 草稿token已采纳","f":false},{"c":["genInfo"],"k":"speculativeDecodingTooltip","v":"已采纳 {{accepted}}/{{total}} 个草稿token","f":false},{"c":[],"k":"actions/createFolder/error","v":"新建文件夹失败","f":false}]},"config":{"sigs":[["noInstanceSelected","未选择模型实例"],["resetToDefault","重置"],["showAdvancedSettings","显示高级设置"]],"ops":[{"c":[],"k":"llm.prediction.reasoning.budgetTokens/title","v":"推理预算","f":false},{"c":[],"k":"llm.prediction.reasoning.budgetTokens/subTitle","v":"思考的 token 预算：关闭表示不限制，0 表示立即结束思考，N > 0 表示限定 token 预算","f":false},{"c":[],"k":"llm.load.promptTemplate/title","v":"聊天模板","f":false},{"c":[],"k":"llm.load.promptTemplate/subTitle","v":"引擎协议用于聊天、工具、推理和多模态格式化的模板。更改后需要重新加载模型。","f":false},{"c":[],"k":"llm.load.numParallelSessions/title","v":"最大并发预测数","f":false},{"c":[],"k":"llm.load.numParallelSessions/subTitle","v":"模型同一时间可执行的最大预测数。并发会降低单个预测的速度，但每个预测能更快启动，总吞吐量也更高","f":false},{"c":[],"k":"llm.load.useUnifiedKvCache/title","v":"统一 KV 缓存","f":false},{"c":[],"k":"llm.load.useUnifiedKvCache/subTitle","v":"控制并发预测是否共享同一份 KV 缓存以节省内存。禁用后每个预测都能使用完整上下文长度，但会占用更多内存","f":false},{"c":[],"k":"llm.load.llama.contextCheckpoints/title","v":"上下文检查点","f":false},{"c":[],"k":"llm.load.llama.contextCheckpoints/subTitle","v":"每个槽位保留的上下文检查点上限。较低的值可减少 SWA/循环模型的内存占用。0 表示禁用检查点。","f":false},{"c":[],"k":"llm.load.llama.reasoningBudgetMessage/title","v":"推理预算耗尽消息","f":false},{"c":[],"k":"llm.load.llama.reasoningBudgetMessage/subTitle","v":"推理预算耗尽时，注入到思考结束标签前的消息（默认：无）","f":false},{"c":[],"k":"llm.load.numCpuExpertLayersRatio/title","v":"强制置于 CPU 的 MoE 层数","f":false},{"c":[],"k":"llm.load.numCpuExpertLayersRatio/subTitle","v":"强制放到 CPU 的专家层数。可节省显存，且可能比部分 GPU 卸载更快。若模型能完全装入显存，不建议使用。","f":false},{"c":[],"k":"llm.load.numCpuExpertLayersRatio/info","v":"指定强制置于 CPU 的专家层数。注意力层保留在 GPU 上，在保持较快推理速度的同时节省显存。","f":false},{"c":[],"k":"llm.load.llama.autoFit/title","v":"根据硬件自动优化","f":false},{"c":[],"k":"llm.load.llama.autoFit/subTitle","v":"加载时由 llama.cpp 根据可用内存自动选择上下文长度和 GPU 布局","f":false},{"c":[],"k":"llm.load.llama.physicalBatchSize/subTitle","v":"单个数据块处理的最大提示 token 数。较大的值可能提升性能，但会占用更多内存","f":false},{"c":[],"k":"llm.load.mlx.autoFit/title","v":"自动上下文长度","f":false},{"c":[],"k":"llm.load.mlx.autoFit/subTitle","v":"加载时由 MLX 运行时根据可用内存选择安全的上下文长度","f":false},{"c":[],"k":"llm.load.yuzu.autoFit/title","v":"自动上下文长度","f":false},{"c":[],"k":"llm.load.yuzu.autoFit/subTitle","v":"加载时由运行时根据可用内存选择安全的上下文长度","f":false},{"c":[],"k":"llm.load.mlx.diskCache/title","v":"提示磁盘缓存","f":false},{"c":[],"k":"llm.load.mlx.diskCache/subTitle","v":"将提示状态缓存到磁盘，在多次请求之间复用","f":false},{"c":["presets"],"k":"saveChanges","v":"保存","f":false},{"c":["presets"],"k":"saveChanges/description","v":"将您的更改保存到预设。","f":false},{"c":["presets"],"k":"saveChanges.manual","v":"检测到新字段。您可以选择要将哪些更改保存到预设中。","f":false},{"c":["presets"],"k":"saveChanges.manual.hold.0","v":"按住","f":false},{"c":["presets"],"k":"saveChanges.manual.hold.1","v":"以选择要保存到预设的更改。","f":false},{"c":["presets"],"k":"saveChanges.saveAll.hold.0","v":"按住","f":false},{"c":["presets"],"k":"saveChanges.saveAll.hold.1","v":"以保存全部更改。","f":false},{"c":["presets"],"k":"saveChanges.saveInPreset.hold.0","v":"按住","f":false},{"c":["presets"],"k":"saveChanges.saveInPreset.hold.1","v":"以仅保存预设中已包含字段的更改。","f":false},{"c":["presets"],"k":"saveChanges/error","v":"保存预设更改失败。","f":false},{"c":["presets"],"k":"saveChanges.manual/description","v":"选择要包含在预设中的更改。","f":false},{"c":["presets"],"k":"cannotSaveChangesNoChanges","v":"没有可保存的更改。","f":false},{"c":[],"k":"reasoningBudgetUncheckedHint","v":"不限制","f":false}]},"discover":{"sigs":[["collectionsColumn","集合"],["collectionsColumn/collectionError","加载集合详情时出错，请尝试上方的刷新按钮"],["bookmarksColumn","书签"]],"ops":[]},"developer":{"sigs":[["tabs/server","本地服务器"],["tabs/extensions","LM 运行环境"],["loadSettings/title","加载设置"]],"ops":[{"c":[],"k":"serverOptions/allowMcp/title","v":"允许远程 MCP","f":false},{"c":[],"k":"serverOptions/allowMcp/hint","v":"允许使用 mcp.json 中未列出的 MCP。此类 MCP 连接是临时的，仅在请求期间存在。目前仅支持远程 MCP。","f":false},{"c":[],"k":"serverOptions/allowMcp/mode/off","v":"关闭","f":false},{"c":[],"k":"serverOptions/allowMcp/mode/off/hint","v":"不允许服务器请求使用 MCP","f":false},{"c":[],"k":"serverOptions/allowMcp/mode/remote","v":"远程","f":false},{"c":[],"k":"serverOptions/allowMcp/mode/remote/hint","v":"允许连接远程 MCP 服务器","f":false},{"c":[],"k":"serverOptions/start/error","v":"启动服务器失败","f":false},{"c":[],"k":"serverOptions/stop/error","v":"停止服务器失败","f":false},{"c":[],"k":"endpoints/openaiCompatRest/segmentedLabel","v":"OpenAI 兼容","f":false},{"c":[],"k":"endpoints/openaiCompatRest/postResponses","v":"生成模型响应的高级接口。将上一个响应的 id 作为输入传给下一个，即可创建有状态的交互。","f":false},{"c":[],"k":"endpoints/lmStudioRest/segmentedLabel","v":"LM Studio","f":false},{"c":[],"k":"endpoints/lmStudioRestV1/getModels","v":"列出可用模型","f":false},{"c":[],"k":"endpoints/lmStudioRestV1/postModelsLoad","v":"加载模型（含选项）","f":false},{"c":[],"k":"endpoints/lmStudioRestV1/postModelsDownload","v":"下载模型","f":false},{"c":[],"k":"endpoints/lmStudioRestV1/postChat","v":"与模型聊天。支持有状态多轮对话和 MCP","f":false},{"c":[],"k":"endpoints/lmStudioRestV1/getModelsDownloadStatus","v":"获取模型下载状态","f":false},{"c":[],"k":"endpoints/anthropicCompatRest/segmentedLabel","v":"Anthropic 兼容","f":false},{"c":[],"k":"endpoints/openaiCompatRest/title","v":"支持的端点{{extra}}（与 OpenAI 兼容的格式）","f":true},{"c":[],"k":"modelState/computingDecision","v":"正在计算决策","f":false}]},"download":{"sigs":[["postDownloadActionExecutor.zipExtraction/status","解压中..."],["postDownloadActionExecutor.tarGzExtraction/status","解压中..."],["postDownloadActionExecutor.runtimeIndexerTarGzExtraction/status","解压中..."]],"ops":[]},"settings":{"sigs":[["settingsDialogTitle","应用设置"],["settingsDialogButtonTooltip","应用设置"],["accountDialogButtonTooltip","账户"]],"ops":[{"c":[],"k":"appNavigationBarPositionLabel","v":"导航栏位置","f":false},{"c":[],"k":"appNavigationBarPositionTop","v":"顶部","f":false},{"c":[],"k":"appNavigationBarPositionLeft","v":"左侧","f":false},{"c":[],"k":"modelDefaultsLabel","v":"模型默认值","f":false},{"c":[],"k":"autoFitMinContextLength.label","v":"AutoFit 最小上下文长度","f":false},{"c":[],"k":"autoFitMinContextLength.description","v":"要求 AutoFit 至少提供这么多 token 的上下文。无法满足该最小要求的模型将加载失败。","f":false},{"c":[],"k":"modelLoadingGuardrails.alwaysAllowLoadAnyway","v":"（不推荐）始终允许「仍然加载」，无需按住 Alt/Option","f":false},{"c":["defaultContextLength"],"k":"label","v":"默认上下文长度","f":false},{"c":["defaultContextLength"],"k":"maxTitle","v":"模型最大值","f":false},{"c":["defaultContextLength"],"k":"customTitle","v":"自定义值","f":false},{"c":["defaultContextLength"],"k":"maxSubtitle","v":"使用每个模型支持的最大上下文长度。","f":false},{"c":["defaultContextLength"],"k":"customSubtitle","v":"设置加载新模型时的默认上下文长度。若模型支持的最大上下文长度更小，则使用那个值。","f":false},{"c":["defaultContextLength"],"k":"invalidNaNError","v":"无效的上下文长度值。将使用 {{value}}","f":false},{"c":["defaultContextLength"],"k":"invalidRangeError","v":"无效的上下文长度值。应在 1 到 2^30 之间。将使用 {{value}}","f":false},{"c":["defaultContextLength"],"k":"largeContextWarning","v":"上下文长度越大，模型占用的内存就越多。如不确定，请勿更改默认值","f":false},{"c":["jitTTL"],"k":"subtitle","v":"JIT 加载的模型在空闲指定时长后会被自动卸载。","f":false}]},"models":{"sigs":[["pageTitle","我的模型"],["filterModels.placeholder","筛选模型..."],["aggregate_one","您有 {{count}} 个本地模型，占用了 {{size}} 的磁盘空间。"]],"ops":[{"c":[],"k":"indexingPageLoaderText","v":"正在索引模型...","f":false},{"c":[],"k":"loader.guardrails.estimatedMemoryUsage","v":"预估内存占用","f":false},{"c":[],"k":"loader.guardrails.total","v":"总计","f":false},{"c":[],"k":"loader.guardrails.gpu","v":"GPU","f":false},{"c":[],"k":"loader.guardrails.unavailable","v":"无法预估该模型的内存占用","f":false},{"c":[],"k":"loader.guardrails.notEnoughResources","v":"当前设置下系统资源不足，无法加载该模型","f":false},{"c":[],"k":"loader.guardrails.notEnoughResources/options","v":"选项","f":false},{"c":[],"k":"loader.guardrails.notEnoughResources.moreInfoSection.appearsNotEnoughMemory","v":"您的系统内存似乎不足以加载该模型。","f":false},{"c":[],"k":"loader.guardrails.notEnoughResources.moreInfoSection.ifYouBelieveThisIsIncorrect","v":"您可以在设置中调整模型加载守卫，或按住 <altOptionKey /> 仍然加载。","f":false},{"c":[],"k":"loader.guardrails.notEnoughResources.moreInfoSection.warning","v":"加载过大的模型可能使系统过载，导致卡死。","f":false},{"c":[],"k":"loader.guardrails.notEnoughResources.alwaysAllowLoadAnyway","v":"（不推荐）始终允许「仍然加载」，无需按住 Alt/Option","f":false},{"c":["virtual","altsSelect"],"k":"title","v":"切换模型来源","f":false},{"c":["virtual","altsSelect"],"k":"resetButton","v":"恢复默认","f":false},{"c":["virtual","altsSelect"],"k":"description","v":"该模型有多个可用的源文件。","f":false},{"c":["virtual","altsSelect"],"k":"trigger","v":"变体","f":false},{"c":[],"k":"decisionModels","v":"决策模型","f":false},{"c":[],"k":"loader.info.activePredictionLoopHandlerWarning","v":"您正在使用带有活跃预测循环处理器的插件。当前加载的模型是否适用于该插件，取决于处理器的具体实现方式","f":false}]},"onboarding":{"sigs":[["action.skipOnboarding","跳过引导"],["action.next","下一步"],["action.back","上一步"]],"ops":[]},"shared":{"sigs":[["copyLmStudioLinkButton/toolTip","复制模型下载链接"],["filter.noMatches","没有匹配项"],["incompatible","不兼容"]],"ops":[{"c":[],"k":"beta","v":"测试版","f":false}]}},"beta_old":"简体中文 (Beta)","beta_new":"简体中文"}"""
)

# ---------------- console ----------------
_IS_TTY = sys.stdout.isatty()
if os.name == 'nt':
    os.system('')  # enable ANSI escape on Windows console
if not _IS_TTY:
    try:
        if sys.stdout.encoding and 'utf' not in sys.stdout.encoding.lower():
            sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass

class C:
    R = '\033[0m' if _IS_TTY else ''
    CYAN = '\033[96m' if _IS_TTY else ''
    BLUE = '\033[94m' if _IS_TTY else ''
    YELLOW = '\033[93m' if _IS_TTY else ''
    GREEN = '\033[92m' if _IS_TTY else ''
    RED = '\033[91m' if _IS_TTY else ''
    DIM = '\033[2m' if _IS_TTY else ''

def banner():
    line = '=' * 56
    print(C.CYAN + line + C.R)
    print(C.CYAN + '  LM Studio 简体中文补丁  ' + C.DIM + 'v' + VERSION + C.R)
    print(C.CYAN + line + C.R)
    print(C.BLUE + '  项目链接：' + C.R + 'https://github.com/HeLeiawa/lmstudio_chinese')
    print(C.BLUE + '  酷安：' + C.R + 'https://www.coolapk.com/u/43912900')
    print(C.BLUE + '  B站：' + C.R + 'https://space.bilibili.com/397051896')
    print(C.YELLOW + '  开发者：HeLei_awa' + C.R)
    print(C.CYAN + line + C.R)
    print()

# ---------------- install dir discovery ----------------
def _valid_install_dir(d):
    if not d:
        return False
    return os.path.isfile(os.path.join(d, 'resources', 'app', '.webpack', 'renderer', 'main_window.js'))

def _registry_candidates():
    out, seen = [], set()
    try:
        import winreg
    except ImportError:
        return out
    roots = [winreg.HKEY_CURRENT_USER, winreg.HKEY_LOCAL_MACHINE]
    subs = [r'Software\Microsoft\Windows\CurrentVersion\Uninstall',
            r'Software\WOW6432Node\Microsoft\Windows\CurrentVersion\Uninstall']
    for root in roots:
        for sub in subs:
            try:
                k = winreg.OpenKey(root, sub)
            except OSError:
                continue
            i = 0
            while True:
                try:
                    name = winreg.EnumKey(k, i)
                    i += 1
                except OSError:
                    break
                try:
                    sk = winreg.OpenKey(k, name)
                    disp = winreg.QueryValueEx(sk, 'DisplayName')[0]
                except OSError:
                    continue
                if 'lm studio' not in disp.lower():
                    continue
                for val in ('InstallLocation', 'DisplayIcon'):
                    try:
                        v = winreg.QueryValueEx(sk, val)[0].strip('"').strip()
                    except OSError:
                        continue
                    if v.lower().endswith('.exe'):
                        v = os.path.dirname(v)
                    if v and v.lower() not in seen and _valid_install_dir(v):
                        seen.add(v.lower())
                        out.append(v)
    return out

def _common_candidates():
    envs = [
        r'%LOCALAPPDATA%\Programs\lm-studio',
        r'%LOCALAPPDATA%\Programs\LM Studio',
        r'%ProgramFiles%\LM Studio',
        r'%ProgramFiles%\lm-studio',
        r'%ProgramFiles(x86)%\LM Studio',
        r'K:\LM Studio',
    ]
    return [os.path.expandvars(e) for e in envs if _valid_install_dir(os.path.expandvars(e))]

def find_install_dir(explicit, interactive):
    if explicit:
        if _valid_install_dir(explicit):
            return explicit
        print(C.RED + '[错误] 指定目录无效（未找到 resources\\app\\.webpack\\renderer\\main_window.js）: ' + explicit + C.R)
        return None
    cands = []
    for d in _registry_candidates() + _common_candidates():
        if d.lower() not in [x.lower() for x in cands]:
            cands.append(d)
    if not cands:
        if not interactive:
            print(C.RED + '[错误] 未找到 LM Studio 安装目录。' + C.R)
            print('请用 --dir 指定，例如: python lmstudio_chinese_patch.py --dir "K:\\LM Studio"')
            return None
        print(C.YELLOW + '未自动找到 LM Studio 安装目录。' + C.R)
        d = input('请输入 LM Studio 安装目录路径（例如 K:\\LM Studio）: ').strip().strip('"')
        if _valid_install_dir(d):
            return d
        print(C.RED + '[错误] 目录无效: ' + d + C.R)
        return None
    if len(cands) == 1:
        return cands[0]
    if not interactive:
        return cands[0]
    print('发现多个 LM Studio 安装目录：')
    for i, d in enumerate(cands, 1):
        print(f'  [{i}] {d}')
    while True:
        s = input('输入序号选择目录: ').strip()
        if s.isdigit() and 1 <= int(s) <= len(cands):
            return cands[int(s) - 1]
        print(C.YELLOW + '输入无效，请重新输入。' + C.R)

# ---------------- payload helpers ----------------
def js_unescape(s):
    out = []
    i = 0
    while i < len(s):
        c = s[i]
        if c == '\\':
            nxt = s[i+1] if i+1 < len(s) else ''
            mapping = {'\\':'\\', "'":"'", '"':'"', 'n':'\n', 't':'\t', 'r':'\r', 'b':'\b', 'f':'\f', 'v':'\v', '0':'\0'}
            if nxt in mapping: out.append(mapping[nxt]); i += 2; continue
            if nxt == 'u': out.append(chr(int(s[i+2:i+6], 16))); i += 6; continue
            if nxt == 'x': out.append(chr(int(s[i+2:i+4], 16))); i += 4; continue
            out.append(nxt); i += 2; continue
        out.append(c); i += 1
    return ''.join(out)

def js_escape(s):
    return s.replace('\\', '\\\\').replace("'", "\\'")

def load_renderer(install_dir):
    path = os.path.join(install_dir, 'resources', 'app', '.webpack', 'renderer', 'main_window.js')
    raw = open(path, 'rb').read()
    try:
        text = raw.decode('utf-8')
    except UnicodeDecodeError:
        print(C.RED + '[错误] main_window.js 不是有效的 UTF-8 文件，中止。' + C.R)
        sys.exit(1)
    return path, text

def locate_payload(text, sigs):
    anchor_key, anchor_val = sigs[0]
    anchor = '"%s":"%s"' % (anchor_key, anchor_val)
    pos = 0
    while True:
        hit = text.find(anchor, pos)
        if hit == -1:
            return None
        pos = hit + 1
        jstart = text.rfind("JSON.parse('", 0, hit)
        if jstart == -1 or hit - jstart > 5000000:
            continue
        qs = jstart + len("JSON.parse('")
        i = qs
        end = None
        while i < len(text):
            c = text[i]
            if c == '\\': i += 2; continue
            if c == "'": end = i; break
            i += 1
        if end is None:
            continue
        payload = js_unescape(text[qs:end])
        try:
            obj = json.loads(payload)
        except Exception:
            continue
        if not isinstance(obj, dict):
            continue
        if all(obj.get(k) == v for k, v in sigs):
            return qs, end, payload
    return None

def apply_ops(obj, ops):
    applied = 0
    already = 0
    for op in ops:
        node = obj
        for ck in op['c']:
            if ck not in node or not isinstance(node[ck], dict):
                node[ck] = {}
            node = node[ck]
        if op['k'] in node and node[op['k']] == op['v']:
            already += 1
            continue
        if op['f'] or op['k'] not in node:
            node[op['k']] = op['v']
            applied += 1
        else:
            already += 1
    return applied, already

def lm_studio_running():
    try:
        r = subprocess.run(['tasklist', '/FI', 'IMAGENAME eq LM Studio.exe'],
                           capture_output=True, timeout=10,
                           creationflags=0x08000000)
        return b'LM Studio.exe' in r.stdout
    except Exception:
        return False

# ---------------- actions ----------------
def get_state(install_dir):
    _, text = load_renderer(install_dir)
    has_beta = ('children:"%s"' % PATCH_DATA['beta_old']) in text
    ok = True
    for ns, nd in PATCH_DATA['namespaces'].items():
        if not nd['ops']:
            continue
        loc = locate_payload(text, nd['sigs'])
        if loc is None:
            ok = False
            continue
        obj = json.loads(loc[2])
        _, already = apply_ops(obj, nd['ops'])
        if already != len(nd['ops']):
            ok = False
    return ok and not has_beta

def do_status(install_dir):
    path, text = load_renderer(install_dir)
    print('目标文件:', path)
    print('文件大小: %.1f MB' % (len(text.encode('utf-8')) / 1048576))
    has_beta = ('children:"%s"' % PATCH_DATA['beta_old']) in text
    print('语言列表 Beta 标记:', '仍存在（未打补丁）' if has_beta else '已移除')
    all_done = True
    for ns, nd in PATCH_DATA['namespaces'].items():
        if not nd['ops']:
            continue
        loc = locate_payload(text, nd['sigs'])
        if loc is None:
            print(C.YELLOW + f'  [{ns}] 未找到翻译模块（LM Studio 版本可能已更新）' + C.R)
            all_done = False
            continue
        obj = json.loads(loc[2])
        _, already = apply_ops(obj, nd['ops'])
        n = len(nd['ops'])
        if already != n:
            all_done = False
            print(f'  [{ns:10}] {already}/{n} 条翻译已就位 ' + C.YELLOW + f'（缺 {n - already} 条）' + C.R)
        else:
            print(f'  [{ns:10}] {already}/{n} 条翻译已就位 ' + C.GREEN + '完整' + C.R)
    print('总体状态:', (C.GREEN + '补丁已完整应用' + C.R) if all_done else (C.YELLOW + '补丁未完整应用' + C.R))
    return all_done

def do_apply(install_dir):
    path, text = load_renderer(install_dir)
    backup = path + BACKUP_SUFFIX
    print('目标文件:', path)
    located = {}
    for ns, nd in PATCH_DATA['namespaces'].items():
        if not nd['ops']:
            continue
        loc = locate_payload(text, nd['sigs'])
        if loc is None:
            print(C.RED + f'[错误] 未找到 [{ns}] 的翻译模块，文件结构可能已变化，未做任何修改。' + C.R)
            print('LM Studio 更新后需要等待适配新版本的补丁。')
            sys.exit(1)
        located[ns] = loc
    if not os.path.exists(backup):
        shutil.copy2(path, backup)
        print(C.GREEN + '已创建备份: ' + backup + C.R)
    else:
        print('备份已存在，保留最早的原始备份: ' + backup)
    splices = []
    total_applied = 0
    for ns, (qs, end, payload) in located.items():
        obj = json.loads(payload)
        applied, already = apply_ops(obj, PATCH_DATA['namespaces'][ns]['ops'])
        total_applied += applied
        new_payload = json.dumps(obj, ensure_ascii=False, separators=(',', ':'))
        new_escaped = js_escape(new_payload)
        if new_escaped != text[qs:end]:
            splices.append((qs, end, new_escaped, ns, applied, already))
        else:
            print(f'  [{ns:10}] 已是最新（无需修改）')
    for qs, end, new_escaped, ns, applied, already in sorted(splices, reverse=True):
        text = text[:qs] + new_escaped + text[end:]
        print(f'  [{ns:10}] 新增 {applied} 条翻译（此前已就位 {already} 条）')
    beta_old = 'children:"%s"' % PATCH_DATA['beta_old']
    beta_new = 'children:"%s"' % PATCH_DATA['beta_new']
    cnt = text.count(beta_old)
    if cnt == 1:
        text = text.replace(beta_old, beta_new)
        print('  [语言列表] 已移除「简体中文 (Beta)」的 Beta 标记')
    elif cnt == 0:
        print('  [语言列表] Beta 标记不存在（可能已移除）')
    else:
        print(C.YELLOW + f'[警告] Beta 标记出现 {cnt} 次，跳过该处修改' + C.R)
    for ns in located:
        loc2 = locate_payload(text, PATCH_DATA['namespaces'][ns]['sigs'])
        if loc2 is None:
            print(C.RED + f'[错误] 修改后校验失败: [{ns}]，已中止写入（文件未被修改）。' + C.R)
            sys.exit(1)
        json.loads(loc2[2])
    raw = text.encode('utf-8')
    with open(path, 'wb') as f:
        f.write(raw)
    print(C.GREEN + f'完成: 共新增 {total_applied} 条翻译，文件已写入。' + C.R)
    if lm_studio_running():
        print(C.YELLOW + '检测到 LM Studio 正在运行，请完全退出（含托盘图标）后重新打开。' + C.R)
    else:
        print('请启动 LM Studio，在 Settings - Language 中选择「简体中文」。')

def do_restore(install_dir):
    path, _ = load_renderer(install_dir)
    backup = path + BACKUP_SUFFIX
    if not os.path.exists(backup):
        print(C.RED + '[错误] 未找到备份文件，无法卸载: ' + backup + C.R)
        sys.exit(1)
    shutil.copy2(backup, path)
    print(C.GREEN + '已恢复原始文件（补丁已卸载）: ' + path + C.R)
    if lm_studio_running():
        print(C.YELLOW + '检测到 LM Studio 正在运行，请完全退出（含托盘图标）后重新打开。' + C.R)

# ---------------- interactive ----------------
def pause_exit():
    print()
    try:
        input('按回车键退出...')
    except EOFError:
        pass
    sys.exit(0)

def interactive():
    banner()
    print('正在查找 LM Studio 安装目录...')
    install_dir = find_install_dir(None, True)
    if not install_dir:
        pause_exit()
    print(C.GREEN + 'LM Studio 目录: ' + install_dir + C.R)
    try:
        installed = get_state(install_dir)
    except Exception as e:
        print(C.RED + '[错误] 读取文件失败: ' + str(e) + C.R)
        pause_exit()
    print('当前补丁状态: ' + ((C.GREEN + '已安装' + C.R) if installed else (C.YELLOW + '未安装' + C.R)))
    print()
    print('请选择操作：')
    print('  [1] 安装中文补丁')
    print('  [2] 卸载中文补丁')
    choice = input('输入对应数字回车开始执行（q 退出）: ').strip().lower()
    if choice == '1':
        do_apply(install_dir)
    elif choice == '2':
        do_restore(install_dir)
    elif choice in ('q', 'quit', 'exit', ''):
        print('已退出，未做任何修改。')
    else:
        print(C.YELLOW + '无效输入，未做任何修改。' + C.R)
    pause_exit()

def main():
    args = sys.argv[1:]
    mode = None
    explicit_dir = None
    it = iter(args)
    for a in it:
        if a == '--apply':
            mode = 'apply'
        elif a in ('--restore', '--uninstall'):
            mode = 'restore'
        elif a == '--status':
            mode = 'status'
        elif a == '--dir':
            explicit_dir = next(it, None)
        elif a in ('-h', '--help'):
            print(__doc__)
            sys.exit(0)
        else:
            print('未知参数:', a)
            sys.exit(1)
    if mode is None:
        interactive()
        return
    banner()
    install_dir = find_install_dir(explicit_dir, False)
    if not install_dir:
        sys.exit(1)
    print('LM Studio 目录:', install_dir)
    if mode == 'apply':
        do_apply(install_dir)
    elif mode == 'restore':
        do_restore(install_dir)
    else:
        do_status(install_dir)

if __name__ == '__main__':
    main()
