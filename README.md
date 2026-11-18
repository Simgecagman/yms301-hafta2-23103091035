# YMS 301 - 2. Hafta: Kontrol Akışı + Comprehension

Bu repoda 2. haftanın canlı kodlama defteri ([`canli_kodlama_hafta2.ipynb`](canli_kodlama_hafta2.ipynb))
ve 7 Lab Alıştırması'nın çözümleri yer alıyor. Bu hafta truthy/falsy değerleri, ternary ifadeyi,
`is` ile `==` farkını (küçük tam sayı önbellekleme), `for`/`range`/`enumerate`/`zip` döngülerini,
`for...else` yapısını, liste/sözlük comprehension'ı ve `try/except/finally` ile hata yönetimini öğrendim.
Mini proje olarak Parola Gücü Ölçer v0.2'yi yazdım: parolanın büyük/küçük harf, rakam ve özel karakter
sayılarını comprehension ile hesaplayıp puan sistemiyle "zayıf/orta/güçlü" kararı veren iki fonksiyon.

## Parola Gücü Ölçer v0.2 (komut satırı aracı)

[`parola_olcer.py`](parola_olcer.py), haftanın mini projesini defterden bağımsız çalışan bir programa
dönüştürür. Yalnızca 1. ve 2. haftada işlenen konular kullanılmıştır: fonksiyonlar, tip ipuçları,
comprehension, truthy/falsy, `try/except`, `for...else`, `enumerate` ve `zip`.

```bash
python parola_olcer.py                  # parolayı klavyeden sorar
python parola_olcer.py Abc123!x         # tek parola
python parola_olcer.py abc Abc123!x     # birden fazla parola + özet
```

Puanlama (her kriter 1 puan): en az 8 karakter, büyük ve küçük harf, rakam, özel karakter.
Parolada boşluk varsa 1 puan düşer. Karar: 0–1 zayıf, 2–3 orta, 4 güçlü.

Örnek çıktı:

```
==================================
PAROLA GÜÇ RAPORU: A******x
==================================
uzunluk        : 8
buyuk_harf     : 1
kucuk_harf     : 3
rakam          : 3
ozel_karakter  : 1
bosluk_var_mi  : False
PUAN           : 4/4
KARAR          : GÜÇLÜ
Eksikler       : yok
```

## Lab Alıştırmaları

| Görev | Konu |
|---|---|
| 1 | `bos_mu()` – `not deger` ile falsy kontrolü |
| 2 | Boşluk kriteri: boşluk varsa puan düşer (negatif olmaz) |
| 3 | Virgülle girilen parolaları tek liste comprehension ile değerlendirme |
| 4 | `for...else` ile ilk güçlü parolayı arama |
| 5 | `parola_tekrar_sayisi()` – dict comprehension ile |
| 6 | Hata ayıklama: eksik `:` → `SyntaxError` |
| 7 | Hata ayıklama: truthy/falsy sessiz mantık hatası (`>= 8` kontrolü eksik) |

## Çalıştırma

Defteri Jupyter Notebook ya da VS Code ile açıp hücreleri sırayla çalıştırın.
