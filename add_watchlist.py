import json

# 1. Update tickers.json
tickers_path = "scripts/tickers.json"
with open(tickers_path, "r") as f:
    tickers = json.load(f)

watchlist = [
    "DTCR.DE", "IQQH.DE", "IS3U.DE", "QDVW.DE", "XDWT.DE", "QDVA.DE", "IUS3.DE", "EXI5.DE", "SPAB.DE", "ZPRV.DE", "XDRE.DE",
    "ADYEN.AS", "ASML.AS", "BRK-B", "BOIL.CN", "BGRP.DE", "BRN.AX", "0291.HK", "QBTS", "DOU.DE", "ELE.DE", "EL.PA", "FIE.DE",
    "FI", "VH2.DE", "GXI.DE", "HABA.DE", "HDD.DE", "HXL", "IMB.L", "KGX.DE", "LIN", "LHA.PA", "PTC.DE", "PTP.DE", "PUIG.MC",
    "RGV.MI", "RR.L", "SBF.DE", "NCH2.DE"
]

# Create a new dict preserving order and inserting portfolio_watchlist after energy
new_tickers = {}
for k, v in tickers.items():
    new_tickers[k] = v
    if k == "portfolio_energy":
        new_tickers["portfolio_watchlist"] = watchlist

with open(tickers_path, "w") as f:
    json.dump(new_tickers, f, indent=2)

# 2. Update symbolMaps.json
maps_path = "config/symbolMaps.json"
with open(maps_path, "r") as f:
    sym_maps = json.load(f)

new_names = {
    "DTCR.DE": {"name": "Global X Data Center"},
    "IQQH.DE": {"name": "iShares Clean Energy"},
    "IS3U.DE": {"name": "iShares Growth Portfolio"},
    "QDVW.DE": {"name": "iShares Europe IT"},
    "XDWT.DE": {"name": "iShares World IT"},
    "QDVA.DE": {"name": "iShares S&P Comm"},
    "IUS3.DE": {"name": "iShares SmallCap 600"},
    "EXI5.DE": {"name": "STOXX Europe Real Estate"},
    "SPAB.DE": {"name": "Scalable AC World"},
    "ZPRV.DE": {"name": "SPDR USA Small Cap Value"},
    "XDRE.DE": {"name": "Xtrackers EPRA/NAREIT"},
    
    "ADYEN.AS": {"name": "Adyen"},
    "ASML.AS": {"name": "ASML Holding"},
    "BRK-B": {"name": "Berkshire Hathaway B"},
    "BOIL.CN": {"name": "Beyond Oil"},
    "BGRP.DE": {"name": "Bigrep"},
    "BRN.AX": {"name": "BrainChip Holdings"},
    "0291.HK": {"name": "China Resources Beer"},
    "QBTS": {"name": "D-Wave Quantum"},
    "DOU.DE": {"name": "Douglas"},
    "ELE.DE": {"name": "Eleving Group"},
    "EL.PA": {"name": "EssilorLuxottica"},
    "FIE.DE": {"name": "Fielmann"},
    "FI": {"name": "Fiserv"},
    "VH2.DE": {"name": "Friedrich Vorwerk"},
    "GXI.DE": {"name": "Gerresheimer"},
    "HABA.DE": {"name": "Hamborner REIT"},
    "HDD.DE": {"name": "Heidelberger Druck"},
    "HXL": {"name": "Hexcel Co"},
    "IMB.L": {"name": "Imperial Brands"},
    "KGX.DE": {"name": "KION Grp"},
    "LIN": {"name": "Linde"},
    "LHA.PA": {"name": "Louis Hachette"},
    "PTC.DE": {"name": "Partec"},
    "PTP.DE": {"name": "Pentixapharm"},
    "PUIG.MC": {"name": "Puig Brands"},
    "RGV.MI": {"name": "Rigsave"},
    "RR.L": {"name": "Rolls-Royce"},
    "SBF.DE": {"name": "SBF"},
    "NCH2.DE": {"name": "Thyssenkrupp Nucera"}
}

sym_maps["symbols"].update(new_names)

with open(maps_path, "w") as f:
    json.dump(sym_maps, f, indent=2)

print("Tickers and mappings updated!")
