#reads sample_data_3vars.csv and writes the csv

import csv

INFILE = "sample_data_3vars.csv"

# code 1 = direct, code 2 = vector,code 3 = indirect
BYTES_PER_ITER     = {"code 1": 0, "code 2": 8,  "code 3": 16}
ACCESSES_PER_ITER  = {"code 1": 0, "code 2": 1,  "code 3": 2}

#peak bandwidth
CAPACITY_BPS = 204_800_000_000.0  # 204.8e9

rows = []
with open(INFILE, newline="") as f:
    r = csv.DictReader(f)
    for row in r:
        rows.append({
            "Problem Size": int(row["Problem Size"]),
            "code 1": float(row["code 1"]),
            "code 2": float(row["code 2"]),
            "code 3": float(row["code 3"]),
        })

def write_csv(fname, header, make_vals):
    with open(fname, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(header)
        for row in rows:
            w.writerow(make_vals(row))

# MFLOP/s
write_csv(
    "mflops_3vars.csv",
    ["Problem Size", "code 1", "code 2", "code 3"],
    lambda row: [row["Problem Size"]]
    + [(row["Problem Size"]/1e6)/max(row[c], 1e-12) for c in ("code 1","code 2","code 3")]
)

# % peak memory bandwidth
def bw_pct(code, row):
    bytes_total = row["Problem Size"] * BYTES_PER_ITER[code]
    return ((bytes_total/max(row[code], 1e-12)) / CAPACITY_BPS) * 100.0

write_csv(
    "percent_bw_3vars.csv",
    ["Problem Size", "code 1", "code 2", "code 3"],
    lambda row: [row["Problem Size"]] + [bw_pct(c, row) for c in ("code 1","code 2","code 3")]
)

# avg memory latency
def lat_ns(code, row):
    acc = row["Problem Size"] * ACCESSES_PER_ITER[code]
    return "" if acc == 0 else (row[code]/acc) * 1e9

write_csv(
    "latency_ns_3vars.csv",
    ["Problem Size", "code 1", "code 2", "code 3"],
    lambda row: [row["Problem Size"]] + [lat_ns(c, row) for c in ("code 1","code 2","code 3")]
)

print("Wrote: mflops_3vars.csv, percent_bw_3vars.csv, latency_ns_3vars.csv")
