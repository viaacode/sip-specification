---
layout:       default
title:        Package level
parent:       Structure
grand_parent:  2.1
nav_order:    1
nav_exclude:  false
---

{% assign package_constraints = site.data.2_1._data.GENERAL | where_exp: "c",
"c.Level == 'Package'" %}

# Package level
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

The package level is the top level of the meemoo SIP and consists of at least a `METS.xml` file, a `/metadata` directory and a `/representations` directory.
It contains information about the IE(s) of the SIP and the SIP as a whole.

The package level may contain a `/documentation` and a `/schemas` directory.
The former may contain additional information aiding the interpretation of the SIP, while the latter may contain XML Schema Definition (XSD) files of the metadata schemas used in the SIP.
These two directories are ignored during ingest and will therefore not be archived.

***Example***

```plaintext
uuid-e4eb34c0-4fc6-4395-b61c-0671f8e0b04c                     (= root directory)
└──METS.xml
│
└──metadata
│  │
│  └──descriptive
│  │  |   ...
│  │
│  └──preservation
│     |   ... 
│
└──representations
   │   ...
```

***Requirements***

{% assign general_constraints = package_constraints | where_exp: "c",
"c.Path == '/'" %}

{% include_relative _list_constraints.liquid constraints = general_constraints %}

## METS.xml (file)

