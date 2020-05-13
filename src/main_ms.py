from data_manager import *
from tree import Tree
from website import Webpage
from category import Category, Product

def main():

    config = read_json("ms_config")["M&S"]
    print(config)

    web_tree = Tree()
    create_categories(web_tree, config)

    for category_name in config["categories"].keys():
        webpage = Webpage()
        parent_category = web_tree.get_category_by_name(category_name)
        url = config["base_url"] + parent_category.get_href()
        soup = Webpage.get_source_code(url)

        sub_menu_nav = Webpage.get_element(soup, "div", "class", "content-replace-holder nav-primary__submenu nav-submenu__six-col-gnav")
        for sub_element in Webpage.get_element(sub_menu_nav, "ul", "class", "nav-submenu__link-list"):
            new_subcategory2 = Category(name=sub_element["data-mns-sub-navigation-content"])
            web_tree.add_category(new_subcategory2)
            web_tree.create_edge(parent_category, new_subcategory2)
            for li in Webpage.get_element(sub_element, "a"):
                try:
                    new_subcategory3 = Category(name=li.get_text(), href=li['href'])
                    web_tree.add_category(new_subcategory3)
                    web_tree.create_edge(new_subcategory2, new_subcategory3)
                    soup = Webpage.get_source_code(config["base_url"]+li['href']).find( "div", {"class": "product__list col-xs-12 remove-padding"})
                    for product_details in Webpage.get_element(soup, "li"):
                        title = product_details.find("h3", {"class":"product__title"}).get_text().strip()
                        price = product_details.find("div", {"class":"product__price"}).get_text().strip()
                        new_product = Product(title=title, price=price)
                        new_subcategory3.add_product(new_product)
                        print(new_product)
                        #break
                except Exception as ex:
                    print(f"ERROR *****************************************{ex}")
                    continue
        print("--------------------------------------------")
    
    write_to_csv("m&s", web_tree, config)
    #web_tree.display()
    
def create_categories(web_tree, config):
    soup = Webpage.get_source_code(config["base_url"])
    for category_id in config["categories"].values():
        element = Webpage.get_element(soup,"a", "id", category_id)
        new_category = Category(name=element.get_text(), href=element["href"])
        web_tree.add_category(new_category)


if __name__ == "__main__":
    main()