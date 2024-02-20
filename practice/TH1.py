import pandas as pd

file = 'e:/DA/practice/file ví dụ.xlsx'
df = pd.read_excel(file)
# Thiết lập hiển thị tất cả các cột
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_rows', None)
#print(df.info()) #thông tin chi tiết về data frame
#print(df.head())
#kiểm tra xem có dữ liệu trùng hay không
#print(df.duplicated().sum())
# # Tạo một mask để xác định các dòng bị trùng lặp
# mask_duplicate = df.duplicated()

# # Lọc các dòng bị trùng lặp
# duplicate_rows = df[mask_duplicate]

# # Hiển thị các dòng bị trùng lặp
# print("Các dòng bị trùng lặp:")
# print(duplicate_rows)

#Kiểm tra các vị trị bị thiếu
#print(df.isna().sum())
#Xử lý dữ liệu khi bị khuyết
#df1 = df.dropna() # xóa luôn dòng
df2 = df.fillna({"B/L Number Or AWB Number":0,"Flight/Voyage Number":0})#Thay thế bằng không
print(df2.info())
print(df2.isna().sum())
# #Xóa dữ liệu thừa
# df2=df.drop(["Export Port","Port of loading"],axis = 1, inplace = True)
# print(df.info())
# df2 = df.transportation.unique()
# print(df2)
df2 = df.transportation.value_counts()
print(df2)
