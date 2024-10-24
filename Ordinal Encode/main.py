import pandas as pd
import random
data=pd.read_csv("trial.csv")

def OrdinalEncoder(column):


  if column in data.columns:
    print("Column found")
    if data[column].dtype=='object':
      print("Encoding")
      column_list=list(data[column].unique())
      List=list(range(len(column_list)))
      Dict={}
      for i in column_list:
        Dict[i]=random.choice(List)
        List.remove(Dict[i])
      EncodedList=[]
      for j in data[column]:
        EncodedList.append(Dict[j])
      data[column]=EncodedList
      print(data)
