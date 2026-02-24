# 🛍️ Django E-Ticaret REST API

Modern, ölçeklenebilir ve güvenli bir e-ticaret backend sistemi. Django REST Framework kullanılarak geliştirilmiştir.

## 📋 İçindekiler

- [Özellikler](#-özellikler)
- [Teknolojiler](#-teknolojiler)
- [Kurulum](#-kurulum)
- [API Dokümantasyonu](#-api-dokümantasyonu)
- [Proje Yapısı](#-proje-yapısı)
- [Kullanım](#-kullanım)
- [Güvenlik](#-güvenlik)
- [Katkıda Bulunma](#-katkıda-bulunma)

## ✨ Özellikler

### 🔐 Kimlik Doğrulama & Yetkilendirme
- JWT (JSON Web Token) tabanlı kimlik doğrulama
- Access token (1 saat) ve Refresh token (7 gün) desteği
- Rol bazlı yetkilendirme (Admin/User)
- API Key authentication desteği

### 🛒 Alışveriş Özellikleri
- Ürün katalog yönetimi (CRUD işlemleri)
- Kategori bazlı ürün filtreleme
- Gelişmiş arama ve sıralama
- Ürün görselleri yönetimi
- Sepet yönetimi
- Sipariş oluşturma ve takibi
- İndirim kuponu sistemi

### 💳 Ödeme Sistemi
- İyzico entegrasyonu
- Güvenli ödeme işlemleri
- Sandbox ve production desteği

### 📝 İçerik Yönetimi
- Ürün yorumları ve değerlendirme
- Aktif/pasif yorum moderasyonu
- Kullanıcı bazlı yorum filtreleme

### 🚀 Performans & Güvenlik
- Rate limiting (istek hızı sınırlama)
- Throttling (anonim ve kimlikli kullanıcılar için)
- CORS yapılandırması
- Sayfalama (pagination) desteği
- Detaylı loglama sistemi
- Özel hata yönetimi

### 📚 Dokümantasyon
- Swagger UI entegrasyonu
- Otomatik API dokümantasyonu
- ReDoc alternatif dokümantasyon

## 🛠 Teknolojiler

### Backend Framework
- **Django 5.2.3** - Modern Python web framework
- **Django REST Framework 3.16.1** - RESTful API geliştirme
- **djangorestframework-simplejwt 5.5.1** - JWT authentication

### Veritabanı
- **SQLite3** - Development için hafif veritabanı
- PostgreSQL/MySQL desteği (production için önerilir)

### Dokümantasyon & Test
- **drf-spectacular 0.29.0** - OpenAPI 3.0 schema ve Swagger UI
- **django-filter 25.2** - Gelişmiş filtreleme

### Ödeme & Entegrasyonlar
- **iyzipay 1.0.46** - Ödeme gateway entegrasyonu

### Güvenlik & Utilities
- **djangorestframework-api-key 2.3.0** - API key yönetimi
- **django-cors-headers 4.9.0** - CORS yapılandırması
- **Pillow 12.1.1** - Görsel işleme
- **PyYAML 6.0.3** - YAML yapılandırma desteği

## 📦 Kurulum

### Ön Gereksinimler
- Python 3.10 veya üzeri
- pip (Python paket yöneticisi)
- Virtual environment (önerilir)

### 1. Projeyi Klonlayın
```bash
git clone <repository-url>
cd django-api
```

### 2. Virtual Environment Oluşturun
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Bağımlılıkları Yükleyin
```bash
pip install -r requirements.txt
```

### 4. Veritabanı Migrasyonlarını Uygulayın
```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Superuser Oluşturun
```bash
python manage.py createsuperuser
```

### 6. Static Dosyaları Toplayın
```bash
python manage.py collectstatic --noinput
```

### 7. Sunucuyu Başlatın
```bash
python manage.py runserver
```

Uygulama `http://127.0.0.1:8000/` adresinde çalışacaktır.

## 📖 API Dokümantasyonu

### Swagger UI
API dokümantasyonuna erişmek için:
```
https://batuhanyilmaz1.pythonanywhere.com/api/docs
```
```

## 📁 Proje Yapısı

```
django-api/
├── 📁 app/                      # Ana proje ayarları
│   ├── settings.py             # Django ayarları
│   ├── urls.py                 # Ana URL yapılandırması
│   ├── throttles.py            # Rate limiting ayarları
│   └── wsgi.py                 # WSGI yapılandırması
│
├── 📁 users/                    # Kullanıcı yönetimi
│   ├── models.py               # CustomUser modeli
│   ├── serializers.py          # Kullanıcı serileştiricileri
│   ├── views.py                # Kayıt, giriş, profil işlemleri
│   ├── tokens.py               # JWT token yönetimi
│   └── urls.py                 # Kullanıcı endpoint'leri
│
├── 📁 products/                 # Ürün yönetimi
│   ├── models.py               # Product ve ProductImage modelleri
│   ├── serializers.py          # Ürün serileştiricileri
│   ├── views.py                # Ürün CRUD işlemleri
│   ├── filters.py              # Ürün filtreleme
│   ├── services.py             # İş mantığı katmanı
│   └── urls.py                 # Ürün endpoint'leri
│
├── 📁 categories/               # Kategori yönetimi
│   ├── models.py               # Category modeli
│   ├── serializers.py          # Kategori serileştiricileri
│   ├── views.py                # Kategori CRUD işlemleri
│   ├── services.py             # Kategori iş mantığı
│   └── urls.py                 # Kategori endpoint'leri
│
├── 📁 cards/                    # Sepet yönetimi
│   ├── models.py               # Cart ve CartItem modelleri
│   ├── serializers.py          # Sepet serileştiricileri
│   ├── views.py                # Sepet işlemleri
│   ├── services.py             # Sepet iş mantığı
│   └── urls.py                 # Sepet endpoint'leri
│
├── 📁 orders/                   # Sipariş yönetimi
│   ├── models.py               # Order ve OrderItem modelleri
│   ├── serializers.py          # Sipariş serileştiricileri
│   ├── views.py                # Sipariş işlemleri
│   ├── services.py             # Sipariş iş mantığı
│   └── urls.py                 # Sipariş endpoint'leri
│
├── 📁 comments/                 # Yorum sistemi
│   ├── models.py               # Comment modeli
│   ├── serializers.py          # Yorum serileştiricileri
│   ├── views.py                # Yorum CRUD işlemleri
│   ├── filters.py              # Yorum filtreleme
│   └── urls.py                 # Yorum endpoint'leri
│
├── 📁 addresses/                # Adres yönetimi
│   ├── models.py               # Address modeli
│   ├── serializers.py          # Adres serileştiricileri
│   ├── views.py                # Adres CRUD işlemleri
│   ├── services.py             # Adres iş mantığı
│   └── urls.py                 # Adres endpoint'leri
│
├── 📁 coupons/                  # Kupon sistemi
│   ├── models.py               # Coupon modeli
│   ├── serializers.py          # Kupon serileştiricileri
│   ├── views.py                # Kupon işlemleri
│   ├── services.py             # Kupon validasyonu
│   └── urls.py                 # Kupon endpoint'leri
│
├── 📁 payments/                 # Ödeme sistemi
│   ├── models.py               # Payment modeli
│   ├── serializers.py          # Ödeme serileştiricileri
│   ├── views.py                # Ödeme işlemleri
│   ├── services.py             # İyzico entegrasyonu
│   └── urls.py                 # Ödeme endpoint'leri
│
├── 📁 core/                     # Ortak araçlar
│   ├── paginations.py          # Sayfalama ayarları
│   ├── permissions.py          # Özel izin sınıfları
│   ├── exceptions.py           # Özel hata yönetimi
│   └── utils.py                # Yardımcı fonksiyonlar
│
├── 📁 media/                    # Yüklenen dosyalar
│   └── product_images/         # Ürün görselleri
│
├── 📁 staticfiles/              # Static dosyalar
├── 📁 logs/                     # Log dosyaları
│   └── django.log              # Uygulama logları
│
├── db.sqlite3                  # SQLite veritabanı
├── manage.py                   # Django yönetim komutları
├── requirements.txt            # Python bağımlılıkları
└── README.md                   # Bu dosya
```

## 🔧 Kullanım

### Kimlik Doğrulama

#### Kullanıcı Kaydı
```bash
POST /api/users/register/
Content-Type: application/json

{
    "username": "kullanici_adi",
    "email": "email@example.com",
    "password": "güçlü_şifre",
    "password2": "güçlü_şifre",
    "first_name": "Ad",
    "last_name": "Soyad"
}
```

#### Giriş Yapma
```bash
POST /api/users/login/
Content-Type: application/json

{
    "username": "kullanici_adi",
    "password": "güçlü_şifre"
}

Response:
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

#### Token Yenileme
```bash
POST /api/users/token/refresh/
Content-Type: application/json

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
}
```

### Ürün İşlemleri

#### Ürün Listesi (Herkese Açık)
```bash
GET /api/products/?category=1&search=laptop&ordering=price
Authorization: Bearer <access_token>
```

#### Ürün Detayı
```bash
GET /api/products/{slug}/
```

#### Ürün Oluşturma (Admin)
```bash
POST /api/products/admin/create/
Authorization: Bearer <admin_access_token>
Content-Type: application/json

{
    "name": "Ürün Adı",
    "description": "Ürün açıklaması",
    "price": 999.99,
    "stock": 50,
    "slug": "urun-adi",
    "category": 1
}
```

#### Ürün Görseli Yükleme
```bash
POST /api/products/admin/{id}/images/
Authorization: Bearer <admin_access_token>
Content-Type: multipart/form-data

{
    "image": <file>,
    "alt_text": "Görsel açıklaması"
}
```

### Sepet İşlemleri

#### Sepete Ürün Ekleme
```bash
POST /api/cart/add/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "product_id": 1,
    "quantity": 2
}
```

#### Sepeti Görüntüleme
```bash
GET /api/cart/
Authorization: Bearer <access_token>
```

#### Sepet Ürün Güncelleme
```bash
PUT /api/cart/items/{item_id}/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "quantity": 5
}
```

### Sipariş İşlemleri

#### Sipariş Oluşturma
```bash
POST /api/orders/create/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "delivery_address": 1,
    "billing_address": 1,
    "coupon_code": "INDIRIM20"
}
```

#### Siparişlerimi Görüntüleme
```bash
GET /api/orders/
Authorization: Bearer <access_token>
```

### Yorum İşlemleri

#### Yorum Ekleme
```bash
POST /api/comments/create/
Authorization: Bearer <access_token>
Content-Type: application/json

{
    "product": 1,
    "text": "Harika bir ürün!",
    "rating": 5
}
```

## 🔒 Güvenlik

### Rate Limiting
API'de istek hızı sınırlamaları mevcuttur:

- **Anonim Kullanıcılar:**
  - Minimum: 25 istek/gün
  - Maximum: 50 istek/gün

- **Kimlikli Kullanıcılar:**
  - Minimum: 50 istek/gün
  - Maximum: 100 istek/gün

### CORS Ayarları
Geliştirme ortamında tüm originlere izin verilmektedir. Production ortamında `CORS_ALLOWED_ORIGINS` ayarını yapılandırın:

```python
# settings.py
CORS_ALLOWED_ORIGINS = [
    'https://yourdomain.com',
    'https://www.yourdomain.com',
]
```

### Ortam Değişkenleri
Production ortamı için önemli ayarlar:

```python
# settings.py
DEBUG = False
SECRET_KEY = 'production-secret-key'  # Güçlü bir key kullanın
ALLOWED_HOSTS = ['yourdomain.com']

# İyzico Production Keys
IYZICO_API_KEY = "your-production-api-key"
IYZICO_SECRET_KEY = "your-production-secret-key"
IYZICO_BASE_URL = "api.iyzipay.com"
```

## 📝 Loglama

Uygulama detaylı loglama sistemine sahiptir. Loglar `logs/django.log` dosyasında saklanır:

- **INFO:** Genel bilgi mesajları
- **WARNING:** Uyarılar
- **ERROR:** Hatalar
- **CRITICAL:** Kritik hatalar

## 🧪 Test

```bash
python manage.py test
```

Belirli bir app için test:
```bash
python manage.py test products
```

## 🚀 Production Deployment

### 1. Debug Modunu Kapatın
```python
DEBUG = False
```

### 2. Güvenli Secret Key Kullanın
```python
import secrets
SECRET_KEY = secrets.token_urlsafe(50)
```

### 3. Veritabanını Yapılandırın
PostgreSQL kullanımı önerilir:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 4. Static ve Media Dosyalarını Yapılandırın
```bash
python manage.py collectstatic
```

### 5. HTTPS Kullanın
```python
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
```

## 🤝 Katkıda Bulunma

1. Fork yapın
2. Feature branch oluşturun (`git checkout -b feature/amazing-feature`)
3. Değişikliklerinizi commit edin (`git commit -m 'Add some amazing feature'`)
4. Branch'inizi push edin (`git push origin feature/amazing-feature`)
5. Pull Request açın

## 📞 İletişim

batuhanyilmaz0011@gmail.com

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

---

## 🎨 Frontend Entegrasyonu

Bu proje React tabanlı bir frontend ile entegre edilmiştir. Frontend entegrasyon detayları için [`FRONTEND/frontend_for_website/README_INTEGRATION.md`](./FRONTEND/frontend_for_website/README_INTEGRATION.md) dosyasına bakabilirsiniz.

### Frontend Özellikleri

#### ✅ Tamamlanan Entegrasyonlar

**API Service Katmanı:**
- Tüm backend endpoint'leri için service katmanı
- Otomatik JWT token yenileme
- Request/Response interceptors
- Gelişmiş hata yönetimi

**Authentication Sistemi:**
- JWT tabanlı kimlik doğrulama
- Persistent authentication (localStorage)
- Auto-refresh token mekanizması
- Admin/User rol yönetimi

**Sepet Yönetimi:**
- Real-time sepet güncellemeleri
- Ürün miktar yönetimi
- Toplam fiyat hesaplama
- Kupon kodu desteği

**Sayfalar:**
- ✅ Login/Register sayfaları (Backend entegre)
- ✅ Ana sayfa (Ürün vitrin)
- ✅ Ürün listesi (Filtreleme ve sıralama)
- ✅ Ürün detay sayfası
- ⏳ Sepet sayfası (Backend ready)
- ⏳ Checkout sayfası (Backend ready)
- ⏳ Kullanıcı paneli (Backend ready)

### Backend - Frontend API Uyumu

#### Düzeltilen Endpoint'ler:
```
❌ /auth/register  →  ✅ /api/users/signup
❌ /auth/login     →  ✅ /api/users/login
❌ /cart/*         →  ✅ /api/cards/*
```

#### Token Response Formatı:
```json
{
  "message": "Login successfull",
  "token": {
    "access": "eyJ0eXAiOiJKV1QiLCJhbGc...",
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGc..."
  },
  "user": {
    "id": 1,
    "email": "user@example.com",
    "first_name": "John",
    "last_name": "Doe",
    "phone": "05551234567",
    "role": "user"
  }
}
```

### Frontend Kurulum

```bash
# Frontend dizinine git
cd FRONTEND/frontend_for_website

# Bağımlılıkları yükle
npm install

# Development server'ı başlat
npm start
```

### Environment Variables (.env)
```env
REACT_APP_BACKEND_URL=http://localhost:8000
```

### Frontend Kullanım Örnekleri

#### Authentication:
```javascript
import { useAuth } from '@/context/AuthContext';

const { login, register, user } = useAuth();

// Kullanıcı kaydı
await register({
  first_name: 'John',
  last_name: 'Doe',
  email: 'john@example.com',
  phone: '05551234567',
  password: 'SecurePass123',
  password2: 'SecurePass123'
});

// Giriş
await login('john@example.com', 'SecurePass123');
```

#### Sepet İşlemleri:
```javascript
import { useCart } from '@/context/CartContext';

const { addToCart, cart, cartCount } = useCart();

// Sepete ürün ekle
await addToCart(productId, 2);

// Toplam ürün sayısı
console.log(cartCount); // 2
```

#### API Servisleri:
```javascript
import { productService, categoryService } from '@/lib/api';

// Ürün listesi (filtreleme ile)
const products = await productService.getAll({
  category: 1,
  sort_by: 'price_asc',
  min_price: 100,
  max_price: 500,
  in_stock: true
});

// Kategoriler
const categories = await categoryService.getAll();
```

### Backend İyileştirme Gereksinimleri

Frontend'in tam performans gösterebilmesi için backend'de bazı değişiklikler gereklidir. Detaylı liste için [`FRONTEND/frontend_for_website/BACKEND_CHANGES_REQUIRED.md`](./FRONTEND/frontend_for_website/BACKEND_CHANGES_REQUIRED.md) dosyasına bakın.

**Kritik Değişiklikler:**
1. Product model: `original_price`, `featured`, `created_at` fields
2. Category model: `slug`, `image` fields
3. Serializers: `category_name`, `category_id`, `product_count`, `images[].url`
4. Product filtering: `featured`, `category`, `price_range`, `in_stock`, `search`
5. Response format standardization

---

**Not:** Bu proje eğitim amaçlı geliştirilmiştir. Production ortamında kullanmadan önce güvenlik testlerini yapın ve gerekli optimizasyonları uygulayın.