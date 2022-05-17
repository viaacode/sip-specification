---
layout:       default
title:        Representation level
parent:       SIP Structure
nav_order:    7
nav_exclude:  false
---
Status: WIP
{: .label .label-yellow }
# Representation level
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

The representation level consists of at least one `/representation_*` directory (where `*` is a positive integer).
Each `/representation_*` directory contains information about the representation of (one of) the (sub-)IE(s) of the package level, together with the media files making up the representation.

***Example***

```plaintext
root_directory
│   ...
│
└──data
   │   ...
   │
   └──representations
      │
      └──representation_1
      │  │   mets.xml
      │  │
      │  └──data
      │  │  │   ...
      │  │
      │  └──metadata
      │     │
      │     └──descriptive
      │     │  │   ...
      │     │
      │     └──preservation
      │        │   ...
      │
      │
      │
      └──representation_*
         │   ...
```

## /representation_* (directory)

A `/representation_*` directory consists of at least a `mets.xml` file, a `/data` directory and a `/metadata` directory.
It contains both descriptive and preservation metadata, as well as the actual media files making up a certain representation of the (sub-)IE(s) of the SIP.

Each `/representation_*` directory contains its own `mets.xml` file which acts similarly as the package `mets.xml` and serves as an inventory of the files and directories of the representation level.

A `/representation_*` directory may contain a `/documentation` and a `/schemas` directory. 
The former may contain additional information aiding the interpretation of the representation, while the latter may contain XML Schema Definition (XSD) files of the metadata schemas used in the representation.
These two directories are ignored during ingest and will therefore not be archived.

***Requirements***

- A `/representation_*` directory MUST contain exactly one `mets.xml` file.
- A `/representation_*` directory MUST contain exactly one `/metadata` directory.
- A `/representation_*` directory MUST contain exactly one `/data` directory.
- A `/representation_*` directory MAY contain exactly one `/documentation` directory.
- A `/representation_*` directory MAY contain exactly one `/schemas` directory.

## mets.xml (file)

