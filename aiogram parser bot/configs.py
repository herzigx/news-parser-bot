CATEGORIES = {
    'Общество': 'society/',
    'Политика': 'politics/',
    'Экономика': 'economy/',
    'Спорт': 'sport/',
    'Колумнисты': 'column/',
    'Мир': 'world/'
}

def get_value(key):
    for k, v in CATEGORIES.items():
        if k == key:
            return v