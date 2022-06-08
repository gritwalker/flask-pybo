

from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'f\xe6cE=\xb6-\xd3\xd8\xc1\xdb?\xde\xae\x80\xd4'