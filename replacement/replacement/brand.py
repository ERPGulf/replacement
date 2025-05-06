

# # import requests
# # import csv

# # def get_arabic_translation(text):
# #     url = "https://erp.dallahmzad.com:8012/api/method/auction.auction.Auction.chatgpt"
# #     headers = {'Cookie': 'full_name=Guest; sid=Guest; system_user=yes; user_id=Guest; user_image='}
# #     data = {'question': f'Write in Arabic - {text}'}
# #     response = requests.post(url, headers=headers, data=data)
# #     if response.status_code == 200:
# #         return response.json().get('message', '')
# #     else:
# #         return ''

# # brands = [
# #    "acura",
# #     "aero",
# #     "ak",
# #     "alfa_romeo",
# #     "ariel",
# #     "ashok",
# #     "aston_martin",
# #     "audi",
# #     "austin_healey",
# #     "avatr",
# #     "baic",
# #     "bentley",
# #     "bestune",
# #     "bmw",
# #     "borgward",
# #     "bugatti",
# #     "buggy",
# #     "buick",
# #     "cadillac",
# #     "changan",
# #     "chery",
# #     "chevrolet",
# #     "chrysler",
# #     "citroen",
# #     "cmc",
# #     "daewoo",
# #     "daihatsu",
# #     "dallara",
# #     "datsun",
# #     "dodge",
# #     "domy",
# #     "dong_sing",
# #     "dongfeng",
# #     "exeed",
# #     "factory_five",
# #     "ferrari",
# #     "fiat",
# #     "fisker",
# #     "force",
# #     "ford",
# #     "forthing",
# #     "foton",
# #     "fun_car",
# #     "fuso",
# #     "gac",
# #     "geely",
# #     "genesis",
# #     "gmc",
# #     "golf_car",
# #     "great_wall",
# #     "haima",
# #     "haval",
# #     "higer",
# #     "hino",
# #     "honda",
# #     "hongqi",
# #     "hongsheng",
# #     "hummer",
# #     "hyundai",
# #     "imperial",
# #     "ineos",
# #     "infiniti",
# #     "international",
# #     "isuzu",
# #     "iveco",
# #     "jac_motors",
# #     "jaguar",
# #     "jbc",
# #     "jeep",
# #     "jensen",
# #     "jetour",
# #     "jinbei",
# #     "jmc",
# #     "kia",
# #     "king_long",
# #     "koenigsegg",
# #     "ktm",
# #     "lada",
# #     "lamborghini",
# #     "lancia",
# #     "land_rover",
# #     "leapmotor",
# #     "lexus",
# #     "ligier",
# #     "lincoln",
# #     "local_motors",
# #     "lotus",
# #     "lykan",
# #     "lynk_&_co",
# #     "mack",
# #     "mahindra",
# #     "mangosta",
# #     "maserati",
# #     "maxus",
# #     "maybach",
# #     "mazda",
# #     "mclaren",
# #     "mercedes-benz",
# #     "mercury",
# #     "mg",
# #     "mini",
# #     "mini_mark",
# #     "mitsubishi",
# #     "mitsuoka",
# #     "morgan",
# #     "nissan",
# #     "noble_automotive",
# #     "oldsmobile",
# #     "omoda",
# #     "opel",
# #     "pagani",
# #     "panoz",
# #     "peugeot",
# #     "plymouth",
# #     "polaris",
# #     "polestar",
# #     "pontiac",
# #     "porsche",
# #     "proton",
# #     "radical",
# #     "rally_fighter",
# #     "rariro",
# #     "renault",
# #     "rivian",
# #     "rolls-royce",
# #     "saab",
# #     "saic_maxus",
# #     "saturn",
# #     "scania",
# #     "seat",
# #     "skoda",
# #     "smart",
# #     "ssangyong",
# #     "studebaker",
# #     "subaru",
# #     "suzuki",
# #     "tata",
# #     "taxi_london",
# #     "tesla",
# #     "toyota",
# #     "triumph",
# #     "tvr",
# #     "vanderhall",
# #     "volkswagen",
# #     "volvo",
# #     "wiseman",
# #     "wuling",
# #     "yamaha"
# # ]

