# Video Downloader

Bu proje, Python kullanarak herhangi bir video platformundan video indirmenize olanak tanır. **yt-dlp** kütüphanesini temel alır ve kullanıcı dostu bir şekilde video indirmenizi sağlar.

---

## Özellikler

- Video URL'si girerek kolayca video indirme
- Otomatik olarak en iyi video kalitesini seçme
- İndirilen videoları belirtilen bir klasöre kaydetme
- Desteklenen platformlar: YouTube, Vimeo, Dailymotion...

---

## Gereksinimler

Bu projeyi kullanmadan önce aşağıdaki gereksinimlerin yüklü olduğundan emin olun:

1. **Python 3.7+**
2. `yt-dlp` kütüphanesi

---

## Kurulum

1. Bu projeyi klonlayın:
   ```bash
   git clone https://github.com/canoka/video-downloader.git
   cd video-downloader
   ```

2. Gerekli kütüphaneyi yükleyin:
   ```bash
   pip install yt-dlp
   ```

---

## Kullanım

1. Uygulamayı çalıştırın:
   ```bash
   python video_downloader.py
   ```

2. Sizden bir video bağlantısı girmeniz istenecektir. Örneğin:
   ```
   Lütfen indirilecek video URL'sini girin: https://www.youtube.com/watch?v=dQw4w9WgXcQ
   ```

3. Video indirme işlemi başlar ve tamamlandığında "İndirme tamamlandı!" mesajı görürsünüz.

4. İndirilen videolar varsayılan olarak `İndirilen Videolar` klasörüne kaydedilir.

---

## Özelleştirme

Varsayılan olarak, videolar `İndirilen Videolar` klasörüne indirilir. Bu klasörü değiştirmek için `video_downloader.py` dosyasındaki `output_path` değişkenini düzenleyebilirsiniz:

```python
output_path = "C:\KendiKlasorunuz"
```

---

## Desteklenen Platformlar

**yt-dlp**, aşağıdaki platformlar dahil olmak üzere birçok popüler video sitesini destekler:
- YouTube
- Vimeo
- Dailymotion
- Facebook
- Tam liste için: https://github.com/yt-dlp/yt-dlp#supported-sites

---


