---
layout:       default
title:        Newspaper
parent:       Profiles
nav_order:    2
nav_exclude:  false
---
# Profile: Newspaper 

The newspaper profile supports the ingest of digitised newspaper content.
It is an extension of the generic SIP specification and it shows how to deal with multiple media files (in formats such as TIFF, ALTO XML and PDF) and the relationships between them and their metadata.
It also allows to use the [MODS metadata schema](https://www.loc.gov/standards/mods/) for descriptive metadata, which is the default for describing newspaper content.

**Permalink:** <https://data.hetarchief.be/id/sip/1.0/newspaper>

**Example Directory structure:**

```plaintext
root_directory
│── manifest-md5.txt
│── bagit.txt
│
└── data
    │── mets.xml
    │── metadata
    |   |── descriptive
    |   |   └── dc.xml
    |   |   └── mods.xml
    |   └── preservation
    |       └── premis.xml
    │
    └── representations
        │──representation_1
        │   │── mets.xml
        │   │──data
        │   |  |── file_1.tiff
        │   │  └── ...
        │   │
        │   └──metadata
        │      └──preservation
        │         └── premis.xml
        │
        │──representation_2
        │    │── mets.xml
        │    │──data
        │    |  |── file_1.xml
        │    │  └── ...
        │    │
        │    └──metadata
        │       └──preservation
        │          └── premis.xml
        │
        └──representation_3
            │── mets.xml
            │──data
            |  └── file_1.pdf
            │
            └──metadata
               └──preservation
                  └── premis.xml
```

## Requirements

### General

- A newspaper SIP MUST contain exactly one newspaper edition.
- There MUST be exactly one IE, i.e. the newspaper edition.
- There MUST NOT be any descriptive metadata at the representation level.

### Package METS

- The `csip:CONTENTINFORMATIONTYPE` attribute MUST be set to `https://data.hetarchief.be/id/sip/1.0/newspaper`.

### Package Descriptive Metadata

- A descriptive metadata file `descriptive/mods.xml` MUST be present at the package level.
- A descriptive metadata file `descriptive/dc.xml` MAY be present at the package level.
- The `descriptive/mods.xml` file MUST follow the [MODS](https://www.loc.gov/standards/mods/v3/mods-3-7.xsd) metadata schema (v3.7.).
- The `descriptive/dc.xml` file MUST follow the [DCTERMS](https://www.dublincore.org/schemas/xmls/qdc/dcterms.xsd) metadata schema.
- The `descriptive/mods.xml` file MUST contain a shared identifier with the `preservation/premis.xml` to indicate which PREMIS object is being described in the `descriptive/mods.xml` file.
- The `descriptive/mods.xml` file MUST minimally implement the MODS metadata elements outlined below.

| Element | `mods:mods` |
|-----------------------|-----------|
| Name | MODS root element |
| Description | This root element MUST contain the XML schema namespace of [MODS](http://www.loc.gov/mods/v3).<br>It MUST NOT contain any other XML schema namespaces besides MODS. |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mods:mods/@version` |
|-----------------------|-----------|
| Name | MODS version attribute |
| Description | This attribute indicates which version of MODS is being used.<br>It MUST be set to `3.7` to indicate conformance with MODS v3.7. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:titleInfo[not(@*)]/mods:title` |
|-----------------------|-----------|
| Name | MODS title element |
| Description |  |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:identifier[not(@*)]` |
|-----------------------|-----------|
| Name | MODS identifier element |
| Description |  |
| Datatype | [ID]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#id) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:typeOfResource` |
|-----------------------|-----------|
| Name | MODS type of resource element |
| Description |  |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:originInfo/mods:dateIssued[@encoding="edtf"]` |
|-----------------------|-----------|
| Name | MODS issuance date element |
| Description |  |
| Datatype | [EDTF]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#edtf) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:relatedItem[@type="series"]/mods:identifier[@type="abraham_id"]` |
|-----------------------|-----------|
| Name | Abraham ID |
| Description | This element contains the Abraham identifier taken from the [Abraham Belgian Newspaper Catalog](https://krantencatalogus.be). Note that an Abraham identifier refers to newspaper titles rather than newspaper editions; multiple editions can therefore share the same Abraham identifier.<br><br>This element MUST contain the `@type` attribute, with its value set to `abraham_id`. The `@type` attribute of its parent element (i.e. `mets:relatedItem`) MUST be set to `series`. |
| Datatype | [ID]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#id) |
| Cardinality | 1..1 |
| Obligation | SHOULD |

| Element | `mods:mods/mods:relatedItem[@type="series"]/mods:identifier[@type="abraham_uri"]` |
|-----------------------|-----------|
| Name | Abraham URI |
| Description |  |
| Datatype | [URI]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#uri) |
| Cardinality | 1..1 |
| Obligation | SHOULD |

| Element | `mods:mods/mods:note[@type="license"]` |
|-----------------------|-----------|
| Name | License element |
| Description | This element MAY be used to add any licensing info needed. It MUST contain the `@type` attribute, with its value set to `license`. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | MAY |

### Package Preservation Metadata

### Representation METS

### Representation Preservation Metadata

## Use Cases