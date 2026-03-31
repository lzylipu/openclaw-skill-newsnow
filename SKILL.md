---
name: "newsnow-skill"
description: "NewsNow 热点新闻技能 - 基于 ourongxing/newsnow 项目，提供每日热点速览服务"
---

# NewsNow 热点新闻技能

基于 [ourongxing/newsnow](https://github.com/ourongxing/newsnow) 项目改造的 OpenClaw Skill。

## 功能特性

- ✅ **多源新闻聚合**: 40+ 新闻源实时抓取
- ✅ **分类精准**: 信访/治理、时政、社会民生、法律政策等分类
- ✅ **本地化支持**: 优先洛阳本地新闻
- ✅ **定时任务**: 每日7点自动生成《每日热点速览》
- ✅ **格式规范**: 符合简报格式要求

## 使用方法

### 1. 配置环境变量
```bash
# NewsNow API 基础 URL
export NEWSNOW_BASE_URL="https://newsnow.busiyi.world"

# 或者部署自己的实例
export NEWSNOW_BASE_URL="http://localhost:3000"
```

### 2. 调用技能
```python
from newsnow_skill import NewsNowClient

client = NewsNowClient()
daily_brief = client.generate_daily_brief()
print(daily_brief)
```

### 3. 定时任务配置
```yaml
# OpenClaw 定时任务配置
- name: "daily-hotspot"
  schedule: "0 7 * * *"  # 每天7点
  command: "python3 /path/to/newsnow-skill/daily_brief.py"
  channel: "openclaw-weixin"
```

## 输出格式

```
《每日热点速览》 YYYY年MM月DD日 星期X HH:mm
洛阳天气：xx，xx℃~xx℃

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

支持自定义新闻源，修改 `sources.json`:

```json
{
  "categories": {
    "信访/治理": ["洛阳网", "人民网", "新华网"],
    "时政": ["人民日报", "央视新闻", "新华社"],
    "社会民生": ["澎湃新闻", "南方都市报", "大河报"],
    "法律政策": ["法制日报", "中国法院网", "司法部官网"],
    "热点补充": ["今日头条", "微博热搜", "知乎热榜"]
  }
}
```

## 部署选项

### 选项1: 使用公共 API
- 直接调用 `https://newsnow.busiyi.world`
- 无需部署，开箱即用

### 选项 2: 自主部署
```bash
git clone https://github.com/ourongxing/newsnow.git
cd newsnow
pnpm install
pnpm run build
# 部署到 Cloudflare Pages 或 Vercel
```

### 选项 3: Docker 部署
```bash
docker-compose up -d
# 默认端口 3000
```

## 错误处理

- **网络错误**: 自动重试 3 次
- **API 限流**: 启用缓存机制
- **无新闻**: 返回占位格式，保留栏目结构

## 许可证

MIT License - ourongxing/newsnow