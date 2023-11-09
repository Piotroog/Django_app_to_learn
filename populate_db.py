from aplikacja_ang.models import Slowko

slownik_polsko_angielski = [
    ('rybka', 'fish'),
    ('chomik', 'hamster'),
    ('żółw', 'turtle'),
    ('królik', 'rabbit'),
    ('miłość', 'love'),
    ('kanarek', 'canary'),
    ('wąż', 'snake'),
    ('mysz', 'mouse'),
    ('szczur', 'rat'),
    ('stół', 'table'),
    ('krzesło', 'chair'),
    ('łóżko', 'bed'),
    ('sofa', 'sofa'),
    ('szafa', 'wardrobe'),
    ('telewizor', 'TV'),
    ('telefon', 'phone'),
    ('komputer', 'computer'),
    ('zegar', 'clock'),
    ('drzwi', 'door'),
    ('okno', 'window'),
    ('książka', 'book'),
    ('notatnik', 'notebook'),
    ('długopis', 'pen'),
    ('ołówek', 'pencil'),
    ('plecak', 'backpack'),
    ('buty', 'shoes'),
    ('koszula', 'shirt'),
    ('spodnie', 'pants'),
    ('sukienka', 'dress'),
    ('kawa', 'coffee'),
    ('herbata', 'tea'),
    ('mleko', 'milk'),
    ('chleb', 'bread'),
    ('masło', 'butter'),
    ('ser', 'cheese'),
    ('pomarańcza', 'orange'),
    ('banan', 'banana'),
    ('piłka nożna', 'football'),
    ('koszykówka', 'basketball'),
    ('tenis', 'tennis'),
    ('pływanie', 'swimming'),
    ('bieganie', 'running'),
]



obiekty_slowko = [Slowko(polskie=par[0], angielskie=par[1]) for par in slownik_polsko_angielski]

Slowko.objects.bulk_create(obiekty_slowko)