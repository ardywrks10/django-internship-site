from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest, HttpResponse
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from .models import BlogPost

class AboutView(LoginRequiredMixin, TemplateView):
    template_name = "about.html"

def index(request: HttpRequest) -> HttpResponse:
    blog_posts_qs = BlogPost.objects.all()
    paginator = Paginator(blog_posts_qs, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,      
        "blog_posts": page_obj,    
    }
    return render(request, "index.html", context)

def blog_detail(request: HttpRequest, slug: str) -> HttpResponse:
    post = get_object_or_404(BlogPost, slug=slug)
    return render(request, "blog_detail.html", {"post": post})

# BLOG_POSTS = [
#     {
#         "slug": "penerjunan-magang",
#         "image": "theme/assets/img/blog/1.jpeg",
#         "author_name": "Kusuma",
#         "author_image": "theme/assets/img/blog/b6.jpg",
#         "tag": "Ardy",
#         "title": "Penerjunan Magang di PT. Dimata Sora Jayate",
#         "description": (
#             "Enam mahasiswa magang dari Program Studi Ilmu Komputer di "
#             "PT. Dimata Sora Jayate dibagi ke dalam dua divisi, yakni Machine Learning dan DevOps."
#         ),
#         "time": "Agustus 04, 2025",
#         "content": (
#             "Penerjunan mahasiswa magang Program Studi Ilmu Komputer dilaksanakan "
#             "serentak pada 4 Agustus 2025. Enam mahasiswa yang ditempatkan di PT. "
#             "Dimata Sora Jayate terbagi ke dalam dua divisi, yaitu <b>Machine Learning (ML)</b> "
#             "dan <b>DevOps</b>. Empat mahasiswa tergabung di divisi ML, sementara dua lainnya "
#             "di divisi DevOps. Pada hari pertama magang, mentor memberikan "
#             "arahan yang terstruktur serta memastikan setiap mahasiswa mendapatkan proyek "
#             "yang sejalan dengan konsentrasi masing-masing.\n\n"

