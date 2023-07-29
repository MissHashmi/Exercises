# Flaten a list
my_list=[0,10,[20,30],40,50,[60,70,80],[90,100,110,120]]
flat_list=[]
for elements in my_list:
    if isinstance(elements,list):
        for nested_elem in elements:
            flat_list.append(nested_elem)
    else:
        flat_list.append(elements)
print(flat_list)
#Print Uncommon numbers
#solution1
list1 = [1, 3, 5, 7, ]
list2 = [1, 2, 4, 6, 6, 8]
m_list = []

for nums in list1:
    m_list.append(nums)

for elem in list2:
    if elem not in m_list:
        m_list.append(elem)

print(m_list)
#solution2
list1 = [1, 3, 5, 7, 9]
list2 = [1, 2, 4, 6, 6, 8]

m_set = set(list1)
m_set.update(list2)

m_list = list(m_set)
print(m_list)

#find all occurences of India in a given string ignoring the case

str1="Welcome to india.india  awesome,isn't it?"