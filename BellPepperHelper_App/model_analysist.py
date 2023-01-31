ripe=0
sum=0
for index, row in df.iterrows():
     if row['score']>0.75:
       sum+=1
       if row['class_id']==1:
         ripe+=1
    
if sum==0:
  precent=0
else:
  precent=(sum/ripe)*100
print("Fruit number is "+str(sum) + "\nRipe fruits precentage is: "+ str(precent))