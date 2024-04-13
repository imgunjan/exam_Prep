def calculate_rec_area(length, breadth):
    area = length * breadth
    return round(area)


lenght = float(input("Enter the length :"))
breath = float(input("Enter the breadth :"))

print(calculate_rec_area(lenght, breath))
