import React, { createContext, useCallback, useContext, useEffect, useState, type ReactNode } from 'react';

const STORAGE_KEY = 'market_dashboard_hot_watchlist';

interface HotWatchlistContextValue {
  pinnedSymbols: string[];
  togglePin: (sym: string) => void;
  isPinned: (sym: string) => boolean;
  clearAllPins: () => void;
}

const HotWatchlistContext = createContext<HotWatchlistContextValue | null>(null);

export function HotWatchlistProvider({ children }: { children: ReactNode }) {
  const [pinnedSymbols, setPinnedSymbols] = useState<string[]>(() => {
    try {
      const stored = localStorage.getItem(STORAGE_KEY);
      if (stored) {
        const parsed = JSON.parse(stored);
        if (Array.isArray(parsed)) {
          return parsed.filter((item): item is string => typeof item === 'string');
        }
      }
    } catch (e) {
      console.warn('Failed to load hot watchlist from localStorage:', e);
    }
    return [];
  });

  useEffect(() => {
    try {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(pinnedSymbols));
    } catch (e) {
      console.warn('Failed to save hot watchlist to localStorage:', e);
    }
  }, [pinnedSymbols]);

  const togglePin = useCallback((sym: string) => {
    if (!sym) return;
    setPinnedSymbols((prev) =>
      prev.includes(sym) ? prev.filter((s) => s !== sym) : [...prev, sym]
    );
  }, []);

  const isPinned = useCallback(
    (sym: string) => pinnedSymbols.includes(sym),
    [pinnedSymbols]
  );

  const clearAllPins = useCallback(() => {
    setPinnedSymbols([]);
  }, []);

  return (
    <HotWatchlistContext.Provider
      value={{
        pinnedSymbols,
        togglePin,
        isPinned,
        clearAllPins,
      }}
    >
      {children}
    </HotWatchlistContext.Provider>
  );
}

export function useHotWatchlist(): HotWatchlistContextValue {
  const context = useContext(HotWatchlistContext);
  if (!context) {
    throw new Error('useHotWatchlist must be used within a HotWatchlistProvider');
  }
  return context;
}
