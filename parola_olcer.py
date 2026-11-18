"""
YMS 301 - 2. Hafta: Parola Gücü Ölçer v0.2 (Karar Motoru)
Açıklama: Bir ya da birden fazla parolayı analiz eder; büyük/küçük harf,
rakam ve özel karakter sayılarını comprehension ile hesaplar ve puan
sistemiyle "zayıf / orta / güçlü" kararı verir.

Kullanım:
    python parola_olcer.py                  -> parolayı klavyeden sorar
    python parola_olcer.py Abc123!x         -> tek parola
    python parola_olcer.py abc Abc123!x     -> birden fazla parola
"""

import sys

ESIK_UZUNLUK = 8          # sabit: PEP 8'e göre TUM_BUYUK_HARF
CIZGI = "=" * 34


def parola_istatistikleri(parola: str) -> dict:
    """Parolanın detaylı istatistiklerini comprehension ile hesaplar."""
    return {
        "uzunluk": len(parola),
        "buyuk_harf": len([k for k in parola if k.isupper()]),
        "kucuk_harf": len([k for k in parola if k.islower()]),
        "rakam": len([k for k in parola if k.isdigit()]),
        "ozel_karakter": len([k for k in parola if not k.isalnum()]),
        "bosluk_var_mi": " " in parola,
    }


def parola_puani(istatistik: dict) -> int:
    """Dört kriterden kaç tanesinin sağlandığını sayar; boşluk puan düşürür."""
    puan = 0
    if istatistik["uzunluk"] >= ESIK_UZUNLUK:
        puan += 1
    if istatistik["buyuk_harf"] > 0 and istatistik["kucuk_harf"] > 0:
        puan += 1
    if istatistik["rakam"] > 0:
        puan += 1
    if istatistik["ozel_karakter"] > 0:
        puan += 1
    if istatistik["bosluk_var_mi"]:
        puan = max(puan - 1, 0)       # puan negatif olmasın
    return puan


def parola_gucunu_degerlendir(istatistik: dict) -> str:
    """Puana göre zayıf / orta / güçlü kararı verir."""
    puan = parola_puani(istatistik)
    if puan <= 1:
        return "zayıf"
    elif puan <= 3:
        return "orta"
    else:
        return "güçlü"


def eksik_kriterler(istatistik: dict) -> list:
    """Sağlanmayan kriterlerin adlarını liste olarak döndürür."""
    kriterler = {
        f"en az {ESIK_UZUNLUK} karakter": istatistik["uzunluk"] >= ESIK_UZUNLUK,
        "büyük ve küçük harf": istatistik["buyuk_harf"] > 0 and istatistik["kucuk_harf"] > 0,
        "rakam": istatistik["rakam"] > 0,
        "özel karakter": istatistik["ozel_karakter"] > 0,
        "boşluk içermemeli": not istatistik["bosluk_var_mi"],
    }
    return [ad for ad, saglandi_mi in kriterler.items() if not saglandi_mi]


def maskele(parola: str) -> str:
    """İlk ve son karakteri gösterir, aradakileri * ile gizler (slicing)."""
    if len(parola) <= 2:
        return "*" * len(parola)
    return parola[0] + "*" * len(parola[1:-1]) + parola[-1]


def rapor_yazdir(parola: str) -> None:
    """Tek bir parola için ayrıntılı rapor yazdırır."""
    istatistik = parola_istatistikleri(parola)
    karar = parola_gucunu_degerlendir(istatistik)
    eksikler = eksik_kriterler(istatistik)

    print(CIZGI)
    print(f"PAROLA GÜÇ RAPORU: {maskele(parola)}")
    print(CIZGI)
    for anahtar, deger in istatistik.items():
        print(f"{anahtar:<15}: {deger}")
    print(f"{'PUAN':<15}: {parola_puani(istatistik)}/4")
    print(f"{'KARAR':<15}: {karar.upper()}")
    # truthy/falsy: boş liste falsy
    print("Eksikler       : " + (", ".join(eksikler) if eksikler else "yok"))


def parola_al() -> str:
    """Klavyeden parola alır; boş girişte ValueError fırlatır."""
    parola = input("Bir deneme parolası girin: ")
    if not parola:
        raise ValueError("Parola boş olamaz")
    return parola


def main() -> None:
    """Programın giriş noktası."""
    parolalar = sys.argv[1:]

    if not parolalar:                 # argüman yoksa klavyeden sor
        try:
            parolalar = [parola_al()]
        except ValueError as e:
            print(f"Hata: {e}")
            return
        except (EOFError, KeyboardInterrupt):
            print("\nGiriş iptal edildi.")
            return

    for parola in parolalar:
        rapor_yazdir(parola)

    if len(parolalar) > 1:
        # comprehension ile tüm kararları tek satırda topla
        kararlar = [parola_gucunu_degerlendir(parola_istatistikleri(p)) for p in parolalar]
        print(CIZGI)
        print("ÖZET")
        for i, (parola, karar) in enumerate(zip(parolalar, kararlar), start=1):
            print(f"{i}. {maskele(parola):<12} -> {karar}")

        # for...else: ilk güçlü parolayı ara, bulamazsan else çalışır
        for parola, karar in zip(parolalar, kararlar):
            if karar == "güçlü":
                print(f"İlk güçlü parola: {maskele(parola)}")
                break
        else:
            print("Listede hiç güçlü parola yok!")


if __name__ == "__main__":
    main()
