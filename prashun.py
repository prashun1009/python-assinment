import json, gzip, sys

# takes input file via command
a = sys.argv[1]
b = sys.argv[2]
#f = open('/Home/t.json.gz','r')
# this is another way to input file.

urlh1 = {}
cat1 = []
sub1 = []
for i in gzip.open(a):
	k = json.loads(i)
       #taking urlh and available_price from 1st file and storing it into urlh1
	urlh1[k.get('urlh','')] = k.get("available_price","")
        #3. no of unique categories in file 1
	if k.get('category','') not in cat1:
		cat1.append(k.get('category',''))
        sub1.append(k.get('subcategory',''))

urlh2 = {}
cat2 = []
sub2 = []
for j in gzip.open(b):
	ki = json.loads(j)
        #taking urlh and available_price from 2nd file and storing it into urlh2
	urlh2[ki.get('urlh','')] = ki.get("available_price","")
        #3. no of unique categories in file 2
	if ki.get('category','') not in cat2:
                cat2.append(ki.get('category',''))
        sub2.append(ki.get('subcategory',''))


# 1. No of URLH which are overlapping
# 2. calculate price difference if urlh is overlapping
count = 0
for i in urlh1:
    if i in urlh2:
        count += 1
        try:
            diff = float(urlh1[i]) - float(urlh2[i])
        except:
            diff = ""
        if diff != 0.0:
            print("Difference :",diff)
print("No of overlapping URLH", count)


#3 Number of unique categories in both files
print("Unique categories in file 1", len(cat1))
print("Unique categories in file 2", len(cat2))


#4. categories which are not overlapping
uniq_cat = []
for i in cat1:
	if i not in cat2:
		uniq_cat.append(i)
for i in cat2:
	if i not in cat1:
		uniq_cat.append(i)

print('List of unique categories', uniq_cat)


#5. Create Taxonomy
count_1 = []
count_2 = []
sub_tax1 = {}
sub_tax2 = {}
for i in sub1:
    if i not in count_1:
        count_1.append(i)
for j in sub2:
    if j not in count_2:
        count_2.append(j)

for i in count_1:
    sub_tax1[i] = sub1.count(i)
for j in count_2:
    sub_tax2[j] = sub2.count(j)

print("TAXONOMY FOR FILE 1 :")
for i in t_cat1.keys():
    for t in sub_tax1:
        if t in t_cat1[i]:
            print(i,">", t,">", sub_tax1[t])

print("TAXONOMY FOR FILE 2 :")
for i in t_cat2.keys():
    for t in sub_tax2:
        if t in t_cat2[i]:
            print(i,">", t,">", sub_tax2[t])


#6. Creating new file where mrp is normalized as "NA" where mrp is 0.
f = open('/tmp/mrp_normalized.txt','w')
for i in gzip.open(a):
   ks = json.loads(i)
   if ks.get('mrp','') == '0' or ks.get('mrp','') is None:
       ks['mrp'] = 'NA'
   f.write(json.dumps(ks)+ "\n")
print("NORMALIZED FILE CREATED IN TMP DIRECTORY")