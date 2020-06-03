data = []    # question 1
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1
		if count % 10000 == 0:  # % 是用来求余数
		   print(len(data))
print('档案读取完了, 总共有', len(data), '笔资料') 

sum_len = 0
for d in data:
	sum_len = sum_len + len(d)  # sum_len += len(d)
    

print('留言的平均长度为', sum_len/len(data))


new = []   # question 2
for d in data:# for d in data 是这个data清单一笔一笔数据叫出来 # 每一个"d" 是单独留言
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '留笔言张度小於100') 
print(new[0])
print(new[2]) 

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '笔留言提到good')
print(good[0])


