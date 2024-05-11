geese = ["African", "Roman Tufted", "Toulouse", "Pilgrim", "Steinbacher"]
def goose_filter(birds):
    sorted_birds = []
    for item in birds:
        if item in geese:
            continue
        else:
            sorted_birds.append(item)
    print(sorted_birds)

goose_filter(["Mallard", "Hook Bill", "African", "Crested", "Pilgrim", "Toulouse", "Blue Swedish"])
# ["Mallard", "Hook Bill", "Crested", "Blue Swedish"]