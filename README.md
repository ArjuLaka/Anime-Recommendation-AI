# Anime-Recommendation-AI
Anime-Recommendation-AI merupakan suatu project machine learning yang dibuat untuk membuat sistem rekomendasi dan memprediksi ketertarikan pengguna terhadap Anime yang relevan saat ini. 

## Dataset
Dataset ini berisi mengenai data Anime-Anime relevan yang dikumpulkan melalui survey terhadap aktivitas kalangan penonton anime terkait apa anime yang mereka tonton terakhir kali. 

Dataset ini mencakup sebanyak 40 judul anime yang tersurvey oleh puluhan penonton anime (tanpa menyangkut demografi), data ini dikumpulkan di antara 29 Mei 2025 hingga 18 Juni 2025.

> Variabel dari data diatas sebagai berikut:
> - id : (ID)
> - ttl : (Title)
> - yr : (Year Realeased)
> - rt : (Rating)
> - ec : (Episode Count)
> - gnr : (Genres)
> - dg : (Demographic)
> - std : (Studio)

## Cara Penggunaan
1. Install Python
   > a. Instalasi di Windows
     - Download [Windows Python Installer](https://www.python.org/downloads/windows) versi stable atau newest
     - Jalankan Python Installernya
     - Buatlah environment variable untuk eksekusi file binary-nya
     - Buka CMD/Command Prompt dan ketik
     - ```
       py --version
       ```
   > b. Instalasi di MacOs
     - Download [MacOs Python Installer](https://www.python.org/downloads/macos) versi stable atau newest
     - Jalankan Python Installernya
     - Buka terminal dan ketik
     - ```
       python --version
       ```
   > c. Instalasi di Linux (Ubuntu/Debian)
     - Buka terminal dan ketik
     - ```
       sudo apt install python3 python-venv
       ```
2. Install dependencies
   ```
   pip install -r requirements.txt
   ```
