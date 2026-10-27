# Archive storage

The complete archive is stored locally in this project's `originals/` folder. All 13 original files retain their contents, filenames, and internal directory structure. The parent project folder was renamed from `pagejaune.fr-scraping` to `pagesjaunes-contact-extraction` when this repository was prepared.

| Material | Local archive | Private GitHub repository |
|---|---|---|
| `PJ_Scarper/PJ_Scarper.scg` agent configuration | Complete original | Complete original |
| `fr-urls.db` and `fr-phone-leads.db` | Complete originals | Inventory, hashes, schema, and aggregate counts |
| Runtime/debug SQLite files | Complete originals | File inventory and hashes |
| CSV exports and browser log | Complete originals | File inventory and hashes |
| Case study and inspection script | Included | Included |

The two large SQLite files total 2,242,318,336 bytes. Git ignore rules keep all original runtime files and datasets local while allowing the original `.scg` configuration to be tracked. A Git clone therefore contains the write-up and configuration; it does not include the local datasets. The GitHub repository is not a backup of those excluded files.

## Inspecting the archive

With Python 3.11 or later and the complete local archive in place:

```text
python tools/inspect_archive.py
```

The script opens SQLite files in read-only immutable mode and regenerates `docs/inventory.json` and `docs/schema.sql`. It reports file metadata, table definitions, and aggregate counts; it does not export contact records. The immutable connection assumes the archived databases are not being modified by another application during inspection.

[Back to the project](../README.md)
