# Extraction results

The extraction ran on a VPS for one week and produced two primary SQLite files: one for directory URLs and one for extracted contact records. The [complete results are available on GitHub](https://github.com/Amine-Belgacem/pagesjaunes-contact-extraction/releases/tag/results-2021). Counts below were measured from the original files using read-only SQLite connections.

## URL collection

| File | Table | Rows | Columns |
|---|---|---:|---|
| `fr-urls.db` | `URLs` | 963,207 | `Letter`, `LastName`, `FirstName`, `URL`, `id` |

The first 1,000 stored URL rows all use the hostname `www.pagesjaunes.fr`. This establishes the target for that sample; it is not a claim that all stored URLs were checked.

## Contact collection

| File | Table | Rows |
|---|---|---:|
| `fr-phone-leads.db` | `A` | 169,828 |
| `fr-phone-leads.db` | `B` | 769,072 |
| `fr-phone-leads.db` | `C` | 470,335 |
| `fr-phone-leads.db` | `PJWScarper` | 93,200 |
| `fr-phone-leads.db` | `eee` | 368,179 |
| **Total across these tables** | | **1,870,614** |

The total describes stored rows across five tables. Overlap between tables and uniqueness of people, addresses, or telephone numbers have not been measured. Each row can contain up to two telephone fields, which can also be empty.

| Field group | Stored columns |
|---|---|
| Name | Surname and given-name columns, with naming variations between tables. |
| Address | `Street`, `Zip`, `City`. |
| Telephone | `Phone`, `Phone (2)`. |
| Additional labels | `Allowed`, `Allowed (2)`; meaning is not established by the schema. |
| Traversal state | URL, page, and block fields in some tables. |

The [schema](schema.sql) preserves the original column names and definitions without including contact values. The [inventory](inventory.json) records counts, file sizes, and SHA-256 hashes.

[Back to the project](../README.md)
