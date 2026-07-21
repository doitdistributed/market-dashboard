import re

with open("scripts/fetch_data.py", "r") as f:
    content = f.read()

# 1. Update BATCH_SECTIONS
old_batch = "'portfolio_energy', 'portfolio_energy'),"
new_batch = "'portfolio_energy', 'portfolio_energy'),\n    ('portfolio_watchlist', 'portfolio_watchlist'),"
content = content.replace(old_batch, new_batch)

# 2. Update PRICE_SECTIONS
old_price = "'portfolio_europe', 'portfolio_energy',"
new_price = "'portfolio_europe', 'portfolio_energy', 'portfolio_watchlist',"
content = content.replace(old_price, new_price)

# 3. Update output dictionary
old_output = "'portfolio_software': [], 'portfolio_europe': [], 'portfolio_energy': [],"
new_output = "'portfolio_software': [], 'portfolio_europe': [], 'portfolio_energy': [], 'portfolio_watchlist': [],"
content = content.replace(old_output, new_output)

# 4. Update loops in lines 909 and 945
# Line 909 loop
old_loop = "for key in ('portfolio_core', 'portfolio_us_tech', 'portfolio_software', 'portfolio_europe', 'portfolio_energy'):"
new_loop = "for key in ('portfolio_core', 'portfolio_us_tech', 'portfolio_software', 'portfolio_europe', 'portfolio_energy', 'portfolio_watchlist'):"
content = content.replace(old_loop, new_loop)

# Line 945 condition
old_cond = "if out_key in ('portfolio_core', 'portfolio_us_tech', 'portfolio_software', 'portfolio_europe', 'portfolio_energy')]"
new_cond = "if out_key in ('portfolio_core', 'portfolio_us_tech', 'portfolio_software', 'portfolio_europe', 'portfolio_energy', 'portfolio_watchlist')]"
content = content.replace(old_cond, new_cond)

with open("scripts/fetch_data.py", "w") as f:
    f.write(content)

print("fetch_data.py patched successfully!")
