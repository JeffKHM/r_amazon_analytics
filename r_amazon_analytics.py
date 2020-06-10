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
print('一共有', len(new), '笔留言长度小于100')
print(new[0])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good), '笔留言提到good')

#文字计数
wc = {} # word_count
for d in data:
    words = d.split(' ')
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1 # 新增的Key进wc字典

for word in wc:
    if wc[word] > 1000000:
        print(word, wc[word])

print(len(wc))
print(wc['Jeff'])

while True:
	word = input('请问你想查什麽字:')
	if word == 'q':
		break             
	if word in wc:	
		print(word,'出现过的次数为：', wc[word])
	else:
		print('这个字没有出现过噢！')

print('感谢使用本查讯功能')
 

 