[Metadata Encoding and Transmission Standard](https://www.loc.gov/standards/mets/mets-home.html) (METS) is a metadata standard for encoding descriptive, administrative and structural metadata.
In the case of the meemoo SIP, the `METS.xml` file's main purpose is to act as an inventory of the files and directories contained within.
Since it is situated at the package-level, it is also known as the _package METS file_.

It should not be confused with the `METS.xml` files situated in their respective [representation folders](./6_structure_representation.html).
The package `METS.xml` file does not record the internal structure of the different representations in the `/representations` directory.
It only references the different `METS.xml` files contained in each representation directory.
Each of the `METS.xml` files at the [representation level](./6_structure_representation.html) references its own internal structure.

### Elements and internal references

A `METS.xml` file typically consists of a number of fixed elements, outlined below.
Each of these elements is covered in a dedicated subsection in the remainder of this section.

- `<mets>` element: the root tag; this element contains a number of attributes with information about the type of SIP and its identification.
- `<metsHdr>` element: this tag mainly covers the agents (such as software or the CP) involved with the creation and submission process of the SIP.
- `<dmdSec>` element: this tag contains descriptive metadata, either embedded within the tag or with a reference to an external metadata file.
- `<amdSec>` element: this tag contains preservation metadata, either embedded within the tag or with a reference to an external metadata file.
- `<fileSec>` element: this tag acts as an inventory of the files that comprise the digital object being described in the `METS.xml` file.
- `<structMap>` element: this tag organizes the digital content represented in the `<fileSec>`, `<dmdSec>`, and `<amdSec>` elements into a coherent hierarchical structure. This is important for a correct comprehension and navigation of digital content with complex relationships between the digital objects, such as newspapers. 

Some of these elements, or their child elements, are identified with an identifier, contained in the `@ID` attribute (see the requirements in the sections below).
These identifiers must be unique within the SIP. 

The `<structMap>` serves as the entrypoint for locating the metadata, data or manifest files during parsing of the SIP.
Therefore, it contains pointers to the `@ID` identifiers defined in the `<fileSec>`, `<dmdSec>`, and `<amdSec>` sections.
An overview of the different elements and references on the package level is given in the following figure.

<figure class="mx-auto">
  <img src="../../../../../assets/images_spec/sip-package-pointers.svg" alt="Internal references between elements in the package METS.xml" /> 
  <figcaption>Internal references between elements in the METS.xml.</figcaption>
</figure>

In addition, 
the `<fileGrp>` and `<file>` elements can also reference contents of the `<amdSec>` and `<dmdSec>`, however this is optional.
A summary of all possible references and their obligation is given in the table below.

| Pointer | Obligation | Target |
| ------- | ---------- | ---------- |
| [`mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Metadata']/@DMDID`](#structMap-csip-div-div-metadata-dmdid) | MUST | [`mets/dmdSec/@ID`](#dmdSec-id) |
| [`mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Metadata']/@ADMID`](#structMap-csip-div-div-metadata-admid) | MUST | [`mets/amdSec/digiprovMD/@ID`](#digiprovMD-id) |
| [`mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Documentation']/fptr/@FILEID`](#structMap-csip-div-div-documentation-fptr-fileid) | MUST | [`mets/fileSec/fileGrp/@ID`](#fileGrp-id) or [`mets/fileSec/fileGrp/file/@ID`](#file-id) if allowed by the profile. |
| [`mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Schemas']/fptr/@FILEID`](#structMap-csip-div-div-schemas-fptr-fileid) | MUST | [`mets/fileSec/fileGrp/@ID`](#fileGrp-id) or [`mets/fileSec/fileGrp/file/@ID`](#file-id) if allowed by the profile. |
| [`mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Representations/representation_*']/mptr/@xlink:title`](#structMap-csip-div-div-representations-fptr-fileid) | SHOULD | [`mets/fileSec/fileGrp/@ID`](#fileGrp-id) (or [`mets/fileSec/fileGrp/file/@ID`](#file-id) if allowed by the profile.)  |
| [`mets/fileSec/fileGrp/@ADMID`](#fileGrp-admid) | MAY | [`mets/amdSec/digiprovMD/@ID`](#digiprovMD-id) |
| [`mets/fileSec/fileGrp/file/@DMDID`](#fileGrp-file-dmdid) | MAY | [`mets/dmdSec/@ID`](#dmdSec-id) |
| [`mets/fileSec/fileGrp/file/@ADMID`](#fileGrp-file-admid) | MAY | [`mets/amdSec/digiprovMD/@ID`](#digiprovMD-id) |


### \<mets\> section

This is the root element of the package METS file.
It contains a number of XML schema namespaces together with a number of attributes to uniquely identify the package METS file and the type of data it lists.
The various requirements are listed in the table below.

***Example***

```xml
<?xml version='1.0' encoding='UTF-8'?>
<mets xmlns="http://www.loc.gov/METS/"
      xmlns:csip="https://DILCIS.eu/XML/METS/CSIPExtensionMETS"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xmlns:xlink="http://www.w3.org/1999/xlink"
      OBJID="uuid-fae4ef8f-5954-4602-9a1e-0d6eb83f3727"
      TYPE="Photographs – Digital"
      PROFILE="https://earksip.dilcis.eu/profile/E-ARK-SIP.xml"
      csip:CONTENTINFORMATIONTYPE="OTHER" csip:OTHERCONTENTINFORMATIONTYPE="https://data.hetarchief.be/id/sip/2.1/basic" 
      xsi:schemaLocation="https://www.w3.org./1999/xlink http://www.loc.gov/standards/xlink/xlink.xsd  http://www.loc.gov/METS/ https://www.loc.gov/standards/mets/mets.xsd https://DILCIS.eu/XML/METS/CSIPExtensionMETS https://earkcsip.dilcis.eu/schema/DILCISExtensionMETS.xsd ">


  <metsHdr>...</metsHdr>
  <dmdSec>...</dmdSec>
  <amdSec>...</amdSec>
  <fileSec>...</fileSec>
  <structMap>...</structMap>

</mets>
```

***Requirements***

{% assign constraints = package_constraints | where_exp: "c",
"c.Section == 'mets'" %}

{% include_relative _constraints.liquid constraints = constraints %}

### \<metsHdr\> section

This element contains administrative metadata about the SIP such as its creator and its creation software.
It does so by using separate `agent` tags for every role in the SIPs creation and submission process.

***Example***

```xml
<metsHdr CREATEDATE="2022-02-16T10:01:15.014+02:00" csip:OAISPACKAGETYPE="SIP">
  <!-- information about the software -->
  <agent ROLE="CREATOR" TYPE="OTHER" OTHERTYPE="SOFTWARE">
    <name>meemoo SIP creator</name>
    <note csip:NOTETYPE="SOFTWARE VERSION">0.1.</note>
  </agent>
  <!-- information about the archival creator-->
  <agent ROLE="ARCHIVIST" TYPE="ORGANIZATION">
    <name>Flemish Cat Museum</name>
    <note csip:NOTETYPE="IDENTIFICATIONCODE">OR-m30wc4t</note>
  </agent>
  <!-- information about the submitting organisation -->
  <agent ROLE="CREATOR" TYPE="ORGANIZATION">
    <name>Flemish Cat Museum</name>
    <note csip:NOTETYPE="IDENTIFICATIONCODE">OR-m30wc4t</note>
  </agent>
</metsHdr>
```

***Requirements***

{% assign constraints = package_constraints | where_exp: "c",
"c.Section == 'metsHdr'" %}

{% include_relative _constraints.liquid constraints = constraints %}

### \<dmdSec\> section

The `dmdSec` element (short for 'descriptive metadata section') contains descriptive metadata about the IE(s) in the SIP.
Descriptive metadata in the meemoo SIP MUST be contained in dedicated metadata files located in the `/metadata/descriptive` directory of the package level.
This means that the `dmdSec` MUST use `<mdRef>` elements to reference the external metadata files.

***Example***

```xml
<dmdSec ID="uuid-c6a678a7-b4b0-45af-a7d4-33123d9f0911">
  <mdRef LOCTYPE="URL" MDTYPE="DC" xlink:type="simple" xlink:href="./metadata/descriptive/dc_1.xml" MIMETYPE="text/xml" SIZE="663" CREATED="2022-02-16T10:01:15.014+02:00" CHECKSUM="cd17cbb2153946c8462e10b337e0e9c1" CHECKSUMTYPE="MD5" />
</dmdSec>

<!-- ref to descriptive metadata about IE1 -->
<dmdSec ID="uuid-7a3443ed-9925-414b-819f-fc4830475e22">
    <mdRef LOCTYPE="URL" MDTYPE="DC" xlink:type="simple" xlink:href="./metadata/descriptive/dc_2.xml" MIMETYPE="text/xml" SIZE="738" CREATED="2022-02-16T10:01:15.014+02:00" CHECKSUM="fbab574560f2d548fd84c6c1fd1cb7f2" CHECKSUMTYPE="MD5" />
</dmdSec>

<!-- ref to descriptive metadata about IE2 -->
<dmdSec ID="uuid-dff9e2ad-ab58-490a-9d80-df6c812404d2">
    <mdRef LOCTYPE="URL" MDTYPE="DC" xlink:type="simple" xlink:href="./metadata/descriptive/dc_3.xml" MIMETYPE="text/xml" SIZE="748" CREATED="2022-02-16T10:01:15.014+02:00" CHECKSUM="9d55815152e83db76a32f74990d79cd3" CHECKSUMTYPE="MD5" />
</dmdSec>
```

***Requirements***

{% assign constraints = package_constraints | where_exp: "c",
"c.Section == 'dmdSec'" %}

{% include_relative _constraints.liquid constraints = constraints %}

### \<amdSec\> section

The `amdSec` element (short for 'administrative metadata section') contains preservation metadata about the IE(s) of the SIP and about the SIP as a whole.
Preservation data in the meemoo SIP MUST be contained in dedicated metadata files located in the `metadata/preservation` directory of the package-level.
This means that the `amdSec` MUST use `<mdRef>` elements, contained in `<digiprovMD>` elements, to reference the external metadata files.

***Example***

```xml
<!-- ref to the PREMIS metadata about IE(s)/package -->
<amdSec>
  <digiprovMD ID="uuid-4ac13924-fe19-4711-b51f-6b5acc692ec0">
    <mdRef LOCTYPE="URL" MDTYPE="PREMIS" xlink:type="simple" xlink:href="./metadata/preservation/premis.xml" MIMETYPE="text/xml" SIZE="6295" CREATED="2022-02-16T10:01:15.014+02:00" CHECKSUM="01de8b0a874407472a183aeece47505d" CHECKSUMTYPE="MD5" />
  </digiprovMD>
</amdSec>
```

***Requirements***

{% assign constraints = package_constraints | where_exp: "c",
"c.Section == 'amdSec'" %}

{% include_relative _constraints.liquid constraints = constraints %}

### \<fileSec\> section

The `fileSec` element (short for 'file section') lists all files of the package level in the SIP.
It contains references to the representation `METS.xml` files of the different representations, but does not list other files of those representations.
The listing of other representation files (i.e. metadata files and media files) is left to the respective representation `METS.xml` files.

***Example***

```xml
<!-- file section -->
<fileSec ID="uuid-0c53fd9b-f640-4def-a872-2e4622f691d9">
  <fileGrp USE="Representations/representation_1" ID="uuid-700c97da-3164-4863-9e58-d6d62156052e">
      <file ID="uuid-0fe40ffc-b5f3-465e-af3a-d266d94453b7" MIMETYPE="text/xml" SIZE="4264" CREATED="2022-02-16T10:01:15.014+02:00" CHECKSUM="297f0482f32b2836d2ac7e2ff0a5884d" CHECKSUMTYPE="MD5">
          <FLocat LOCTYPE="URL" xlink:type="simple" xlink:href="./representations/representation_1/METS.xml" />
      </file>
  </fileGrp>
  <fileGrp USE="Representations/representation_2" ID="uuid-c0fed1c6-96c8-4f15-9e82-abc7be2e981c">
      <file ID="uuid-625629a4-e5f8-4087-9114-66e4a943bf50" MIMETYPE="text/xml" SIZE="3865" CREATED="2022-02-16T10:01:15.014+02:00" CHECKSUM="95cd90cad81c9227f76d5f584182b308" CHECKSUMTYPE="MD5">
          <FLocat LOCTYPE="URL" xlink:type="simple" xlink:href="./representations/representation_2/METS.xml" />
      </file>
  </fileGrp>
</fileSec>
```

***Requirements***

{% assign fileSec_constraints = package_constraints | where_exp: "c",
"c.Section == 'fileSec'" %}

{% assign constraints = fileSec_constraints | where_exp: "c",
"c.Type == 'General'" %}

{% include_relative _list_constraints.liquid constraints = constraints %}

{% assign constraints = fileSec_constraints | where_exp: "c",
"c.Path == '/METS.xml'" %}

{% include_relative _constraints.liquid constraints = constraints %}

### \<structMap\> section

The `structMap` element outlines the hierarchical structure of the package level of the SIP.
It provides links between elements and metadata files located elsewhere in the package level.

***Example***

```xml
<!-- structural map -->
<structMap ID="uuid-1ce2cef4-cb9a-4649-8983-c916870cf2b4" TYPE="PHYSICAL" LABEL="CSIP">
    <div ID="uuid-33cd69c8-b297-40e1-9491-1b5db58890bd" LABEL="package-example">
        <div ID="uuid-c0a73bbc-d6f3-42a0-b5e1-f53a4601101b" LABEL="Metadata"
            DMDID="uuid-c6a678a7-b4b0-45af-a7d4-33123d9f0911 uuid-7a3443ed-9925-414b-819f-fc4830475e22 uuid-dff9e2ad-ab58-490a-9d80-df6c812404d2"
            ADMID="uuid-4ac13924-fe19-4711-b51f-6b5acc692ec0" />
        <div ID="uuid-c5cab13b-aced-4024-bbc3-d38c682602d2" LABEL="Representations/representation_1">
            <mptr xlink:type="simple" xlink:href="./representations/representation_1/METS.xml" LOCTYPE="URL" xlink:title="uuid-700c97da-3164-4863-9e58-d6d62156052e" />
        </div>
        <div ID="uuid-daeba358-46ee-4363-b2a2-bd745c128f6f" LABEL="Representations/representation_2">
            <mptr xlink:type="simple" xlink:href="./representations/representation_2/METS.xml" LOCTYPE="URL" xlink:title="uuid-c0fed1c6-96c8-4f15-9e82-abc7be2e981c" />
        </div>
    </div>
</structMap>
```

***Requirements***

{% assign constraints = package_constraints | where_exp: "c",
"c.Section == 'structMap'" %}

{% include_relative _constraints.liquid constraints = constraints %}


## /metadata (directory)

The `/metadata` directory contains both descriptive and preservation metadata about the IE(s) at the package level.
It also contains preservation metadata about the SIP as a whole.

***Requirements***

{% assign constraints = package_constraints | where_exp: "c",
"c.Section == 'metadata'" %}

{% include_relative _list_constraints.liquid constraints = constraints %}

### /descriptive (directory)

The `/descriptive` directory contains descriptive metadata about the IE(s) at the package level.
This descriptive metadata is stored in different XML files, depending on the number of IE(s) present in the SIP.
Examples are `mods.xml` and `dc+schema.xml`.
These files apply a certain metadata schema, such as [DCTERMS](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) or [MODS](https://www.loc.gov/standards/mods/).
The concrete requirements of descriptive metadata files and the applied metadata schemas are defined by the [content profiles]({{ site.baseurl }}{% link docs/diginstroom/sip/2.1/profiles/index.md %}).

### /preservation (directory)

The `/preservation` directory contains preservation metadata about the IE(s) at the package level.

***Requirements***

{% assign constraints = package_constraints | where_exp: "c",
"c.Section == 'preservation'" %}

{% include_relative _list_constraints.liquid constraints = constraints %}

The `premis.xml` file at the package-level contains preservation metadata about the IE(s) of the SIP, and about the SIP as a whole.
It also contains any additional IDs related to the IE(s) of the SIP.
It relies on the [Preservation Metadata: Implementation Strategies (PREMIS)](https://www.loc.gov/standards/premis/) standard in order to provide basic preservation information.
More detailed preservation information can be described [using PREMIS events and PREMIS agents](#adding-provenance-of-representations).

If descriptive metadata is available for a given IE, a link is established via a shared ID between the relevant PREMIS object in the `premis.xml` file and the corresponding `descriptive/dc*.xml` file.
This ID is stored in the `<premis:objectIdentifier>` element of the relevant PREMIS object and in the `<dcterms:identifier>` element of the corresponding `dc*.xml` file in the `/descriptive` directory. 

#### Describing Intellectual Entities

On the package level, the preservation metadata is used to express

- what the different IEs are contained in the SIP; and 
- how they relate to each other and to possible representations. 

***Example***

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

  <!-- IE about the Felis Catus Flamens -->
  <premis:object xsi:type="premis:intellectualEntity">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-b21a86aa-97a3-4f7b-a9f5-4d330af641c0</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship between the main IE and the nested IEs -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/hsp">has part</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-948e2213-ca54-459c-8c87-5818adeb9444</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-01d59d41-f523-4d06-a549-4bf6f7cef853</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>

  <!-- nested IE1 about the Felis Catus Flamens lying on the sofa -->
  <premis:object xsi:type="premis:intellectualEntity">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-948e2213-ca54-459c-8c87-5818adeb9444</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship between nested IE1 and the main IE -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isp">is part of</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-b21a86aa-97a3-4f7b-a9f5-4d330af641c0</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship between nested IE1 and its representation -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isr">is represented by</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-541292c3-223a-4b80-b747-66bc86ff4a89</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>

  <!-- nested IE2 about the Felis Catus Flamens sitting on its cat tree -->
  <premis:object xsi:type="premis:intellectualEntity">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-01d59d41-f523-4d06-a549-4bf6f7cef853</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship between nested IE2 and the main IE -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isp">is part of</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-b21a86aa-97a3-4f7b-a9f5-4d330af641c0</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship between nested IE2 and its representation -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isr">is represented by</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-de83045d-3b0f-4161-9f96-40079af0d480</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>

</premis:premis>
```

 <a id="premis-relationships"></a>***Overview of relevant PREMIS relationships***

The table below gives an overview of the different relationship types that can be used on the package level:

| Direction | Relationship type | Relationship subtype | Reciprocal/inverse relationship | Description |
|-------------------|----------------------|---------------------------------|-------------|
| From (main) IE to (sub) IE | [`structural`](http://id.loc.gov/vocabulary/preservation/relationshipType/str) | [`has part`](http://id.loc.gov/vocabulary/preservation/relationshipSubType/hsp) | [`is part of`](http://id.loc.gov/vocabulary/preservation/relationshipSubType/isp) | A larger IE, such as the main IE, has another IE as a part. |
| From IE to Representation | [`structural`](http://id.loc.gov/vocabulary/preservation/relationshipType/str) | [`is represented by`](http://id.loc.gov/vocabulary/preservation/relationshipSubType/isr) | [`represents`](http://id.loc.gov/vocabulary/preservation/relationshipSubType/rep) | A IE object is represented by one of its representations. |
| From IE to master | [`structural`](http://id.loc.gov/vocabulary/preservation/relationshipType/str) | [`has master copy`](https://data.hetarchief.be/ns/object/hasMasterCopy) | [`is master copy of`](https://data.hetarchief.be/ns/object/isMasterCopyOf) | A IE object is represented by a high resolution master copy. |
| From IE to mezzanine | [`structural`](http://id.loc.gov/vocabulary/preservation/relationshipType/str) | [`has mezzanine copy`](https://data.hetarchief.be/ns/object/hasMezzanineCopy) | [`is mezzanine copy of`](https://data.hetarchief.be/ns/object/isMezzanineCopyOf) | A IE object is represented by a mezzanine copy. |

***Requirements***

{% assign constraints = package_constraints | where_exp: "c",
"c.Section == 'premis'" %}

{% include_relative _constraints.liquid constraints = constraints %}

#### Adding provenance of representations

If desired, a representation's provenance trail can be added to the preservation metadata using PREMIS events and agents.
In most cases, events are used to submit information about the digitization process that created the representations. 
The use of events might be prohibited or enforced depending on the given content profile. 

{: .note }
The possible event types are limited and managed by a controlled list. This list is still under development and will be published in a future release of the specification.
<!--
TODO: Link to list of possible eventTypes
TODO: figure out the IDs
-->

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

    <!-- description of objects (left out for clarity) -->
    ...

    <!-- description of the digitization event that created the supplied representation -->
    <premis:event>
        <premis:eventIdentifier>
            <premis:eventIdentifierType>UUID</premis:eventIdentifierType>
            <premis:eventIdentifierValue>uuid-f0513e06-4c57-4faf-a758-042043d99b81</premis:eventIdentifierValue>
        </premis:eventIdentifier>
        <premis:eventType>DIGITIZATION</premis:eventType>
        <premis:eventDateTime>2022-05-17T11:50:13</premis:eventDateTime>
        <premis:eventDetailInformation>
            <premis:eventDetail />
        </premis:eventDetailInformation>
        <premis:eventOutcomeInformation>
            <premis:eventOutcome valueURI="http://id.loc.gov/vocabulary/preservation/eventOutcome/suc">succes</premis:eventOutcome>
        </premis:eventOutcomeInformation>
        <premis:linkingAgentIdentifier>
            <premis:linkingAgentIdentifierType>MEEMOO-OR-ID</premis:linkingAgentIdentifierType>
            <premis:linkingAgentIdentifierValue>OR-m30wc4t</premis:linkingAgentIdentifierValue>
            <premis:linkingAgentRole valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp">implementer</premis:linkingAgentRole>
        </premis:linkingAgentIdentifier>
        <premis:linkingAgentIdentifier>
            <premis:linkingAgentIdentifierType>UUID</premis:linkingAgentIdentifierType>
            <premis:linkingAgentIdentifierValue>uuid-1cc1fe7a-da78-4c53-847a-0fd141ce2d3b</premis:linkingAgentIdentifierValue>
            <premis:linkingAgentRole>instrument</premis:linkingAgentRole>
        </premis:linkingAgentIdentifier>
        <premis:linkingObjectIdentifier>
            <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
            <premis:linkingObjectIdentifierValue>uuid-de83045d-3b0f-4161-9f96-40079af0d480</premis:linkingObjectIdentifierValue>
            <premis:linkingObjectRole valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/out">outcome</premis:linkingObjectRole>
        </premis:linkingObjectIdentifier>
    </premis:event>

    <!-- description of the video player used to digitize an analog carrier -->
    <premis:agent>
        <premis:agentIdentifier>
            <premis:agentIdentifierType>UUID</premis:agentIdentifierType>
            <premis:agentIdentifierValue>uuid-1cc1fe7a-da78-4c53-847a-0fd141ce2d3b</premis:agentIdentifierValue>
        </premis:agentIdentifier>
        <premis:agentName>SONY PDW-U2</premis:agentName>
        <premis:agentType>hardware</premis:agentType>
        <premis:agentExtension xmlns:schema="http://schema.org/">
            <schema:model>PDW-U2</schema:model>
            <schema:brand>
                <schema:name>SONY</schema:name>
            </schema:brand>
            <schema:serialNumber>123456</schema:serialNumber>
        </premis:agentExtension>
    </premis:agent>
...
</premis:premis>
```

{% assign constraints = package_constraints | where_exp: "c",
"c.Section == 'premisEvent'" %}

{% include_relative _constraints.liquid constraints = constraints %}

## /representations (directory)

The `/representations` directory contains a separate directory for each representation of (the) IE(s) of the package level.

***Requirements***

{% assign constraints = package_constraints | where_exp: "c",
"c.Section == 'representations'" %}

{% include_relative _list_constraints.liquid constraints = constraints %}

<small>
Continue to [representation level]({{ site.baseurl }}{% link docs/diginstroom/sip/2.1/sip_structure/6_structure_representation.md %}).
</small>
