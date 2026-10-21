import json

def load_categories():
    with open("data/category.json", encoding="utf-8") as f:
        return json.load(f)
def load_products(q=None, cates_id=None):
    with open("data/products.json", encoding="utf-8") as f:
        prods = json.load(f)
        if q:
            prods = [p for p in prods if p["name"].find(q)>=0]
            if cates_id:
                prods =[p for p in prods if p["cates_id"].__eq__(int(cates_id))]
        return prods
if __name__=="__main__":
        print(load_categories())
