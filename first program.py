"import pandas as pd;print(pd.__version__)"

import pandas as pd
print("pandas version:", pd.__version__)
df = pd.DataFrame({'a': [1,2,3], 'b': [4,5,6]})
print(df)
import pandas as pd
import os

csv_path = r"C:\Users\DELL\Internship Python ML 6 months\real_estate_db.csv\real_estate_db.csv"

try:
	print("pandas version:", pd.__version__)
	# If the CSV exists, load it; otherwise create a small sample DataFrame
	if os.path.exists(csv_path):
		df = pd.read_csv(csv_path)
		print(f"Loaded CSV: {csv_path}")
		print("rows:", len(df))
		print(df.head(5).to_string(index=False))
	else:
		print("CSV not found at:", csv_path)
		df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
		print("Using sample DataFrame:")
		print(df)
except Exception as e:
	print("Error while running test:", e)