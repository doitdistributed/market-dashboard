import type { MarketData } from '../types';
import { formatPrice } from '../utils/formatting';

function formatPct(val?: number): string {
  if (val === undefined || val === null || Number.isNaN(val)) return '—';
  const sign = val > 0 ? '+' : '';
  const emoji = val > 0 ? '📈' : val < 0 ? '📉' : '➖';
  return `${emoji} ${sign}${val.toFixed(2)}%`;
}

export async function sendHotWatchlistToGoogleChat(
  webhookUrl: string,
  items: MarketData[]
): Promise<boolean> {
  if (!webhookUrl || !webhookUrl.trim()) {
    throw new Error('Bitte gib eine gültige Google Chat Webhook URL in den Einstellungen an.');
  }

  if (!items || items.length === 0) {
    throw new Error('Keine Assets in der Hot Watch List vorhanden.');
  }

  const uptrendItems = items.filter((i) => i.ema_uptrend === true);
  const downtrendItems = items.filter((i) => i.ema_uptrend === false);
  const otherItems = items.filter((i) => i.ema_uptrend === undefined);

  const lines = ['🔥 *HOT WATCH LIST — TREND SUMMARY*', ''];

  if (uptrendItems.length > 0) {
    lines.push('🟢 *IM AUFWÄRTSTREND (10-EMA > 20-EMA):*');
    uptrendItems.forEach((item) => {
      const name = item.name || item.sym;
      const priceStr = item.price !== undefined ? formatPrice(item.price) : '—';
      const d1Str = formatPct(item.d1);
      const w1Str = formatPct(item.w1);
      lines.push(`  • ✅ *${name}* (${item.sym}): ${priceStr} | 1D: ${d1Str} | 1W: ${w1Str}`);
    });
    lines.push('');
  }

  if (downtrendItems.length > 0) {
    lines.push('🔴 *IM ABWÄRTSTREND / NEUTRAL:*');
    downtrendItems.forEach((item) => {
      const name = item.name || item.sym;
      const priceStr = item.price !== undefined ? formatPrice(item.price) : '—';
      const d1Str = formatPct(item.d1);
      const w1Str = formatPct(item.w1);
      lines.push(`  • ❌ *${name}* (${item.sym}): ${priceStr} | 1D: ${d1Str} | 1W: ${w1Str}`);
    });
    lines.push('');
  }

  if (otherItems.length > 0) {
    lines.push('⚪ *WEITERE ASSETS:*');
    otherItems.forEach((item) => {
      const name = item.name || item.sym;
      const priceStr = item.price !== undefined ? formatPrice(item.price) : '—';
      const d1Str = formatPct(item.d1);
      const w1Str = formatPct(item.w1);
      lines.push(`  • *${name}* (${item.sym}): ${priceStr} | 1D: ${d1Str} | 1W: ${w1Str}`);
    });
    lines.push('');
  }

  lines.push(`_Gesendet aus Market Dashboard · ${new Date().toLocaleTimeString()} Uhr_`);

  const text = lines.join('\n');

  try {
    const response = await fetch(webhookUrl.trim(), {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json; charset=UTF-8',
      },
      body: JSON.stringify({ text }),
    });

    if (!response.ok) {
      const errText = await response.text().catch(() => '');
      throw new Error(`HTTP ${response.status}: ${errText || response.statusText}`);
    }

    return true;
  } catch (err) {
    console.error('Failed to post to Google Chat Webhook:', err);
    throw err;
  }
}
