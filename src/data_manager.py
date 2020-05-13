import json
from pathlib import Path
import pandas as pd

def read_json(file_name, path= Path.cwd().parent.joinpath(r"config\\")):
    with open(path.joinpath(file_name + ".json"), "r", encoding="utf-8") as f:
        json_data = json.load(f)
    return json_data

def write_to_json():
    pass

def write_to_csv(file_name, tree,  config=None):
    path = Path.cwd().parent.joinpath(r"data\\")
    columns = ["Category 1", "Category 2", "Category 3", "Product Description", "Price", "Currency"]
    df = pd.DataFrame(columns=columns)

    for category_name in config["categories"].keys():
        main_category =  tree.get_category_by_name(category_name)
        if main_category and tree.contain_subcategory(main_category) > 0: 
            for subCategory in main_category.get_subcategories():
                for subsubcategory in subCategory.get_subcategories():
                    for product in subsubcategory.get_products():
                        df2 = pd.DataFrame({"Category 1": main_category.get_name(),
                                            "Category 2": subCategory.get_name(),
                                            "Category 3": subsubcategory.get_name(),
                                            "Product Description": product.get_title(),
                                            "Price": product.get_price().get_numberic_price(),
                                            "Currency": [config["currency"]]})
                        df = df.append(df2, ignore_index = True)

    df.to_csv(path.joinpath(file_name + ".csv"), index=False, encoding='utf-8-sig')
