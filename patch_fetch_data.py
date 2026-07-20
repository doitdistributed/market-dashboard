import re

with open("scripts/fetch_data.py", "r") as f:
    content = f.read()

# 1. Update BATCH_SECTIONS
old_batch = """BATCH_SECTIONS = [
    ('portfolio_core', 'portfolio_core'),
    ('portfolio_tech', 'portfolio_tech'),
    ('portfolio_value', 'portfolio_value'),
    ('crypto', 'crypto'),
    ('dxvix', 'dxvix'),
    ('futures', 'futures'),
    ('metals', 'metals'),
    ('commod', 'energy'),
]"""
new_batch = """BATCH_SECTIONS = [
    ('portfolio_core', 'portfolio_core'),
    ('portfolio_us_tech', 'portfolio_us_tech'),
    ('portfolio_software', 'portfolio_software'),
    ('portfolio_europe', 'portfolio_europe'),
    ('portfolio_energy', 'portfolio_energy'),
    ('crypto', 'crypto'),
    ('dxvix', 'dxvix'),
    ('futures', 'futures'),
    ('metals', 'metals'),
    ('commod', 'energy'),
]"""
content = content.replace(old_batch, new_batch)

# 2. Update PRICE_SECTIONS
old_price = """PRICE_SECTIONS = [
    'futures', 'dxvix', 'crypto', 'metals', 'commod', 'yields',
    'global', 'portfolio_core', 'portfolio_tech', 'portfolio_value',
]"""
new_price = """PRICE_SECTIONS = [
    'futures', 'dxvix', 'crypto', 'metals', 'commod', 'yields',
    'global', 'portfolio_core', 'portfolio_us_tech', 'portfolio_software', 'portfolio_europe', 'portfolio_energy',
]"""
content = content.replace(old_price, new_price)

# 3. Update output dictionary
old_output = """    output = {
        'generated_at': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        'futures':  [], 'dxvix':   [], 'metals':   [], 'commod':  [],
        'yields':   [], 'global':  [], 'etfmain':  [], 'submarket':[],
        'sector':   [], 'sectorew':[], 'thematic': [], 'country': [],
        'crypto':   [],
        'holdings': existing.get('holdings', {}),
        'breadth':  existing.get('breadth',  {}),
    }"""
new_output = """    output = {
        'generated_at': datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ'),
        'futures':  [], 'dxvix':   [], 'metals':   [], 'commod':  [],
        'yields':   [], 'global':  [], 'portfolio_core': [], 'portfolio_us_tech': [],
        'portfolio_software': [], 'portfolio_europe': [], 'portfolio_energy': [],
        'crypto':   [],
        'holdings': existing.get('holdings', {}),
        'breadth':  existing.get('breadth',  {}),
    }"""
content = content.replace(old_output, new_output)

# 4. Simplify yf_etf_batches
old_batches = """    yf_etf_batches = [(out_key, tickers_key) for out_key, tickers_key in BATCH_SECTIONS
                      if out_key in ('etfmain', 'submarket', 'sector', 'sectorew', 'thematic', 'country')]
    yf_batches = [(out_key, tickers_key) for out_key, tickers_key in BATCH_SECTIONS
                  if out_key not in ('etfmain', 'submarket', 'sector', 'sectorew', 'thematic', 'country')]"""
new_batches = """    yf_etf_batches = [(out_key, tickers_key) for out_key, tickers_key in BATCH_SECTIONS if out_key.startswith('portfolio_')]
    yf_batches = [(out_key, tickers_key) for out_key, tickers_key in BATCH_SECTIONS if not out_key.startswith('portfolio_')]"""
content = content.replace(old_batches, new_batches)

with open("scripts/fetch_data.py", "w") as f:
    f.write(content)

print("fetch_data.py updated successfully!")
