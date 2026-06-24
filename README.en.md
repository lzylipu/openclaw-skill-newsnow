# NewsNow Skill - OpenClaw Skill

**[English](./README.en.md) | [中文](./README.md)**

News aggregation skill based on [ourongxing/newsnow](https://github.com/ourongxing/newsnow), providing daily hotspot briefs.

## Features

- **Multi-source aggregation**: 40+ news sources fetched in real-time
- **Categorized**: Petition/Governance, Politics, Society, Law & Policy, etc.
- **Local support**: Prioritizes local news
- **Scheduled**: Daily auto-generate "Daily Hotspot Brief"
- **Structured output**: Follows brief formatting standards

## Installation

### 1. Install Dependencies

```bash
pip install requests
```

### 2. Configure Environment

```bash
# NewsNow API base URL
export NEWSNOW_BASE_URL="https://your-newsnow-instance.example.com"

# Or deploy your own instance
export NEWSNOW_BASE_URL="http://localhost:3000"
```

### 3. Install to OpenClaw

Copy the skill directory to OpenClaw's skills folder:

```bash
cp -r newsnow-skill /path/to/openclaw/skills/
```

## Usage

### Command Line

```bash
# Generate daily brief
python3 daily_brief_task.py

# Use client directly
python3 newsnow_client.py --help
```

### Cron Task

```yaml
- name: "daily-hotspot"
  schedule: "0 7 * * *"
  command: "python3 /path/to/newsnow-skill/daily_brief_task.py"
  channel: "openclaw-weixin"
```

### In Chat

```
User: 今日热点
AI: Fetching trending news...

《Daily Hotspot Brief》 2026-03-31 Monday 07:00
City Weather: xx, xx℃~xx℃

I. Petition/Governance
Keyword1: One-line summary

II. Politics
Keyword1: One-line summary

III. Society
Keyword1: One-line summary

IV. Law & Policy
Keyword1: One-line summary

V. Supplement
Keyword1: One-line summary

Today's Focus: One-sentence highlight
```

## News Source Configuration

Customizable news sources — edit config to adjust:

- **Petition/Governance**: Local news, People's Daily, Xinhua
- **Politics**: People's Daily, CCTV News, Xinhua
- **Society**: The Paper, Southern Metropolis Daily
- **Law & Policy**: Legal Daily, China Court Network
- **Supplement**: Toutiao, Weibo Hot, Zhihu Hot

## Deployment Options

### Option 1: Public API
- Call `https://your-newsnow-instance.example.com` directly
- Zero deploy, works out of the box

### Option 2: Self-Hosted

```bash
git clone https://github.com/ourongxing/newsnow.git
cd newsnow
pnpm install
pnpm run build
# Deploy to Cloudflare Pages or Vercel
```

### Option 3: Docker

```bash
docker-compose up -d
# Default port 3000
```

## Technical Stack

- **Python 3** - Main language
- **requests** - HTTP client
- **NewsNow API** - News data source
- **Cron** - OpenClaw scheduler

## Error Handling

- **Network error**: Auto-retry 3 times
- **API rate limit**: Enable caching
- **No news**: Return placeholder format preserving structure

## File Structure

```
newsnow-skill/
├── SKILL.md                 # Skill specification
├── README.md                # Chinese README
├── README.en.md             # English README
├── newsnow_client.py        # NewsNow API client
├── daily_brief_task.py      # Daily brief task
├── prompt_template.md       # Prompt template
└── complete_prompt.md       # Complete prompt
```

## Notes

- Requires network access to NewsNow API
- Configure Cron for daily automation
- Adjust news sources and categories as needed

## Acknowledgements

Based on [ourongxing/newsnow](https://github.com/ourongxing/newsnow) open-source project.

## License

MIT License
