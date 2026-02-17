#task 1
products=["phone","buds","charger","adapter","connector","specs"]

#task 2
sample_product=("phone",35000,"electronic")

#task 3
print("2nd product is:", products[1])
print("last product is:", products[-1])

#task 4
products.append("tablet")
products.append("laptop")

print(products)

#task 5
list_sample_product=list(sample_product)
list_sample_product=["phone",50000,"electronic"]
sample_product=tuple(list_sample_product)

print(sample_product)