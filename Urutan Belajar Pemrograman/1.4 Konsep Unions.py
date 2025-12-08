class UnionLike:
    def __init__(self):
        self.value = None
        self.type = None

    def set_int(self, n: int):
        self.value = int(n)
        self.type = "int"

    def set_float(self, f: float):
        self.value = float(f)
        self.type = "float"

    def set_char(self, c: str):
        if len(c) != 1:
            raise ValueError("Harus 1 karakter!")
        self.value = c
        self.type = "char"

    def __str__(self):
        return f"[{self.type}] = {self.value}"

#HASIL MODIFIKASI
"""
UNIONS - Prototype CLI (Python)
Fitur:
- Paket wisata (list + detail)
- Booking (simpan ke file)
- Pembayaran simulasi (mark paid)
- UMKM (lihat & preorder)
- Dashboard ringkas (jumlah booking, pendapatan)
- Persistensi sederhana ke JSON
"""

import json
from datetime import datetime
from typing import List, Dict, Optional
import os

DATA_FILE = "unions_data.json"

class Paket:
    def __init__(self, kode: str, nama: str, harga: float, deskripsi: str, kapasitas:int):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.deskripsi = deskripsi
        self.kapasitas = kapasitas

    def to_dict(self):
        return {"kode": self.kode, "nama": self.nama, "harga": self.harga,
                "deskripsi": self.deskripsi, "kapasitas": self.kapasitas}

    @classmethod
    def from_dict(cls, d): return cls(d["kode"], d["nama"], d["harga"], d["deskripsi"], d.get("kapasitas",0))

class Booking:
    def __init__(self, id_: str, paket_kode: str, tanggal: str, jumlah_orang: int, nama_pemesan: str,
                 contact: str, total: float, paid: bool=False, created=None):
        self.id = id_
        self.paket_kode = paket_kode
        self.tanggal = tanggal
        self.jumlah_orang = jumlah_orang
        self.nama_pemesan = nama_pemesan
        self.contact = contact
        self.total = total
        self.paid = paid
        self.created = created or datetime.now().isoformat(timespec="seconds")

    def to_dict(self):
        return self.__dict__

    @classmethod
    def from_dict(cls, d): return cls(d["id"], d["paket_kode"], d["tanggal"], d["jumlah_orang"],
                                       d["nama_pemesan"], d["contact"], d["total"], d["paid"], d["created"])

class UMKMItem:
    def __init__(self, id_: str, nama: str, harga: float):
        self.id = id_; self.nama = nama; self.harga = harga
    def to_dict(self): return {"id":self.id,"nama":self.nama,"harga":self.harga}
    @classmethod
    def from_dict(cls,d): return cls(d["id"], d["nama"], d["harga"])

