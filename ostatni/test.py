list1 = [1,2,3]
list2 = ["zelenina","jabko","Anananananas"]
result = []
for i in list1:
    if i > 1:
        i = i*5
        result.append(i)
print(result)

a = [(i,b) for i in list1 for b in list2 if i > 1]
print(f"HAHAHA {a}")