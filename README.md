# PagesJaunes contact extraction

A research operation conducted in **2017** to extract contact information from PagesJaunes into structured databases. The extraction ran on a **VPS for one week** and produced separate SQLite datasets for directory URLs and contact records.

## Research objective

Investigate the collection of contact information distributed across directory result pages and consolidate it into a dataset that could be queried independently of the website.

## Method

| Stage | Approach |
|---|---|
| URL collection | Collect directory URLs together with associated name fields. |
| Directory traversal | Process result pages and follow pagination. |
| Field extraction | Capture names, address components, and telephone fields. |
| Data storage | Store the collected results in SQLite, retaining page and block tracking fields where present. |
| Execution | Run the collection on a VPS over one week. |

## Findings

The operation successfully converted directory information into structured SQLite results. URL collection and contact records were retained in separate databases.

| Area | Result |
|---|---|
| Directory URLs | 963,207 stored URL rows with associated name and letter fields. |
| Contact records | 1,870,614 stored rows across five tables. |
| Extracted fields | Surname, given name, street, postcode, city, and up to two telephone fields per row. |
| Traversal information | Some tables retain the source URL, page count, current page, or block identifiers. |
| Output size | 2.24 GB across the two SQLite files. |

Counts describe stored rows across the tables; they have not been deduplicated into unique people or telephone numbers.

## Results

The complete SQLite files are available in the private [2017 research results release](https://github.com/Amine-Belgacem/pagesjaunes-contact-extraction/releases/tag/results-2017).

| Dataset | Size | Download |
|---|---:|---|
| Directory URLs | 163,897,344 bytes | [fr-urls.db](https://github.com/Amine-Belgacem/pagesjaunes-contact-extraction/releases/download/results-2017/fr-urls.db) |
| Contact records | 2,078,420,992 bytes | [fr-phone-leads.db](https://github.com/Amine-Belgacem/pagesjaunes-contact-extraction/releases/download/results-2017/fr-phone-leads.db) |

### Contact-table breakdown

| Table | Stored rows |
|---|---:|
| `A` | 169,828 |
| `B` | 769,072 |
| `C` | 470,335 |
| `PJWScarper` | 93,200 |
| `eee` | 368,179 |
| **Total** | **1,870,614** |

The [database schema](schema.sql) documents the original table and column definitions. The downloadable databases retain their original contents and structure.
