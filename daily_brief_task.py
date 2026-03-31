#!/usr/bin/env python3
"""
NewsNow 每日热点速览定时任务
每天7点自动生成并发送到微信
"""

import os
import sys
import json
from datetime import datetime, time as dtime
import subprocess

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from newsnow_client import NewsNowClient

def send_to_wechat(message: str):
    """发送消息到当前微信（模拟实现）"""
    try:
        # 这里应该调用 OpenClaw 的 message 工具
        # 由于在独立脚本中，先打印消息
        print(message)
        
        # 实际部署时替换为：
        # subprocess.run([
        #     "openclaw", "message", "send",
        #     "--channel", "openclaw-weixin",
        #     "--message", message
        # ])
        
    except Exception as e:
        print(f"发送失败: {e}")

def main():
    """主函数 - 生成并发送每日热点速览"""
    try:
        print(f"开始生成每日热点速览 - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        
        # 创建 NewsNow 客户端
        client = NewsNowClient()
        
        # 生成热点速览
        daily_brief = client.generate_daily_brief()
        
        # 发送到微信
        send_to_wechat(daily_brief)
        
        print("每日热点速览发送完成！")
        
        # 保存备份
        backup_file = f"/vol1/@apphome/trim.openclaw/data/workspace/skills/newsnow-skill/history/daily-hotspot-{datetime.now().strftime('%Y%m%d')}.txt"
        os.makedirs(os.path.dirname(backup_file), exist_ok=True)
        with open(backup_file, 'w', encoding='utf-8') as f:
            f.write(daily_brief)
        
        print(f"备份已保存: {backup_file}")
        
    except Exception as e:
        print(f"任务执行失败: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()