The `mets.xml` file at the representation level (also known as the representation mets) generally follows the same structure and requirements as the package mets discussed in the section [package mets.xml](./5_structure_package.html#metsxml-file).
Since the `dmdSec`, `amdSec`, `fileSec` and `structMap` sections follow the same requirements, where possible, as the package `mets.xml` file, this section only lists requirements regarding the `mets` and `metsHdr` sections.

### \<mets\> section

***Example***

```xml
<?xml version="1.0"?>
<mets xmlns="http://www.loc.gov/METS/"
      xmlns:csip="https://DILCIS.eu/XML/METS/CSIPExtensionMETS"
      xmlns:sip="https://DILCIS.eu/XML/METS/SIPExtensionMETS"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xmlns:xlink="http://www.w3.org/1999/xlink"
      OBJID="uuid-08dd6a01-19a3-44e2-88fa-702a97f8b83f"
      TYPE="Photographs – Digital"
      PROFILE="https://earksip.dilcis.eu/profile/E-ARK-SIP.xml">

<metsHdr>...</metsHdr>
<dmdSec>...</dmdSec>
<amdSec>...</amdSec>
<fileSec>...</fileSec>
<structMap>...</structMap>

</mets>
```

***Requirements***

| Element | `mets` |
|-----------------------|-----------|
| Name | METS root element |
| Description | This is the root element of the representation METS.<br>It MUST contain the following XML schema namespaces:<br>[`mets: http://www.loc.gov/METS/`](http://www.loc.gov/METS/)<br>[`csip: https://dilcis.eu/XML/METS/CSIPExtensionMETS`](https://dilcis.eu/XML/METS/CSIPExtensionMETS)<br>[`sip: https://dilcis.eu/XML/METS/SIPExtensionMETS`](https://dilcis.eu/XML/METS/SIPExtensionMETS)<br>[`xsi: http://www.w3.org/2001/XMLSchema-instance`](http://www.w3.org/2001/XMLSchema-instance)<br>[`xlink: http://www.w3.org/1999/xlink`](http://www.w3.org/1999/xlink)|
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/@OBJID` |
|-----------------------|-----------|
| Name | Representation identifier |
| Description | This is an identifier for the METS document. For the representation METS, this MUST be the same name as the one used for the corresponding representation directory. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/@TYPE` |
|-----------------------|-----------|
| Name | Content category |
| Description | This attribute MUST be set to declare the category of the content held in the representation directory. |
| Datatype | String; fixed vocabulary |
| Vocabulary | `Textual works - Print`<br>`Textual works - Digital`<br>`Textual works - Electronic Serials`<br>`Photographs - Print`<br>`Photographs - Digital`<br>`Other Graphic Images - Print`<br>`Other Graphic Images - Digital`<br>`Audio - On Tangible Medium (digital or analog)`<br>`Audio - Media-independent (digital)`<br>`Motion Pictures – Digital and Physical Media`<br>`Video – File-based and Physical Media`<br>`Collection`<br>`Physical object`<br>`Mixed`<br>`OTHER` |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets[@TYPE="OTHER"]/@csip:OTHERTYPE` |
|-----------------------|-----------|
| Name | Other content category |
| Description | When the `mets/@TYPE` attribute is set to `OTHER`, the `mets/@csip:OTHERTYPE` attribute SHOULD be used to declare the content category of the representation not contained in the fixed vocabulary of the `@TYPE` attribute. |
| Datatype | String |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Attribute | `mets/@PROFILE` |
|-----------------------|-----------|
| Name | METS profile |
| Description | The URL of the E-ARK METS profile that the SIP conforms with.<br>This URL MUST be set to [`https://earksip.dilcis.eu/profile/E-ARK-SIP.xml`](https://earksip.dilcis.eu/profile/E-ARK-SIP.xml) to indicate conformance with the E-ARK specification. |
| Datatype | URL |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/@LABEL` |
|-----------------------|-----------|
| Name | Package name |
| Description | An optional short text describing the contents of the representation. |
| Datatype | String |
| Cardinality | 0..1 |
| Obligation | MAY |

### \<metsHdr\> section

***Example***

```xml
<metsHdr CREATEDATE="2022-02-16T10:02:37.009+02:00"/>
```

***Requirements***

| Element | `mets/metsHdr` |
|-----------------------|-----------|
| Name | Representation header |
| Description | General element that contains descriptive information about the representation. |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/metsHdr/@CREATEDATE` |
|-----------------------|-----------|
| Name | Representation creation datetime |
| Description | This attribute records the date and time the representation was created. |
| Datatype | EDTF |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/metsHdr/@LASTMODDATE` |
|-----------------------|-----------|
| Name | Representation last modification datetime |
| Description | In case the representation was modified since its creation, this attribute records the date and time of that modification.<br>This attribute MUST be present and used when the representation has been modified since its creation datetime. |
| Datatype | EDTF |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Attribute | `mets/metsHdr/@RECORDSTATUS` |
|-----------------------|-----------|
| Name | Representation status |
| Description | A way of indicating the status of the representation and to instruct meemoo on how to properly handle it.<br>If not set, the expected value is `NEW`.<br>Meemoo investigates the use of the `@RECORDSTATUS` attribute for future use cases such as e.g. a metadata update (i.e. ingest of metadata only with the goal of updating, adding or deleting existing metadata in meemoo's archive system). |
| Datatype | String; fixed vocabulary |
| Vocabulary | `NEW`<br>`SUPPLEMENT`<br>`REPLACEMENT`<br>`TEST`<br>`VERSION`<br>`DELETE`<br>`OTHER` |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `mets/metsHdr/agent` |
|-----------------------|-----------|
| Name | Agent |
| Cardinality | 0..* |
| Obligation | MAY |

| Attribute | `mets/metsHdr/agent/@ROLE` |
|-----------------------|-----------|
| Name | Agent role |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/metsHdr/agent/@TYPE` |
|-----------------------|-----------|
| Name | Agent type |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/metsHdr/agent/@OTHERTYPE` |
|-----------------------|-----------|
| Name | Agent other type |
| Description | This attribute MUST be used if the attribute `agent/@TYPE` is set to `OTHER`. It is used to specify the exact other type that is being used. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/metsHdr/agent/name` |
|-----------------------|-----------|
| Name | Agent name |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/metsHdr/agent/note` |
|-----------------------|-----------|
| Name | Agent additional information |
| Datatype | String |
| Cardinality | 0..1 |
| Obligation | MAY |

## /data (directory)

The `/data` directory contains the media files of a specific representation of the SIP.
Depending on the use-case and the CP, these files can be digital pictures, video, audio...

***Requirements***

- The `/data` directory MUST NOT contain any subdirectories.
- All files in the `/data` directory MUST be referenced in the corresponding representation `mets.xml` file.

## /metadata (directory)

The `/metadata` directory contains both descriptive and preservation metadata about the representation and the media files at the representation level.

***Requirements***

- The `/metadata` directory MUST contain exactly two subdirectories: `/descriptive` and `/preservation`.

### /descriptive (directory)

The `/descriptive` directory contains descriptive metadata about the representation.

***Requirements***

- The `/descriptive` directory MAY contain exactly one file: `descriptive.xml`.

The `descriptive.xml` file at the representation level contains descriptive metadata about a specific representation of the SIP.

Descriptive metadata about the representation is put into a separate `<premis:object>` element with a unique identifier.
The link between the `<premis:object>` element in the descriptive metadata and the `<premis:object>` element in the preservation metadata (in the `preservation.xml` in `/data/representations/representation_*/metadata/preservation`) is made using a shared UUID in the `<premis:objectIdentifier>` elements of both files.

***Example***

```xml
<?xml version='1.0' encoding='UTF-8'?>
<premis:premis xmlns:dcterms="http://purl.org/dc/terms/" xmlns:premis="http://www.loc.gov/premis/v3" xmlns:xs="http://www.w3.org/2001/XMLSchema/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance/">

  <premis:object>
    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-541292c3-223a-4b80-b747-66bc86ff4a89</premis:objectIdentifierValue>
    </premis:objectIdentifier>
    <!-- general title for the representation -->
    <dcterms:title>Colour representation of the Felis Catus Flamens lying on a sofa</dcterms:title>

    <!-- id for the FCF in an imaginary cat database -->
    <dcterms:identifier>FCatus_FelisCatusFlamens_Sofa_01_001</dcterms:identifier>

    <!-- date when representation was created -->
    <dcterms:created xsi:type="edtf">2022-01~</dcterms:created>

    <!-- multiple keywords about the representation -->
    <dcterms:subject>Cat</dcterms:subject>
    <dcterms:subject>Felis Catus Flamens</dcterms:subject>
    <dcterms:subject>Sofa</dcterms:subject>
  </premis:object>

</premis:premis> 
```

***Requirements***

The `descriptive.xml` of the representation level follows the same requirements regarding metadata elements of the `descriptive.xml` file discussed in the [/descriptive section](./5_structure_package.html#descriptive-directory) of the package level.
Additional requirements are discussed below:

- The `descriptive.xml` file MUST embed the descriptive metadata about the representation in a `<premis:object/>` element.

### /preservation (directory)

The `/preservation` directory contains preservation metadata about the representation and the media files.

***Requirements***

- The `/preservation` directory MUST contain exactly one file: `preservation.xml`.

The `preservation.xml` file of the representation level contains preservation metadata about the representation and the media files of the representation level.
It relies on the [Preservation Metadata: Implementation Strategies (PREMIS)](https://www.loc.gov/standards/premis/) standard in order to provide basic preservation information such as checksums.
More detailed preservation information can be described using PREMIS events and PREMIS agents.

***Example***

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3">

  <premis:object>
    <premis:objectCategory>representation</premis:objectCategory>

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-541292c3-223a-4b80-b747-66bc86ff4a89</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship between representation and its files -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/inc">includes</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-bd610fa4-077c-40cc-a278-74220df0a0c1</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-950ea040-5e79-4223-b804-b76660ec7e85</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship between representation and its IE/subIE -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/rep">represents</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-948e2213-ca54-459c-8c87-5818adeb9444</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>
  </premis:object>

  <premis:object>
    <premis:objectCategory>file</premis:objectCategory>

    <premis:originalName>data/1445.jpeg</premis:originalName>

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-bd610fa4-077c-40cc-a278-74220df0a0c1</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:objectCharacteristics>
      <premis:fixity>
        <premis:messageDigestAlgorithm authority="cryptographicHashFunctions" authorityURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions" valueURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5">
                MD5
        </premis:messageDigestAlgorithm>
        <premis:messageDigest>b7ae37f6094794e313402b9d064978e8</premis:messageDigest>
      </premis:fixity>
    </premis:objectCharacteristics>

    <!-- relationship between file and its representation -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isi">is included in</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-541292c3-223a-4b80-b747-66bc86ff4a89</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>

  <premis:object>
    <premis:objectCategory>file</premis:objectCategory>

    <premis:originalName>data/1450.jpeg</premis:originalName>

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-950ea040-5e79-4223-b804-b76660ec7e85</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:objectCharacteristics>
      <premis:fixity>
        <premis:messageDigestAlgorithm authority="cryptographicHashFunctions" authorityURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions" valueURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5">
                MD5
        </premis:messageDigestAlgorithm>
        <premis:messageDigest>d4985ba4b67ff067a0e84c53b6d35355</premis:messageDigest>
      </premis:fixity>
    </premis:objectCharacteristics>

    <!-- relationship between file and its representation -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isi">is included in</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-541292c3-223a-4b80-b747-66bc86ff4a89</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>

</premis:premis>
```

***Requirements***

- The `preservation.xml` file MUST contain a PREMIS object for the representation.
- The `preservation.xml` file MUST contain a PREMIS object for each media file in the `/data` directory.
- Each PREMIS object MUST contain a unique identifier.
- Each PREMIS object with the value set to `FILE` MUST contain a checksum.
- The `preservation.xml` file SHOULD contain PREMIS events detailing, a.o., the creation and each modification of the representation and the media files.

<small>
Continue to [Content Profiles]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/profiles/index.md %}).
</small>