class UnionsApp:
    def __init__(self):
        self.paket: List[Paket] = []
        self.bookings: List[Booking] = []
        self.umkm: List[UMKMItem] = []
        self.load()

    def seed_defaults(self):
        # contoh paket & UMKM
        self.paket = [
            Paket("P01","Camping Basic",150000.0,"Camping + spot foto + fasilitas toilet",50),
            Paket("P02","Pine Picnic",80000.0,"Area piknik, meja & kebun kecil",100),
            Paket("P03","Treehouse Stay",350000.0,"Menginap di rumah pohon (1 malam)",10),
        ]
        self.umkm = [
            UMKMItem("U1","Bakso Kayu",25000.0),
            UMKMItem("U2","Kopi Tapango",15000.0),
            UMKMItem("U3","Souvenir Pinus",50000.0),
        ]

    def save(self):
        payload = {
            "paket":[p.to_dict() for p in self.paket],
            "bookings":[b.to_dict() for b in self.bookings],
            "umkm":[u.to_dict() for u in self.umkm]
        }
        with open(DATA_FILE,"w",encoding="utf-8") as f:
            json.dump(payload,f,ensure_ascii=False,indent=2)

    def load(self):
        if not os.path.exists(DATA_FILE):
            self.seed_defaults()
            self.save()
            return
        with open(DATA_FILE,"r",encoding="utf-8") as f:
            obj = json.load(f)
        self.paket = [Paket.from_dict(d) for d in obj.get("paket",[])]
        self.bookings = [Booking.from_dict(d) for d in obj.get("bookings",[])]
        self.umkm = [UMKMItem.from_dict(d) for d in obj.get("umkm",[])]

    def list_paket(self):
        print("\n-- Daftar Paket UNIONS --")
        for p in self.paket:
            print(f"{p.kode} | {p.nama} | Rp{p.harga:,.0f} | Kapasitas: {p.kapasitas}")
            print(f"    {p.deskripsi}")

    def paket_detail(self, kode):
        for p in self.paket:
            if p.kode==kode:
                print(f"\nDetail Paket {p.kode} - {p.nama}")
                print("Harga:",p.harga)
                print("Deskripsi:",p.deskripsi)
                print("Kapasitas:",p.kapasitas)
                return p
        print("Paket tidak ditemukan.")
        return None

    def create_booking(self):
        self.list_paket()
        kode = input("Pilih kode paket: ").strip()
        p = self.paket_detail(kode)
        if not p: return
        tanggal = input("Tanggal kunjungan (YYYY-MM-DD): ").strip()
        try:
            jml = int(input("Jumlah orang: "))
        except:
            print("Jumlah harus integer.")
            return
        if jml > p.kapasitas:
            print("Melebihi kapasitas paket.")
            return
        nama = input("Nama pemesan: ").strip()
        contact = input("Kontak (WA/Phone): ").strip()
        total = p.harga * jml
        id_ = f"B{len(self.bookings)+1:04d}"
        b = Booking(id_, p.kode, tanggal, jml, nama, contact, total, paid=False)
        self.bookings.append(b)
        self.save()
        print(f"Booking dibuat. ID: {b.id} | Total: Rp{b.total:,.0f} | Status: UNPAID")

    def list_bookings(self):
        if not self.bookings:
            print("Belum ada booking.")
            return
        print("\n-- Booking Terdaftar --")
        for b in self.bookings:
            status = "PAID" if b.paid else "UNPAID"
            print(f"{b.id} | {b.nama_pemesan} | Paket {b.paket_kode} | {b.tanggal} | {b.jumlah_orang} org | Rp{b.total:,.0f} | {status}")

    def pay_booking(self):
        self.list_bookings()
        id_ = input("Masukkan ID booking untuk bayar: ").strip()
        for b in self.bookings:
            if b.id==id_:
                if b.paid:
                    print("Sudah LUNAS.")
                    return
                # simulasi pembayaran
                print(f"Total yang harus dibayar Rp{b.total:,.0f}. (Simulasi pembayaran)")
                confirm = input("Konfirmasi bayar? (y/n): ").strip().lower()
                if confirm=="y":
                    b.paid = True
                    self.save()
                    print("Pembayaran berhasil. Status: PAID")
                return
        print("Booking ID tidak ditemukan.")

    def dashboard(self):
        total_bookings = len(self.bookings)
        paid = sum(1 for b in self.bookings if b.paid)
        unpaid = total_bookings - paid
        revenue = sum(b.total for b in self.bookings if b.paid)
        print("\n-- DASHBOARD UNIONS (RINGKAS) --")
        print(f"Total booking : {total_bookings}")
        print(f"Paid / Unpaid : {paid} / {unpaid}")
        print(f"Pendapatan    : Rp{revenue:,.0f}")

    def list_umkm(self):
        print("\n-- UMKM / Lapak --")
        for u in self.umkm:
            print(f"{u.id} | {u.nama} | Rp{u.harga:,.0f}")

    def preorder_umkm(self):
        self.list_umkm()
        id_ = input("Pilih ID item untuk pre-order: ").strip()
        for u in self.umkm:
            if u.id==id_:
                qty = int(input("Jumlah: "))
                nama = input("Nama pemesan: ")
                total = u.harga * qty
                print(f"Pre-order tercatat: {u.nama} x{qty} | Total Rp{total:,.0f}")
                # di prototype hanya tampilkan; implementasi lanjut bisa simpan
                return
        print("Produk UMKM tidak ditemukan.")

    def run_cli(self):
        while True:
            print("\n===== UNIONS CLI =====")
            print("1. Lihat Paket")
            print("2. Buat Booking")
            print("3. List Booking")
            print("4. Bayar Booking")
            print("5. UMKM / Pre-order")
            print("6. Dashboard")
            print("7. Keluar")
            pilih = input("Pilih (1-7): ").strip()
            if pilih=="1": self.list_paket()
            elif pilih=="2": self.create_booking()
            elif pilih=="3": self.list_bookings()
            elif pilih=="4": self.pay_booking()
            elif pilih=="5":
                print("1. Lihat UMKM\n2. Pre-order")
                s = input("Pilih: ").strip()
                if s=="1": self.list_umkm()
                else: self.preorder_umkm()
            elif pilih=="6": self.dashboard()
            elif pilih=="7":
                print("Selesai. Data tersimpan di", DATA_FILE)
                break
            else:
                print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    app = UnionsApp()
    app.run_cli()