import os
import json
import zipfile

# 1. Automatically extract the zip file if needed
script_dir = os.path.dirname(os.path.abspath(__file__))
zip_path = os.path.join(script_dir, "twitter-archive-class.zip")
extracted_dir = os.path.join(script_dir, "twitter-archive-class")

if not os.path.exists(extracted_dir) and os.path.exists(zip_path):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(script_dir)

def load_ytd(path):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if '=' in content:
        _, json_str = content.split('=', 1)
        return json.loads(json_str.strip().rstrip(';'))
    return json.loads(content)

def load_dataset(data_dir, name):
    files_to_load = []
    if not os.path.exists(data_dir):
        return []
    for filename in os.listdir(data_dir):
        if not filename.endswith('.js'):
            continue
        stem = filename[:-3]
        if stem == name:
            files_to_load.append((0, filename))
        elif stem.startswith(name + "-part"):
            part_suffix = stem[len(name) + len("-part"):]
            if part_suffix.isdigit():
                files_to_load.append((int(part_suffix), filename))
                    
    files_to_load.sort(key=lambda x: x[0])
    combined_data = []
    for _, filename in files_to_load:
        path = os.path.join(data_dir, filename)
        data = load_ytd(path)
        if isinstance(data, list):
            combined_data.extend(data)
        elif isinstance(data, dict):
            combined_data.append(data)
    return combined_data

data_directory = os.path.join(extracted_dir, "data")
ad_engagements = load_dataset(data_directory, "ad-engagements")

target_advertiser = "Remix Institute"
ad_count = 0
impression_timestamps = []
targeting_types = set()

for record in ad_engagements:
    ads_user_data = record.get('ad', {}).get('adsUserData', {})
    ad_engagements_obj = ads_user_data.get('adEngagements', {})
    engagements_list = ad_engagements_obj.get('engagements', [])
    
    for engagement in engagements_list:
        impression_attrs = engagement.get('impressionAttributes', {})
        advertiser_info = impression_attrs.get('advertiserInfo', {})
        advertiser_name = advertiser_info.get('advertiserName', '')
        
        if advertiser_name == target_advertiser:
            ad_count += 1
            
            # Extract impressionTime correctly
            imp_time = impression_attrs.get('impressionTime')
            if imp_time:
                impression_timestamps.append(imp_time)
                
            # Collect unique targeting types
            criteria_list = impression_attrs.get('matchedTargetingCriteria', [])
            for criterion in criteria_list:
                t_type = criterion.get('targetingType')
                if t_type:
                    targeting_types.add(t_type)

# Format the first date (YYYY-MM-DD)
first_date_str = "N/A"
if impression_timestamps:
    impression_timestamps.sort()
    # Take the first 10 characters since format is "YYYY-MM-DD HH:MM:SS"
    first_date_str = impression_timestamps[0][:10]

print(f"\n--- Analysis for '{target_advertiser}' ---")
print(f"a. How many ads from this advertiser were shown? {ad_count}")
print(f"b. First date shown (UTC, YYYY-MM-DD): {first_date_str}")
print(f"c. Number of different targeting types used: {len(targeting_types)}")
print(f"   Targeting types found: {list(targeting_types)}")