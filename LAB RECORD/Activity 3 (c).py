def merge_dictionaries_with_overlap():
    
    print("Enter the elements of the first dictionary (key:value pairs, separated by commas):")
    dict1_input = input()
    dict1 = {key.strip(): int(value.strip()) for key, value in [item.split(":") for item in dict1_input.split(",")]}

    print("Enter the elements of the second dictionary (key:value pairs, separated by commas):")
    dict2_input = input()
    dict2 = {key.strip(): int(value.strip()) for key, value in [item.split(":") for item in dict2_input.split(",")]}

    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] += value 
        else:
            merged_dict[key] = value  
    print("\nMerged Dictionary:")
    print(merged_dict)

merge_dictionaries_with_overlap()