# # # Open a CSV file for writing
# # with open('brands.csv', 'w', newline='', encoding='utf-8') as file:
# #     writer = csv.writer(file)
# #     # Write the header row
# #     writer.writerow(['Brand', 'Model', 'Brand (Arabic)', 'Model (Arabic)'])

# #     for brand in brands:
# #         url = f"https://production-api.qatarsale.com/api/v2/DefinitionsList/GetChildren?categoryUri=cars_for_sale&defId=5308&parentUri={brand}"
# #         response = requests.get(url)
# #         if response.status_code == 200:
# #             models = response.json()
# #             brand_arabic = get_arabic_translation(brand)
# #             for model in models:
# #                 model_arabic = get_arabic_translation(model['name'])
# #                 # Write each brand, model, and their Arabic translations to the CSV file
# #                 writer.writerow([brand, model['name'], brand_arabic, model_arabic])
# #         else:
# #             print(f"Failed  for brand: {brand}")

# # import csv

# # # Open the CSV file for reading
# # with open('brands.csv', 'r', encoding='utf-8') as file:
# #     reader = csv.reader(file)
# #     # Read and print each row
# #     for row in reader:
# #         print(row)

# # # with open('brands.csv', 'w', newline='') as file:
# # #     writer = csv.writer(file)
# # #     # Write the header row
# # #     writer.writerow(['Brand', 'Model'])

# # #     for brand in brands:
# # #         url = f"https://production-api.qatarsale.com/api/v2/DefinitionsList/GetChildren?categoryUri=cars_for_sale&defId=5308&parentUri={brand}"
# # #         response = requests.get(url)
# # #         if response.status_code == 200:
# # #             models = response.json()
# # #             for model in models:
# # #                 # Write each brand and model to the CSV file
# # #                 writer.writerow([brand, model['name']])
# # #         else:
# # #             print(f"Failed for brand: {brand}")

# # # import csv

# # # # Open the CSV file for reading
# # # with open('brands.csv', 'r') as file:
# # #     reader = csv.reader(file)
# # #     # Iterate over each row in the CSV file and print it
# # #     for row in reader:
# # #         print(row)


# # # for brand in brands:
# # #     url = f"https://production-api.qatarsale.com/api/v2/DefinitionsList/GetChildren?categoryUri=cars_for_sale&defId=5308&parentUri={brand}"
# # #     response = requests.get(url)
# # #     if response.status_code == 200:
# # #         models = response.json()
# # #         print(f"Brand: {brand}")
# # #         for model in models:
# # #             print(f" - Model: {model['name']}")
# # #     else:
# # #         print(f"Failed to fetch models: {brand}")
            

# import requests
# import csv

# def get_proper_name(text):
#     url = "https://erp.dallahmzad.com:8012/api/method/auction.auction.Auction.chatgpt"
#     headers = {'Cookie': 'full_name=Guest; sid=Guest; system_user=yes; user_id=Guest; user_image='}
#     data = {'question': f'Make this a proper name - {text}'}
#     response = requests.post(url, headers=headers, data=data)
#     if response.status_code == 200:
#         return response.json().get('message', '')
#     else:
#         return ''

# def get_arabic_translation(text):
#     url = "https://erp.dallahmzad.com:8012/api/method/auction.auction.Auction.chatgpt"
#     headers = {'Cookie': 'full_name=Guest; sid=Guest; system_user=yes; user_id=Guest; user_image='}
#     data = {'question': f'Write in Arabic - {text}'}
#     response = requests.post(url, headers=headers, data=data)
#     if response.status_code == 200:
#         return response.json().get('message', '')
#     else:
#         return ''

