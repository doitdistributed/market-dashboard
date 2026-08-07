import React, { useMemo } from 'react';
import { Card, CardLabel, MarketTable, Section } from '../../components/common';
import { Icon } from '../../components/common/Icon';
import { useHotWatchlist } from '../../context/HotWatchlistContext';
import { useMarketStore } from '../../store/marketStore';
import { colors } from '../../utils/formatting';
import { usePenCompatibleClick } from '../../utils/penClick';
import type { MarketData, MarketTableOptions } from '../../types';

const rankByW1: Pick<MarketTableOptions, 'sortBy' | 'sortOrder'> = {
  sortBy: 'w1',
  sortOrder: 'desc',
};

export const HotWatchlistSection: React.FC = () => {
  const { pinnedSymbols, clearAllPins } = useHotWatchlist();
  const store = useMarketStore();

  const clearPenClick = usePenCompatibleClick(clearAllPins);

  // Map all known market items across categories
  const hotItems = useMemo(() => {
    if (pinnedSymbols.length === 0) return [];

    const map = new Map<string, MarketData>();
    const categories: (keyof typeof store)[] = [
      'portfolio_core',
      'portfolio_us_tech',
      'portfolio_software',
      'portfolio_europe',
      'portfolio_energy',
      'portfolio_watchlist',
      'futures',
      'crypto',
      'metals',
      'commodities',
      'yields',
      'global',
    ];

    categories.forEach((catKey) => {
      const arr = store[catKey];
      if (Array.isArray(arr)) {
        (arr as MarketData[]).forEach((item) => {
          if (item && item.sym && !map.has(item.sym)) {
            map.set(item.sym, item);
          }
        });
      }
    });

    return pinnedSymbols
      .map((sym) => map.get(sym))
      .filter((item): item is MarketData => Boolean(item));
  }, [pinnedSymbols, store]);

  if (pinnedSymbols.length === 0) {
    return (
      <Section number="🔥" title="Hot Watch List" subtitle="0 Pinned Assets">
        <div
          style={{
            background: colors.bg2,
            border: `1px dashed ${colors.border}`,
            borderRadius: '4px',
            padding: '14px 18px',
            display: 'flex',
            alignItems: 'center',
            gap: '12px',
            color: colors.text3,
            fontSize: '12px',
            fontFamily: 'IBM Plex Mono, monospace',
            marginBottom: '9px',
          }}
        >
          <span style={{ color: '#eab308', display: 'inline-flex' }}>
            <Icon name="star" size="md" />
          </span>
          <div>
            <strong style={{ color: colors.text, display: 'block', marginBottom: '2px' }}>
              Keine Favoriten ausgewählt
            </strong>
            Klicke auf das Stern-Icon (<span style={{ color: '#eab308' }}>☆</span>) bei einer beliebigen Aktie oder einem ETF in der Tabelle, um sie in deine persönliche Hot Watch List aufzunehmen.
          </div>
        </div>
      </Section>
    );
  }

  return (
    <Section number="🔥" title="Hot Watch List" subtitle={`${hotItems.length} Pinned Asset${hotItems.length > 1 ? 's' : ''}`}>
      <Card
        label={
          <CardLabel>
            <span style={{ color: '#f59e0b', display: 'inline-flex', alignItems: 'center', gap: '5px' }}>
              <Icon name="local_fire_department" size="sm" /> HOT SELECTION ({hotItems.length})
            </span>
          </CardLabel>
        }
        symbols={hotItems.map((x) => x.sym)}
        headerAction={
          <button
            type="button"
            className="table-expand-btn"
            {...clearPenClick}
            title="Alle aus der Hot Watch List entfernen"
            style={{ color: colors.red, borderColor: colors.border }}
          >
            <Icon name="delete_outline" size="xs" /> CLEAR ALL
          </button>
        }
        style={{ marginBottom: '9px' }}
      >
        <MarketTable
          data={hotItems}
          nameLabel="Asset"
          showTrend
          showHoldings
          holdings={store.holdings}
          {...rankByW1}
        />
      </Card>
    </Section>
  );
};
