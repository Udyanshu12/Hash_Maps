from hashTable import HashMap, item_in_common

a_list = [10, 30, 40, 55, 22, 60, 70, 35, 67, 76]
b_list = [5, 11, 15, 21, 26, 31, 36, 42, 37, 58]
print(item_in_common(a_list, b_list))

my_table = HashMap()
my_table.set_item("red", 500)
my_table.set_item("blue", 1200)
my_table.set_item("green", 1700)
my_table.set_item("yellow", 1500)
my_table.set_item("orange", 300)
my_table.set_item("pink", 150)

print(my_table.get('green'))
print(my_table.keys())
my_table.print_table()
