from urllib.parse import quote

from django.test import TestCase

from bananas import url

__test__ = {
    'Doctest': url
}


class DBURLTest(TestCase):
    def test_sqlite_memory(self):
        conf = url.database_conf_from_url('sqlite://')

        self.assertDictEqual(conf, {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '',
            'USER': None,
            'HOST': None,
            'PORT': None,
            'PARAMS': {},
            'SCHEMA': None,
            'PASSWORD': None,
        })

    def test_db_url(self):
        conf = url.database_conf_from_url(
            'pgsql://joar:hunter2@5monkeys.se:4242/tweets/tweetschema'
            '?hello=world')

        self.assertDictEqual(conf, {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'HOST': '5monkeys.se',
            'NAME': 'tweets',
            'PARAMS': {'hello': 'world'},
            'PASSWORD': 'hunter2',
            'PORT': 4242,
            'SCHEMA': 'tweetschema',
            'USER': 'joar',
        })

    def test_db_url_with_slashes(self):
        name = quote('/var/db/tweets.sqlite', safe='')
        conf = url.database_conf_from_url('sqlite3:///{0}'.format(name))

        self.assertDictEqual(conf, {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': '/var/db/tweets.sqlite',
            'USER': None,
            'HOST': None,
            'PORT': None,
            'PARAMS': {},
            'SCHEMA': None,
            'PASSWORD': None,
        })
