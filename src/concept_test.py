
from data_manager import *
from category import Category, Product
from tree import Tree
from website import Webpage

def main():
    config = read_json("test")["UK"]["M&S"]
    search_url = config["base_url"]
    categories = config["categories"]

    web_tree = Tree()

    for category, items in categories.items():
        new_category = Category(name=category) 
        web_tree.add_category(new_category)
        for item in items:
            # Create subcategory and link it to parent category
            new_subcategory = Category(name=item)
            web_tree.add_category(new_subcategory)
            web_tree.create_edge(new_category, new_subcategory)

            #Search for item on website
            soup = Webpage.get_source_code(search_url + item).find("div", {"class": "search-result-content"})
            if soup:
                for product_on_web in Webpage.get_element(soup, "li"):
                    new_product = get_product_details(product_on_web)
                    if new_product:
                        new_subcategory.add_product(new_product)
    
    display(web_tree)
    write_csv("consept_test", web_tree, config)
  
def display(web_tree):
    for category in web_tree.get_categories():
        if len(category.get_subcategories()) > 0:
            print(category)
        for subcategory in category.get_subcategories():
            print(f"\t{subcategory}")
            for product in subcategory.get_products():
                print(f"\t\t{product}")
        
def get_product_details(product_details):
    try:
        title = product_details.find("h3", {"class":"product__title"}).get_text().strip()
        price = product_details.find("div", {"class":"product__price"}).get_text().strip()
        new_product = Product(title=title, price=price)
        return new_product
    except Exception as ex:
        print(f"Error - get_product_details {ex}")
    
def write_csv(file_name, web_tree, config=None):
    path = Path.cwd().parent.joinpath(r"data\\")
    columns = ["Category", "Searched Item", "Product Description", "Price", "Currency"]
    df = pd.DataFrame(columns=columns)

    for category in web_tree.get_categories():
        for subcategory in category.get_subcategories():
            for product in subcategory.get_products():
                df2 = pd.DataFrame({"Category": category.get_name(),
                                    "Searched Item": subcategory.get_name(),
                                    "Product Description": product.get_title(),
                                    "Price": product.get_price().get_numberic_price(),
                                    "Currency": ["£"]})
                df = df.append(df2, ignore_index = True)

    df.to_csv(path.joinpath(file_name + ".csv"), index=False, encoding='utf-8-sig')

if __name__ == "__main__":
    main()


# TODO:
# [x] Read json
# [x] loop categories
# [x] loop items
# [X] search item in website
# [X] get product details
# [X] write to csv

# Process is category specific, results are already filtered from beginning
# We have control on categories and subcategories
# No need to map for products in survey and scraping result(aggregation part) - huge increased performance: n2 is removed