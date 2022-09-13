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
│──manifest-md5.txt
│──bagit.txt
│
└──data
    │──mets.xml
    │──metadata
    |   |──descriptive
    |   |  └──dc.xml
    |   |  └──mods.xml
    |   └──preservation
    |       └──premis.xml
    │
    └──representations
        │──representation_1
        │    │──mets.xml
        │    │──data
        │    |   |──file_1.tiff
        │    │   └──...
        │    │
        │    └──metadata
        │        └──preservation
        │            └──premis.xml
        │
        │──representation_2
        │    │──mets.xml
        │    │──data
        │    |   |──file_1.xml
        │    │   └──...
        │    │
        │    └──metadata
        │       └──preservation
        │          └──premis.xml
        │
        └──representation_3
            │──mets.xml
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
- The newspaper edition MUST be digitised per page, i.e. each TIFF and/or ALTO XML file contained in their respective representation directories MUST represent exactly one page.
  - <a id="pdf"></a>An exception to this requirement MAY be made with regards to the PDF file: if a PDF file is present, it SHOULD contain the contents of the entire newspaper edition (i.e. all pages are present in one single PDF file).
- There MUST be exactly one IE present in the SIP, i.e. the newspaper edition.
- Preservation metadata in the SIP MUST be limited to the PREMIS metadata schema.
- There MUST be preservation metadata at the package level in the `preservation/premis.xml` file.
- There MUST be preservation metadata at the representation level in the respective `preservation/premis.xml` files.
- There MUST NOT be any descriptive metadata at the representation level.

### Package METS

- The `csip:CONTENTINFORMATIONTYPE` attribute MUST be set to `https://data.hetarchief.be/id/sip/1.0/newspaper`.

### Package Descriptive Metadata

