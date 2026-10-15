# a list of decimal numbers (Decimal)
numbers_list = [10, 42, 255, 100, 7]

# تعریف اعداد با مبناهای مختلف:
# 0b1010 معادل باینری عدد 10 است
# 0o52 معادل اکتال عدد 42 است
# 0xff معادل هگزادسیمال عدد 255 است

hex_num = 0xff   # 255
bin_num = 0b1010 # 10
oct_num = 0o52   # 42

dec_num = 100    # 100

dec_minus = dec_num - 40 # 60
dec_sum = dec_num + 30 # 130
dec_div = dec_num / 2 # 50.0
dec_mul = dec_num * 2 # 200

print(type(numbers_list))

print(dec_num , "in" , numbers_list , ":" , dec_num in numbers_list)
print(dec_minus , "in" , numbers_list , ":" , dec_minus in numbers_list)
print(dec_sum , "in" , numbers_list , ":" , dec_sum in numbers_list)
print(dec_div , "in" , numbers_list , ":" , dec_div in numbers_list)
print(dec_mul , "in" , numbers_list , ":" , dec_mul in numbers_list)

print(hex_num , "in" , numbers_list , ":" , hex_num in numbers_list)
print(bin_num , "in" , numbers_list , ":" , bin_num in numbers_list)
print(oct_num , "in" , numbers_list , ":" , oct_num in numbers_list)
print("############################################################")
print(0x14 , "in" , numbers_list , ":" , 0x14 in [10, 20, 30, 40])