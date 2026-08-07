#!/usr/bin/env python3
"""
Send a Google Chat notification with the daily Hot Watch List summary.
Usage:
  python scripts/notify_google_chat.py [--url WEBHOOK_URL] [--watchlist SYM1,SYM2]
Environment variables:
  GOOGLE_CHAT_WEBHOOK_URL: Webhook URL for Google Chat space
  GOOGLE_CHAT_WATCHLIST: Comma-separated list of symbols to include
"""

import json
import os
import sys
import argparse
from pathlib import Path
import urllib.request
import urllib.error

def format_pct(val):
    if val is None:
        return "—"
    sign = "+" if val > 0 else ""
    emoji = "📈" if val > 0 else "📉" if val < 0 else "➖"
    return f"{emoji} {sign}{val:.2f}%"

def format_price(val):
    if val is None:
        return "—"
    if val >= 1000:
        return f"${val:,.2f}"
    elif val >= 1:
        return f"${val:.2f}"
    else:
        return f"${val:.4f}"

def load_market_data():
    data_path = Path(__file__).parent.parent / "public" / "data.json"
    if not data_path.exists():
        print(f"Error: {data_path} not found.")
        return None
    with open(data_path, "r", encoding="utf-8") as f:
        return json.load(f)

def build_message_text(data, watchlist_symbols=None):
    all_items = {}
    categories = [
        "portfolio_core",
        "portfolio_us_tech",
        "portfolio_software",
        "portfolio_europe",
        "portfolio_energy",
        "portfolio_watchlist",
        "futures",
        "crypto",
        "metals",
        "commodities",
        "yields",
        "global",
    ]

    for cat in categories:
        for item in data.get(cat, []):
            sym = item.get("sym")
            if sym and sym not in all_items:
                all_items[sym] = item

    selected_items = []
    if watchlist_symbols:
        for sym in watchlist_symbols:
            clean_sym = sym.strip()
            if clean_sym in all_items:
                selected_items.append(all_items[clean_sym])
    else:
        # If no watchlist specified, default to top core items & movers
        for cat in ["portfolio_core", "portfolio_us_tech", "futures", "crypto"]:
            for item in data.get(cat, [])[:4]:
                if item["sym"] not in [x["sym"] for x in selected_items]:
                    selected_items.append(item)

def format_simple_pct(val):
    if val is None:
        return "—"
    sign = "+" if val > 0 else ""
    return f"{sign}{val:.2f}%"

def format_trend_icon(val):
    if val is True:
        return "✅"
    elif val is False:
        return "❌"
    return "—"

def build_message_text(data, watchlist_symbols=None):
    all_items = {}
    categories = [
        "portfolio_core",
        "portfolio_us_tech",
        "portfolio_software",
        "portfolio_europe",
        "portfolio_energy",
        "portfolio_watchlist",
        "futures",
        "crypto",
        "metals",
        "commodities",
        "yields",
        "global",
    ]

    for cat in categories:
        for item in data.get(cat, []):
            sym = item.get("sym")
            if sym and sym not in all_items:
                all_items[sym] = item

    selected_items = []
    if watchlist_symbols:
        for sym in watchlist_symbols:
            clean_sym = sym.strip()
            if clean_sym in all_items:
                selected_items.append(all_items[clean_sym])
    else:
        for cat in ["portfolio_core", "portfolio_us_tech", "futures", "crypto"]:
            for item in data.get(cat, [])[:4]:
                if item["sym"] not in [x["sym"] for x in selected_items]:
                    selected_items.append(item)

    if not selected_items:
        return "🔥 *Hot Watch List Daily Update*\nNo selected assets found in current market data."

    lines = ["🔥 *HOT WATCH LIST — TREND MONITOR*", "```"]
    lines.append(f"{'SYMBOL':<10} {'PREIS':>9} {'1D%':>8} {'1W%':>8}   {'5/10':^4} {'5/15':^4} {'10/20':^4}")
    lines.append("-" * 55)

    for item in selected_items:
        sym = item.get("sym", "")[:10]
        price = format_price(item.get("price"))
        d1 = format_simple_pct(item.get("d1"))
        w1 = format_simple_pct(item.get("w1"))
        
        t_5_10 = format_trend_icon(item.get("ema_5_10"))
        t_5_15 = format_trend_icon(item.get("ema_5_15"))
        t_10_20 = format_trend_icon(item.get("ema_uptrend"))

        lines.append(f"{sym:<10} {price:>9} {d1:>8} {w1:>8}   {t_5_10:^4} {t_5_15:^4} {t_10_20:^4}")

    lines.append("```")
    lines.append("*Trend-Legende:*")
    lines.append("• *5/10*: Hyper-sensibel (EMA 5 > 10)")
    lines.append("• *5/15*: Die goldene Mitte (EMA 5 > 15)")
    lines.append("• *10/20*: Standard (EMA 10 > 20)")

    generated_at = data.get("generatedAt")
    if generated_at:
        lines.append("")
        lines.append(f"_Stand: {generated_at}_")

    return "\n".join(lines).strip()

def send_notification(webhook_url, text):
    payload = json.dumps({"text": text}).encode("utf-8")
    req = urllib.request.Request(
        webhook_url,
        data=payload,
        headers={"Content-Type": "application/json; charset=UTF-8"},
        method="POST"
    )
    try:
        with urllib.request.urlopen(req) as resp:
            print(f"Notification sent successfully! HTTP Status: {resp.status}")
            return True
    except urllib.error.HTTPError as e:
        print(f"Failed to send notification: HTTP {e.code} - {e.reason}")
        print(e.read().decode("utf-8", errors="ignore"))
        return False
    except Exception as e:
        print(f"Error sending webhook notification: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description="Send Google Chat Notification")
    parser.add_argument("--url", help="Google Chat Webhook URL")
    parser.add_argument("--watchlist", help="Comma-separated list of symbols")
    parser.add_argument("--dry-run", action="store_true", help="Print message without sending")
    args = parser.parse_args()

    webhook_url = args.url or os.environ.get("GOOGLE_CHAT_WEBHOOK_URL")
    watchlist_env = args.watchlist or os.environ.get("GOOGLE_CHAT_WATCHLIST")
    
    watchlist_symbols = [s.strip() for s in watchlist_env.split(",")] if watchlist_env else None

    data = load_market_data()
    if not data:
        sys.exit(1)

    message_text = build_message_text(data, watchlist_symbols)

    if args.dry_run or not webhook_url:
        print("=== DRY RUN / NO WEBHOOK URL CONFIGURED ===")
        print(message_text)
        if not webhook_url:
            print("\nNote: Set GOOGLE_CHAT_WEBHOOK_URL environment variable to send.")
        sys.exit(0)

    success = send_notification(webhook_url, message_text)
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
