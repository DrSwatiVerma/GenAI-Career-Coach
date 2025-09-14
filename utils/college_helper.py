import json

def recommend_colleges(specialization, data_path="data/colleges.json"):
    with open(data_path, "r") as f:
        colleges = json.load(f)

    results = [c for c in colleges if specialization in c["specialization"]]
    return results
