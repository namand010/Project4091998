#print("There are {} different telephone numbers in the records.".format(len(lis1)))

#with open('calls.csv', 'r') as f:
 #   reader = csv.reader(f)
  #  calls = list(reader)

#lis2 = []
#for row in range(len(calls)):
#    if calls[row][0] not in lis2:
#        lis2.append(calls[row][0])

#print("There are {} different telephone numbers in the records.".format(len(set(lis1+lis2))))



#lis_u = []
#for row in range(len(calls)):
#    if calls[row][0] not in lis_u:
#        lis_u.append(calls[row][0])

#db = dict.fromkeys(set(lis_u))
#print(len(db))
#for i in range(len(calls)):
#        if db[calls[i][0]] == None:
#            db[calls[i][0]] = calls[i][3]
#        else:
#            db[calls[i][0]] = db[calls[i][0]] + calls[i][3]
#print(max(db.values()))
