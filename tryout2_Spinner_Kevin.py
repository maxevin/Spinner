def counterClockwise(list_awal):
    list_baru = []                                              #Membuat list kosong
    x = [list_awal[0][2],list_awal[1][2],list_awal[2][2]]       #Melakukan extract dari index belakang
    y = [list_awal[0][1],list_awal[1][1],list_awal[2][1]]       #Melakukan extract dari index tengah
    z = [list_awal[0][0],list_awal[1][0],list_awal[2][0]]       #Melakukan extract dari index depan
    list_baru.append(x)                                         #Penggabungan list kosong terhadap list extract
    list_baru.append(y)                                         #Penggabungan list kosong terhadap list extract
    list_baru.append(z)                                         #Penggabungan list kosong terhadap list extract
    return list_baru                                            #Penyimpanan Nilai

list_awal = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(counterClockwise(list_awal))                              #Panggil Function