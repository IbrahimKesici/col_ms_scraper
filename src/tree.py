from category import Category

class Tree():

    def __init__(self, category_names=None):
        self.categories = {}

    def get_categories(self):
        return self.categories.values()

    def get_category_by_name(self, name):
        name = name.capitalize()
        for key in self.categories.keys():
            if name in key:
                return self.categories[key]
    
    def add_category(self, category):
        self.categories[category.get_unique_name()] = category

    def create_edge(self, category, subcategory):
        if category.get_unique_name() in self.categories:
            self.categories[category.get_unique_name()].add_subcategory(subcategory)

    def contain_subcategory(self, category):
        return len(category.get_subcategories())

    def display(self):
        for category in self.categories.values():
            print(category)
            for subCategory in category.get_subcategories():
                print("\t" + subCategory.get_unique_name())
                for subsubcategory in subCategory.get_subcategories():
                    print("\t\t" + subsubcategory.get_unique_name())
                   


