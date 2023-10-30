import random
import string

from .models import URLMap


def get_unique_short_id():
    short_id = ''.join(
        random.choices(string.ascii_letters + string.digits, k=16)
    )
    if URLMap.query.filter_by(short=short_id).first():
        return get_unique_short_id()
    return short_id
