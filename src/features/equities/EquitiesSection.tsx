import { Card, CardLabel, MarketTable, Section } from '../../components/common';
import { useMarketStore } from '../../store/marketStore';
import type { MarketTableOptions } from '../../types';

const rankByW1: Pick<MarketTableOptions, 'sortBy' | 'sortOrder'> = {
  sortBy: 'w1',
  sortOrder: 'desc',
};

export function EquitiesSection() {
  const store = useMarketStore();

  return (
    <Section number="02" title="Portfolio Overview">
      <Card label={<CardLabel>CORE ETFS</CardLabel>} symbols={store.portfolio_core.map((x) => x.sym)} style={{ marginBottom: '9px' }}>
        <MarketTable
          data={store.portfolio_core}
          nameLabel="Asset"
          showTrend
          showHoldings
          holdings={store.holdings}
          {...rankByW1}
        />
      </Card>

      <div className="g2" style={{ marginBottom: '9px' }}>
        <Card label={<CardLabel>US-TECHNOLOGIE & BIG DATA</CardLabel>} symbols={store.portfolio_us_tech.map((x) => x.sym)}>
          <MarketTable
            data={store.portfolio_us_tech}
            nameLabel="Asset"
            showTrend
            showHoldings={false}
            {...rankByW1}
          />
        </Card>
        <Card label={<CardLabel>SOFTWARE, CYBERSECURITY & CLOUD</CardLabel>} symbols={store.portfolio_software.map((x) => x.sym)}>
          <MarketTable
            data={store.portfolio_software}
            nameLabel="Asset"
            showTrend
            showHoldings={false}
            {...rankByW1}
          />
        </Card>
      </div>

      <div className="g2" style={{ marginBottom: '9px' }}>
        <Card label={<CardLabel>EUROPÄISCHE BLUE CHIPS</CardLabel>} symbols={store.portfolio_europe.map((x) => x.sym)}>
          <MarketTable
            data={store.portfolio_europe}
            nameLabel="Asset"
            showTrend
            showHoldings={false}
            {...rankByW1}
          />
        </Card>
        <Card label={<CardLabel>ENERGIE, GRUNDSTOFFE & ROHSTOFFE</CardLabel>} symbols={store.portfolio_energy.map((x) => x.sym)}>
          <MarketTable
            data={store.portfolio_energy}
            nameLabel="Asset"
            showTrend
            showHoldings={false}
            {...rankByW1}
          />
        </Card>
      </div>
    </Section>
  );
}
