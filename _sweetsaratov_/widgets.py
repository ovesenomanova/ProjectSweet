from django.forms.widgets import DateInput as baseDateInput


class DateInput(baseDateInput):
    input_type = 'date'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs.setdefault('min', '1950-01-01')
        self.attrs.setdefault('max',' 2030-01-01')
