import pandas as pd

input_file = "./data/telecom.sql"  
output_file = "cleaned_data.csv"  

data_rows = []
with open(input_file, "r") as file:
    for line in file:
        if not line.startswith("COPY") and not line.startswith("\\.") and not line.startswith("--") and line.strip():
            row = line.strip().split("\t")  
            if len(row) > 1:  
                data_rows.append(row)

# Define column names
columns = [
    "Bearer Id", "Start", "Start ms", "End", "End ms", "Dur. (ms)", "IMSI",
    "MSISDN/Number", "IMEI", "Last Location Name", "Avg RTT DL (ms)", "Avg RTT UL (ms)",
    "Avg Bearer TP DL (kbps)", "Avg Bearer TP UL (kbps)", "TCP DL Retrans. Vol (Bytes)",
    "TCP UL Retrans. Vol (Bytes)", "DL TP < 50 Kbps (%)", "50 Kbps < DL TP < 250 Kbps (%)",
    "250 Kbps < DL TP < 1 Mbps (%)", "DL TP > 1 Mbps (%)", "UL TP < 10 Kbps (%)",
    "10 Kbps < UL TP < 50 Kbps (%)", "50 Kbps < UL TP < 300 Kbps (%)", "UL TP > 300 Kbps (%)",
    "HTTP DL (Bytes)", "HTTP UL (Bytes)", "Activity Duration DL (ms)", "Activity Duration UL (ms)",
    "Dur. (ms).1", "Handset Manufacturer", "Handset Type", "Nb of sec with 125000B < Vol DL",
    "Nb of sec with 1250B < Vol UL < 6250B", "Nb of sec with 31250B < Vol DL < 125000B",
    "Nb of sec with 37500B < Vol UL", "Nb of sec with 6250B < Vol DL < 31250B",
    "Nb of sec with 6250B < Vol UL < 37500B", "Nb of sec with Vol DL < 6250B",
    "Nb of sec with Vol UL < 1250B", "Social Media DL (Bytes)", "Social Media UL (Bytes)",
    "Google DL (Bytes)", "Google UL (Bytes)", "Email DL (Bytes)", "Email UL (Bytes)",
    "Youtube DL (Bytes)", "Youtube UL (Bytes)", "Netflix DL (Bytes)", "Netflix UL (Bytes)",
    "Gaming DL (Bytes)", "Gaming UL (Bytes)", "Other DL (Bytes)", "Other UL (Bytes)",
    "Total UL (Bytes)", "Total DL (Bytes)"
]

# Convert rows into a DataFrame
df = pd.DataFrame(data_rows, columns=columns)


df.replace("\\N", pd.NA, inplace=True)

numeric_columns = ["Bearer Id", "Start ms", "End ms", "Dur. (ms)", "IMSI", "MSISDN/Number", "IMEI"]
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")  

# Fix date formats in 'Start' and 'End'
df["Start"] = pd.to_datetime(df["Start"], errors="coerce", format="%m/%d/%Y %H:%M")
df["End"] = pd.to_datetime(df["End"], errors="coerce", format="%m/%d/%Y %H:%M")

df.dropna(subset=["Bearer Id", "Start", "End"], inplace=True)

df.fillna(value={"Bearer Id": 0}, inplace=True)

df.to_csv(output_file, index=False)
print(f"Data has been cleaned and saved to {output_file}.")
