import pandas as pd
import qrcode
import os
import sys

# Settings
excel_file = 'input.xlsx' #file name
sheet_name = 'Sheet1' #sheet 1
column_name = 'Data' #column name
output_dir = 'qr_output' #output filename

# Check if file exists
if not os.path.exists(excel_file):
    print("❌ 'input.xlsx' not found in the current folder.")
    input("Press Enter to exit...")
    sys.exit()

# Create output folder if not exists
os.makedirs(output_dir, exist_ok=True)

# Load Excel
df = pd.read_excel(excel_file, sheet_name=sheet_name)

# Generate QR codes
print("📦 Starting QR code generation...\n")

for idx, value in enumerate(df[column_name]):
    if pd.isna(value):
        continue
    text = str(value)
    print(f"➡️ Generating QR for: {text}")
    qr = qrcode.make(text)
    filename = f"{output_dir}/qr_{idx+1}.png"
    qr.save(filename)

print("\n✅ All QR codes saved in 'qr_output' folder.")
input("Press Enter to exit...")