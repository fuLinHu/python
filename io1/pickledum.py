#!/usr/bin/python3
import pickle,pprint

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)
print(selfref_list)
output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output=open('data.pkl', 'rb')

load = pickle.load(output)

pprint_pprint = pprint.pprint(load)

print(pprint_pprint)

load = pickle.load(output)

pprint_pprint = pprint.pprint(load)
print(pprint_pprint)
output.close()