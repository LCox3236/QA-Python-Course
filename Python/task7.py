companies = []
sales = []
#f = open('carSale.csv', 'r')
with open('carSale.csv', mode='r') as f:
    lines =(f.readlines())
    for x in range(0, len(lines),2):
        companies.append(lines[x].strip())
        sales.append(list(map(int,lines[x+1].strip().split(','))))

total = 0
for x in range (0, len(sales[0]),1):
    monthly = 0
    for y in range (0, len(sales),1):
        monthly += sales[y][x]
    print(f"{monthly}")
    if x < len(companies):
        total+= sum(sales[x])
print(total)

# for line in sales:
#     print(line)
# for l in companies:
#     print(l)
# print(len(companies))
# print(len(sales[0]))