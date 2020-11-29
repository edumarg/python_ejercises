import csv

with open("data.csv","w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["trabsaccion_id", "product_id", "price"])
    writer.writerow(["100", "1", "5.5"])
    writer.writerow(["101", "2", "10"])

with open("data.csv") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)