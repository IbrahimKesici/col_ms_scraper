from data_manager import *
from tree import Tree
from website import Webpage
from category import Category, Product
import re


def main():
    config = read_json("ms_config")["Boots"]
    web_tree = Tree()
    create_categories(web_tree, config)
    assing_hrefs(web_tree, config)

    for category_name in config["categories"].keys():
        category = web_tree.get_category_by_name(category_name)
        print(category.get_name())
        for link in category.get_href(single=False):
            subcategories = re.sub("https://www.boots.com/","",link).split("/")
            
            for i, subcategory in enumerate(subcategories):
                #Create categories and edges between them
                if web_tree.get_category_by_name(subcategory):
                    parent_category = web_tree.get_category_by_name(subcategory)
                    print(f"Parent: {subcategory}")
                    continue                    
                else:
                    print(f"Created: {subcategory}")
                    new_subcategory = Category(name=subcategory)
                    web_tree.add_category(new_subcategory)
                    web_tree.create_edge(parent_category, new_subcategory)
                    parent_category = new_subcategory
                
                #Add product details to leaf
                if i == len(subcategories)-1:
                    print(f"{link}----------------------------------------------------------")
                    try:
                        soup = Webpage.get_source_code(link)
                    except Exception as ex:
                        print(f"Error - link ************************** {link} - {ex}")
                        continue
                    for product_detail in Webpage.get_element(soup, "div", "class", "estore_product_container"):
                        new_product = get_product_details(product_detail)
                        if new_product:
                            parent_category.add_product(new_product)
                            print(new_product)
        
            #print(f"\t{str(link)}")
    
    write_to_csv("boots", web_tree, config)
    #web_tree.display()


def create_categories(web_tree, config):
    for category_name in config["categories"].keys():
        new_category = Category(name=category_name)
        web_tree.add_category(new_category)

def assing_hrefs( web_tree, config):
    soup = Webpage.get_source_code(config["base_url"]).find("div", {"id":"topLevelMenu_1590591"})
    for a in soup.find_all("a", href=True):
        category_name = ""
        try:
            category_name = re.search(r"boots.com/(.*?)/", a["href"]+"/").group(1)
        except:
            continue
        category = web_tree.get_category_by_name(category_name)
        if category:
            category.add_href(a["href"])
            

def get_product_details(product_details):
    try:
        title = product_details.find("div", {"class": "product_name"}).find("a").get_text().strip()
        price = product_details.find("div", {"class": "product_price"}).get_text().strip()
        new_product = Product(title=title, price=price)
        return new_product
    except Exception as ex:
        print(f"Error - get_product_details {ex}")
    

if __name__ == "__main__":
    main()