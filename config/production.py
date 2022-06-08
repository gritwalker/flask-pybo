from logging.config import dictConfig


from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'f\xe6cE=\xb6-\xd3\xd8\xc1\xdb?\xde\xae\x80\xd4'

dictConfig({
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/myproject.log'),
            'maxBytes': 1024*1024 * 5, #5 MB
            'backupCount': 5,
            'formatter': 'default',
        },
    },
    'root': {
        'level': 'INFO',
        'handlers': ['file']
    }
})

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    username='dbmasteruser',
    pw='e{]RI{5N3=Fk?5V3{Fb-)Q{!VTcg;O42',
    url='ls-dd0e4a6b23c673d0cbff8d426dd6dd8b1d19e250.caoi9qja82pl.ap-northeast-2.rds.amazonaws.com',
    db='flask_pybo')