from django.utils.translation import activate

from texts.texts import print_things

print("in English")
activate('en')
print_things()

print('---')
print('now in spanish')
activate('es')
print_things()
