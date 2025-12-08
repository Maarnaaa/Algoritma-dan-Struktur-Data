book = {
    "judul": "Pemrograman Python Dasar",
    "penulis": "Andi Saputra",
    "tahun": 2023
}

print(book["judul"])
print(book["penulis"])
print(book["tahun"])

#HASIL MODIFIKASI
import json
from datetime import datetime
from typing import List, Dict, Optional

class Book:
    def __init__(self, judul: str, penulis: str, tahun: int, isbn: Optional[str]=None):
        if not judul or not penulis:
            raise ValueError("Judul dan penulis wajib diisi.")
        if not isinstance(tahun, int) or tahun < 0:
            raise ValueError("Tahun harus integer positif.")
        self.judul = judul.strip()
        self.penulis = penulis.strip()
        self.tahun = tahun
        self.isbn = isbn or ""
        self.reviews: List[Dict] = []   # tiap review: {"user": str, "rating": int, "comment": str, "date": str}
        self.borrowed_by: Optional[str] = None
        self.borrow_date: Optional[str] = None

    def to_dict(self) -> Dict:
        return {
            "judul": self.judul,
            "penulis": self.penulis,
            "tahun": self.tahun,
            "isbn": self.isbn,
            "reviews": self.reviews,
            "borrowed_by": self.borrowed_by,
            "borrow_date": self.borrow_date
        }

    @classmethod
    def from_dict(cls, d: Dict):
        b = cls(d["judul"], d["penulis"], int(d["tahun"]), d.get("isbn", ""))
        b.reviews = d.get("reviews", [])
        b.borrowed_by = d.get("borrowed_by")
        b.borrow_date = d.get("borrow_date")
        return b

    def add_review(self, user: str, rating: int, comment: str = ""):
        if not (1 <= rating <= 5):
            raise ValueError("Rating harus antara 1 - 5.")
        self.reviews.append({
            "user": user,
            "rating": int(rating),
            "comment": comment.strip(),
            "date": datetime.now().isoformat(timespec="seconds")
        })

    def avg_rating(self) -> Optional[float]:
        if not self.reviews:
            return None
        return sum(r["rating"] for r in self.reviews) / len(self.reviews)

    def borrow(self, user: str):
        if self.borrowed_by:
            raise RuntimeError(f"Buku sedang dipinjam oleh {self.borrowed_by}.")
        self.borrowed_by = user
        self.borrow_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def return_book(self):
        if not self.borrowed_by:
            raise RuntimeError("Buku tidak sedang dipinjam.")
        self.borrowed_by = None
        self.borrow_date = None

    def __str__(self):
        avg = self.avg_rating()
        rating_str = f"{avg:.2f}/5" if avg is not None else "N/A"
        status = f"Borrowed by {self.borrowed_by}" if self.borrowed_by else "Available"
        return (f"\"{self.judul}\" by {self.penulis} ({self.tahun}) | ISBN: {self.isbn or '-'}\n"
                f"  Rating: {rating_str} | {status} | Reviews: {len(self.reviews)}")

class Library:
    def __init__(self):
        self.books: List[Book] = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book_by_title(self, judul: str) -> bool:
        for i, b in enumerate(self.books):
            if b.judul.lower() == judul.lower():
                del self.books[i]
                return True
        return False

    def find_by_title(self, keyword: str) -> List[Book]:
        k = keyword.lower()
        return [b for b in self.books if k in b.judul.lower()]

    def find_by_author(self, author: str) -> List[Book]:
        a = author.lower()
        return [b for b in self.books if a in b.penulis.lower()]

    def list_books(self) -> List[Book]:
        return self.books

    def recommend_top(self, n: int = 3) -> List[Book]:
        rated = [b for b in self.books if b.avg_rating() is not None]
        rated.sort(key=lambda x: x.avg_rating(), reverse=True)
        return rated[:n]

    def save_to_file(self, filepath: str):
        data = [b.to_dict() for b in self.books]
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump({"saved_at": datetime.now().isoformat(timespec="seconds"), "books": data}, f, ensure_ascii=False, indent=2)

    def load_from_file(self, filepath: str):
        with open(filepath, "r", encoding="utf-8") as f:
            obj = json.load(f)
        self.books = [Book.from_dict(d) for d in obj.get("books", [])]

    def print_table(self):

        print("="*86)
        print(f"| {'No':<3} | {'Judul':<30} | {'Penulis':<18} | {'Tahun':<5} | {'Rating':<6} | {'Status':<12} |")
        print("-"*86)
        for i, b in enumerate(self.books, start=1):
            avg = b.avg_rating()
            r = f"{avg:.2f}" if avg is not None else "-"
            status = "Borrowed" if b.borrowed_by else "Available"
            judul = (b.judul[:27] + "...") if len(b.judul) > 30 else b.judul
            penulis = (b.penulis[:15] + "...") if len(b.penulis) > 18 else b.penulis
            print(f"| {i:<3} | {judul:<30} | {penulis:<18} | {b.tahun:<5} | {r:<6} | {status:<12} |")
        print("="*86)

if __name__ == "__main__":
    lib = Library()

    lib.add_book(Book("Pemrograman Python Dasar", "Andi Saputra", 2023, isbn="978-1111111111"))
    lib.add_book(Book("Algoritma & Struktur Data", "Siti Nurhayati", 2020))
    lib.add_book(Book("Belajar Data Science", "Budi Santoso", 2022))

    lib.books[0].add_review("Rina", 5, "Sangat membantu pemula.")
    lib.books[0].add_review("Kaka", 4, "Bagus, tapi kurang contoh.")
    lib.books[1].add_review("Dedi", 5, "Penjelasan detail.")
    lib.books[2].add_review("Ika", 3, "Lumayan.")

    lib.books[2].borrow("Mahasiswa A")

    print("\n-- Daftar Buku di Perpustakaan --")
    lib.print_table()

    print("\n-- Cari dengan kata kunci 'python' --")
    for b in lib.find_by_title("python"):
        print(b)
        print()

    print("\n-- Rekomendasi Top 2 (berdasarkan rating)--")
    for b in lib.recommend_top(2):
        print(b)
        print()

    lib.save_to_file("library_data.json")
    print("Library disimpan ke file library_data.json")
