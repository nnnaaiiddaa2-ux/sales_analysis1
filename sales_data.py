# sales_data.py
sales_data = [100, 200, 300, 400, 500]

def total_sales(data):
    return sum(data)

def average_sales(data):
    return sum(data) / len(data)

print(f"Sales data: {sales_data}")
print(f"Total sales: {total_sales(sales_data)}")
print(f"Average sales: {average_sales(sales_data)}")
