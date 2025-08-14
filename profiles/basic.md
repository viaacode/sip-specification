---
layout:       default
title:        Basic
parent:       Profiles
grand_parent:  2.1
nav_order:    1
nav_exclude:  false
---
{% assign basic_constraints = site.data.2_1.BASIC_PROFILE %}

# Profile: Basic 

The basic profile supports simple cases consisting of a single media file accompanied by limited metadata.

**Permalink:** <https://data.hetarchief.be/id/sip/2.1/basic>

## Example Directory structure

```plaintext
root_directory
│── METS.xml
│── metadata
|   |── descriptive
|   |   └── dc+schema.xml
|   └── preservation
|       └── premis.xml
│
└── representations
    └──representation_1
        │── METS.xml
        └──data
        |  |── file_1.xyz
        │  └── ...
        │
        └──metadata
          └──preservation
              └── premis.xml
```

## Requirements

### General

{% assign constraints = basic_constraints | where_exp: "c",
"c.Section == 'general'" %}

{% include_relative _list_constraints.liquid constraints = constraints %}

Only the MD5 hashing algorithm is allowed to compute the fixity, thus:

{% assign constraints = basic_constraints | where_exp: "c",
"c.Section == 'md5'" %}

{% include_relative _list_constraints.liquid constraints = constraints %}

### Package METS

{% assign constraints = basic_constraints | where_exp: "c",
"c.Section == 'mets'" %}

{% include_relative _list_constraints.liquid constraints = constraints %}

### <span id="dc-requirements"></span>Descriptive metadata

{% assign constraints = basic_constraints | where_exp: "c",
"c.Section == 'descriptive'" %}

{% include_relative _list_constraints.liquid constraints = constraints %}

{: .important }
For elements that require the `@xml:lang` attribute, it is still necessary to supply an element with `@xml:lang` set to `nl` even if there is no Dutch content available (e.g., the original title is in English or French and no translation was ever made, or the title is the same in both languages). In that case, a title in another language can be copied as if it were Dutch. 

#### Root element

{% assign constraints = basic_constraints | where_exp: "c",
"c.Section == 'metadata'" %}

{% include_relative _constraints.liquid constraints = constraints %}

#### DCMI Terms elements

{% assign constraints = basic_constraints | where_exp: "c",
"c.Section == 'dcterms'" %}

{% include_relative _constraints.liquid constraints = constraints %}

#### Schema.org elements

{% assign constraints = basic_constraints | where_exp: "c",
"c.Section == 'schema'" %}

{% include_relative _constraints.liquid constraints = constraints %}

### Validation

The XML files that are required by this profile can be validated using the following XML schema definitions:

| File | Format | XML Schema |
| `METS.xml` | METS v1.12.1 | [mets.xsd](https://www.loc.gov/standards/mets/mets.xsd) |
| `premis.xml` | PREMIS v3.0 | [premis-v3-0.xsd](https://www.loc.gov/standards/premis/v3/premis-v3-0.xsd) |
| `dc+schema.xml` | Dublin Core (custom schema) | [dc_basic.xsd](https://raw.githubusercontent.com/viaacode/sipin-sip-validator/main/app/resources/xsd/dc_basic.xsd)<br>_depends on: [edtf.xsd](https://raw.githubusercontent.com/viaacode/sipin-sip-validator/main/app/resources/xsd/edtf.xsd), [dcterms.xsd](https://github.com/viaacode/sipin-sip-validator/blob/main/app/resources/xsd/dcterms.xsd), [dcmitype.xsd](https://raw.githubusercontent.com/viaacode/sipin-sip-validator/main/app/resources/xsd/dcmitype.xsd), [dc.xsd](https://raw.githubusercontent.com/viaacode/sipin-sip-validator/main/app/resources/xsd/dc.xsd)_|

## Connecting the descriptive metadata to PREMIS

The `dc+schema.xml` file at the package-level contains descriptive metadata about the IE(s) of the SIP.
It relies on the [DCTERMS](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) and [SCHEMA](http://schema.org) metadata schema in order to facilitate a basic description with a limited number of descriptive metadata elements.

There is a link present between each `dc+schema.xml` file and the PREMIS Intellectual Entity in the `preservation/premis.xml` file via a shared ID.
This shared ID is stored in the `<dcterms:identifier>` element of each `dc+schema.xml` file and in a `<premis:objectIdentifier>` element of each PREMIS object in the `preservation/premis.xml` file.

Please note that additional IDs must be dealt with in the `preservation/premis.xml` file via `<premis:objectIdentifier>` elements in which the type of ID is specified using the `<premis:objectIdentifierType>` element.

***Example***

```xml
<?xml version='1.0' encoding='UTF-8'?>
<metadata xmlns="https://data.hetarchief.be/id/sip/2.1/basic" 
      xmlns:dcterms="http://purl.org/dc/terms/" 
      xmlns:xs="http://www.w3.org/2001/XMLSchema/" 
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xmlns:edtf="http://id.loc.gov/datatypes/edtf/">


  <!-- general title for the resource -->
  <dcterms:title xml:lang="nl">Felis Catus Flamens</dcterms:title>

  <!-- linking id between dc and premis -->
  <dcterms:identifier>uuid-b21a86aa-97a3-4f7b-a9f5-4d330af641c0</dcterms:identifier>

  <!-- date unknown -->
  <dcterms:created xsi:type="edtf:EDTF-level1">XXXX</dcterms:created>

  <!-- multiple keywords about the resource -->
  <dcterms:subject xml:lang="nl">Cat</dcterms:subject>
  <dcterms:subject xml:lang="nl">Felis Catus Flamens</dcterms:subject>


</metadata>   
```

## Use Cases

Some use cases that implement this profile are:

{% include _usecases.liquid  %}

---

[^1]: Unique language tag required
