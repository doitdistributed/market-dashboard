import { create } from 'zustand';
import type { MarketState, MarketData } from '../types';

interface MarketStore extends MarketState {
  loadAll: (data: Partial<MarketState>) => void;
  setLoading: (loading: boolean) => void;
  setError: (error: string | null) => void;
  updatePrice: (sym: string, price: number, d1: number, updatedAt?: number) => void;
}

const initialState: MarketState = {
  futures: [],
  dxvix: [],
  crypto: [],
  metals: [],
  commodities: [],
  yields: [],
  global: [],
  portfolio_core: [],
  portfolio_us_tech: [],
  portfolio_software: [],
  portfolio_europe: [],
  portfolio_energy: [],
  breadth: null,
  holdings: {},
  generatedAt: null,
  lastUpdated: null,
  loading: true,
  error: null,
};

export const useMarketStore = create<MarketStore>((set) => ({
  ...initialState,

  setLoading: (loading) => set({ loading }),
  setError: (error) => set({ error }),

  loadAll: (data) =>
    set(() => {
      const initialTime = data.generatedAt ? new Date(data.generatedAt).getTime() : Date.now();
      const addTimestamp = <T extends MarketData>(arr?: T[]): T[] => {
        if (!arr) return [];
        return arr.map((item) => ({ ...item, updatedAt: item.updatedAt ?? initialTime }));
      };

      return {
        ...initialState,
        ...data,
        futures: addTimestamp(data.futures),
        dxvix: addTimestamp(data.dxvix),
        crypto: addTimestamp(data.crypto),
        metals: addTimestamp(data.metals),
        commodities: addTimestamp(data.commodities),
        yields: addTimestamp(data.yields),
        global: addTimestamp(data.global),
        portfolio_core: addTimestamp(data.portfolio_core),
        portfolio_us_tech: addTimestamp(data.portfolio_us_tech),
        portfolio_software: addTimestamp(data.portfolio_software),
        portfolio_europe: addTimestamp(data.portfolio_europe),
        portfolio_energy: addTimestamp(data.portfolio_energy),
        loading: false,
        error: null,
      };
    }),

  updatePrice: (sym, price, d1, updatedAt) =>
    set((state) => {
      const timestamp = updatedAt ?? Date.now();
      const updateArray = <T extends MarketData>(arr: T[]): T[] =>
        arr.map((item) => (item.sym === sym ? { ...item, price, d1, updatedAt: timestamp } : item));

      return {
        futures: updateArray(state.futures),
        dxvix: updateArray(state.dxvix),
        crypto: updateArray(state.crypto),
        metals: updateArray(state.metals),
        commodities: updateArray(state.commodities),
        yields: updateArray(state.yields),
        global: updateArray(state.global),
        portfolio_core: updateArray(state.portfolio_core),
        portfolio_us_tech: updateArray(state.portfolio_us_tech),
        portfolio_software: updateArray(state.portfolio_software),
        portfolio_europe: updateArray(state.portfolio_europe),
        portfolio_energy: updateArray(state.portfolio_energy),
      };
    }),
}));
