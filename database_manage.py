#!/usr/bin/env python
from migrate.versioning.shell import main

if __name__ == '__main__':
    main(debug='False', repository='database_migrate', url='sqlite:///app.db')
