# PagesJaunes contact extraction

**Amine Belgacem · Data extraction research · Archived run: April 2021**

A research operation conducted on PagesJaunes to extract directory contacts into structured SQLite datasets. The work combined URL collection, result-page navigation, pagination, and contact-field extraction through a configured scraping agent. The operation produced a URL database and a larger contact database containing names, addresses, and telephone fields.

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
| Directory traversal | Configure result-page navigation, pagination, and next-page processing. | Agent tables for the main workflow, `Pagination`, `Bloc`, and `Next`. |
| Contact extraction | Capture names, address components, and telephone fields. | Five contact tables in `fr-phone-leads.db`. |
| Structured storage | Retain the extracted fields in SQLite for later querying. | Original databases, CSV exports, and runtime files. |

The resulting schema separates surname, given name, street, postcode, city, and two telephone fields. Some tables also retain page and block tracking fields. The original labels, including the `Allowed` columns, remain as stored; their meaning is not inferred from their names.

## Scraping tool

The [original `PJ_Scarper.scg` file](originals/PJ_Scarper/PJ_Scarper.scg) is the scraping agent configuration. Its `.scg` format and `SWSIR` internal-table structure identify the **Content Grabber / Sequentum** tool family. The contribution presented here is the research operation and workflow configuration. The exact application version is not recorded in the inspected files.

The vendor's [Content Grabber manual](https://contentgrabber.com/Manual/running_agents_from_the_comman.htm) documents `.scg` agent files. Its [internal-database example](https://sequentum.atlassian.net/wiki/spaces/SKB/pages/81428485/Accessing+the+Internal+Database+at+Runtime) uses the same `SWSIR` prefix and `Sequentum.ContentGrabber` namespaces found in this tool family.

The archived internal database contains a run timestamp of **1 April 2021**. This dates that saved run, not the entire collection period.

## Project files

```text
pagesjaunes-contact-extraction/
    README.md
    docs/
        results.md              Table counts and dataset description
        storage.md              Local archive and GitHub contents
        inventory.json          File hashes, sizes, schemas, and counts
        schema.sql              Table definitions without contact records
    tools/
        inspect_archive.py      Read-only inspection of the local archive
    originals/
        PJ_Scarper/
            PJ_Scarper.scg      Original agent configuration, tracked in Git
            Data/               Local runtime databases
            Debug/              Local debug files and export
            Export/             Local CSV export
            Log/                Local browser log
        fr-urls.db              Local URL dataset
        fr-phone-leads.db       Local contact dataset
```

The private GitHub repository contains the case study, schema, inventory, inspection script, and original agent configuration. SQLite files, CSV exports, and runtime logs remain in the local `originals/` folder. [Storage details](docs/storage.md).

The complete original files are retained without redaction or byte changes. This case study was prepared in 2026 from the archived configuration and datasets.