#             "Perusahaan menyediakan fasilitas belajar yang memadai dan lingkungan yang "
#             "mendukung pengembangan kompetensi mahasiswa melalui keterlibatan langsung "
#             "dalam proyek industri. Mentor secara berkala memantau perkembangan proyek "
#             "yang dikerjakan mahasiswa, sekaligus memberikan arahan apabila terdapat "
#             "kendala dalam proses pengerjaan."
#         ),
#     },
#     {
#         "slug": "hut-dimata",
#         "image": "theme/assets/img/blog/2.jpeg",
#         "author_name": "Kusuma",
#         "author_image": "theme/assets/img/blog/b6.jpg",
#         "tag": "Ardy",
#         "title": "HUT ke-23 PT. Dimata Sora Jayate",
#         "description": (
#             "Dalam rangka HUT ke-23, PT Dimata Sora Jayate mengangkat tema"
#             " \"Dimata Bertumbuh & Kuat dalam Semangat Tri Hita Karana\"" 
#         ),
#         "time": "Agustus 30, 2025",
#         "content": (
#             "Pada Sabtu, 30 Agustus 2025, PT. Dimata Sora Jayate merayakan hari jadinya yang ke-23 "
#             "dengan penuh rasa syukur ke hadapan Tuhan Yang Maha Esa. Mengangkat tema "
#             "\"Dimata Bertumbuh & Kuat dalam Semangat Tri Hita Karana\", perayaan tahun ini tidak hanya "
#             "menjadi momen ulang tahun perusahaan, tetapi juga refleksi bagaimana Dimata terus bertumbuh "
#             "selaras dengan harmoni antara manusia, alam, dan Sang Pencipta. Rangkaian acara dimulai pada "
#             "pukul 08.30 WITA, di mana seluruh pegawai, staf, dan mahasiswa magang berkumpul di Workshop (WS) "
#             "sebelum berangkat bersama menuju Pura Sidakarya untuk melakukan persembahyangan dengan busana adat "
#             "Bali lengkap.\n\n"
#             "Setelah persembahyangan selesai, rangkaian acara dilanjutkan dengan coffee break di Dimata Workshop "
#             "sekitar pukul 09.50–10.15 WITA, yang sekaligus menjadi momen santai dan sesi penyampaian arah serta "
#             "rencana pertumbuhan Dimata ke depannya. Dalam kegiatan ini, seluruh peserta dihimbau untuk hadir tepat "
#             "waktu, menggunakan busana sesuai agenda, menjaga kesakralan area Pura (terutama dalam mengambil foto), "
#             "serta membawa tumbler pribadi guna mengurangi penggunaan plastik sekali pakai. Untuk memastikan kebutuhan "
#             "konsumsi yang disediakan, setiap tim juga diminta melakukan konfirmasi kehadiran atau menyampaikan apabila "
#             "berhalangan hadir melalui WhatsApp. Melalui rangkaian sederhana namun penuh makna ini, Dimata berharap "
#             "semangat Tri Hita Karana benar-benar tercermin dalam cara perusahaan bertumbuh dan bekerja setiap hari."
#         ),
#     },
#     {
#         "slug": "optical-character-recognition",
#         "image": "theme/assets/img/blog/3.jpg",
#         "author_name": "Kusuma",
#         "author_image": "theme/assets/img/blog/b6.jpg",
#         "tag": "Ardy",
#         "title": "Mengenal Optical Character Recognition (OCR)",
#         "description": (
#             "Alur kerja Optical Character Recognition (OCR) mencakup beberapa tahapan seperti "
#             "pre-processing gambar, localization, segmentation, hingga tahap recognition."   
#         ),
#         "time": "March 25, 2023",
#         "content": (
#             "Pada awal magang, saya terlibat langsung dalam proyek yang memanfaatkan OCR "
#             "(Optical Character Recognition) untuk mengotomatisasi pembacaan dokumen, sehingga penting "
#             "memahami OCR secara fundamental. Secara teknis, alur kerja OCR dapat dijelaskan melalui "
#             "empat langkah yang tersusun secara sistematis. Langkah pertama adalah <b>image acquisition & pre-processing</b> "
#             ", di mana sistem menerima citra atau gambar teks dari kamera, kemudian "
#             "masuk ke proses cleaning dengan beberapa metode seperti binarisasi agar teks tampak jelas "
#             "hitam-putih, mengurangi noise, mengubahnya ke grayscale, atau melakukan deskew (meluruskan "
#             "kemiringan). Langkah kedua yaitu <b>localization</b>, ketika sistem menelusuri bagian-bagian pada "
#             "gambar yang mengandung teks sehingga pada akhirnya diperoleh blok-blok teks lengkap dengan "
#             "koordinat (bounding box). Ketiga yaitu <b>segmentation</b>, di mana hasil proses localization "
#             "dipisahkan terlebih dahulu menjadi baris teks, kemudian dipecah lagi menjadi kata, dan akhirnya "
#             "menjadi karakter tunggal dengan memanfaatkan jarak antar piksel. Setelah setiap karakter terisolasi, "
#             "proses berlanjut ke tahap keempat, yaitu <b>recognition</b>. Pada tahap ini, citra karakter dikonversi "
#             "menjadi huruf atau angka melalui pendekatan klasik seperti template matching menggunakan "
#             "algoritma klasifikasi seperti SVM, K-NN, atau MLP, maupun melalui pendekatan yang lebih modern "
#             "berbasis deep learning, misalnya CNN dengan arsitektur tertentu.\n\n"

