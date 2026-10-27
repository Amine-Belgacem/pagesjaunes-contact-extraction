# Result storage and downloads

The complete original databases are hosted as assets in the private [results release](https://github.com/Amine-Belgacem/pagesjaunes-contact-extraction/releases/tag/results-2021). They preserve the output of the week-long VPS operation without redaction or byte changes.

| Result | Bytes | Download |
|---|---:|---|
| URL database | 163,897,344 | [fr-urls.db](https://github.com/Amine-Belgacem/pagesjaunes-contact-extraction/releases/download/results-2021/fr-urls.db) |
| Contact database | 2,078,420,992 | [fr-phone-leads.db](https://github.com/Amine-Belgacem/pagesjaunes-contact-extraction/releases/download/results-2021/fr-phone-leads.db) |

The two files total 2,242,318,336 bytes. They are release downloads because they exceed GitHub's normal Git file-size limit. The repository and its release remain private.

Local copies are stored in `originals/fr-urls.db` and `originals/fr-phone-leads.db`. A Git clone contains the documentation and inspection script; download the release assets into `originals/` to inspect the complete results locally. [SHA-256 hashes and inventory](inventory.json).

## Inspecting the archive

With Python 3.11 or later and the complete local archive in place:

```text
python tools/inspect_archive.py
```

The script opens SQLite files in read-only immutable mode and regenerates `docs/inventory.json` and `docs/schema.sql`. It reports file metadata, table definitions, and aggregate counts; it does not export contact records. The immutable connection assumes the archived databases are not being modified by another application during inspection.

[Back to the project](../README.md)
