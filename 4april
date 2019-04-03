import pandas as pd
import numpy as np

labels=['a','b','c','d']  
data=[10,20,30,40]  

arr=np.array(data)
  
#d={'a':10,'b':20,'c':30,'d':40} 
s=pd.Series(data)
#s=pd.Series(data)
#s2=pd.Series(data, labels)
s1=pd.Series(data, labels)

s2=pd.Series(['Apple', 'Cherry', 'Kiwi'] , ['f1','f2','f3'])

s3=pd.Series(['Apple', 'Cherry', 'Kiwi'] , ['f1','f2','f2'])

s3['f2']

sd=pd.Series(d)
type(sd)
sd.dtype
s1['d']

l1=[[1,2,3],[22,1,12],[21,22,23]] 

a1=np.array(l1) 

ss=pd.DataFrame(s3)
type(ss)
ss1=pd.DataFrame(a1,['a','b','c'], columns=['x','y','z'])

#data=pd.DataFrame(data,index,columns=[])

ss1['z']['b']
ss1['x']['b']
ss1['y']['c']

sx=ss1.x
sx=ss1['x']


s=pd.Series([10,34,6,34], index=['a','c','d','e'])
s3 = pd.Series([7, 4,-2, 3],index=['a','b', 'c', 'd']) 
splus=s + s3
s_str=pd.Series(['a','b','c'],index=[1,2,3])
s2_str=pd.Series(['a1','b1'],index=[1,2])
s_str.add(s2_str, fill_value=0)

s.add(s3, fill_value=0)
s.sub(s3, fill_value=2)
ssd=s.div(s3, fill_value=4)
s[~(s > 16)] 


                    
#Series s where value is not >1 >>> 
s[(s < -1) | (s > 122)] 
          #s where value is <-1 or >2 >>>

df=pd.DataFrame(a1)
type(df)
df=pd.DataFrame(a1,['a','b','c'], columns=['x','y','z'])
df[['x','y']]['a']#need to check
df[['x''y']['a']]
df.iloc
df.iloc[[0,1],[2]]
df.iat[0,2]
df.at['a','y']
df.loc[['a','b'],['y','z']]
df.ix[2]
df.ix[2,'z']
shape_df=df.shape            
df.index  
df.columns      
df.info()
df=pd.DataFrame(a1,['a','e','c'], columns=['x','y','z'])
df.sort_index()
df.sort_values(by='y') 
df.rank()
df.drop(['x'], axis=1)   
#Drop values from rows (axis=0)
df.drop('Country', axis=1)
def squaren(x):
    return x**2
squaren(6)
def muln(x):
    return x*2
muln(6)   
f = lambda x: x*2 
df=df.apply(f)      
df.apply(f)#inplace to be checked.  
df.applymap(f)
df.sum(axis=1)               
df.cumsum()                                     
df.min()
df.max()      
df.idxmin()
df.idxmax() 
df.describe()          
df.mean()
df.median()

www.poojaangurala.com
github.com/m-pooja