- A descriptive metadata file `descriptive/mods.xml` MUST be present at the package level.
- A descriptive metadata file `descriptive/dc.xml` MAY be present at the package level.
- The `descriptive/mods.xml` file MUST follow the [MODS](https://www.loc.gov/standards/mods/v3/mods-3-7.xsd) metadata schema (v3.7.).
- The `descriptive/dc.xml` file MUST follow the [DCTERMS](https://www.dublincore.org/schemas/xmls/qdc/dcterms.xsd) metadata schema.
- The `descriptive/mods.xml` file MUST contain a shared identifier with the `preservation/premis.xml` to indicate which PREMIS object is being described in the `descriptive/mods.xml` file.
- If present, the `descriptive/dc.xml` file MUST contain a shared identifier with the `preservation/premis.xml` to indicate which PREMIS object is being described in the `descriptive/dc.xml` file.
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
| Description | This element contains the title of the newspaper.<br>Its parent element (`<mods:titleInfo/>`) MUST NOT contain any attributes in order to differentiate from other optional `<mods:titleInfo/>` elements which, if present, MUST contain `@type` attributes to indicate e.g. alternative titles for the newspaper. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:identifier[not(@*)]` |
|-----------------------|-----------|
| Name | MODS identifier element |
| Description | A unique identifier for the newspaper edition.<br>This identifier MUST be shared with the relevant PREMIS object in the `preservation/premis.xml` file.<br>This metadata element MUST NOT contain any attributes.  |
| Datatype | [ID]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#id) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:typeOfResource` |
|-----------------------|-----------|
| Name | MODS type of resource element |
| Description | This element indicates which type of resource is being described. Its value MUST be set to `newspaper edition`. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:originInfo/mods:dateIssued[@encoding="edtf"]` |
|-----------------------|-----------|
| Name | MODS issuance date element |
| Description | This element contains the date the newspaper edition was issued. Its value MUST be EDTF-compliant, as indicated by the `@encoding` attribute which MUST be set to `edtf`.  |
| Datatype | [EDTF]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#edtf) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:relatedItem[@type="series"]/mods:identifier[@type="abraham_id"]` |
|-----------------------|-----------|
| Name | Abraham ID |
| Description | This element contains the Abraham identifier taken from the [Abraham Belgian Newspaper Catalog](https://krantencatalogus.be). Note that an Abraham identifier refers to newspaper titles rather than newspaper editions; multiple editions can therefore share the same Abraham identifier.<br><br>This element MUST contain the `@type` attribute, with its value set to `abraham_id`. The `@type` attribute of its parent element (i.e. `<mets:relatedItem/>`) MUST be set to `series`. |
| Datatype | [ID]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#id) |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Element | `mods:mods/mods:relatedItem[@type="series"]/mods:identifier[@type="abraham_uri"]` |
|-----------------------|-----------|
| Name | Abraham URI |
| Description | This element contains the Abraham URI taken from the [Abraham Belgian Newspaper Catalog](https://krantencatalogus.be). Note that an Abraham URI refers to newspaper titles rather than newspaper editions; multiple editions can therefore share the same Abraham URI.<br><br>This element MUST contain the `@type` attribute, with its value set to `abraham_uri`. The `@type` attribute of its parent element (i.e. `<mets:relatedItem/>`) MUST be set to `series`. Note that the Abraham URI contains the Abraham identifier. |
| Datatype | [URI]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#uri) |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Element | `mods:mods/mods:note[@type="license"]` |
|-----------------------|-----------|
| Name | License element |
| Description | This element MAY be used to add any licensing info needed. It MUST contain the `@type` attribute, with its value set to `license`. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | MAY |

### Package Preservation Metadata

- A preservation metadata file `preservation/premis.xml` MUST be present at the package level.
- The `preservation/premis.xml` file MUST follow the [PREMIS](https://www.loc.gov/standards/premis/v3/premis-v3-0.xsd) metadata schema (v3.0.).
- If the SIP contains ALTO XML files, the `preservation/premis.xml` file MUST contain a PREMIS event of type `transcription` to link the TIFF and ALTO XML files. See the example below for more information.
- If the SIP contains a PDF file (which SHOULD contain all pages of the newspaper edition, cf. [supra](#pdf), the `preservation/premis.xml` file MUST contain a PREMIS event of type `creation` to link the TIFF and ALTO XML files to the PDF file. See the example below for more information.

Example of a PREMIS transcription event (linking the TIFF and ALTO XML files):

```xml
<premis:event>
    <premis:eventIdentifier>
      <premis:eventIdentifierType>UUID</premis:eventIdentifierType>
      <premis:eventIdentifierValue>uuid-34ae79f8-a8e7-4768-a269-4d6d895662d6</premis:eventIdentifierValue>
    </premis:eventIdentifier>
    <premis:eventType>transcription</premis:eventType>
    <premis:eventDateTime>2022-02-16T10:01:15.014+02:00</premis:eventDateTime>
    <premis:eventDetailInformation>
      <premis:eventDetail>Generate ALTO XML from TIFF via OCR</premis:eventDetail>
    </premis:eventDetailInformation>
    <premis:linkingObjectIdentifier>
      <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
      <premis:linkingObjectIdentifierValue>uuid-d8fd6dde-53a5-4614-823c-32f64588efe6</premis:linkingObjectIdentifierValue>
      <premis:linkingObjectRole>source</premis:linkingObjectRole>
    </premis:linkingObjectIdentifier>
    <premis:linkingObjectIdentifier>
      <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
      <premis:linkingObjectIdentifierValue>uuid-1fca6190-a4bd-4773-8529-272b9e7d536a</premis:linkingObjectIdentifierValue>
      <premis:linkingObjectRole>outcome</premis:linkingObjectRole>
    </premis:linkingObjectIdentifier>
  </premis:event>
```

Example of a PREMIS creation event (linking the TIFF, ALTO XML and PDF files):

```xml
<premis:event>
    <premis:eventIdentifier>
      <premis:eventIdentifierType>UUID</premis:eventIdentifierType>
      <premis:eventIdentifierValue>uuid-16a5c827-e513-4ec5-ad75-f75c7b9bde1f</premis:eventIdentifierValue>
    </premis:eventIdentifier>
    <premis:eventType>creation</premis:eventType>
    <premis:eventDateTime>2022-02-16T10:01:15.014+02:00</premis:eventDateTime>
    <premis:eventDetailInformation>
      <premis:eventDetail>Generate PDF from ALTO XML and TIFF</premis:eventDetail>
    </premis:eventDetailInformation>
    <premis:linkingObjectIdentifier>
      <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
      <premis:linkingObjectIdentifierValue>uuid-d8fd6dde-53a5-4614-823c-32f64588efe6</premis:linkingObjectIdentifierValue>
      <premis:linkingObjectRole>source</premis:linkingObjectRole>
    </premis:linkingObjectIdentifier>
    <premis:linkingObjectIdentifier>
      <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
      <premis:linkingObjectIdentifierValue>uuid-1fca6190-a4bd-4773-8529-272b9e7d536a</premis:linkingObjectIdentifierValue>
      <premis:linkingObjectRole>source</premis:linkingObjectRole>
    </premis:linkingObjectIdentifier>
    <premis:linkingObjectIdentifier>
      <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
      <premis:linkingObjectIdentifierValue>uuid-3d371b39-90af-4655-91e9-d93c55f25da1</premis:linkingObjectIdentifierValue>
      <premis:linkingObjectRole>outcome</premis:linkingObjectRole>
    </premis:linkingObjectIdentifier>
  </premis:event>
```

### Representation METS

### Representation Preservation Metadata

## Use Cases

Some use cases that implement this profile are:

{% for page in site.pages %}
{% if page.sip_profile == "newspaper" %}
- [{{ page.title }}]({{ page.url }})
{% endif %}
{% endfor %}