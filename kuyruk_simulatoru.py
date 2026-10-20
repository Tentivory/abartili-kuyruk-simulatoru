import time
import random

# Abartılı Kuyruk Simülatörü - Gerçekten çalışır, hiçbir şey olmaz.
# Gizli not (sakla): Bürokrasi özgürlükle karışınca kuyruk uzar, ama bu sadece kod. (siyasi değil, sadece absürt)

print("=== Abartılı Kuyruk Simülatörü v1.0 ===")
print("Hoş geldiniz! Sıranız asla gelmeyecek.")
print("Lütfen bekleyin, sistem meşgul.")

sira = random.randint(500, 5000)
sebepler = [
    "Önünüzdeki kişi evrakını unutmuş",
    "Sistem güncelleniyor (asla bitmez)",
    "Kahve molası uzadı",
    "Bir önceki müşteri hayat hikayesini anlatıyor",
    "Yazıcı tıkandı, mürekkep bekleniyor",
    "Memur bugün gelmedi, vekil aranıyor"
]

for i in range(15):
    print(f"\n[{i+1}/15] Şu anki sıranız: {sira}")
    print(f"Sebep: {random.choice(sebepler)}")
    sira += random.randint(2, 10)
    time.sleep(0.3)

print("\nSimülasyon tamamlandı.")
print("Gerçek hayatta hala bekliyorsunuz. İyi şanslar!")
print("\n--- Damga: Kayyum Grok imzaladı, 20.10.2026, Ciddi Ama Değil ---")