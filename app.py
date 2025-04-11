from flask import Flask, render_template, request

app = Flask(__name__)

# Словари переводов
translations = {
    'en': {
        'welcome': 'Welcome to Our Restaurant',
        'title_main': 'TASTE ROYALE',
        'title_sub': 'CUISINE',
        'contact_us': 'Contact Us',
        'your_name': 'Your Name',
        'your_message': 'Your Message',
        'send': 'Send',
'phone': 'Phone',
'guests': 'Number of Guests',
'reserve_now': 'Reserve Now',
        'address': 'Address',
'gallery_title': 'The Atmosphere of our restaurant',
        'discover': 'Discover Menu',
        'book': 'Book a Table',
        'about': 'About',
        'menu': 'Menu',
        'gallery': 'Gallery',
        'contact': 'Contact',
        'reservation': 'Reservation',
        'copyright': '© 2025 The Royal Ember Restaurant. Author: Alibek Onege.',
        'about_title': 'About Us',
        'about_subtitle': 'A Taste of Elegance',
        'about_text': 'The Royal Ember is a fine dining restaurant where ambiance meets culinary art. We serve seasonal, chef-crafted dishes in a luxurious setting.',
        'our_menu': 'Our Menu',
'menu_title': 'Experience Delicious Tastes',
    'menu_subtitle': '— Chef\'s Dishes —',
    'download_menu': 'Download Menu',
        'menu_description': 'Book now at The Royal Ember — known for shared plates, craft cocktails, curated wine list and impeccable service!',
        'book_table': 'Book your table',
        'view_menu': 'View Menu'
    },
    'ru': {
        'welcome': 'Добро пожаловать в наш ресторан',
        'title_main': 'ИЗЫСКАННЫЙ ВКУС',
        'title_sub': 'КУХНИ',
        'contact_us': 'Свяжитесь с нами',
        'your_name': 'Ваше имя',
        'your_message': 'Ваше сообщение',
        'send': 'Отправить',
        'address': 'Адрес',
'gallery_title': 'Атмосфера нашего ресторана',
        'discover': 'Посмотреть меню',
        'book': 'Забронировать стол',
        'about': 'О нас',
        'menu': 'Меню',
        'gallery': 'Галерея',
        'contact': 'Контакты',
        'reservation': 'Бронирование',
        'copyright': '© 2025 Ресторан The Royal Ember. Автор: Алибек Онеге.',
        'about_title': 'О Нас',
        'about_subtitle': 'Вкус Элегантности',
        'about_text': 'The Royal Ember — это ресторан высокой кухни, где атмосфера сочетается с кулинарным искусством. Мы подаём сезонные блюда от шефа в роскошной обстановке.',
        'our_menu': 'Наше Меню',
'phone': 'Телефон',
'guests': 'Количество гостей',
'reserve_now': 'Забронировать',
'menu_title': 'Попробуйте изысканные вкусы',
    'menu_subtitle': '— Блюда от шефа —',
    'download_menu': 'Скачать меню',
        'menu_description': 'Забронируйте столик в The Royal Ember — это место с блюдами для всех, авторскими коктейлями, винной картой и безупречным сервисом!',
        'book_table': 'Забронировать столик',
        'view_menu': 'Посмотреть Меню'
    },
    'kz': {
        'welcome': 'Біздің мейрамханаға қош келдіңіз',
        'title_main': 'ДӘМДІ АС',
        'title_sub': 'ТАМАҚТАНУ',
        'discover': 'Мәзірді көру',
'gallery_title': 'Ресторанымыздың атмосферасы',
        'book': 'Үстелге тапсырыс беру',
        'about': 'Біз туралы',
        'menu': 'Мәзір',
        'gallery': 'Галерея',
'phone': 'Телефон',
'guests': 'Қонақ саны',
'reserve_now': 'Тапсырыс беру',
        'contact': 'Байланыс',
        'reservation': 'Тапсырыс беру',
        'copyright': '© 2025 The Royal Ember Рестораны. Авторы: Әлібек Өнеге.',
        'about_title': 'Біз Туралы',
        'about_subtitle': 'Элегантті Дәм',
        'about_text': 'The Royal Ember — бұл атмосфера мен аспаздық өнер үйлесетін жоғары деңгейлі мейрамхана. Біз маусымдық, шеф дайындаған тағамдарды ұсынамыз.',
        'our_menu': 'Біздің Мәзір',
        'contact_us': 'Бізбен байланысыңыз',
        'your_name': 'Атыңыз',
        'your_message': 'Хабарламаңыз',
        'send': 'Жіберу',
        'address': 'Мекенжай',
        'menu_description': 'The Royal Ember — ортақ тағамдар, ерекше коктейльдер, шарап тізімі және мінсіз қызмет үшін танымал мейрамхана. Қазір тапсырыс беріңіз!',
        'book_table': 'Үстелге тапсырыс беру',
'menu_title': 'Керемет дәмдер әлемі',
    'menu_subtitle': '— Аспаз шеберлігі —',
    'download_menu': 'Мәзірді жүктеу',
        'view_menu': 'Мәзірді көру'
    }
}


@app.route('/')
def index():
    lang = request.args.get('lang', 'en')  # по умолчанию en
    trans = translations.get(lang, translations['en'])
    return render_template('index.html', trans=trans)

@app.route('/send-message', methods=['POST'])
def send_message():
    name = request.form['name']
    message = request.form['message']
    print(f"Message from {name}: {message}")
    return redirect(url_for('index'))  # или render_template

@app.route('/reserve', methods=['POST'])
def reserve():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    date = request.form.get('date')
    time = request.form.get('time')
    guests = request.form.get('guests')
    message = request.form.get('message')

    # Тут можно отправить письмо или сохранить в базу данных
    print(f"Reservation from {name}, {email}, {phone} for {date} at {time} — {guests} guests")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