#             "Secara umum untuk proses implementasi, terdapat tiga kelompok utama toolset OCR. Pertama adalah "
#             "proprietary yang berarti software berlisensi dan berbayar seperti ABBYY FineReader atau Adobe Acrobat. "
#             "Kedua adalah toolset open source seperti <b>Tesseract</b>, <b>EasyOCR</b>, dan <b>PaddleOCR</b> yang kode sumbernya dapat "
#             "diakses secara gratis, sehingga dapat dikustomisasi, diintegrasikan melalui command line atau API, ataupun diretrain sesuai kebutuhan. "
#             "Ketiga adalah online services yaitu layanan OCR berbasis web seperti Free-Online OCR atau OnlineOCR, "
#             "di mana pengguna cukup mengunggah dokumen tanpa instalasi tambahan.\n\n"

#             "Untuk proyek magang yang akan dikerjakan, toolset OCR open source akan digunakan karena lebih fleksibel "
#             "dan selaras dengan kebutuhan pengembangan di lingkungan R&D. Melalui toolset tersebut dapat dengan "
#             "mudah mengintegrasikan OCR secara langsung ke dalam pipeline aplikasi perusahaan.\n\n"

#             "<b style='font-size: 20px;'>Referensi</b>"
#             "<ul>"
#             "<li><a style='color: black; text-decoration: underline;' href='https://journalskuwait.org/kjs/index.php/KJS/article/view/9589' target='_blank' rel='noopener noreferrer'>https://journalskuwait.org/kjs/index.php/KJS/article/view/9589</a></li>"
#             "<li><a style='color: black; text-decoration: underline;' href='https://www.mdpi.com/2079-9292/12/3/754' target='_blank' rel='noopener noreferrer'>https://www.mdpi.com/2079-9292/12/3/754</a></li>"
#             "<li><a style='color: black; text-decoration: underline;' href='https://medium.com/@eldokarim.rk/fundamentals-of-optical-character-recognition-ocr-8b89dd5f8714' target='_blank' rel='noopener noreferrer'>https://medium.com/@eldokarim.rk/fundamentals-of-optical-character-recognition-ocr-8b89dd5f8714</a></li>"
#             "</ul>"
#         ),
#     },
#     {
#         "slug": "dbscan-kmeans-clustering",
#         "image": "theme/assets/img/blog/4.jpg",
#         "author_name": "Kusuma",
#         "author_image": "theme/assets/img/blog/b6.jpg",
#         "tag": "Ardy",
#         "title": "DBSCAN vs K-Means Clustering: Mana yang Lebih Unggul?",
#         "description": (
#             "Algoritma clustering seperti K-Means dan DBSCAN banyak diterapkan pada sistem rekomendasi "
#             "maupun analisis data spesifik seperti ekstraksi tabel."
#         ),
#         "time": "March 30, 2023",
#         "content": (
#             "Dalam konteks pengolahan data, termasuk ketika ingin mengelompokkan pola tertentu dari hasil "
#             "ekstraksi OCR, algoritma clustering berperan penting untuk membagi titik-titik data ke dalam kelompok "
#             "tertentu secara otomatis. Dua algoritma yang sering digunakan adalah <b>K-Means</b> dan <b>DBSCAN</b>, yang "
#             "secara teknis berbeda dari cara mendefinisikan cluster. K-Means merupakan algoritma "
#             "centroid-based yang mengasumsikan jumlah cluster (𝑘) sudah ditentukan di awal, kemudian secara iteratif "
#             "menginisialisasi centroid (pusat cluster), meng-assign tiap titik ke centroid terdekat (biasanya menggunakan jarak "
#             "Euclidean), dan memperbarui centroid sebagai rata-rata titik dalam cluster hingga konvergen. "
#             "Sebaliknya, DBSCAN adalah algoritma density-based yang tidak membutuhkan jumlah cluster di awal, "
#             "melainkan menggunakan dua parameter utama yaitu ε (radius tetangga) dan MinPts (jumlah tetangga minimum). Sebuah "
#             "titik menjadi core point (titik tengah cluster) apabila di dalam radius tersebut terdapat setidaknya MinPts titik lain, kemudian cluster "
#             "(kelompok) dibentuk dengan memperluas titik-titik yang density-reachable, sementara titik yang berada di "
#             "luar cluster dianggap sebagai noise.\n\n"
#             "Berdasarkan cara kerja masing-masing algoritma, K-Means unggul ketika cluster "
#             "cenderung berbentuk bulat atau terpisah dengan cukup jelas. Selain itu, fungsi objektifnya yaitu meminimalkan "
#             "jarak ke centroid relatif mudah dipahami dan diimplementasikan. Namun kekurangannya, K-Means membutuhkan "
#             "metode tambahan seperti <b>Elbow Method</b> untuk menentukan jumlah cluster yang optimal "
#             "Di sisi lain, DBSCAN memiliki kelebihan utama yaitu tidak memerlukan inisialisasi jumlah cluster di awal proses "
#             "dan mampu menemukan cluster dengan bentuk arbitrer, misalnya melengkung atau tidak "
#             "beraturan. Kekurangannya, DBSCAN cukup sensitif terhadap pemilihan epsilon dan MinPts, serta "
#             "memerlukan waktu lebih lama ketika berhadapan dengan data berdimensi tinggi.\n\n"
#             "Kedua algoritma banyak dimanfaatkan dalam sistem rekomendasi, misalnya untuk mengelompokkan "
#             "customer maupun item berdasarkan kemiripan perilaku dan preferensi. Selain itu, keduanya juga "
#             "dapat dipadukan dengan OCR untuk tugas spesifik seperti ekstraksi tabel pada sebuah dokumen.\n\n"
#             "<b style='font-size: 20px;'>Referensi</b>"
#             "<ul>"
#             "<li><a style='color: black; text-decoration: underline;' href='https://e-journal.unair.ac.id/JISEBI/article/view/47770' target='_blank' rel='noopener noreferrer'>https://e-journal.unair.ac.id/JISEBI/article/view/47770</a></li>"
#             "<li><a style='color: black; text-decoration: underline;' href='https://www.neliti.com/publications/436923/analisis-pengelompokan-data-nilai-siswa-untuk-menentukan-siswa-berprestasi-mengg' target='_blank' rel='noopener noreferrer'>https://www.neliti.com/publications/436923/analisis-pengelompokan-data-nilai-siswa-untuk-menentukan-siswa-berprestasi-mengg</a></li>"
#             "</ul>"
#         ),
#     },
#     {
#         "slug": "kunjungan-dospem-1",
#         "image": "theme/assets/img/blog/5.jpg",
#         "author_name": "Tim Norton",
#         "author_image": "theme/assets/img/blog/b6.jpg",
#         "tag": "Ardy",
#         "title": "5 ways to improve user retention for your startup",
#         "description": (
#             "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
#             "Lorem Ipsum has been the industry's standard."
#         ),
#         "time": "March 30, 2023",
#         "content": (
#             "Ini bisa kamu kaitkan ke fitur-fitur yang kamu buat di project magang "
#             "yang berhubungan dengan UX, notifikasi, dashboard, dsb."
#         ),
#     },
# ]
# def index(request: HttpRequest) -> HttpResponse:
#     blog_posts  = BLOG_POSTS
#     paginator   = Paginator(blog_posts, 3)
#     page_number = request.GET.get("page")
#     page_obj    = paginator.get_page(page_number)
#     context     = {
#         "page_obj": page_obj,
#         "blog_posts": page_obj,
#     }
#     return render(request, "index.html", context)

# def blog_detail(request: HttpRequest, slug: str) -> HttpResponse:
#     blog_post = next((post for post in BLOG_POSTS if post["slug"] == slug), None)
#     if blog_post is None:
#         from django.http import Http404
#         raise Http404("Blog post not found")

#     return render(request, "blog_detail.html", {"post": blog_post})

