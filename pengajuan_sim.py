import time
print("=== SISTEM PENDAFTARAN & UJIAN SIM DIGITAL (SIMULASI) ===")
    
# 1. Pengecekan Syarat Utama (Outer Conditional)
usia = int(input("Masukkan usia Anda saat ini: "))

if usia >= 17:
    print("\n[✓] Usia memenuhi syarat minimum (>= 17 tahun).")
    print("Pilih Golongan SIM yang ingin diajukan:")
    print("1. SIM A (Mobil Penumpang)")
    print("2. SIM C (Sepeda Motor)")
    pilihan_sim = input("Masukkan pilihan (1/2): ")
        
    # 2. Pengecekan Dokumen & Tes Kesehatan (Inner Conditional Level 1)
    has_ktp = input("Apakah Anda memiliki E-KTP? (y/n): ").lower()
    sehat_jasmani = input("Apakah Anda lulus tes kesehatan jasmani? (y/n): ").lower()
    sehat_rohani = input("Apakah Anda lulus tes psikologi? (y/n): ").lower()
        
    if has_ktp == 'y' and sehat_jasmani == 'y' and sehat_rohani == 'y':
        print("\n[✓] Validasi dokumen dan administrasi sukses!")
        print("Memulai simulasi Ujian Teori Online. Harap konsentrasi...")
        time.sleep(1)
            
        # 3. Pelaksanaan Ujian Teori (Inner Conditional Level 2)
        print("\n--- SOAL UJIAN TEORI ---")
        print("Apa arti lampu lalu lintas berwarna kuning?")
        print("a. Berhenti mendadak\nb. Bersiap-siap berhenti / berhati-hati\nc. Tancap gas")
        jawaban = input("Jawaban Anda (a/b/c): ").lower()
            
        if jawaban == 'b':
            print("\n[✓] Selamat! Anda LULUS Ujian Teori.")
                
            # 4. Penentuan Biaya Resmi PNBP Berdasarkan Golongan SIM (Inner Conditional Level 3)
            if pilihan_sim == '1':
                jenis_sim = "SIM A"
                biaya_pnbp = 120000
            elif pilihan_sim == '2':
                jenis_sim = "SIM C"
                biaya_pnbp = 100000
            else:
                jenis_sim = "Tidak Diketahui"
                biaya_pnbp = 0
                
            # Kalkulasi total biaya (PNBP + Biaya Tes Medis Flat Rp75.000)
            total_biaya = biaya_pnbp + 75000 if biaya_pnbp > 0 else 0
                        
            if total_biaya > 0:
                print(f"\n==========================================")
                print(f"STATUS: DIREKOMENDASIKAN UNTUK UJIAN PRAKTIK")
                print(f"Jenis SIM   : {jenis_sim}")
                print(f"Biaya PNBP  : Rp{biaya_pnbp:,}")
                print(f"Biaya Tes   : Rp75,000")
                print(f"Total Bayar : Rp{total_biaya:,}")
                print(f"==========================================")
                print("Silakan datang ke Satpas terdekat untuk jadwal ujian praktik lapangan.")
            else:
                print("\n[X] Pilihan golongan SIM tidak valid. Proses dibatalkan.")
    
        else:
            print("\n[X] Anda GAGAL Ujian Teori. Silakan pelajari kembali materi dan coba lagi 14 hari kemudian.")
    
    else:
     print("\n[X] Pendaftaran Ditolak: Dokumen E-KTP atau hasil tes medis Anda tidak lengkap.")
            
else:
    print(f"\n[X] Pendaftaran Ditolak: Usia Anda ({usia} tahun) belum mencukupi.")
    print("Syarat minimal pembuatan SIM adalah 17 tahun.")