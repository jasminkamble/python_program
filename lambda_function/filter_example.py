list_str =["jasmine","merigold","sunflower","blue lily","rose","mogra"]

filter_list1 =filter(lambda a:len(a)==4,list_str)
filter_list2 =filter(lambda a:len(a)==5,list_str)
filter_list3=filter(lambda a:len(a)>6,list_str)
filter_list4 =filter(lambda a:len(a)>8,list_str)

print(list(filter_list1))
print(list(filter_list2))
print(list(filter_list3))
print(list(filter_list4))
