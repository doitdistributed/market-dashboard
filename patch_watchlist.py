import json

# Update tickers.json
tickers_path = "scripts/tickers.json"
with open(tickers_path, "r") as f:
    tickers = json.load(f)

# Remove old portfolio categories
for key in ["portfolio_core", "portfolio_tech", "portfolio_value"]:
    tickers.pop(key, None)

# Add new 5 portfolio categories at the beginning
new_tickers = {
    "portfolio_core": ["XDWD.DE"],
    "portfolio_us_tech": ["APC.DE", "AMZ.DE", "FB2A.DE", "INL.DE", "IBM.DE"],
    "portfolio_software": ["C3K.DE", "CY8.DE", "00E.DE", "2AP.DE"],
    "portfolio_europe": ["SAP.DE", "MBG.DE", "DTE.DE", "IFX.DE", "ASME.DE"],
    "portfolio_energy": ["F3A.DE", "ALB.DE", "CJ0.DE", "DUO.DE", "URNU.DE"]
}
new_tickers.update(tickers) # maintain order for macro parts
with open(tickers_path, "w") as f:
    json.dump(new_tickers, f, indent=2)

print("tickers.json updated!")

# Update symbolMaps.json
maps_path = "config/symbolMaps.json"
with open(maps_path, "r") as f:
    sym_maps = json.load(f)

new_names = {
    "AMZ.DE": {"name": "Amazon"},
    "FB2A.DE": {"name": "Meta Platforms"},
    "INL.DE": {"name": "Intel Corp"},
    "IBM.DE": {"name": "IBM"},
    "C3K.DE": {"name": "Crowdstrike"},
    "CY8.DE": {"name": "CyberArk"},
    "00E.DE": {"name": "Elastic NV"},
    "SAP.DE": {"name": "SAP SE"},
    "MBG.DE": {"name": "Mercedes-Benz"},
    "DTE.DE": {"name": "Deutsche Telekom"},
    "IFX.DE": {"name": "Infineon Technologies"},
    "F3A.DE": {"name": "First Solar"},
    "CJ0.DE": {"name": "Cameco Corp"},
    "DUO.DE": {"name": "DuPont de Nemours"},
    "URNU.DE": {"name": "Global X Uranium UCITS"}
}

sym_maps["symbols"].update(new_names)

with open(maps_path, "w") as f:
    json.dump(sym_maps, f, indent=2)

print("symbolMaps.json updated!")
