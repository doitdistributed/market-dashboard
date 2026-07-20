import json

path = "scripts/tickers.json"
with open(path, "r") as f:
    data = json.load(f)

data["submarket"] = ["IS3R.DE","IS3Q.DE","IS3S.DE","IS3T.DE","IS3V.DE"]
data["sectors"] = ["QDVE.DE","QDVG.DE","QDVF.DE","QDVH.DE","QDVK.DE","QDVJ.DE","QDVD.DE","QDVQ.DE","QDVN.DE","QDVW.DE"]
data["sectors_ew"] = []
data["thematic"] = ["IQQH.DE","2B76.DE","2B79.DE","IS0E.DE","4GLD.DE","IQQQ.DE","IPRV.DE","LITU.DE","VVSM.DE"]
data["country"] = ["EUNL.DE","EUNM.DE","SXR1.DE","NDIA.DE","ICGA.DE","SMEA.DE"]

with open(path, "w") as f:
    json.dump(data, f, indent=2)

print("tickers.json updated!")

map_path = "config/symbolMaps.json"
with open(map_path, "r") as f:
    map_data = json.load(f)

ucits_symbols = {
    "IS3R.DE": {"name": "MSCI World Momentum"},
    "IS3Q.DE": {"name": "MSCI World Quality"},
    "IS3S.DE": {"name": "MSCI World Value"},
    "IS3T.DE": {"name": "MSCI World Size"},
    "IS3V.DE": {"name": "MSCI World Min Vol"},
    "QDVE.DE": {"name": "S&P 500 Info Tech"},
    "QDVG.DE": {"name": "S&P 500 Health Care"},
    "QDVF.DE": {"name": "S&P 500 Financials"},
    "QDVH.DE": {"name": "S&P 500 Energy"},
    "QDVK.DE": {"name": "S&P 500 Cons Discr"},
    "QDVJ.DE": {"name": "S&P 500 Industrials"},
    "QDVD.DE": {"name": "S&P 500 Materials"},
    "QDVQ.DE": {"name": "S&P 500 Utilities"},
    "QDVN.DE": {"name": "S&P 500 Cons Staples"},
    "QDVW.DE": {"name": "S&P 500 Comm Svcs"},
    "IQQH.DE": {"name": "Global Clean Energy"},
    "2B76.DE": {"name": "Automation & Robotics"},
    "2B79.DE": {"name": "Digitalisation"},
    "IS0E.DE": {"name": "Cyber Security"},
    "4GLD.DE": {"name": "Xetra-Gold"},
    "IQQQ.DE": {"name": "Global Water"},
    "IPRV.DE": {"name": "Listed Private Equity"},
    "LITU.DE": {"name": "Lithium & Battery"},
    "VVSM.DE": {"name": "Semiconductor"},
    "EUNL.DE": {"name": "MSCI World"},
    "EUNM.DE": {"name": "MSCI Emerging Markets"},
    "SXR1.DE": {"name": "MSCI Japan"},
    "NDIA.DE": {"name": "MSCI India"},
    "ICGA.DE": {"name": "MSCI China"},
    "SMEA.DE": {"name": "MSCI Europe"}
}

map_data["symbols"].update(ucits_symbols)

with open(map_path, "w") as f:
    json.dump(map_data, f, indent=2)

print("symbolMaps.json updated!")
