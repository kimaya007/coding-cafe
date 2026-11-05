import os
import json
import zipfile
from collections import Counter

# 1. Automatically extract the zip file if needed
script_dir = os.path.dirname(os.path.abspath(__file__))
zip_path = os.path.join(script_dir, "twitter-archive-class.zip")
extracted_dir = os.path.join(script_dir, "twitter-archive-class")

if not os.path.exists(extracted_dir) and os.path.exists(zip_path):
    print("Extracting twitter-archive-class.zip...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(script_dir)
    print("Extraction complete!")

def load_ytd(path):
    """Return the data stored in one archive .js file (a list of dicts, or a dict for manifest.js)."""
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    if '=' in content:
        _, json_str = content.split('=', 1)
        return json.loads(json_str.strip().rstrip(';'))
    return json.loads(content)

def load_dataset(data_dir, name):
    """Return ONE list combining name.js, name-part1.js, name-part2.js, ... in part order (or [] if none)."""
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

# Analysis logic with correct nesting paths
matching_ads_count = 0
advertisers_set = set()
advertiser_counts = Counter()

for record in ad_engagements:
    # Navigate through the correct nested structure: ad -> adsUserData -> adEngagements -> engagements
    ads_user_data = record.get('ad', {}).get('adsUserData', {})
    ad_engagements_obj = ads_user_data.get('adEngagements', {})
    engagements_list = ad_engagements_obj.get('engagements', [])
    
    for engagement in engagements_list:
        # Each engagement has impressionAttributes -> matchedTargetingCriteria
        impression_attrs = engagement.get('impressionAttributes', {})
        criteria_list = impression_attrs.get('matchedTargetingCriteria', [])
        
        # Check for exact match: targetingType == 'Interests' and targetingValue == 'Shopping'
        has_match = any(
            criterion.get('targetingType') == 'Interests' and 
            criterion.get('targetingValue') == 'Shopping'
            for criterion in criteria_list
        )
        
        if has_match:
            matching_ads_count += 1
            
            # Retrieve advertiser name from advertiserInfo
            advertiser_info = impression_attrs.get('advertiserInfo', {})
            advertiser_name = advertiser_info.get('advertiserName', 'Unknown')
            
            advertisers_set.add(advertiser_name)
            advertiser_counts[advertiser_name] += 1

print("\n--- Quiz Answers ---")
print(f"a. Matching ads count: {matching_ads_count}")
print(f"b. Unique advertisers count: {len(advertisers_set)}")
if advertiser_counts:
    top_advertiser, top_count = advertiser_counts.most_common(1)[0]
    print(f"c. Top advertiser name: {top_advertiser} (used in {top_count} ads)")
else:
    print("c. Top advertiser name: None found")