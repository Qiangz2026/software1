#Data Serialization
import json

save_data = {"player": "Matti",
             "level": 5,
             "equipment": ["sword", "shield", "armor"]
}

with open("save.json", "w") as file:
    json.dump(save_data, file)
with open("save.json", "r") as file:
    data_read = json.load(file)
print(f"Player: {data_read['player']}, level: {data_read['level']}, equipment: {data_read['equipment']}")