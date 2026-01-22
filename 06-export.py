#The following script has been polished by Claude

# Set my destination folder

output_folder = r"D:\BCIT\Winter 2026\BI2\CS1"

# Export to Excel
excel_file = output_folder + r"\merged_transactions_final4.xlsx"                             
df_final.to_excel(excel_file, index=False)
print(f"Saved Excel: {excel_file}")

print(f"\nDone! Exported {len(df_final)} transactions")                                                                                                  
