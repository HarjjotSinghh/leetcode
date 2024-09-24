import os
import datetime

def create_files_for_year(year):
    start_date = datetime.date(year, 8, 8)
    end_date = datetime.date(year, 12, 31)
    current_date = start_date
    
    while current_date <= end_date:
        month_folder = os.path.join(str(year), current_date.strftime("%B"))
        os.makedirs(month_folder, exist_ok=True)
        
        file_name = current_date.strftime("%d_%m_%Y.py")
        file_path = os.path.join(month_folder, file_name)
        
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write("# This day has not yet come. This file is currently empty.")
            print(f"Created: {file_path}")
            
        else:
            print(f"Skipped existing file: {file_path}")
        current_date += datetime.timedelta(days=1)

create_files_for_year(2024)
print("Process completed successfully!")