# brands = [
#    "acura",
#     "aero",
#     "ak",
#     "alfa_romeo",
#     "ariel",
#     "ashok",
#     "aston_martin",
#     "audi",
#     "austin_healey",
#     "avatr",
#     "baic",
#     "bentley",
#     "bestune",
#     "bmw",
#     "borgward",
#     "bugatti",
#     "buggy",
#     "buick",
#     "cadillac",
#     "changan",
#     "chery",
#     "chevrolet",
#     "chrysler",
#     "citroen",
#     "cmc",
#     "daewoo",
#     "daihatsu",
#     "dallara",
#     "datsun",
#     "dodge",
#     "domy",
#     "dong_sing",
#     "dongfeng",
#     "exeed",
#     "factory_five",
#     "ferrari",
#     "fiat",
#     "fisker",
#     "force",
#     "ford",
#     "forthing",
#     "foton",
#     "fun_car",
#     "fuso",
#     "gac",
#     "geely",
#     "genesis",
#     "gmc",
#     "golf_car",
#     "great_wall",
#     "haima",
#     "haval",
#     "higer",
#     "hino",
#     "honda",
#     "hongqi",
#     "hongsheng",
#     "hummer",
#     "hyundai",
#     "imperial",
#     "ineos",
#     "infiniti",
#     "international",
#     "isuzu",
#     "iveco",
#     "jac_motors",
#     "jaguar",
#     "jbc",
#     "jeep",
#     "jensen",
#     "jetour",
#     "jinbei",
#     "jmc",
#     "kia",
#     "king_long",
#     "koenigsegg",
#     "ktm",
#     "lada",
#     "lamborghini",
#     "lancia",
#     "land_rover",
#     "leapmotor",
#     "lexus",
#     "ligier",
#     "lincoln",
#     "local_motors",
#     "lotus",
#     "lykan",
#     "lynk_&_co",
#     "mack",
#     "mahindra",
#     "mangosta",
#     "maserati",
#     "maxus",
#     "maybach",
#     "mazda",
#     "mclaren",
#     "mercedes-benz",
#     "mercury",
#     "mg",
#     "mini",
#     "mini_mark",
#     "mitsubishi",
#     "mitsuoka",
#     "morgan",
#     "nissan",
#     "noble_automotive",
#     "oldsmobile",
#     "omoda",
#     "opel",
#     "pagani",
#     "panoz",
#     "peugeot",
#     "plymouth",
#     "polaris",
#     "polestar",
#     "pontiac",
#     "porsche",
#     "proton",
#     "radical",
#     "rally_fighter",
#     "rariro",
#     "renault",
#     "rivian",
#     "rolls-royce",
#     "saab",
#     "saic_maxus",
#     "saturn",
#     "scania",
#     "seat",
#     "skoda",
#     "smart",
#     "ssangyong",
#     "studebaker",
#     "subaru",
#     "suzuki",
#     "tata",
#     "taxi_london",
#     "tesla",
#     "toyota",
#     "triumph",
#     "tvr",
#     "vanderhall",
#     "volkswagen",
#     "volvo",
#     "wiseman",
#     "wuling",
#     "yamaha"
# ]


# # Open a CSV file for writing
# with open('brands.csv', 'w', newline='', encoding='utf-8') as file:
#     writer = csv.writer(file)
#     # Write the header row
#     writer.writerow(['Brand ', 'Model', 'Brand (Arabic)', 'Model (Arabic)'])

#     for brand in brands:
#         url = f"https://production-api.qatarsale.com/api/v2/DefinitionsList/GetChildren?categoryUri=cars_for_sale&defId=5308&parentUri={brand}"
#         response = requests.get(url)
#         if response.status_code == 200:
#             models = response.json()
#             brand_proper = get_proper_name(brand)
#             brand_arabic = get_arabic_translation(brand_proper)
#             for model in models:
#                 model_arabic = get_arabic_translation(model['name'])
#                 # Write each brand (proper name), model, and their Arabic translations to the CSV file
#                 writer.writerow([brand_proper, model['name'], brand_arabic, model_arabic])
#         else:
#             print(f"Failed  for brand: {brand}")

# # Open the CSV file for reading
# with open('brands.csv', 'r') as file:
#     reader = csv.reader(file)
#     # Iterate over each row in the CSV file and print it
#     for row in reader:
#         print(row)




import requests
import csv

def get_proper_name(text):
    url = "https://erp.dallahmzad.com:8012/api/method/auction.auction.Auction.chatgpt"
    headers = {'Cookie': 'full_name=Guest; sid=Guest; system_user=yes; user_id=Guest; user_image='}
    data = {'question': f'Make this a proper name - {text}'}
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json().get('message', '')
    else:
        return ''

