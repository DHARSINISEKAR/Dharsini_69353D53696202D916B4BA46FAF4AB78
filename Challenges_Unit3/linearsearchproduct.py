def linear_search_product(productlist,targetproduct):
 indices=[]
 for index,product in enumerate(productlist):
     if product==targetproduct:
       indices.append(index)
 return indices
product=["shoes","boot","loater","shoes","sandal","shoes"]
target="shoes"
target2="apple"
result=linear_search_product(product,target)
print(result)
result=linear_search_product(product,target)
print(result)
 
