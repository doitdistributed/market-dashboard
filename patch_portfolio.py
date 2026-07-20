import json

# Update tickers.json
tickers_path = "scripts/tickers.json"
with open(tickers_path, "r") as f:
    tickers = json.load(f)

# Remove old equities categories
for key in ["etfmain", "submarket", "sectors", "sectors_ew", "thematic", "country"]:
    tickers.pop(key, None)

# Add new portfolio categories at the beginning
new_tickers = {
    "portfolio_core": [
        "XDWD.DE", "XNAS.DE", "XMME.DE", "XESX.DE", "AM60.DE",
        "QDSA.DE", "EXI5.DE", "XAIX.DE", "XDRE.DE", "XAD6.DE"
    ],
    "portfolio_tech": [
        "APC.DE", "ASME.DE", "QCI.DE", "ADYEN.AS",
        "2AP.DE", "A1Z.DE", "G4G.F"
    ],
    "portfolio_value": [
        "BRYN.DE", "PEP.DE", "MMM.DE", "ALU.DE",
        "ADS.DE", "ALB.DE", "AOX.DE", "JW.F",
        "PTP.DE", "PUIG.MC", "TUI1.DE", "VFP.DE",
        "WAC.DE", "ZAL.DE"
    ]
}
new_tickers.update(tickers) # maintain order for macro parts
with open(tickers_path, "w") as f:
    json.dump(new_tickers, f, indent=2)

print("tickers.json updated!")

# Update symbolMaps.json
maps_path = "config/symbolMaps.json"
with open(maps_path, "r") as f:
    sym_maps = json.load(f)

portfolio_names = {
    "XDWD.DE": {"name": "Xtrackers MSCI World"},
    "XNAS.DE": {"name": "Xtrackers Nasdaq 100"},
    "XMME.DE": {"name": "Xtrackers MSCI EM"},
    "XESX.DE": {"name": "Xtrackers Euro Stoxx 50"},
    "AM60.DE": {"name": "Amundi Core Stoxx 600"},
    "QDSA.DE": {"name": "iShares S&P 500 Materials"},
    "EXI5.DE": {"name": "iShares Stoxx 600 Real Estate"},
    "XAIX.DE": {"name": "Xtrackers AI & Big Data"},
    "XDRE.DE": {"name": "Xtrackers FTSE EPRA/NAREIT"},
    "XAD6.DE": {"name": "Xtrackers Physical Silver"},
    "APC.DE": {"name": "Apple"},
    "ASME.DE": {"name": "ASML Holding"},
    "QCI.DE": {"name": "Qualcomm"},
    "ADYEN.AS": {"name": "Adyen"},
    "2AP.DE": {"name": "Appian"},
    "A1Z.DE": {"name": "Arista Networks"},
    "G4G.F": {"name": "Alphagen Intelligence"},
    "BRYN.DE": {"name": "Berkshire Hathaway"},
    "PEP.DE": {"name": "PepsiCo"},
    "MMM.DE": {"name": "3M"},
    "ALU.DE": {"name": "Air Liquide"},
    "ADS.DE": {"name": "adidas"},
    "ALB.DE": {"name": "Albemarle"},
    "AOX.DE": {"name": "Alstria office REIT"},
    "JW.F": {"name": "John Wiley & Sons"},
    "PTP.DE": {"name": "Pentixapharm"},
    "PUIG.MC": {"name": "Puig Brands"},
    "TUI1.DE": {"name": "TUI"},
    "VFP.DE": {"name": "V.F. Corp"},
    "WAC.DE": {"name": "Vertex Pharm."},
    "ZAL.DE": {"name": "Zalando"}
}

sym_maps["symbols"].update(portfolio_names)

with open(maps_path, "w") as f:
    json.dump(sym_maps, f, indent=2)

print("symbolMaps.json updated!")
