import json

with open("data.json") as f:
    data = json.load(f)


def compare_songs(s1, s2):
    key_dist = abs(s1["key"] - s2["key"])
    tempo_dist = abs(s1["tempo"] - s2["tempo"])
    energy_dist = abs(s1["energy"] - s2["energy"])

    all_genres = s1["genre"] + s2["genre"]
    common_genres = len(all_genres) - len(set(all_genres))

    return (key_dist / 11 + tempo_dist / 141.873 + energy_dist / .851)


for song in data:
    print(compare_songs(data[0], song))