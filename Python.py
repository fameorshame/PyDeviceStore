prices = {
    "iPhone 5": 15,
    "Galaxy S8": 16,
    "Sony Xperia Z5": 14
}
left = {
    "iPhone 5": 0,
    "Galaxy S8": 4,
    "Sony Xperia Z5": 6
}

'''for charger in prices:
    print("\n"+charger)
    print("The cost of the products is: %s" % prices[charger])
    print("We have %s" % left[charger]+" left")'''
for charger in prices.keys():
    print("We have in stock:" + charger)
buy_spec = input("What would you like to purchase? ")

if buy_spec == "iPhone 5":
    print("Alright, let me check if that's available...")
    if left["iPhone 5"] >= 1:
        print("Congrats, it is indeed available")
    else:
        print("It's not your day, unfortunately")
else:
    print("Failure")
