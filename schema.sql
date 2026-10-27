-- Original table definitions only; no contact records.

-- File: fr-urls.db | Table: URLs
CREATE TABLE "URLs" (
  "Letter" TEXT(255),
  "LastName" TEXT(255),
  "FirstName" TEXT(255),
  "URL" TEXT(255),
  "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT
);

-- File: fr-phone-leads.db | Table: A
CREATE TABLE "A" (
  "Last Name" TEXT(255),
  "First Name" TEXT(255),
  "Street" TEXT(255),
  "Zip" TEXT(255),
  "City" TEXT(255),
  "Phone" TEXT(255),
  "Allowed" TEXT(255),
  "Phone (2)" TEXT(255),
  "Allowed (2)" TEXT(255)
);

-- File: fr-phone-leads.db | Table: B
CREATE TABLE "B" (
  "Lastname" TEXT(255),
  "Name" TEXT(255),
  "Street" TEXT(255),
  "Zip" TEXT(255),
  "City" TEXT(255),
  "Phone" TEXT(255),
  "Allowed" TEXT(255),
  "Phone (2)" TEXT(255),
  "Allowed (2)" TEXT(255)
);

-- File: fr-phone-leads.db | Table: C
CREATE TABLE "C" (
  "CurrentURL" TEXT(255),
  "PageCount" TEXT(255),
  "currentPage" TEXT(255),
  "CurrentBlock" TEXT(255),
  "Lastname" TEXT(255),
  "name" TEXT(255),
  "Street" TEXT(255),
  "Zip" TEXT(255),
  "City" TEXT(255),
  "Phone" TEXT(255),
  "Allowed" TEXT(255),
  "Phone (2)" TEXT(255),
  "Allowed (2)" TEXT(255)
);

-- File: fr-phone-leads.db | Table: PJWScarper
CREATE TABLE "PJWScarper" (
  "URL" TEXT(255),
  "RS" TEXT(255),
  "PC" TEXT(255),
  "P" TEXT(255),
  "Num" TEXT(255),
  "Lastname" TEXT(255),
  "Name" TEXT(255),
  "Street" TEXT(255),
  "Zip" TEXT(255),
  "City" TEXT(255),
  "Phone" TEXT(255),
  "Allowed" TEXT(255),
  "Phone (2)" TEXT(255),
  "Allowed (2)" TEXT(255)
);

-- File: fr-phone-leads.db | Table: eee
CREATE TABLE "eee" (
  "URL" TEXT(255),
  "RS" TEXT(255),
  "PC" TEXT(255),
  "P" TEXT(255),
  "Num" TEXT(255),
  "Lastname" TEXT(255),
  "Name" TEXT(255),
  "Street" TEXT(255),
  "Zip" TEXT(255),
  "City" TEXT(255),
  "Phone" TEXT(255),
  "Allowed" TEXT(255),
  "Phone (2)" TEXT(255),
  "Allowed (2)" TEXT(255)
);
