def merge_dictionaries():
   
    print("Enter the elements of the first dictionary (key:value pairs, separated by commas):")
    dict1_input = input()
    dict1 = {key.strip(): value.strip() for key, value in [item.split(":") for item in dict1_input.split(",")]}

    print("Enter the elements of the second dictionary (key:value pairs, separated by commas):")
    dict2_input = input()
    dict2 = {key.strip(): value.strip() for key, value in [item.split(":") for item in dict2_input.split(",")]}

    merged_dict = {**dict1, **dict2}

    print("\nMerged Dictionary:")
    print(merged_dict)

merge_dictionaries()
