import json
from collections import Counter
import re
import matplotlib.pyplot as plot

# helper for aggregating methods and functions
def get_file_data_as_json(file_name):
    with open(file_name,'r') as file:
        return json.load(file)

# returns a frequency related analysis 
def get_frequency_analysis(data):
    THRESHOLD_FREQUENCY = 10
    frequency_data = []
    # Collect all function/method labels
    for node in data['analysisData']['graphNodes']: 
        if node['type'] in ('Function', 'Method'):
            frequency_data.append(node['label'])
    counts = Counter(frequency_data)
    classified = {
        label: "utility" if freq > THRESHOLD_FREQUENCY else "business_logic"
        for label, freq in counts.items()
    }
    return classified, counts

# returns a prefix analysis 
def get_prefix_analysis(data):
    result_dict = dict()
    helper_prefix = [
            r'^_',
            r'^get_',
            r'^is_',
            r'^has_',
            r'^create_',
            r'^build_',
            r'^check_',
            r'^validate_'
            ]
    for node in data['analysisData']['graphNodes']: 
        if node['type'] in ('Function','Method'): 
            if any(re.match(pattern,node['label']) for pattern in helper_prefix):
                result_dict[node['label']] = 'helper'
            else:
                result_dict[node['label']] = 'business'
    return result_dict

# vibe coded this formatting thing, don't mind please. 
def print_results(title, data, counts=None):
    print(f"\n{title}")
    print("-" * 60)
    
    # Group by category
    by_category = {}
    for label, category in data.items():
        if category not in by_category:
            by_category[category] = []
        by_category[category].append(label)
    
    # Print counts
    for category, labels in sorted(by_category.items()):
        print(f"{category}: {len(labels)}")
    
    for category, labels in sorted(by_category.items()):
        print(f"{category}:")
        for label in sorted(labels)[:5]:
            if counts:
                print(f"  {label} ({counts.get(label, 1)}x)")
            else:
                print(f"  {label}")
        if len(labels) > 5:
            print(f"  ... {len(labels) - 5} more")
        print()

def main():
    file_name = 'data/analysis-with-code.json'
    json_data = get_file_data_as_json(file_name)
    
    freq_results, counts = get_frequency_analysis(json_data)
    print_results("Frequency Analysis", freq_results, counts)
    
    prefix_results = get_prefix_analysis(json_data)
    print_results("Prefix Analysis", prefix_results)

if __name__ == "__main__":
    main()
