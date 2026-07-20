import json

path = "config/symbolMaps.json"
with open(path, "r") as f:
    data = json.load(f)

new_symbols = {
    "EXS1.DE": {"name": "iShares Core DAX"},
    "EXS2.DE": {"name": "iShares TecDAX"},
    "EXS3.DE": {"name": "iShares MDAX"},
    "EXSA.DE": {"name": "iShares STOXX Europe 600"},
    "BTC-EUR": {"displaySym": "BTC", "tradingView": "COINBASE:BTCEUR"},
    "ETH-EUR": {"displaySym": "ETH", "tradingView": "COINBASE:ETHEUR"},
    "SOL-EUR": {"displaySym": "SOL", "tradingView": "COINBASE:SOLEUR"},
    "XRP-EUR": {"displaySym": "XRP", "tradingView": "COINBASE:XRPEUR"},
    "FDAX=F": {"displaySym": "FDAX", "name": "DAX Futures"},
    "FESX=F": {"displaySym": "FESX", "name": "Euro Stoxx 50 Futures"},
    "FGBL=F": {"displaySym": "FGBL", "name": "Euro Bund Futures"}
}

data["symbols"].update(new_symbols)

with open(path, "w") as f:
    json.dump(data, f, indent=2)

print("symbolMaps.json updated!")
