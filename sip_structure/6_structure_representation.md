---
layout:       default
title:        Representation level
parent:       Structure
grand_parent:  2.1
nav_order:    2
nav_exclude:  false
---

{% assign rep_constraints = site.data["2_1"]._data.GENERAL | where_exp: "c",
"c.Level == 'Representation'" %}

# Representation level
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

The representation level consists of at least one representation directory (in the remainder of this text we will use `representation_1` as an example).
Each representation directory contains information about the representation of (one of) the IE(s) of the package level, together with the media files making up the representation.

***Example***

```plaintext
root_directory
│   ...
│
└──representations
   │
   └──representation_1
   │  │── METS.xml
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

## /representation_1 (directory)

A representation directory consists of at least a `METS.xml` file, a `/data` directory and a `/metadata` directory.
It contains both descriptive and preservation metadata, as well as the actual media files making up a certain representation of the IE(s) of the SIP.

Each representation directory contains its own `METS.xml` file which acts similarly as the package `METS.xml` and serves as an inventory of the files and directories of the representation level.


A representation directory may contain a `/documentation` and a `/schemas` directory. 
The former may contain additional information aiding the interpretation of the representation, while the latter may contain XML Schema Definition (XSD) files of the metadata schemas used in the representation.
These two directories are ignored during ingest and will therefore not be archived.

***Requirements***

{% assign constraints = rep_constraints | where_exp: "c",
"c.Path == '/'" %}

{% include_relative _list_constraints.liquid constraints = constraints %}

## METS.xml (file)

The `METS.xml` file at the representation level (also known as the representation mets) generally follows the same structure and requirements as the package mets discussed in the section [package METS.xml](./5_structure_package.html#metsxml-file).

### Elements and internal references

Since the `dmdSec`, `amdSec`, `fileSec` sections follow the same requirements (where possible) as the package `METS.xml` file,  each dedicated subsection below only lists (additional) requirements regarding the `mets`, `metsHdr` and `structMap` elements.

Some of these elements, or their child elements, are identified with an identifier, contained in the `@ID` attribute (see the requirements in the sections below).
These identifiers must be unique within the SIP. 

The `<structMap>` serves as the entrypoint for locating the metadata, data or manifest files during parsing of the SIP.
Therefore, it contains pointers to the `@ID` identifiers defined in the `<fileSec>`, `<dmdSec>`, and `<amdSec>` sections.
An overview of the different elements and references on the representation level is given in the following figure.

<figure class="mx-auto">
  <img src="../../../../../assets/images_spec/sip-representation-pointers.svg" alt="Internal references between elements in the METS.xml" /> 
  <figcaption>Internal references between elements in the representation METS.xml.</figcaption>
</figure>

In addition, the `<fileGrp>` and `<file>` elements can also reference contents of the `<amdSec>` and `<dmdSec>`, however this is optional.
A summary of all possible references and their obligation is given in the table below.

| Pointer | Obligation | Target |
| ------- | ---------- | ---------- |
| [`mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Representations']/fptr/@FILEID`](#structMap-csip-div-div-representations-fptr-fileid) | MUST | [`mets/fileSec/fileGrp/@ID`](#fileGrp-id) or [`mets/fileSec/fileGrp/file/@ID`](#file-id) if allowed by the profile.  |
| [`mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Metadata']/@DMDID`](#structMap-csip-div-div-metadata-dmdid) | MUST | [`mets/dmdSec/@ID`](#dmdSec-id) |
| [`mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Metadata']/@ADMID`](#structMap-csip-div-div-metadata-admid) | MUST | [`mets/amdSec/digiprovMD/@ID`](#digiprovMD-id) |
| [`mets/fileSec/fileGrp/@ADMID`](#fileGrp-admid) | MAY | [`mets/amdSec/digiprovMD/@ID`](#digiprovMD-id) |
|[`mets/fileSec/fileGrp/file/@DMDID`](#fileGrp-file-dmdid) | MAY | [`mets/dmdSec/@ID`](#dmdSec-id) |
| [`mets/fileSec/fileGrp/file/@ADMID`](#fileGrp-file-admid) | MAY | [`mets/amdSec/digiprovMD/@ID`](#digiprovMD-id) |

### \<mets\> section

***Example***

```xml
<?xml version="1.0"?>
<mets xmlns="http://www.loc.gov/METS/"
      xmlns:csip="https://DILCIS.eu/XML/METS/CSIPExtensionMETS"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xmlns:xlink="http://www.w3.org/1999/xlink"
      OBJID="representation_1"
      TYPE="Photographs – Digital"
      PROFILE="https://earksip.dilcis.eu/profile/E-ARK-SIP-v2-2-0.xml" xsi:schemaLocation="https://www.w3.org./1999/xlink http://www.loc.gov/standards/xlink/xlink.xsd  http://www.loc.gov/METS/ https://www.loc.gov/standards/mets/mets.xsd https://DILCIS.eu/XML/METS/CSIPExtensionMETS https://earkcsip.dilcis.eu/schema/DILCISExtensionMETS.xsd ">

<metsHdr>...</metsHdr>
<dmdSec>...</dmdSec>
<amdSec>...</amdSec>
<fileSec>...</fileSec>
<structMap>...</structMap>

</mets>
```

***Requirements***

{% assign constraints = rep_constraints | where_exp: "c",
"c.Section == 'mets'" %}

{% include_relative _constraints.liquid constraints = constraints %}

### \<metsHdr\> section

***Example***

```xml
<metsHdr CREATEDATE="2022-02-16T10:02:37.009+02:00" csip:OAISPACKAGETYPE="SIP"/>
```

***Requirements***

{% assign constraints = rep_constraints | where_exp: "c",
"c.Section == 'metsHdr'" %}

{% include_relative _constraints.liquid constraints = constraints %}

### \<structMap\> section

The `structMap` element outlines the hierarchical structure of the representation level of the SIP.
Its requirements are very similar to the package level, however, instead of pointing to the contained representations, a `data` division points to the contained files. 

***Example***

```xml
<structMap ID="uuid-f81f8688-b278-4397-b59c-82593b11a2b9" TYPE="PHYSICAL" LABEL="CSIP">
    <div ID="uuid-a5e05d29-49d9-4466-b070-19b8990b5029" LABEL="representation_1">
        <div ID="uuid-af54ed63-8361-4d90-a30f-99d02de24857" LABEL="Metadata" 
            ADMID="uuid-f7972ff5-599e-4f60-8b7e-8bbf4e035482" />
        <div ID="uuid-c137b167-7254-4085-b965-75980976638d" LABEL="data">
            <fptr FILEID="uuid-d020d7d1-f258-40af-8788-04cf62a0032b" />
        </div>
    </div>
</structMap>
```

{% assign constraints = rep_constraints | where_exp: "c",
"c.Section == 'structMap'" %}

{% include_relative _constraints.liquid constraints = constraints %}

## /data (directory)

The `/data` directory contains the media files of a specific representation of the SIP.
Depending on the use-case and the CP, these files can be digital pictures, video, audio...

***Requirements***

{% assign constraints = rep_constraints | where_exp: "c",
"c.Section == 'data'" %}

{% include_relative _list_constraints.liquid constraints = constraints %}

## /metadata (directory)

The `/metadata` directory contains both descriptive and preservation metadata about the representation and the media files at the representation level.

***Requirements***

{% assign constraints = rep_constraints | where_exp: "c",
"c.Section == 'metadata'" %}

{% include_relative _list_constraints.liquid constraints = constraints %}

### /descriptive (directory)

The `/descriptive` directory contains descriptive metadata about the representation.
This descriptive metadata is stored in XML files, describing the specific representation of the SIP.

Descriptive metadata at the represenation level follows the same requirements regarding metadata elements discussed in the [/descriptive section](./5_structure_package.html#descriptive-directory) of the package level.
Hence, the concrete requirements of descriptive metadata files and the applied metadata schemas are defined by the [content profiles]({{ site.baseurl }}{% link docs/diginstroom/sip/2.1/profiles/index.md %}).

### /preservation (directory)

The `/preservation` directory contains preservation metadata about the representation and the media files.

***Requirements***

{% assign constraints = rep_constraints | where_exp: "c",
"c.Section == 'preservation'" %}

{% include_relative _list_constraints.liquid constraints = constraints %}

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
          <premis:formatRegistryKey>fmt/1507</premis:formatRegistryKey>
          <premis:formatRegistryRole authority="formatRegistryRole" authorityURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole" valueURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole/spe">specification</premis:formatRegistryRole>
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
          <premis:formatRegistryKey>fmt/1507</premis:formatRegistryKey>
          <premis:formatRegistryRole authority="formatRegistryRole" authorityURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole" valueURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole/spe">specification</premis:formatRegistryRole>
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

{% assign constraints = rep_constraints | where_exp: "c",
"c.Section == 'premis'" %}

{% include_relative _constraints.liquid constraints = constraints %}

<small>
Continue to [Profiles]({{ site.baseurl }}{% link docs/diginstroom/sip/2.1/profiles/index.md %}).
</small>
