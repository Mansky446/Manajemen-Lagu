# Fungsi konversi dict lagu -> string yang bisa ditulis ke file
def lagu_ke_rawdata(lagu):
    rawdata = "+".join(lagu.values())
    return rawdata

# Fungsi konversi string yang bisa ditulis ke file -> dict lagu
def rawdata_ke_lagu(rawdata):
    list_properti_lagu = rawdata.split("+")
    return {
        "judul": list_properti_lagu[0],
        "penyanyi": list_properti_lagu[1],
        "album": list_properti_lagu[2],
        "genre": list_properti_lagu[3],
        "tahun": list_properti_lagu[4],
        "durasi": list_properti_lagu[5],
        "ditambahkan": list_properti_lagu[6],
        "diedit": list_properti_lagu[7]
    }

# Fungsi konversi string yang bisa ditulis ke file -> list dict lagu
def rawdata_ke_list_lagu(rawdata):
    if len(rawdata.strip()) == 0:
        return []
    list_rawdata_lagu = rawdata.split("?")
    list_lagu = []
    for rawdata_lagu in list_rawdata_lagu:
        list_lagu.append(rawdata_ke_lagu(rawdata_lagu))
    return list_lagu

# Fungsi konversi list dict lagu -> string yang bisa ditulis ke file
def list_lagu_ke_rawdata(list_lagu):
    if len(list_lagu) == 0:
        return ""
    list_rawdata_lagu = []
    for lagu in list_lagu:
        list_rawdata_lagu.append(lagu_ke_rawdata(lagu))
    rawdata = "?".join(list_rawdata_lagu)
    return rawdata
