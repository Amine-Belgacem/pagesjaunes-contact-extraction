# PagesJaunes contact extraction

**Amine Belgacem · Data extraction research · 2021**

A contact extraction operation conducted on PagesJaunes, running on a **VPS for one week**. The work combined URL collection, result-page navigation, pagination, and contact-field extraction to produce structured SQLite datasets containing names, addresses, and telephone fields.

## Download the results

The complete original SQLite files are available in the private [results release](https://github.com/Amine-Belgacem/pagesjaunes-contact-extraction/releases/tag/results-2021):

- [Download the URL database — fr-urls.db](https://github.com/Amine-Belgacem/pagesjaunes-contact-extraction/releases/download/results-2021/fr-urls.db)
- [Download the contact database — fr-phone-leads.db](https://github.com/Amine-Belgacem/pagesjaunes-contact-extraction/releases/download/results-2021/fr-phone-leads.db)

## Outcome

| Output | Stored rows | Size |
|---|---:|---:|
| `fr-urls.db` — `URLs` table | 963,207 | 163,897,344 bytes |
| `fr-phone-leads.db` — five tables combined | 1,870,614 | 2,078,420,992 bytes |
| **Combined SQLite file size** | | **2,242,318,336 bytes (2.24 GB)** |

These are stored row counts. The contact tables include multiple extraction tables; their combined count is not a count of unique people or unique telephone numbers. [Results and table breakdown](docs/results.md).

## Method and findings

| Stage | Work | Preserved result |
|---|---|---|
| URL collection | Assemble directory URLs with associated name fields. | `fr-urls.db`, with letter, name, URL, and identifier columns. |
| Directory traversal | Process directory results and follow pagination. | URL, page, and block tracking fields in the results. |
| Contact extraction | Capture names, address components, and telephone fields. | Five contact tables in `fr-phone-leads.db`. |
| Structured storage | Retain the extracted fields in SQLite for later querying. | Two complete SQLite result databases. |

The resulting schema separates surname, given name, street, postcode, city, and two telephone fields. Some tables also retain page and block tracking fields. The original labels, including the `Allowed` columns, remain as stored; their meaning is not inferred from their names.

## Execution

The extraction ran on a virtual private server for one week. The resulting URL and contact databases preserve the output of that operation, including the original table structures and stored fields.

## Project files

```text
pagesjaunes-contact-extraction/
    README.md
    docs/
        results.md              Table counts and dataset description
        storage.md              Result downloads and local storage
        inventory.json          File hashes, sizes, schemas, and counts
        schema.sql              Table definitions without contact records
    tools/
        inspect_archive.py      Read-only inspection of the local archive
    originals/
        fr-urls.db              Original URL dataset
        fr-phone-leads.db       Original contact dataset
```

The repository contains the case study, schema, inventory, and inspection script. The complete databases are hosted on GitHub as release downloads, with local copies in `originals/`. [Storage details](docs/storage.md).

Both result databases are retained without redaction or byte changes. This case study was prepared in 2026 from the archived datasets.
