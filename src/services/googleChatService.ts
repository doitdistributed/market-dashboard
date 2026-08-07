import type { MarketData } from '../types';
import { formatPrice } from '../utils/formatting';

function formatSimplePct(val?: number): string {
  if (val === undefined || val === null || Number.isNaN(val)) return '—';
  const sign = val > 0 ? '+' : '';
  return `${sign}${val.toFixed(2)}%`;
}

function formatTrendIcon(val?: boolean): string {
  if (val === true) return '✅';
  if (val === false) return '❌';
  return '—';
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

  const lines = ['🔥 *HOT WATCH LIST — TREND MONITOR*', '```'];
  lines.push(`${'SYMBOL'.padEnd(10)} ${'PREIS'.padStart(9)} ${'1D%'.padStart(8)} ${'1W%'.padStart(8)}   ${'5/10'} ${'5/15'} ${'10/20'}`);
  lines.push('-'.repeat(55));

  items.forEach((item) => {
    const sym = item.sym.slice(0, 10).padEnd(10);
    const priceStr = (item.price !== undefined ? formatPrice(item.price) : '—').padStart(9);
    const d1Str = formatSimplePct(item.d1).padStart(8);
    const w1Str = formatSimplePct(item.w1).padStart(8);

    const t510 = formatTrendIcon(item.ema_5_10);
    const t515 = formatTrendIcon(item.ema_5_15);
    const t1020 = formatTrendIcon(item.ema_uptrend);

    lines.push(`${sym} ${priceStr} ${d1Str} ${w1Str}   ${t510}   ${t515}   ${t1020}`);
  });

  lines.push('```');
  lines.push('*Trend-Legende:*');
  lines.push('• *5/10*: Hyper-sensibel (EMA 5 > 10)');
  lines.push('• *5/15*: Die goldene Mitte (EMA 5 > 15)');
  lines.push('• *10/20*: Standard (EMA 10 > 20)');
  lines.push('');
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
