from hashids import Hashids

MIN_LENGTH = 6

PRODUCT_SALT = 'Product Salt. yay!'
PRODUCT = Hashids(salt=PRODUCT_SALT, min_length=MIN_LENGTH)

USER_SALT = 'User Salt. Waaaah!'
USER = Hashids(salt=USER_SALT, min_length=MIN_LENGTH)

CATEGORY_SALT = 'Wow, another salt? Yeah, this one\'s for categories'
CATEGORY = Hashids(salt=CATEGORY_SALT, min_length=MIN_LENGTH)