def get_arabic_translation(text):
    url = "https://erp.dallahmzad.com:8012/api/method/auction.auction.Auction.chatgpt"
    headers = {'Cookie': 'full_name=Guest; sid=Guest; system_user=yes; user_id=Guest; user_image='}
    
    # Check if the entire text is numeric
    if text.isnumeric():
        return text
    
    parts = text.split()
    translated_parts = []
    for part in parts:
        if part.isalpha():  # Check if the part contains only letters
            data = {'question': f'Write in Arabic - {part}'}
            response = requests.post(url, headers=headers, data=data)
            if response.status_code == 200:
                translated_parts.append(response.json().get('message', ''))
            else:
                translated_parts.append(part)
        else:
            translated_parts.append(part)
    return ' '.join(translated_parts)


brands = [
   "acura",
    "aero",
    "ak",
    "alfa_romeo",
    "ariel",
    "ashok",
    "aston_martin",
    "audi",
    "austin_healey",
    "avatr",
    "baic",
    "bentley",
    "bestune",
    "bmw",
    "borgward",
    "bugatti",
    "buggy",
    "buick",
    "cadillac",
    "changan",
    "chery",
    "chevrolet",
    "chrysler",
    "citroen",
    "cmc",
    "daewoo",
    "daihatsu",
    "dallara",
    "datsun",
    "dodge",
    "domy",
    "dong_sing",
    "dongfeng",
    "exeed",
    "factory_five",
    "ferrari",
    "fiat",
    "fisker",
    "force",
    "ford",
    "forthing",
    "foton",
    "fun_car",
    "fuso",
    "gac",
    "geely",
    "genesis",
    "gmc",
    "golf_car",
    "great_wall",
    "haima",
    "haval",
    "higer",
    "hino",
    "honda",
    "hongqi",
    "hongsheng",
    "hummer",
    "hyundai",
    "imperial",
    "ineos",
    "infiniti",
    "international",
    "isuzu",
    "iveco",
    "jac_motors",
    "jaguar",
    "jbc",
    "jeep",
    "jensen",
    "jetour",
    "jinbei",
    "jmc",
    "kia",
    "king_long",
    "koenigsegg",
    "ktm",
    "lada",
    "lamborghini",
    "lancia",
    "land_rover",
    "leapmotor",
    "lexus",
    "ligier",
    "lincoln",
    "local_motors",
    "lotus",
    "lykan",
    "lynk_&_co",
    "mack",
    "mahindra",
    "mangosta",
    "maserati",
    "maxus",
    "maybach",
    "mazda",
    "mclaren",
    "mercedes-benz",
    "mercury",
    "mg",
    "mini",
    "mini_mark",
    "mitsubishi",
    "mitsuoka",
    "morgan",
    "nissan",
    "noble_automotive",
    "oldsmobile",
    "omoda",
    "opel",
    "pagani",
    "panoz",
    "peugeot",
    "plymouth",
    "polaris",
    "polestar",
    "pontiac",
    "porsche",
    "proton",
    "radical",
    "rally_fighter",
    "rariro",
    "renault",
    "rivian",
    "rolls-royce",
    "saab",
    "saic_maxus",
    "saturn",
    "scania",
    "seat",
    "skoda",
    "smart",
    "ssangyong",
    "studebaker",
    "subaru",
    "suzuki",
    "tata",
    "taxi_london",
    "tesla",
    "toyota",
    "triumph",
    "tvr",
    "vanderhall",
    "volkswagen",
    "volvo",
    "wiseman",
    "wuling",
    "yamaha"
]


# Open a CSV file for writing
with open('brands.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    # Write the header row
    writer.writerow(['Brand', 'Model', 'Brand (Arabic)', 'Model (Arabic)'])

    for brand in brands:
        proper_brand_name = get_proper_name(brand)
        url = f"https://production-api.qatarsale.com/api/v2/DefinitionsList/GetChildren?categoryUri=cars_for_sale&defId=5308&parentUri={brand}"
        response = requests.get(url)
        if response.status_code == 200:
            models = response.json()
            brand_arabic = get_arabic_translation(proper_brand_name)
            for model in models:
                model_arabic = get_arabic_translation(model['name'])
                # Write each brand, model, and their Arabic translations to the CSV file
                writer.writerow([proper_brand_name, model['name'], brand_arabic, model_arabic])
        else:
            print(f"Failed for brand: {brand}")
