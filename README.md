# 🚀 راه‌اندازی پروژه

برای راه‌اندازی پروژه، مراحل زیر را دنبال کنید:

## پیش‌نیازها
- **داکر**: اگر داکر و داکر کامپوز نصب نکرده‌اید، راهنمای [نصب داکر](https://docs.docker.com/get-docker/) و [نصب داکر کامپوز](https://docs.docker.com/compose/install/) را دنبال کنید.

---

## مراحل راه‌اندازی

1. **کلون کردن مخزن**

   مخزن پروژه را به سیستم محلی خود کلون کنید:

   ```bash
   git clone https://github.com/Mohamad-bigdeli/ShareHolders.git
   ```

2. **ورود به پوشه پروژه**

   با استفاده از دستور cd به پوشه پروژه بروید:

   ```bash
   cd ShareHolders
   ```

3. **اجرای داکر کامپوز**

   با استفاده از داکر کامپوز، سرویس‌های پروژه را اجرا کنید:

   ```bash
   docker-compose up --build
   ```

4. **ایجاد و اعمال مهاجرت‌ها**

   پس از بالا آمدن سرویس‌ها، مهاجرت‌های پایگاه داده را با دستورات زیر ایجاد و اعمال کنید:

   ```bash
   docker-compose exec backend sh -c "python manage.py makemigrations"
   docker-compose exec backend sh -c "python manage.py migrate"
   ```

5. **ایجاد کاربر ارشد**

   برای دسترسی به پنل مدیریت جنگو، یک کاربر ارشد ایجاد کنید:

   ```bash
   docker-compose exec backend sh -c "python manage.py createsuperuser"
   ```


6. **مشاهده پروژه**

   پروژه شما اکنون روی پورت 8000 اجرا می‌شود. مرورگر خود را باز کرده و به آدرس زیر بروید:

   ```bash
   http://127.0.0.1:8000
   ```

   ```bash
   http://127.0.0.1:8000/swagger
   ```
   **داکیومنت اندپوینت ها:**
       - [endpoints](https://github.com/Mohamad-bigdeli/ShareHolders/blob/main/core/shareholder/docs/document.md)

7. **دسترسی به پنل مدیریت**

   برای دسترسی به پنل مدیریت جنگو، به آدرس زیر برcentes بروید و با اطلاعات کاربر ارشد وارد شوید:

   ```bash
   http://localhost:8000/admin
   ```

## یادداشت‌های اضافی

   - اگر تغییراتی در کد ایجاد کردید و نیاز به راه‌اندازی مجدد سرویس‌ها دارید، از دستور `docker-compose restart` استفاده کنید.
   - برای متوقف کردن سرویس‌ها، از دستور `docker-compose down` استفاده کنید.
