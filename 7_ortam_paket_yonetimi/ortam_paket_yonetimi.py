"""
Environment (Ortam)
    - Bir projenin çalışması için gerekli olan python sürümü, kütüphaneler, paketler gibi bileşenlerin bulunduğu çalışma alanıdır.
    - bir proje için gerekli python araçlarının bulunduğu izloe bir çalışma alanıdır

Neden kullanılır:
    - farklı projelerde farklı paket sürümleri
    - Proje A:
        - numpy == 1.20
    - Proje B:
        - numpy == 1.26

Virtual Environment (Sanal ortam)
    - kurulum: python -m venv venv
    - aktif hale getirmek: 
        - windows: .\venv\Scripts\activate
        - mac, linux: source venv/bin/activate

Paket Yöneticisi (pip)
    - kütüphane = paket
        - numpy: sayısal işlemler
        - pandas: veri analizi
        - matploblit: görselleştirme
    - python paketleri yönetmek için kullanılan araç = pip
        - paket kurabilir
        - silebilir
        - listeleyebilir

Paket kurma:
    - numpy: pip install numpy
    - pandas, matplotlib: pip install pandas matplotlib


requirements.txt
    - bir projenin ihtiyaç duyduğu tüm paketlerin listelendiği dosya
    - bu dosya sayesinde başka bir projeyi kolayca çalıştırabiliriz.
    - pip freeze > requirements.txt

    - Kurulum:
        - pip install -r .\requirements.txt
"""