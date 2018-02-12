from string import Template

class MyTemplate(Template):
	delimiter = '#'

def Main():
	cart = []
	cart.append(dict(item="coke",price=8, qty=2))
	cart.append(dict(item="icetea",price=7, qty=1))
	cart.append(dict(item="hitea",price=9, qty=53))

	t = MyTemplate("#qty * #item = #price")
	total = 0
	print("Cart: ")
	for data in cart:
		print(t.substitute(data))
		total += data["price"]

	print("Total: "+str(total) )

Main()