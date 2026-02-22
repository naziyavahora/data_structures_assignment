#Task 1
products=["powerbank","mobile","laptop","charger","headphones","cable"]
sample_product=("powerbank",200,"Accessories")

print(products[1])
print(products[-1])

products.append("Airpods")
products.append("tablet")

print("updated products: ",products)

sample_product=list(sample_product)
 
sample_product[1]=300

sample_product=tuple(sample_product)
print(sample_product)

#Task 2

categories=["Accessories","electronics","electronics","Accessories",
            "Accessories","Accessories","Accessories","electronics"]

categories_set=set(categories)

print("updated categoty set is here : ",categories_set)

print("Is given category is there: ","electronics" in categories_set)

print("Unique category in set: ",len(categories_set))

#Task 3

price_dict={
    "powerbank":1500,
    "mobile":40000,
    "laptop":85000,
    "charger":2000,
    "headphones":4000,
    "cable":500,
   
}

price_dict["airpods"]=4500
print("price after adding new product: ",price_dict)

price_dict["tablet"]=25000
print("price after adding 2nd product: ",price_dict)

remove_product="diary"
if remove_product in price_dict:
    del price_dict[remove_product]

else:
    print(f"{remove_product} not found in the price_dict")

print(price_dict)

total_price_of_products=sum(price_dict.values())
avg_price=total_price_of_products/len(price_dict)
print("Average price of all products: ",avg_price)


#Task 4 
products=["powerbank","mobile","laptop","charger","headphones","cable","airpods","tablet"]

categories=["Accessories","electronics","electronics","Accessories",
            "Accessories","Accessories","Accessories","electronics"]

catalog=[]

for i in range(len(products)):
    product=products[i]
    price=price_dict[product]
    category=categories[i]
    catalog.append((product,price,category))

print("catalog: ",catalog)

