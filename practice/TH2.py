import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# file = 'e:/DA/practice/file ví dụ.xlsx'
# df = pd.read_excel(file)
#chuyen doi thanh csv
# csv_file = 'e:/DA/practice/csv.csv'
# df.to_csv(csv_file, index = False)
sns.set_theme()
# Đặt tùy chọn hiển thị để hiển thị tất cả các cột
pd.set_option('display.max_columns', None)
df = pd.read_csv('e:/DA/practice/csv.csv',header=0,na_values="NA",comment="\t",sep=',',skipinitialspace = True)
print(df.info())
#print(df["transportation"].unique())
# ax = sns.countplot(data =df,x="transportation",hue ="Method Payment")
# ax.set(title = "Number of Transportation vs number of buyer",xlabel ="Number of Cylinders", ylabel="Number of Cars")
# plt.show()
g = sns.FacetGrid(df,col ="transportation")
g.map(sns.histplot,"HS Code")
plt.show()
