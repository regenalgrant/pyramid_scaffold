import os
import sys
import transaction
import datetime

from pyramid.paster import (
    get_appsettings,
    setup_logging,
    )

from pyramid.scripts.common import parse_vars

from ..models.meta import Base
from ..models import (
    get_engine,
    get_session_factory,
    get_tm_session,
    )
from ..models import Entry


def usage(argv):
    cmd = os.path.basename(argv[0])
    print('usage: %s <config_uri> [var=value]\n'
          '(example: "%s development.ini")' % (cmd, cmd))
    sys.exit(1)


def main(argv=sys.argv):
    if len(argv) < 2:
        usage(argv)
    config_uri = argv[1]
    options = parse_vars(argv[2:])
    setup_logging(config_uri)
    settings = get_appsettings(config_uri, options=options)

    engine = get_engine(settings)
    Base.metadata.create_all(engine)

    session_factory = get_session_factory(engine)

    with transaction.manager:
        dbsession = get_tm_session(session_factory, transaction.manager)

        ENTRIES = [
            {"title": "First Entry", "creation_date": datetime.datetime(2016, 12, 18, 0, 0), "body": "blah.", "category": "Testing", "tags": "Testing"},
            {"title": "LJ - Day 11", "creation_date": datetime.datetime(2016, 12, 19, 0, 0), "body": "blahr.", "category": "Learning Journal", "tags": "Learning Journal"},
            {"title": "LJ - Day 12", "creation_date": datetime.datetime(2016, 12, 20, 0, 0), "body": "blah", "category": "Learning Journal", "tags": "Learning Journal"},

        ]

        for entry in ENTRIES:

            new_entry = Entry(title=entry['title'], body=entry['body'], creation_date=entry['creation_date'], category=entry['category'], tags=entry['tags'])

            dbsession.add(new_entry
                editor = User(name='editor', role='editor')
        editor.set_password('editor')
        dbsession.add(editor)

        basic = User(name='basic', role='basic')
        basic.set_password('basic')
        dbsession.add(basic)

        page = Page(
            name='FrontPage',
            creator=editor,
            data='This is the front page',
        )
        dbsession.add(page)