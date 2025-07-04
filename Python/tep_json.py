import json
import os

def doc_du_lieu(ten_tap_tin):
    if not os.path.exists(ten_tap_tin):
        return []
    with open(ten_tap_tin, 'r', encoding='utf-8') as f:
        return json.load(f)

def ghi_du_lieu(ten_tap_tin, du_lieu):
    with open(ten_tap_tin, 'w', encoding='utf-8') as f:
        json.dump(du_lieu, f, ensure_ascii=False, indent=4)