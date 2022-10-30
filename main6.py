cars = ["Nano", "Tata", "Ford", "BMW", "Thar"]

for i in cars:
    if i == "BMW":
        break
    print(i)
    
    if i == "Tata":
        continue
    print(i)
