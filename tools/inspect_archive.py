"""Inventory the archived files without exporting contact records or changing SQLite files."""
from pathlib import Path
from collections import Counter
from urllib.parse import urlsplit
import hashlib
import json
import sqlite3

ROOT = Path(__file__).resolve().parents[1]
ORIGINALS = ROOT / 'originals'
DOCS = ROOT / 'docs'
PRIMARY = ('fr-urls.db', 'fr-phone-leads.db')


def sha256(file):
    with file.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def quoted(name):
    return '"' + name.replace('"', '""') + '"'


def connect(file):
    connection = sqlite3.connect(file.as_uri() + '?mode=ro&immutable=1', uri=True)
    connection.execute('PRAGMA query_only=ON')
    return connection


def inspect():
    required = [ORIGINALS / name for name in PRIMARY]
    required.append(ORIGINALS / 'PJ_Scarper/PJ_Scarper.scg')
    if any(not file.is_file() for file in required):
        raise SystemExit('The complete local originals are required. See docs/storage.md.')

    inventory = {'format': 1, 'rowCountMeaning': 'Stored rows; not deduplicated contacts.',
                 'files': [], 'databases': [], 'urlHostSample': {}, 'archivedRunDates': {}}
    for file in sorted(file for file in ORIGINALS.rglob('*') if file.is_file()):
        relative = file.relative_to(ORIGINALS).as_posix()
        inventory['files'].append({'path': relative, 'bytes': file.stat().st_size,
                                   'sha256': sha256(file),
                                   'trackedOriginal': relative == 'PJ_Scarper/PJ_Scarper.scg'})

    schema = ['-- Original table definitions only; no contact records.']
    for name in PRIMARY:
        file = ORIGINALS / name
        with connect(file) as connection:
            tables = []
            for table, sql in connection.execute(
                    "SELECT name, sql FROM sqlite_master WHERE type='table' "
                    "AND name NOT LIKE 'sqlite_%' ORDER BY name").fetchall():
                columns = [row[1] for row in connection.execute('PRAGMA table_info(' + quoted(table) + ')')]
                count = connection.execute('SELECT COUNT(*) FROM ' + quoted(table)).fetchone()[0]
                tables.append({'name': table, 'rows': count, 'columns': columns, 'createSql': sql})
                schema.extend(['', '-- File: ' + name + ' | Table: ' + table, sql.replace('\r\n', '\n').rstrip(';') + ';'])
            inventory['databases'].append({'path': name, 'bytes': file.stat().st_size, 'tables': tables})
            if name == 'fr-urls.db':
                hosts = Counter(urlsplit(str(row[0])).hostname or '(relative URL)' for row in
                                connection.execute('SELECT URL FROM URLs ORDER BY id LIMIT 1000'))
                inventory['urlHostSample'] = {'sampleRows': sum(hosts.values()), 'hosts': dict(sorted(hosts.items()))}

    runtime = ORIGINALS / 'PJ_Scarper/Data/PJ_Scarper_internal.db'
    if runtime.is_file():
        with connect(runtime) as connection:
            first, last = connection.execute('SELECT MIN(run_date_), MAX(run_date_) FROM "SWSIR PJ_Scarper"').fetchone()
            inventory['archivedRunDates'] = {'first': first, 'last': last}

    DOCS.mkdir(exist_ok=True)
    (DOCS / 'inventory.json').write_text(json.dumps(inventory, indent=2, ensure_ascii=False) + '\n', encoding='utf-8', newline='\n')
    (DOCS / 'schema.sql').write_text('\n'.join(schema) + '\n', encoding='utf-8', newline='\n')
    print(json.dumps({'originalFiles': len(inventory['files']),
                      'primaryTables': sum(len(db['tables']) for db in inventory['databases']),
                      'generated': ['docs/inventory.json', 'docs/schema.sql']}))


if __name__ == '__main__':
    inspect()
