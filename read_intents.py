import pandas as pd
import json

# Đọc file Excel
df = pd.read_excel('intents.xlsx')

# Tạo danh sách intents
intents = []
for index, row in df.iterrows():
    intent = {
        "tag": row['tag'],
        "patterns": row['patterns'],
        "responses": row['respones'],
        "context_set": ""
    }
    intents.append(intent)

# Tạo dictionary chứa danh sách intents
data = {"intents": intents}

# Ghi dữ liệu vào file JSON
with open('intents_output.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

print("Dữ liệu đã được chuyển đổi và lưu vào file intents_output.json")