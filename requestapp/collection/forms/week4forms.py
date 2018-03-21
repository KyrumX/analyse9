import bleach
from django.forms import ModelForm

from requestapp.models import Message

ALLOWED_TAGS = ['b', 'i', 'a']
ALLOWED_ATTRIBUTES = {'a': ['href', 'rel']}

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['message']

    def clean_message(self):
        data = self.cleaned_data['message']
        cleaned = bleach.clean(data, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRIBUTES)

        return cleaned