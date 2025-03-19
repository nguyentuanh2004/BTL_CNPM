import pandas as pd
input_file = 'data/year3_clean.xlsx'
output_file = 'data/year3_4point_scale_clean.xlsx'
df = pd.read_excel(input_file)
def convert_number_to_char(data: pd.DataFrame):
    df = data.copy()
    for index, row in df.iterrows():
        for col in df.columns:
            cell_value = row[col]
            if isinstance(cell_value, (int, float)) and 1 <= cell_value < 4:
                df.at[index, col] = 'F'
            if isinstance(cell_value, (int, float)) and 4 <= cell_value < 5.5:
                df.at[index, col] = 'D'
            if isinstance(cell_value, (int, float)) and  5.5<= cell_value < 7:
                df.at[index, col] = 'C'
            if isinstance(cell_value, (int, float)) and 7 <= cell_value < 8.5:
                df.at[index, col] = 'B'
            if isinstance(cell_value, (int, float)) and 8.5 <= cell_value <= 10:
                df.at[index, col] = 'A'
    return df
df = convert_number_to_char(df)
df.to_excel(output_file, index=False)