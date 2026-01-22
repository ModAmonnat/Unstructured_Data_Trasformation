#The following script has been polished by Claude

def process_all_files(folder_path):
    data_list = []
    
    # Loop throughall files
    for f in Path(folder_path).iterdir():
        
        # Check if it's a file
        if f.is_file():
            try:
                # Read the file content
                content = f.read_text(encoding='utf-8')

                # Extract transactions and add to main list
                data_list.extend(extract_transactions(content, source_file=f.name))                            
            except Exception as error:
                #If file can't be read, print error with the file name and continue
                print(f"Error {f.name}: {error}")

    df = pd.DataFrame(data_list)
    print(f"Done! Extracted {len(df)} rows from {len(list(Path(folder_path).glob('*')))} files.")                                                               
    return df  

# Run
df_final = process_all_files(r"D:\BCIT\Winter 2026\BI2\CS1\Dataset")
