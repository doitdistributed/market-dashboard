import json

tickers_path = "scripts/tickers.json"
with open(tickers_path, "r") as f:
    tickers = json.load(f)

# Define the enriched lists based on the user's full table
enriched = {
    "portfolio_core": [
        "XDWD.DE", # Core World
        "XNAS.DE", # Nasdaq
        "XMME.DE", # EM
        "XESX.DE", # Euro Stoxx 50
        "EXS1.DE", # DAX
        "XAIX.DE"  # AI & Big Data
    ],
    "portfolio_us_tech": [
        "APC.DE", "AMZ.DE", "FB2A.DE", "INL.DE", "IBM.DE",
        "A1Z.DE", "EQIX.DE", "CCC3.DE"
    ],
    "portfolio_software": [
        "C3K.DE", "CY8.DE", "00E.DE", "2AP.DE"
    ],
    "portfolio_europe": [
        "SAP.DE", "MBG.DE", "DTE.DE", "IFX.DE", "ASME.DE",
        "ALU.DE", "ADS.DE", "ZAL.DE", "TUI1.DE"
    ],
    "portfolio_energy": [
        "F3A.DE", "ALB.DE", "CJ0.DE", "DUO.DE",
        "URNU.DE", "XAD6.DE", "ISLN.DE"
    ]
}

for k, v in enriched.items():
    tickers[k] = v

with open(tickers_path, "w") as f:
    json.dump(tickers, f, indent=2)

# Update symbolMaps.json
maps_path = "config/symbolMaps.json"
with open(maps_path, "r") as f:
    sym_maps = json.load(f)

new_names = {
    "XDWD.DE": {"name": "Xtrackers MSCI World"},
    "XNAS.DE": {"name": "Xtrackers Nasdaq 100"},
    "XMME.DE": {"name": "Xtrackers Emerging Markets"},
    "XESX.DE": {"name": "Xtrackers EURO STOXX 50"},
    "EXS1.DE": {"name": "iShares Core DAX"},
    "XAIX.DE": {"name": "Xtrackers AI & Big Data"},
    
    "APC.DE": {"name": "Apple"},
    "AMZ.DE": {"name": "Amazon"},
    "FB2A.DE": {"name": "Meta Platforms"},
    "INL.DE": {"name": "Intel Corp"},
    "IBM.DE": {"name": "IBM"},
    "A1Z.DE": {"name": "Arista Networks"},
    "EQIX.DE": {"name": "Equinix"},
    "CCC3.DE": {"name": "Coca-Cola"},
    
    "C3K.DE": {"name": "Crowdstrike"},
    "CY8.DE": {"name": "CyberArk"},
    "00E.DE": {"name": "Elastic NV"},
    "2AP.DE": {"name": "Appian"},
    
    "SAP.DE": {"name": "SAP SE"},
    "MBG.DE": {"name": "Mercedes-Benz"},
    "DTE.DE": {"name": "Deutsche Telekom"},
    "IFX.DE": {"name": "Infineon"},
    "ASME.DE": {"name": "ASML Holding"},
    "ALU.DE": {"name": "Air Liquide"},
    "ADS.DE": {"name": "adidas"},
    "ZAL.DE": {"name": "Zalando"},
    "TUI1.DE": {"name": "TUI"},
    
    "F3A.DE": {"name": "First Solar"},
    "ALB.DE": {"name": "Albemarle"},
    "CJ0.DE": {"name": "Cameco"},
    "DUO.DE": {"name": "DuPont"},
    "URNU.DE": {"name": "Global X Uranium"},
    "XAD6.DE": {"name": "Physical Silver ETC"},
    "ISLN.DE": {"name": "iShares Silver ETC"}
}

sym_maps["symbols"].update(new_names)

with open(maps_path, "w") as f:
    json.dump(sym_maps, f, indent=2)

print("Watchlist enriched!")
