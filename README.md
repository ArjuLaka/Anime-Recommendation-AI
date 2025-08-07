# Anime-Recommendation-AI
Anime-Recommendation-AI merupakan suatu project machine learning yang dibuat untuk membuat sistem rekomendasi dan memprediksi ketertarikan pengguna terhadap Anime yang relevan saat ini. 

## Dataset
Dataset ini berisi mengenai data Anime-Anime relevan yang dikumpulkan melalui survey terhadap aktivitas kalangan penonton anime terkait apa anime yang mereka tonton terakhir kali. 

Dataset ini mencakup sebanyak 40 judul anime yang tersurvey oleh puluhan penonton anime (tanpa menyangkut demografi), data ini dikumpulkan di antara 29 Mei 2025 hingga 18 Juni 2025.

> Variabel dari data diatas sebagai berikut:
> - id : (ID)
> - title : (Judul)
> - yearRealeased : (Tahun rilis)
> - rating : (Rating)
> - totalEpisode : (Jumlah episode)
> - genres : (Genre)
> - demographic : (Demografi/Target penonton)
> - studio : (Studio)

## Cara Penggunaan
1. Install Python
   > a. Instalasi di Windows
     - Download [Windows Python Installer](https://www.python.org/downloads/windows) versi stable atau newest
     - Jalankan Python Installernya
     - Buatlah environment variable untuk eksekusi file binary-nya
     - Buka CMD/Command Prompt dan ketik
     - ```
       python3 --version
       ```
       Untuk memastikan apakah python sudah terinstall
   > b. Instalasi di MacOs
     - Download [MacOs Python Installer](https://www.python.org/downloads/macos) versi stable atau newest
     - Jalankan Python Installernya
     - Buka terminal dan ketik
     - ```
       python3 --version
       ```
       Untuk memastikan apakah python sudah terinstall
   > c. Instalasi di Linux (Ubuntu/Debian)
     - Buka terminal dan ketik
     - ```
       sudo apt update && apt install build-essential python3 python-venv -y
       ```
     - Lalu ketik
     - ```
       python3 --version
       ```
       Untuk memastikan apakah python sudah terinstall
2. Install semua dependency
   ```
   pip install -r requirements.txt
   ```
3. Jalankan script
   - Dengan web interface
   ```
   streamlit run main.py
   ```
   - Tanpa web interface
   ```
   python main.py <Nama Anime> <Jumlah Rekomendasi>
   ```
   
## Kontribusi
