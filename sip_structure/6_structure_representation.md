---
layout:       default
title:        Representation level
parent:       Structure
grand_parent:  SIP Specification 1.0
nav_order:    7
nav_exclude:  false
---
# Representation level
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

The representation level consists of at least one `/representation_*` directory (where `*` is a positive integer increasing by 1 for each additional representation).
Each `/representation_*` directory contains information about the representation of (one of) the IE(s) of the package level, together with the media files making up the representation.

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
      │  │── mets.xml
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
It contains both descriptive and preservation metadata, as well as the actual media files making up a certain representation of the IE(s) of the SIP.

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
      OBJID="representation_1"
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
| Description | This is an ID for the METS document. For the representation METS, this MUST be the same name as the one used for the corresponding representation directory. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/@TYPE` |
|-----------------------|-----------|
| Name | Content category |
| Description | This attribute MUST be set to declare the category of the content held in the representation directory. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string); fixed vocabulary |
| Vocabulary | `Textual works - Print`<br>`Textual works - Digital`<br>`Textual works - Electronic Serials`<br>`Photographs - Print`<br>`Photographs - Digital`<br>`Other Graphic Images - Print`<br>`Other Graphic Images - Digital`<br>`Audio - On Tangible Medium (digital or analog)`<br>`Audio - Media-independent (digital)`<br>`Motion Pictures – Digital and Physical Media`<br>`Video – File-based and Physical Media`<br>`Collection`<br>`Physical object`<br>`Mixed`<br>`OTHER` |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets[@TYPE="OTHER"]/@csip:OTHERTYPE` |
|-----------------------|-----------|
| Name | Other content category |
| Description | When the `mets/@TYPE` attribute is set to `OTHER`, the `mets/@csip:OTHERTYPE` attribute SHOULD be used to declare the content category of the representation not contained in the fixed vocabulary of the `@TYPE` attribute. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Attribute | `mets/@PROFILE` |
|-----------------------|-----------|
| Name | METS profile |
| Description | The URL of the E-ARK METS profile that the SIP conforms with.<br>This URL MUST be set to [`https://earksip.dilcis.eu/profile/E-ARK-SIP.xml`](https://earksip.dilcis.eu/profile/E-ARK-SIP.xml) to indicate conformance with the E-ARK specification. |
| Datatype | [URL]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#url) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/@LABEL` |
|-----------------------|-----------|
| Name | Package name |
| Description | An optional short text describing the contents of the representation. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
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
| Datatype | [XML Schema datetime]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#xsd-datetime) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/metsHdr/@LASTMODDATE` |
|-----------------------|-----------|
| Name | Representation last modification datetime |
| Description | In case the representation was modified since its creation, this attribute records the date and time of that modification.<br>This attribute MUST be present and used when the representation has been modified since its creation datetime. |
| Datatype | [XML Schema datetime]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#xsd-datetime) |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Attribute | `mets/metsHdr/@RECORDSTATUS` |
|-----------------------|-----------|
| Name | Representation status |
| Description | A way of indicating the status of the representation and to instruct meemoo on how to properly handle it.<br>If not set, the expected value is `NEW`.<br>Meemoo investigates the use of the `@RECORDSTATUS` attribute for future use cases such as e.g. a metadata update (i.e. ingest of metadata only with the goal of updating, adding or deleting existing metadata in meemoo's archive system). |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string); fixed vocabulary |
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
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/metsHdr/agent/@TYPE` |
|-----------------------|-----------|
| Name | Agent type |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/metsHdr/agent/@OTHERTYPE` |
|-----------------------|-----------|
| Name | Agent other type |
| Description | This attribute MUST be used if the attribute `agent/@TYPE` is set to `OTHER`. It is used to specify the exact other type that is being used. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/metsHdr/agent/name` |
|-----------------------|-----------|
| Name | Agent name |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/metsHdr/agent/note` |
|-----------------------|-----------|
| Name | Agent additional information |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
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

- The `/descriptive` directory MAY contain zero or more `dc*.xml` metadata files.

The `dc*.xml` files at the representation level contains descriptive metadata about a specific representation of the SIP.

***Example***

```xml
<?xml version='1.0' encoding='UTF-8'?>
<metadata xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xs="http://www.w3.org/2001/XMLSchema/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance/">

  <!-- general title for the representation -->
  <dcterms:title>Colour representation of the Felis Catus Flamens lying on a sofa</dcterms:title>

  <!-- linking id between dc and premis -->
  <dcterms:identifier>uuid-541292c3-223a-4b80-b747-66bc86ff4a89</dcterms:identifier>

  <!-- date when representation was created -->
  <dcterms:created xsi:type="edtf">2022-01~</dcterms:created>

  <!-- multiple keywords about the representation -->
  <dcterms:subject>Cat</dcterms:subject>
  <dcterms:subject>Felis Catus Flamens</dcterms:subject>
  <dcterms:subject>Sofa</dcterms:subject>

</metadata> 
```

***Requirements***

The `dc*.xml` files of the representation level follows the same requirements regarding metadata elements of the `dc*.xml` files discussed in the [/descriptive section](./5_structure_package.html#descriptive-directory) of the package level.

### /preservation (directory)

The `/preservation` directory contains preservation metadata about the representation and the media files.

***Requirements***

- The `/preservation` directory MUST contain exactly one file: `premis.xml`.

The `premis.xml` file of the representation level contains preservation metadata about the representation and the media files of the representation level.
It relies on the [PREMIS](https://www.loc.gov/standards/premis/) standard in order to provide basic preservation information such as checksums.
More detailed preservation information can be described using PREMIS events and PREMIS agents.

***Example***

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

  <premis:object xsi:type="premis:representation">

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

    <!-- relationship between representation and its IE -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/rep">represents</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-948e2213-ca54-459c-8c87-5818adeb9444</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>
  </premis:object>

  <premis:object xsi:type="premis:file">

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
      <premis:size>721603</premis:size>
      <premis:format>
        <premis:formatRegistry>
          <premis:formatRegistryName>PRONOM</premis:formatRegistryName>
          <premis:formatRegistryKey>fmt-1507</premis:formatRegistryKey>
          <premis:formatRegistryRole authority="http://id.loc.gov/vocabulary/preservation/formatRegistryRole" valueURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole/spe">specification</premis:formatRegistryRole>
        </premis:formatRegistry>
      </premis:format>
    </premis:objectCharacteristics>

    <premis:originalName>1445.jpeg</premis:originalName>

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

  <premis:object xsi:type="premis:file">

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
      <premis:size>738611</premis:size>
      <premis:format>
        <premis:formatRegistry>
          <premis:formatRegistryName>PRONOM</premis:formatRegistryName>
          <premis:formatRegistryKey>fmt-1507</premis:formatRegistryKey>
          <premis:formatRegistryRole authority="http://id.loc.gov/vocabulary/preservation/formatRegistryRole" valueURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole/spe">specification</premis:formatRegistryRole>
        </premis:formatRegistry>
      </premis:format>
    </premis:objectCharacteristics>

    <premis:originalName>1450.jpeg</premis:originalName>

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

***Overview of relevant PREMIS relationships***

On the representation level, the preservation metadata is used to express 
- what the representations and files are that are contained in the SIP; and 
- how they relate to eachother or to IEs described on the package level. 

The table below gives an overview of the different relationship types that can be used on the representation level:

| Direction | Relationship type | Relationship subtype | Reciprocal/inverse relationship | Description |
|-------------------|----------------------|---------------------------------|-------------|
| From Representation to IE | [`structural`](http://id.loc.gov/vocabulary/preservation/relationshipType/str) | [`represents`](http://id.loc.gov/vocabulary/preservation/relationshipSubType/rep) | [`is represented by`](http://id.loc.gov/vocabulary/preservation/relationshipSubType/isr) | A representation represents a specific IE |
| From Representation to File | [`structural`](http://id.loc.gov/vocabulary/preservation/relationshipType/str) | [`includes`](http://id.loc.gov/vocabulary/preservation/relationshipSubType/inc) | [`is included in`](http://id.loc.gov/vocabulary/preservation/relationshipSubType/isi) | A representation includes one or more file objects |
| From File to Representation | [`structural`](http://id.loc.gov/vocabulary/preservation/relationshipType/str) | [`is included in`](http://id.loc.gov/vocabulary/preservation/relationshipSubType/isi) | [`includes`](http://id.loc.gov/vocabulary/preservation/relationshipSubType/inc) | A file is included in a representation |

***Requirements***

| Element | `premis:premis` |
|-----------------------|-----------|
| Name | PREMIS root element |
| Description | This is the root element of the PREMIS file.<br><br>It MUST contain the following XML schema namespaces: <br>[`xsi: http://www.w3.org/2001/XMLSchema-instance`](http://www.w3.org/2001/XMLSchema-instance)<br>[`premis: http://www.loc.gov/premis/v3`](http://www.loc.gov/premis/v3).|
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `premis:premis/@version` |
|-----------------------|-----------|
| Name | PREMIS version attribute |
| Description | This attribute signals which PREMIS version is being used.<br>The attribute's value MUST be set to `3.0`. |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `premis:premis@/xsi:schemaLocation` |
|-----------------------|-----------|
| Name | Schema location declaration |
| Description | This attribute signals where to find the relevant XSD schema in order to validate the PREMIS file.<br><br>When used, its value MUST be set to `"http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd"` to signal conformance with PREMIS 3.0.|
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Element | `premis:premis/premis:object` |
|-----------------------|-----------|
| Name | PREMIS object |
| Description | A `premis:object` element MUST be defined for each representation and file of the representation level in the SIP. |
| Cardinality | 1..* |
| Obligation | MUST |

| Attribute | `premis:premis/premis:object/@xsi:type` |
|-----------------------|-----------|
| Name | Object type |
| Description | This attribute signals whether a PREMIS object is of type intellectual entity, representation or file.<br><br>In the case of the `premis.xml` file of the representation level, this attribute's value MUST be set to `premis:representation` in the case of a representation object, and to `premis:file` in the case of a file object. |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object/premis:objectIdentifier` |
|-----------------------|-----------|
| Name | Object identifier |
| Description | This element contains object identifier information.<br><br>At least one object identifier MUST be present to uniquely identify the concerned representation or file, and to establish a link between the relevant preservation metadata in the `premis.xml` file and the descriptive metadata in the `dc*.xml` file, if any is present. |
| Cardinality | 1..* |
| Obligation | MUST |

| Element | `premis:premis/premis:object/premis:objectIdentifier/premis:objectIdentifierType` |
|-----------------------|-----------|
| Name | Object identifier type |
| Description | The type of the PREMIS object identifier being used.<br><br>At least one identifier of type ID MUST be defined in order to provide a unique identifier for each PREMIS object.<br><br>This unique identifier is also used to link the concerned PREMIS object with the descriptive metadata in the `/metadata/descriptive/dc*.xml` file, if any is present. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string); fixed vocabulary (e.g. [`PREMIS standard identifiers`](https://id.loc.gov/vocabulary/identifiers.html)) |
| Vocabulary | `local`<br>`ID`<br>`UUID`<br>... |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object/premis:objectIdentifier/premis:objectIdentifierValue` |
|-----------------------|-----------|
| Name | Object identifier value |
| Description | The actual value that makes up the identifier of the PREMIS object. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) (depending on the value of the `premis:objectIdentifierType`) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object/premis:relationship` |
|-----------------------|-----------|
| Name | PREMIS relationship |
| Description | Information about a relationship between the current object and one or more other objects.<br><br> In the case of the `premis.xml` file of the representation level, this element MUST detail the relationships between the representation and IE on the one hand, and between the representation and file(s) on the other hand.|
| Cardinality | 1..* |
| Obligation | MUST |

| Element | `premis:premis/premis:object/premis:relationship/premis:relationshipType` |
|-----------------------|-----------|
| Name | Relationship type |
| Description | A high-level categorization of the nature of the relationship.<br><br>In the case of the `premis.xml` file of the representation level, this element's value MUST be set to `structural`.|
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 1..* |
| Obligation | MUST |

| Attribute | `premis:premis/premis:object/premis:relationship/premis:relationshipType/@authority` |
|-----------------------|-----------|
| Name | Relationship type authority attribute |
| Description | This attribute indicates the name of the authority/controlled vocabulary that is being used for the different relationship types. Its value MUST be set to `"relationshipType"`. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `premis:premis/premis:object/premis:relationship/premis:relationshipType/@authorityURI` |
|-----------------------|-----------|
| Name | Relationship type authority URI |
| Description | This attribute references the URI that contains the authority/controlled vocabulary. Its value MUST be set to `"http://id.loc.gov/vocabulary/preservation/relationshipType"`. |
| Datatype | [URI]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#uri) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `premis:premis/premis:object/premis:relationship/premis:relationshipType/@valueURI` |
|-----------------------|-----------|
| Name | Relationship type value URI |
| Description | This attribute references the URI that contains the specific entry from the authority/controlled vocabulary.<br><br>For the `structural` relationship type, this attribute's value MUST be set to `"http://id.loc.gov/vocabulary/preservation/relationshipType/str"`. |
| Datatype | [URI]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#uri) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object/premis:relationship/premis:relationshipSubType` |
|-----------------------|-----------|
| Name | Relationship subtype |
| Description | A detailed categorization of the nature of the relationship.<br><br>In the case of the `premis.xml` file of the representation level, this element's value MUST be set to `represents` when expressing the relationship between a representation and the IE it represents.<br>When expressing the relationship between a representation and a file, this element's value MUST be set to `includes` when this relationship is expressed from the side of the representation (i.e. the representation is the subject of the relationship); when this relationship is expressed from the side of the file (i.e. the file is the subject of the relationship), this element's value MUST be set to `is included in`.|
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string); fixed vocabulary |
| Vocabulary | `represents`<br>`includes`<br>`is included in` |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `premis:premis/premis:object/premis:relationship/premis:relationshipSubType/@authority` |
|-----------------------|-----------|
| Name | Relationship subtype authority attribute |
| Description | This attribute indicates the name of the authority/controlled vocabulary that is being used for the different relationship subtypes. Its value MUST be set to `"relationshipSubType"`. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `premis:premis/premis:object/premis:relationship/premis:relationshipSubType/@authorityURI` |
|-----------------------|-----------|
| Name | Relationship subtype authority URI |
| Description | This attribute references the URI that contains the authority/controlled vocabulary. Its value MUST be set to `"http://id.loc.gov/vocabulary/preservation/relationshipSubType"`. |
| Datatype | [URI]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#uri) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `premis:premis/premis:object/premis:relationship/premis:relationshipSubType/@valueURI` |
|-----------------------|-----------|
| Name | Relationship subtype value URI |
| Description | This attribute references the URI that contains the specific entry from the authority/controlled vocabulary.<br><br>If the `represents` relationship subtype is being used, this attribute's value MUST be set to `"http://id.loc.gov/vocabulary/preservation/relationshipSubType/rep"`.<br>If the `includes` relationship subtype is being used, this attribute's value MUST be set to `"http://id.loc.gov/vocabulary/preservation/relationshipSubType/inc"`.<br>If the `is included in` relationship subtype is being used, this attribute's value MUST be set to `"http://id.loc.gov/vocabulary/preservation/relationshipSubType/isi"` |
| Datatype | [URI]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#uri); fixed vocabulary |
| Vocabulary | `"http://id.loc.gov/vocabulary/preservation/relationshipSubType/rep"`<br>`"http://id.loc.gov/vocabulary/preservation/relationshipSubType/inc"`<br>`"http://id.loc.gov/vocabulary/preservation/relationshipSubType/isi"` |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object/premis:relationship/premis:relatedObjectIdentifier` |
|-----------------------|-----------|
| Name | Related object identifier |
| Description | This element references the object of the relationship that is expressed. |
| Cardinality | 1..* |
| Obligation | MUST |

| Element | `premis:premis/premis:object/premis:relationship/premis:relatedObjectIdentifier/premis:relatedObjectIdentifierType` |
|-----------------------|-----------|
| Name | Related object identifier type |
| Description | The type of the PREMIS related object identifier being used. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string); fixed vocabulary (e.g. [`PREMIS standard identifiers`](https://id.loc.gov/vocabulary/identifiers.html)) |
| Vocabulary | `local`<br>`ID`<br>`UUID`<br>... |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object/premis:relationship/premis:relatedObjectIdentifier/premis:relatedObjectIdentifierValue` |
|-----------------------|-----------|
| Name | Related object identifier value |
| Description | The actual value that makes up the identifier of the PREMIS related object. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) (depending on the value of the `premis:relatedObjectIdentifierType`) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics` |
|-----------------------|-----------|
| Name | Object characteristics |
| Description | If the PREMIS object is of type file, this element MUST be used to further specify the various characteristics of the file object such as fixity, size and format information. |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:fixity` |
|-----------------------|-----------|
| Name | Fixity |
| Description | This element contains the fixity information of the PREMIS file object. It encapsulates the message digest algorithm that is being used and its value. |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:fixity/premis:messageDigestAlgorithm` |
|-----------------------|-----------|
| Name | Message digest algorithm |
| Description | This element details which algorithm is used to construct the message digest for the digital file object present. The value MUST be set to MD5. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:fixity/premis:messageDigestAlgorithm/@authority` |
|-----------------------|-----------|
| Name | Message digest algorithm authority attribute |
| Description | This attribute indicates the name of the authority/controlled vocabulary that is being used for the different message digest algorithms. Its value MUST be set to `"cryptographicHashFunctions"`. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:fixity/premis:messageDigestAlgorithm/@authorityURI` |
|-----------------------|-----------|
| Name | Message digest algorithm authority URI |
| Description |  This attribute references the URI that contains the authority/controlled vocabulary. Its value MUST be set to `"http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions"`. |
| Datatype | [URI]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#uri) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:fixity/premis:messageDigestAlgorithm/@valueURI` |
|-----------------------|-----------|
| Name | Message digest algorithm value URI |
| Description | This attribute references the URI that contains the specific entry from the authority/controlled vocabulary.<br><br>This attribute's value MUST be set to `"http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5"`. |
| Datatype | [URI]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#uri) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:fixity/premis:messageDigest` |
|-----------------------|-----------|
| Name | Message digest |
| Description | This element contains the actual value calculated message digest algorithm specified in the `premis:messageDigestAlgorithm` element. |
| Datatype | MD5 |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:size` |
|-----------------------|-----------|
| Name | File size |
| Description | The size of the file object. This MUST be expressed in bytes. |
| Datatype | Integer |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:format` |
|-----------------------|-----------|
| Name | File format identification |
| Description | This element contains information about the format of the file object. |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:format/premis:formatDesignation` |
|-----------------------|-----------|
| Name | File format designation |
| Description | This element contains an identification of the format of the file object. |
| Cardinality | 1..1 |
| Obligation | SHOULD |

| Element | `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:format/premis:formatDesignation/premis:formatName` |
|-----------------------|-----------|
| Name | File format name |
| Description | A commonly accepted name for the file format. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string); fixed vocabulary (from a format or technical registry, e.g. [PRONOM](https://www.nationalarchives.gov.uk/PRONOM/Default.aspx)) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:format/premis:formatDesignation/premis:formatVersion` |
|-----------------------|-----------|
| Name | File format version |
| Description | The version of the format named in `premis:formatName`. |
| Cardinality | 1..1 |
| Obligation | SHOULD |

| Element | `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:format/premis:formatRegistry` |
|-----------------------|-----------|
| Name | Format registry |
| Description | This element identifies and/or gives further information about the file format by referencing an entry in a format registry (e.g. [PRONOM](https://www.nationalarchives.gov.uk/PRONOM/Default.aspx)). |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:format/premis:formatRegistry/premis:formatRegistryName` |
|-----------------------|-----------|
| Name | Format registry name |
| Description | Name of the referenced format registry |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:format/premis:formatRegistry/premis:formatRegistryKey` |
|-----------------------|-----------|
| Name | Format registry key |
| Description | Unique key that is used by the format registry for the concerned file format. |
|| Datatype | ID |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:format/premis:formatRegistry/premis:formatRegistryRole` |
|-----------------------|-----------|
| Name | Format registry role |
| Description | The purpose or expected use of the format registry. This MUST be set to `specification`. |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:format/premis:formatRegistry/premis:formatRegistryRole/@authority` |
|-----------------------|-----------|
| Name | Format registry role authority |
| Description | This attribute indicates the name of the authority/controlled vocabulary that is being used. Its value MUST be set to `"http://id.loc.gov/vocabulary/preservation/formatRegistryRole"`. |
| Datatype | [URI]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#uri) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:format/premis:formatRegistry/premis:formatRegistryRole/@valueURI` |
|-----------------------|-----------|
| Name | Format registry role value URI |
| Description | This attribute references the URI that contains the specific entry from the authority/controlled vocabulary.<br><br>This attribute's value MUST be set to `"http://id.loc.gov/vocabulary/preservation/formatRegistryRole/spe"`. |
| Datatype | [URI]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#uri) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object[@xsi:type="premis:file"]/premis:originalName` |
|-----------------------|-----------|
| Name | Original filename |
| Description | This element contains the original name of the file object, including its extension. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

<small>
Continue to [Profiles]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/profiles/index.md %}).
</small>