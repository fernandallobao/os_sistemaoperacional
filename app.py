import os
import platform

usuario = os.environ.get('USERNAME')


print(f'Sistema operacional: {platform.system()} {platform.release()}')
print(f'Nome de usuario: {usuario}')