import json

tickers_path = "scripts/tickers.json"
with open(tickers_path, "r") as f:
    tickers = json.load(f)

# Mapping of .DE to US tickers
mapping = {
    "APC.DE": "AAPL",
    "AMZ.DE": "AMZN",
    "FB2A.DE": "META",
    "INL.DE": "INTC",
    "IBM.DE": "IBM",
    "A1Z.DE": "ANET",
    "EQIX.DE": "EQIX",
    "CCC3.DE": "KO",
    "C3K.DE": "CRWD",
    "CY8.DE": "CYBR",
    "00E.DE": "ESTC",
    "2AP.DE": "APPN",
    "F3A.DE": "FSLR",
    "ALB.DE": "ALB",
    "CJ0.DE": "CCJ",
    "DUO.DE": "DD"
}

# Update tickers.json
for cat in tickers:
    if isinstance(tickers[cat], list):
        tickers[cat] = [mapping.get(sym, sym) for sym in tickers[cat]]

with open(tickers_path, "w") as f:
    json.dump(tickers, f, indent=2)

# Update symbolMaps.json
maps_path = "config/symbolMaps.json"
with open(maps_path, "r") as f:
    sym_maps = json.load(f)

new_symbols = {}
for old_sym, new_sym in mapping.items():
    if old_sym in sym_maps.get("symbols", {}):
        new_symbols[new_sym] = sym_maps["symbols"][old_sym]
        # We don't necessarily delete the old one, but we add the new one.

sym_maps["symbols"].update(new_symbols)

with open(maps_path, "w") as f:
    json.dump(sym_maps, f, indent=2)

print("Tickers updated to US native symbols where applicable!")
