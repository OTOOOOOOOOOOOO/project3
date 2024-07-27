Soal = [

    {
        "soal" : "Hewan Apa Yang Berkaki Tiga ? ",
        "OpsiSoal" : [ "A.Ikan", "B.Kura - Kura", "C.Kancil", "D.Tidak ada" ],
        "Key" : "D"
    },  
    {
        "soal" : "Ignatius Global School Berdiri Pada Tanggal ? ",
        "OpsiSoal" : [ "A.12-12-2012", "B.11-11-2011", "C.6-6-2006", "D.10-10-2010" ],
        "Key" : "A"
    },  
    {
        "soal" : "Nama kepanjangan Sir Sepri ? ",
        "OpsiSoal" : [ "A.Sepriada", "B.Sepriadi", "C.Sepriade", "D.Speriadi" ],
        "Key" : "B"
    },  
    {
        "soal" : "Nama panjang Yusuf ? ",
        "OpsiSoal" : [ "A.Muhammad Thoriq Yusuf", "B.Muhammad Yusuf", "C.Yusuf aja", "D.Ikan" ],
        "Key" : "B"
    },  
    {
        "soal" : "Favorit Yusuf ",
        "OpsiSoal" : [ "A.Musik", "B.Menari", "C.Puisi", "D.Makan" ],
        "Key" : "A"
    },  

]

#function
def Quiz( Prm_Soal ):#Parameter
    score = 0

#Sequencing
    #Iteration
    for soalLoop in Prm_Soal: 
        print( soalLoop["soal"] )
        for opsiLoop in soalLoop["OpsiSoal"]:
            print( opsiLoop )
        answer = input("Jawabannya Apa ? ").upper()

        #Selection
        if answer == soalLoop["Key"]:
            score = score + 1
            print("MANTAP!")
        else:
            print(f"Yahh Salah :<, Jawaban Lebih Tepat : {soalLoop['Key']}")
    print(f"Jawaban benar { score } dari jumlah soal { len(Soal) } " )

Quiz(Soal)

#Notes : Ini Yusuf Kerjakan Sendiri Tanpa Salin Atau Apapun Sir, Memakai Pemahaman Otak Sendiri :>