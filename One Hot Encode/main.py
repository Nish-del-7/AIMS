import pandas as pd

data=pd.read_csv("trial.csv")

def OneHotEncoder(column):
  if column in data.columns:
    if data[column].dtype==object:
      print("OneHotEncoding begins")
      ind=data.columns.get_loc(column)
      cat=list(data[column].unique())
      num_cat=len(cat)

      for i in range(num_cat):
        EncodedList=[]
        for j in data[column]:
          if j==cat[i]:
            EncodedList.append(1.0)
          else:
            EncodedList.append(0.0)
        data.insert(ind,data[column][i],EncodedList)
        print(data)
