s='abc'
t='ahbgdc'
list1 = list(s)
list2 = list(t)
for i in range(0,len(list1)):
    for j in range(0,len(list2)):
        if list1[i]==list2[j]:
            print(list2[j])
            list2[j] = list2[:j]
            break
        else:
            print('False')
            break

    i = i+1
print('True')
