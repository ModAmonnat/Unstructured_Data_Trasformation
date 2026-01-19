def process_all_files(folder_path):
    all_transactions = []
    file_list = [f for f in Path(folder_path).glob('*') if f.is_file()]
    
    for filepath in file_list:
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = f.read()
            transactions = extract_transactions(data, source_file=filepath.name)
            all_transactions.extend(transactions)
        except Exception as e:
            print(f"ERROR: {filepath.name} - {e}")
    
    df = pd.DataFrame(all_transactions)
    
    print(f"COMPLETE! Extracted {len(df)} transactions from {len(file_list)} files")
    
    return df

# Run it
folder_path = r"D:\BCIT\Winter 2026\BI2\CS1\Dataset"
df_final = process_all_files(folder_path)
