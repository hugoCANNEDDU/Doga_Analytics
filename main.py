import os
import json
import pandas as pd

from pandas_profiling import ProfileReport


def extract_data() :

    columns = ["Id", "Reveal Status", "Rarity", "Rarity Score", "Ranking", "Gender", "Breed", "Fur Color", "Eyes Color", "Dominant Personality", "Recessive Personality", "Vitality", "Intelligence", "Robustness", "Obedience", "Friendliness", "Bonding"]
    data_path = "./data"
    save_path = "./data.csv"

    raw_data = []
    for filename in os.listdir(data_path):
       with open(os.path.join(data_path, filename), 'r') as f:
           data = json.load(f)['data']['token'][0]
           row = [data['id'], data['reveal_status']]
           if data['reveal_status'] == 2 :
               data = data['metadata']['attributes']
               row.append(data['rarity_tier']['name'])
               row.append(data['rarity_score'])
               row.append(data['ranking'])
               row.append(data['gender'])
               row.append(data['breed']['name'])
               row.append(data['fur_color'])
               row.append(data['eyes_color'])
               row.append(data['primary_personality'])
               row.append(data['secondary_personality'])
               row.append(data['vitality'])
               row.append(data['intelligence'])
               row.append(data['strength'])
               row.append(data['obedience'])
               row.append(data['friendliness'])
               row.append(data['bonding_level'])

           raw_data.append(row)

    df_data = pd.DataFrame(raw_data, columns=columns)
    df_data.set_index('Id', inplace=True)
    df_data.sort_index(inplace=True)
    df_data.to_csv(save_path, sep=';', decimal=',')

    prof = ProfileReport(df_data)
    prof.to_file(output_file='output.html')

if __name__ == "__main__":
    extract_data()