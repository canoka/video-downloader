import yt_dlp
import os

def download_video(video_url, output_folder="İndirilen Videolar"):
    # İndirilecek dosya konumu
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    ydl_opts = {
        'outtmpl': f'{output_folder}/%(title)s.%(ext)s',  # Dosya adı ve uzantısı
        'format': 'best',  # En iyi video kalitesini indir
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            print("İndirme işlemi başlıyor...")
            ydl.download([video_url])
            print("İndirme tamamlandı!")
    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    print("YouTube Video İndirme Uygulamasına Hoş Geldiniz!")
    video_url = input("Lütfen indirilecek video linkini yapıştırın: ")
    download_folder = input("İndirilecek klasörün yolunu girin (Varsayılan: İndirilen Videolar): ").strip()

    if download_folder == "":
        download_folder = "İndirilen Videolar"

    download_video(video_url, download_folder)
