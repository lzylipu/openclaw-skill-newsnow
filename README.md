# NewsNow 热点新闻技能 - OpenClaw Skill

基于 [ourongxing/newsnow](https://github.com/ourongxing/newsnow) 项目改造的 OpenClaw Skill，提供每日热点速览服务。

## 功能特性

- **多源新闻聚合**: 40+ 新闻源实时抓取
- **分类精准**: 信访/治理、时政、社会民生、法律政策等分类
- **本地化支持**: 优先本地新闻
- **定时任务**: 每日自动生成《每日热点速览》
- **格式规范**: 符合简报格式要求

## 安装

### 1. 安装依赖

```bash
pip install requests
```

### 2. 配置环境变量

```bash
# NewsNow API 基础 URL
export NEWSNOW_BASE_URL="https://newsnow.busiyi.world"

# 或者部署自己的实例
export NEWSNOW_BASE_URL="http://localhost:3000"
```

### 3. 安装到OpenClaw

将此技能目录复制到OpenClaw的skills目录：

```bash
cp -r newsnow-skill /path/to/openclaw/skills/
```

## 使用方法

### 命令行使用

```bash
# 生成每日简报
python3 daily_brief_task.py

# 使用客户端
python3 newsnow_client.py --help
```

### OpenClaw定时任务配置

```yaml
# OpenClaw 定时任务配置
- name: "daily-hotspot"
  schedule: "0 7 * * *"  # 每天7点
  command: "python3 /path/to/newsnow-skill/daily_brief_task.py"
  channel: "openclaw-weixin"
```

### 在对话中使用

```
用户: 今日热点
AI: 正在获取热点新闻...

《每日热点速览》 2026年03月31日 星期一 07:00
洛阳天气：晴，15℃~25℃

一、信访/治理
关键词1：一句话概述
关键词2：一句话概述

二、时政
关键词1：一句话概述
关键词2：一句话概述

...
```

## 输出格式

```
《每日热点速览》 YYYY年MM月DD日 星期X HH:mm
城市天气：xx，xx℃~xx℃

一、信访/治理
关键词1：一句话概述
关键词2：一句话概述

二、时政
关键词1：一句话概述
关键词2：一句话概述

三、社会民生
关键词1：一句话概述
关键词2：一句话概述

四、法律政策
关键词1：一句话概述
关键词2：一句话概述

五、热点补充
关键词1：一句话概述
关键词2：一句话概述

今日关注：一句话总结当天最值得关注的重点
```

## 新闻源配置

支持自定义新闻源，修改配置即可：

- **信访/治理**: 洛阳网、人民网、新华网等
- **时政**: 人民日报、央视新闻、新华社等
- **社会民生**: 澎湃新闻、南方都市报等
- **法律政策**: 法制日报、中国法院网等
- **热点补充**: 今日头条、微博热搜、知乎热榜等

## 部署选项

### 选项1: 使用公共API
- 直接调用 `https://newsnow.busiyi.world`
- 无需部署，开箱即用

### 选项2: 自主部署

```bash
# 克隆原项目
git clone https://github.com/ourongxing/newsnow.git
cd newsnow
pnpm install
pnpm run build

# 部署到 Cloudflare Pages 或 Vercel
```

### 选项3: Docker部署

```bash
docker-compose up -d
# 默认端口 3000
```

## 技术实现

- **Python 3** - 主要编程语言
- **requests** - HTTP请求库
- **NewsNow API** - 新闻数据源
- **定时任务** - OpenClaw调度器

## 错误处理

- **网络错误**: 自动重试 3 次
- **API限流**: 启用缓存机制
- **无新闻**: 返回占位格式，保留栏目结构

## 目录结构

```
newsnow-skill/
├── SKILL.md                 # 技能说明文档
├── README.md                # 本文件
├── newsnow_client.py        # NewsNow API客户端
├── daily_brief_task.py      # 每日简报任务
├── prompt_template.md       # 提示词模板
└── complete_prompt.md       # 完整提示词
```

## 注意事项

- 需要网络访问NewsNow API
- 建议配置定时任务实现自动化
- 可根据需要调整新闻源和分类

## 致谢

本项目基于 [ourongxing/newsnow](https://github.com/ourongxing/newsnow) 开源项目改造，感谢原作者的贡献。

## 许可证

MIT License

## 作者

OpenClaw Community

## 相关链接

- [OpenClaw](https://github.com/openclaw/openclaw)
- [NewsNow原项目](https://github.com/ourongxing/newsnow)