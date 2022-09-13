from DAL.products_dal import ProductsDAL


class ProductsBL():
    def __init__(self):
        self.__productsDAL = ProductsDAL()
    
    def get_all_products(self):
        data = self.__productsDAL.read_file()
        return data["products"]
    
    def get_product(self, id):
        data = self.__productsDAL.read_file()
        arr = data["products"]
        res = list(filter(lambda x : x["id"] == int(id), arr))
        return res[0]

    def add_product(self, obj):
        data = self.__productsDAL.read_file()
        arr = data["products"]
        arr.append(obj)
        data2 = {"products": arr}
        self.__productsDAL.write_file(data2)
        return "Product added !"

    def update_product(self, id, obj):
        data = self.__productsDAL.read_file()
        arr = data["products"]
        for i in range(len(arr)):
            if arr[i]["id"] == int(id):
                arr[i] = obj
                break
        data2 = {"products": arr}
        self.__productsDAL.write_file(data2)
        return "Product updated !"

    def delete_product(self, id):
        data = self.__productsDAL.read_file()
        arr = data["products"]
        index = -1
        for i in range(len(arr)):
            if arr[i]["id"] == int(id):
                index = i
                break
        arr.pop(index)
        data2 = {"products": arr}
        self.__productsDAL.write_file(data2)
        return "Product delete !"