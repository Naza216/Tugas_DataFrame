import pandas as pd

#soal 1
df_dataJabar = pd.read_csv('jumlah_produksi_sampah.csv')
df_dataJabar

#soal 2
sampah_2020 = 0
for index,row in df_dataJabar.iterrows():
  if(row['tahun']==2020):
    sampah_2020 += row['jumlah_produksi_sampah']


df_datasampah2020 = pd.DataFrame({'tahun':'2020','jumlah sampah':[sampah_2020]})
df_datasampah2020.to_csv('data sampah 2021.csv',index=False)
df_datasampah2020.to_excel('data sampah 2021.xlsx',index=False)
print(df_datasampah2020)

#soal 3
sampah_pertahun = {}
for index,row in df_dataJabar.iterrows():
  tahun = row['tahun']
  jumlah = row['jumlah_produksi_sampah']
  if tahun in sampah_pertahun:
    sampah_pertahun[tahun] += jumlah
  else:
     sampah_pertahun[tahun] = 0

df_sampah_pertahun = pd.DataFrame(sampah_pertahun.items(),columns=['tahun','total sampah'])
df_sampah_pertahun.to_csv('sampah setiap tahun.csv',index=False)
df_sampah_pertahun.to_excel('sampah setiap tahun.xlsx',index=False)

print(df_sampah_pertahun)

#soal 4
sampah_kabupaten = {}

for index,row in df_dataJabar.iterrows():
  nama_kabupaten = row['nama_kabupaten_kota']
  tahun = row['tahun']

  if nama_kabupaten not in sampah_kabupaten:
    sampah_kabupaten[nama_kabupaten]={}
  if tahun not in sampah_kabupaten[nama_kabupaten]:
    sampah_kabupaten[nama_kabupaten][tahun] = 0
  
  sampah_kabupaten[nama_kabupaten][tahun] += row['jumlah_produksi_sampah']

df_sampah_kabupatem = pd.DataFrame(sampah_kabupaten)
df_sampah_kabupatem.to_csv('sampah_kab.csv',index=False)

print(sampah_kabupaten)