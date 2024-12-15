from django.db import models
from django.utils.translation import gettext_lazy as _

# region helper field classes
class SeparatedValuesField(models.TextField):
    description = _("Comma-separated values")

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super().__init__(*args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return value.split(self.token)

    def to_python(self, value):
        if isinstance(value, list):
            return value
        if value is None:
            return value
        return value.split(self.token)

    def get_prep_value(self, value):
        if value is None:
            return value
        return self.token.join(value)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)

# endregion