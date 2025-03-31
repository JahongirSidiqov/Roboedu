# Roboedu
# 📌 Django Online Kurs Platformasi

Ushbu loyiha Django asosida yaratilgan va onlayn kurslarni boshqarish uchun mo‘ljallangan. Foydalanuvchilar kurslarga yozilishi, darslarni ko‘rishi va testlardan o‘tishi mumkin.

## 🚀 Loyihani o‘rnatish

1. **GitHub dan loyihani klonlash**

   ```sh
   git clone https://github.com/JahongirSidiqov/Roboedu.git
   cd Roboedu
   ```

2. **Pipenv ni o‘rnatish (Agar yo‘q bo‘lsa)**

   ```sh
   pip install pipenv
   ```

3. **Virtual muhitni yaratish va kutubxonalarni o‘rnatish**

   ```sh
   pipenv install
   ```

4. **Django ma’lumotlar bazasini yaratish**

   ```sh
   pipenv run python manage.py migrate
   ```

5. **Superuser yaratish (admin panelga kirish uchun)**

   ```sh
   pipenv run python manage.py createsuperuser
   ```

6. **Serverni ishga tushirish**

   ```sh
   pipenv run python manage.py runserver
   ```

7. **Brauzerda ochish**

   ```
   http://127.0.0.1:8000/
   ```

## ⚙️ Admin panelga kirish

Admin panelga kirish uchun:

```
http://127.0.0.1:8000/admin/
```

Superuser login va parolingiz bilan tizimga kiring.



