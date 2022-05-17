---
layout:       default
title:        Package level
parent:       SIP Structure
nav_order:    6
nav_exclude:  false
---
Status: WIP
{: .label .label-yellow }
# Package level
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

The package level is stored in the `/data` directory of the [bag](./4_structure_bag.html) and consists of at least a `mets.xml` file, a `/metadata` directory and a `/representations` directory.
It contains information about the (sub-)IE(s) of the SIP and the SIP as a whole.

The package level may contain a `/documentation` and a `/schemas` directory.
The former may contain additional information aiding the interpretation of the SIP, while the latter may contain XML Schema Definition (XSD) files of the metadata schemas used in the SIP.
These two directories are ignored during ingest and will therefore not be archived.

***Example***

```plaintext
root_directory
│   ...
│
└──data
   │  mets.xml
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

- The `/data` directory MUST contain exactly one `mets.xml` file.
- The `/data` directory MUST contain exactly one `/metadata` directory.
- The `/data` directory MUST contain exactly one `/representations` directory.
- The `/data` directory MAY contain exactly one `/documentation` directory.
- The `/data` directory MAY contain exactly one `/schemas` directory.

## mets.xml (file)

[Metadata Encoding and Transmission Standard](https://www.loc.gov/standards/mets/mets-home.html) (METS) is a metadata standard for encoding descriptive, administrative and structural metadata.
In the case of the meemoo SIP, the `mets.xml` file's main purpose is to act as an inventory of the files and directories contained within.
Since it is situated at the package-level, it is also known as the _package METS file_.

It should not be confused with the `mets.xml` files situated in their respective [representation folders](./6_structure_representation.html).
The package `mets.xml` file does not record the internal structure of the different representations in the `/representations` directory.
It only references the different `mets.xml` files contained in each `/representation_*` directory (where `*` is an integer indicating the number of different representations in the `/representation` directory).
Each of the `mets.xml` files at the [representation level](./6_structure_representation.html) references its own internal structure.

A `mets.xml` file typically consists of a number of fixed elements, outlined below.
This section covers each of these elements below in a dedicated subsection.

- `<mets>` element: the root tag; this element contains a number of attributes with information about the type of SIP and its identification.
- `<metsHdr>` element: this tag mainly covers the agents (such as software or the CP) involved with the creation and submission process of the SIP.
- `<dmdSec>` element: this tag contains descriptive metadata, either embedded within the tag or with a reference to an external metadata file.
- `<amdSec>` element: this tag contains preservation metadata, either embedded within the tag or with a reference to an external metadata file.
- `<fileSec>` element: this tag acts as an inventory of the files that comprise the digital object being described in the `mets.xml` file.
- `<structMap>` element: this tag organizes the digital content represented in the `<fileSec>` element into a coherent hierarchical structure. This is important for a correct comprehension and navigation of digital content with complex relationships between the digital objects, such as newspapers.

### \<mets\> section

This is the root element of the package METS file.
It contains a number of XML schema namespaces together with a number of attributes to uniquely identify the package METS file and the type of data it lists.
The various requirements are listed in the table below.

***Example***

```xml
<?xml version='1.0' encoding='UTF-8'?>
<mets xmlns="http://www.loc.gov/METS/"
      xmlns:csip="https://DILCIS.eu/XML/METS/CSIPExtensionMETS"
      xmlns:sip="https://DILCIS.eu/XML/METS/SIPExtensionMETS"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xmlns:xlink="http://www.w3.org/1999/xlink"
      OBJID="uuid-cbee2999-1db5-4a69-9260-f216dee75623"
      TYPE="Photographs – Digital"
      PROFILE="https://earksip.dilcis.eu/profile/E-ARK-SIP.xml"
      csip:CONTENTINFORMATIONTYPE="OTHER"
      csip:OTHERCONTENTINFORMATIONTYPE="">

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
| Description | This is the root element of the package METS.<br>It MUST contain the following XML schema namespaces:<br>[`mets: http://www.loc.gov/METS/`](http://www.loc.gov/METS/)<br>[`csip: https://dilcis.eu/XML/METS/CSIPExtensionMETS`](https://dilcis.eu/XML/METS/CSIPExtensionMETS)<br>[`sip: https://dilcis.eu/XML/METS/SIPExtensionMETS`](https://dilcis.eu/XML/METS/SIPExtensionMETS)<br>[`xsi: http://www.w3.org/2001/XMLSchema-instance`](http://www.w3.org/2001/XMLSchema-instance)<br>[`xlink: http://www.w3.org/1999/xlink`](http://www.w3.org/1999/xlink)|
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/@OBJID` |
|-----------------------|-----------|
| Name | Package identifier |
| Description | This is a UUID identifier for the METS document. For the package METS, this MUST be the same UUID as the one used for the entire bag. |
| Datatype | UUID |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/@TYPE` |
|-----------------------|-----------|
| Name | Content category |
| Description | This attribute MUST be set to declare the category of the content held in the SIP. |
| Datatype | String; fixed vocabulary |
| Vocabulary | `Textual works - Print`<br>`Textual works - Digital`<br>`Textual works - Electronic Serials`<br>`Photographs - Print`<br>`Photographs - Digital`<br>`Other Graphic Images - Print`<br>`Other Graphic Images - Digital`<br>`Audio - On Tangible Medium (digital or analog)`<br>`Audio - Media-independent (digital)`<br>`Motion Pictures – Digital and Physical Media`<br>`Video – File-based and Physical Media`<br>`Collection`<br>`Physical object`<br>`Mixed`<br>`OTHER` |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets[@TYPE="OTHER"]/@csip:OTHERTYPE` |
|-----------------------|-----------|
| Name | Other content category |
| Description | When the `mets/@TYPE` attribute is set to "OTHER", the `mets/@csip:OTHERTYPE` attribute SHOULD be used to declare the content category of the package representation not contained in the fixed vocabulary of the `@TYPE` attribute. |
| Datatype | String |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Attribute | `mets/@csip:CONTENTINFORMATIONTYPE` |
|-----------------------|-----------|
| Name | Content information type specification |
| Description | This attribute is used to declare the Content Information Type Specification used when creating the SIP. Its value MUST be set to `OTHER`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets[@csip:CONTENTINFORMATIONTYPE='OTHER']/@csip:OTHERCONTENTINFORMATIONTYPE` |
|-----------------------|-----------|
| Name | Other content information type specification |
| Description | The `mets/@csip:OTHERCONTENTINFORMATIONTYPE` attribute SHOULD be used to further declare the content information type.<br>Meemoo investigates the use of a controlled vocabulary containing all of the allowed content types (corresponding to the different content [profiles](./../profiles/index.html)) for ingest.|
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
| Description | An optional short text describing the contents of the package. |
| Datatype | String |
| Cardinality | 0..1 |
| Obligation | MAY |

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

| Element | `mets/metsHdr` |
|-----------------------|-----------|
| Name | Package header |
| Description | General element that contains descriptive information about the SIP. |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/metsHdr/@CREATEDATE` |
|-----------------------|-----------|
| Name | Package creation datetime |
| Description | This attribute records the date and time the SIP was created. |
| Datatype | EDTF |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/metsHdr/@LASTMODDATE` |
|-----------------------|-----------|
| Name | Package last modification datetime |
| Description | In case the SIP was modified since its creation, this attribute records the date and time of that modification.<br>This attribute MUST be present and filled in when the SIP has been modified since its creation datetime. |
| Datatype | EDTF |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Attribute | `mets/metsHdr/@RECORDSTATUS` |
|-----------------------|-----------|
| Name | Package status |
| Description | A way of indicating the status of the SIP and to instruct meemoo on how to properly handle it.<br>If not set, the expected value is `NEW`.<br>Meemoo investigates the use of the `@RECORDSTATUS` attribute for future use cases such as e.g. a metadata update (i.e. ingest of metadata only with the goal of updating, adding or deleting existing metadata in meemoo's archive system). |
| Datatype | String; fixed vocabulary |
| Vocabulary | `NEW`<br>`SUPPLEMENT`<br>`REPLACEMENT`<br>`TEST`<br>`VERSION`<br>`DELETE`<br>`OTHER`|
| Cardinality | 0..1 |
| Obligation | MAY |

| Attribute | `mets/metsHdr/@csip:OAISPACKAGETYPE` |
|-----------------------|-----------|
| Name | OAIS Package type information |
| Description | The value of `@csip:OAISPACKAGETYPE` MUST be set to `SIP` to indicate to meemoo that the delivered content is a SIP meant for ingest. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/metsHdr/agent` |
|-----------------------|-----------|
| Name | SIP creator software agent |
| Description | A mandatory agent element records the software used to create the package. |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/metsHdr/agent/@ROLE` |
|-----------------------|-----------|
| Name | SIP creator software agent role |
| Description | The role of the SIP creator software agent.<br>This value MUST be set to `CREATOR`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/metsHdr/agent/@TYPE` |
|-----------------------|-----------|
| Name | SIP creator software agent type |
| Description | The type of the SIP creator software agent.<br>This value MUST be set to `OTHER`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/metsHdr/agent/@OTHERTYPE` |
|-----------------------|-----------|
| Name | SIP creator software agent other type |
| Description | A specification of the type of the SIP creator software agent, indicating it being software.<br>This value MUST be set to `SOFTWARE`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/metsHdr/agent/name` |
|-----------------------|-----------|
| Name | SIP creator software agent name |
| Description | This element records the name of the software tool used to create the SIP. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/metsHdr/agent/note` |
|-----------------------|-----------|
| Name | SIP creator software agent additional information |
| Description | The mandatory note element records the version of the software tool used to create the IP.<br>It MUST have a `@csip:NOTETYPE` attribute with the value `SOFTWARE VERSION`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/metsHdr/agent/note[@csip:NOTETYPE='SOFTWARE VERSION']` |
|-----------------------|-----------|
| Name | Classification of the SIP creator software agent additional information |
| Description | The value of this attribute MUST be set to `SOFTWARE VERSION` to denote the software version of the software being used. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/metsHdr/agent` |
|-----------------------|-----------|
| Name | Archival creator agent |
| Description | A wrapper element that enables to encode the name of the person/people or CP that originally created the content being transferred. This can be different from the CP tasked with preparing and sending the SIP to meemoo (cf. 'submitting agent' below). |
| Cardinality | 0..1 |
| Obligation | MAY |

| Attribute | `mets/metsHdr/agent/@ROLE` |
|-----------------------|-----------|
| Name | Archival creator agent role |
| Description | The role of the person/people or CP responsible for the digital content.<br>This value MUST be set to `ARCHIVIST`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/metsHdr/agent/@TYPE` |
|-----------------------|-----------|
| Name | Archival creator agent type |
| Description | The type of the archival creator agent. When the agent is a CP, this value MUST be set to `ORGANIZATION`.|
| Datatype | String; fixed vocabulary |
| Vocabulary | `ORGANIZATION`<br>`INDIVIDUAL`<br>`OTHER` |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/metsHdr/agent/name` |
|-----------------------|-----------|
| Name | Archival creator agent name |
| Description | The name of the CP that originally created the digital content being transferred. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/metsHdr/agent/note` |
|-----------------------|-----------|
| Name | Archival creator agent additional information |
| Description | The archival creator agent MAY have a note providing a unique identification code for the archival creator. |
| Datatype | OR-id |
| Cardinality | 0..1 |
| Obligation | MAY |

| Attribute | `mets/metsHdr/agent/note/@csip:NOTETYPE` |
|-----------------------|-----------|
| Name | Classification of the archival creator agent additional information |
| Description | The archival creator agent note attribute value MUST be set to `IDENTIFICATIONCODE`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/metsHdr/agent` |
|-----------------------|-----------|
| Name | Submitting agent |
| Description | The name of the CP submitting the package to meemoo. |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/metsHdr/agent/@ROLE` |
|-----------------------|-----------|
| Name | Submitting agent role |
| Description | The role of the CP responsible for creating and/or submitting the SIP. This value MUST be set to `CREATOR`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/metsHdr/agent/@TYPE` |
|-----------------------|-----------|
| Name | Submitting agent type |
| Description | The type of the submitting agent. When the agent is a CP, this value MUST be set to `ORGANIZATION`. |
| Datatype | String; fixed vocabulary |
| Vocabulary | `ORGANIZATION`<br>`INDIVIDUAL`<br>`OTHER` |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/metsHdr/agent/name` |
|-----------------------|-----------|
| Name | Submitting agent name |
| Description | Name of the CP or individual submitting the SIP to meemoo. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/metsHdr/agent/note` |
|-----------------------|-----------|
| Name | Submitting agent additional information |
| Description | The submitting agent MUST have a note providing a unique identification code. |
| Datatype | OR-id |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/metsHdr/agent/note/@csip:NOTETYPE` |
|-----------------------|-----------|
| Name | Classification of the submitting agent agent additional information |
| Description | This submitting agent note attribute value MUST be set to `IDENTIFICATIONCODE`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/metsHdr/agent` |
|-----------------------|-----------|
| Name | Contact person agent |
| Description | Optional contact person for meemoo for the submission of the SIP. |
| Cardinality | 0..* |
| Obligation | MAY |

| Attribute | `mets/metsHdr/agent/@ROLE` |
|-----------------------|-----------|
| Name | Contact person agent role |
| Description | The role of the contact person agent MUST be set to `CREATOR`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/metsHdr/agent/@TYPE` |
|-----------------------|-----------|
| Name | Contact person agent type |
| Description | The type of the contact person agent MUST be set to `INDIVIDUAL`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/metsHdr/agent/name` |
|-----------------------|-----------|
| Name | Contact person agent name |
| Description | Name of the contact person. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/metsHdr/agent/note` |
|-----------------------|-----------|
| Name | Contact person agent additional information |
| Description | The contact person agent MAY have one or more notes providing the actual contact information, such as an address, e-mail, telephone number... |
| Datatype | String |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `mets/metsHdr/agent` |
|-----------------------|-----------|
| Name | Preservation agent |
| Description | The CP, organization or person/people that preserve the package. |
| Cardinality | 0..1 |
| Obligation | MAY |

| Attribute | `mets/metsHdr/agent/@ROLE` |
|-----------------------|-----------|
| Name | Preservation agent role |
| Description | The role of the preservation agent MUST be set to `PRESERVATION`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/metsHdr/agent/@TYPE` |
|-----------------------|-----------|
| Name | Preservation agent type |
| Description | The type of the preservation agent. |
| Datatype | String |
| Vocabulary | `ORGANIZATION`<br>`INDIVIDUAL`<br>`OTHER` |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/metsHdr/agent/name` |
|-----------------------|-----------|
| Name | Preservation agent name |
| Description | Name of the preservation agent. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MAY |

| Element | `mets/metsHdr/agent/note` |
|-----------------------|-----------|
| Name | Preservation agent additional information |
| Description | The preservation agent MAY have a note providing a unique identification code. |
| Datatype | String |
| Cardinality | 0..1 |
| Obligation | MAY |

| Attribute | `mets/metsHdr/agent/note/@csip:NOTETYPE` |
|-----------------------|-----------|
| Name | Classification of the preservation agent additional information |
| Description | This preservation agent note attribute value MUST be set to `IDENTIFICATIONCODE`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/metsHdr/altRecordID[@TYPE='SUBMISSIONAGREEMENT']` |
|-----------------------|-----------|
| Name | Submission agreement |
| Description | An optional reference to the submission agreement associated with the SIP.<br>When used, this attribute MUST be set to `SUBMISSIONAGREEMENT`. |
| Datatype | URL |
| Cardinality | 0..1 |
| Obligation | MAY |

| Attribute | `mets/metsHdr/altRecordID[@TYPE='PREVIOUSSUBMISSIONAGREEMENT']` |
|-----------------------|-----------|
| Name | Previous submission agreement |
| Description | An optional reference to a previous submission agreement associated with the SIP.<br>When used, this attribute MUST be set to `PREVIOUSSUBMISSIONAGREEMENT`. |
| Datatype | URL |
| Cardinality | 0..* |
| Obligation | MAY |

| Attribute | `mets/metsHdr/altRecordID[@TYPE='REFERENCECODE']` |
|-----------------------|-----------|
| Name | Archival reference code |
| Description | An optional reference to indicate where in the archival hierarchy the package shall be placed in meemoo's archive.<br>When used, this attribute MUST be set to `REFERENCECODE`. |
| Datatype | URL |
| Cardinality | 0..1 |
| Obligation | MAY |

| Attribute | `mets/metsHdr/altRecordID[@TYPE='PREVIOUSREFERENCECODE']` |
|-----------------------|-----------|
| Name | Previous archival reference code |
| Description | In cases where the SIP originates from other institutions maintaining a reference code structure, this element can be used to record these reference codes and therefore support the provenance of the package when a whole archival description is not submitted with the submission.<br>When used, this attribute MUST be set to `PREVIOUSREFERENCECODE`. |
| Datatype | URL |
| Cardinality | 0..* |
| Obligation | MAY |

### \<dmdSec\> section

The `dmdSec` element (short for 'descriptive metadata section') contains descriptive metadata about the (sub-)IE(s) in the SIP.
Descriptive metadata in the meemoo SIP MUST be contained in dedicated metadata files located in the `/metadata/descriptive` directory of the package level.
This means that the `dmdSec` MUST use `<mdRef>` elements to reference the external metadata files.

***Example***

```xml
<!-- ref to descriptive metadata about IE -->
<dmdSec ID="uuid-786829da-2ad8-4d77-8cf7-157f63227e6b">
  <mdRef  ID="uuid-88191f66-f7ae-42c7-9427-8af2a8e7557f"
          LOCTYPE="URL"
          MDTYPE="OTHER"
          xlink:type="simple"
          xlink:href="./metadata/descriptive/descriptive.xml"
          MIMETYPE="text/xml"
          SIZE="2655"
          CREATED="2022-02-16T10:01:15.014+02:00"
          CHECKSUM="7c513b9cb8848860ddcb4d4b680171bc"
          CHECKSUMTYPE="MD5" />
</dmdSec>
```

***Requirements***

| Element | `mets/dmdSec` |
|-----------------------|-----------|
| Name | Descriptive metadata section |
| Description | Wrapper element that contains a reference to a separate descriptive metadata file in the directory `/metadata/descriptive`.<br>It MUST be used if descriptive metadata for the package content is available. <br>Each `dmdsec` contains a single description and MUST be repeated for multiple descriptions, when available. |
| Cardinality | 0..* |
| Obligation | MUST |

| Attribute | `mets/dmdSec/@ID` |
|-----------------------|-----------|
| Name | Descriptive metadata section identifier |
| Description | A unique identifier for the `dmdSec` used for internal package references.<br>It MUST be unique within the SIP. |
| Datatype | UUID |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/dmdSec/@CREATED` |
|-----------------------|-----------|
| Name | Descriptive metadata creation datetime |
| Description | Creation date and time of the descriptive metadata in this section. |
| Datatype | EDTF |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/dmdSec/@STATUS` |
|-----------------------|-----------|
| Name | Status of the descriptive metadata |
| Description | Describes the status of the `dmdSec` which is supported by the profile.<br>Meemoo investigates the use of the `@STATUS` attribute for future use cases such as e.g. a descriptive metadata update (i.e. ingest of metadata only with the goal of updating, adding or deleting existing metadata in meemoo's archive system). |
| Datatype | String; fixed vocabulary |
| Vocabulary | `CURRENT`<br>`SUPERSEDED` |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Element | `mets/dmdSec/mdRef`
|-----------------------|-----------|
| Name | Reference to the document with the descriptive metadata (when not embedded within the `dmdSec`) |
| Description | Reference to the descriptive metadata file(s) when located in the `/metadata/descriptive directory`. |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Attribute | `mets/dmdSec/mdRef[@LOCTYPE='URL']` |
|-----------------------|-----------|
| Name | Type of locator |
| Description | Indication of the locator type used to refer to the descriptive metadata file in the /metadata/descriptive directory.<br>It MUST always be used with the value `URL`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/dmdSec/mdRef[@xlink:type='simple']` |
|-----------------------|-----------|
| Name | Type of link |
| Description | This attribute's value MUST be set to `simple`, in order to indicate a simple 'HTML-like' link. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/dmdSec/mdRef/@xlink:href` |
|-----------------------|-----------|
| Name | Resource location |
| Description | Indication of the actual location of the descriptive metadata file.<br>As indicated by the `@LOCTYPE` attribute, this filepath MUST be a URL type filepath.  |
| Datatype | URL |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/dmdSec/mdRef/@MDTYPE` |
|-----------------------|-----------|
| Name | Type of descriptive metadata |
| Description | Specification of the type of metadata that is used in the externally located descriptive metadata file(s) in the `/metadata/descriptive` directory. |
| Datatype | String; fixed vocabulary |
| Vocabulary | `MODS`<br>`DC`<br>`PREMIS`<br>`METSRIGHTS`<br>`OTHER` |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/dmdSec/mdRef/@MIMETYPE` |
|-----------------------|-----------|
| Name | File mime type |
| Description | The media/mime type of the referenced file. |
| Datatype | IANA mime type |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/dmdSec/mdRef/@SIZE` |
|-----------------------|-----------|
| Name | File size |
| Description | Size of the referenced file; this MUST be in bytes. |
| Datatype | Integer |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/dmdSec/mdRef/@CREATED` |
|-----------------------|-----------|
| Name | File creation datetime |
| Description | The creation date and time of the referenced file. |
| Datatype | EDTF |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/dmdSec/mdRef/@CHECKSUM` |
|-----------------------|-----------|
| Name | File checksum |
| Description | The checksum of the referenced file. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/dmdSec/mdRef/@CHECKSUMTYPE` |
|-----------------------|-----------|
| Name | File checksum type |
| Description | A value from the METS-standard which identifies the algorithm used to calculate the checksum for the referenced file. This MUST be set to `MD5`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

### \<amdSec\> section

The `amdSec` element (short for 'administrative metadata section') contains preservation metadata about the (sub-)IE(s) in the SIP and about the SIP as a whole.
Preservation data in the meemoo SIP MUST be contained in dedicated metadata files located in the `metadata/preservation` directory of the package-level.

***Example***

```xml
<!-- ref to the PREMIS metadata about IE/subIE(s)/package -->
<amdSec ID="b9143f83-2567-4122-a55c-87389e6263ec">
  <digiprovMD ID="uuid-3f8709ad-2c02-48a2-9fb4-871df03cb929">
    <mdRef  ID="uuid-bf966b2c-c1a2-4c75-aae6-18877d2f58cc"
            LOCTYPE="URL"
            MDTYPE="PREMIS"
            xlink:type="simple"
            xlink:href="./metadata/preservation/preservation.xml"
            MIMETYPE="text/xml"
            SIZE="6277"
            CREATED="2022-02-16T10:01:15.014+02:00"
            CHECKSUM="8c2914e1df1e2827c9c4059804075120"
            CHECKSUMTYPE="MD5" />
  </digiprovMD>
</amdSec>
```

***Requirements***

| Element | `mets/amdSec` |
|-----------------------|-----------|
| Name | Administrative metadata section |
| Description | Wrapper element that contains a reference to a separate preservation metadata file in the directory `/metadata/preservation`.<br>It MUST be used if preservation metadata for the package content is available.<br>All preservation metadata MUST be present in a single metadata file, resulting in a single `amdSec` element. |
| Cardinality | 0..1 |
| Obligation | MUST |

| Element | `mets/amdSec/digiprovMD` |
|-----------------------|-----------|
| Name | Digital provenance metadata |
| Description | Wrapper element for including preservation information using the PREMIS standard.<br>Each piece of PREMIS metadata MUST be included in a separate `digiprovMD` element.|
| Cardinality | 0..* |
| Obligation | MUST |

| Attribute | `mets/amdSec/digiprovMD/@ID` |
|-----------------------|-----------|
| Name | Digital provenance metadata identifier |
| Description | A unique identifier used for internal package references.<br>It MUST be unique within the SIP. |
| Datatype | UUID |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/amdSec/digiprovMD/@STATUS` |
|-----------------------|-----------|
| Name | Status of the digital provenance metadata |
| Description | Describes the status of the `digiprovMD` which is supported by the profile.<br>Meemoo investigates the use of the `@STATUS` attribute for future use cases such as e.g. a preservation metadata update (i.e. ingest of metadata only with the goal of updating, adding or deleting existing metadata in meemoo's archive system). |
| Datatype | String; fixed vocabulary |
| Vocabulary | `CURRENT`<br>`SUPERSEDED` |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Element | `mets/amdSec/digiprovMD/mdRef` |
|-----------------------|-----------|
| Name | Reference to the file with the preservation metadata. |
| Description | Reference to the preservation metadata file(s) when located in the `/metadata/preservation` directory. |
| Cardinality | 0..1 |
| Obligation | MUST |

| Attribute | `mets/amdSec/digiprovMD/mdRef[@LOCTYPE='URL']` |
|-----------------------|-----------|
| Name | Type of locator |
| Description | Indication of the locator type used to refer to the preservation metadata file in the `/metadata/preservation` directory.<br>It MUST always be used with the value `URL`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/amdSec/digiprovMD/mdRef[@xlink:type='simple']` |
|-----------------------|-----------|
| Name | Type of link |
| Description | This attribute's value MUST be set to `simple`, in order to indicate a simple 'HTML-like' link. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/amdSec/digiprovMD/mdRef/@xlink:href` |
|-----------------------|-----------|
| Name | Resource location |
| Description | Indication of the actual location of the preservation metadata file.<br>As indicated by the `@LOCTYPE` attribute, this filepath MUST be a URL type filepath. |
| Datatype | URL |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/amdSec/digiprovMD/mdRef/@MDTYPE` |
|-----------------------|-----------|
| Name | Type of preservation metadata |
| Description | Specification of the type of metadata that is used in the externally located preservation metadata file in the `/metadata/preservation directory`. |
| Datatype | String; fixed vocabulary |
| Vocabulary | `MODS`<br>`DC`<br>`PREMIS`<br>`METSRIGHTS`<br>`OTHER` |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/amdSec/digiprovMD/mdRef/@MIMETYPE` |
|-----------------------|-----------|
| Name | File mime type |
| Description | The media/mime type of the referenced file. |
| Datatype | IANA mime type |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/amdSec/digiprovMD/mdRef/@SIZE` |
|-----------------------|-----------|
| Name | File size |
| Description | Size of the referenced file; this MUST be in bytes. |
| Datatype | Integer |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/amdSec/digiprovMD/mdRef/@CREATED` |
|-----------------------|-----------|
| Name | File creation datetime |
| Description | The creation date and time of the referenced file. |
| Datatype | EDTF |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/amdSec/digiprovMD/mdRef/@CHECKSUM` |
|-----------------------|-----------|
| Name | File checksum |
| Description | The checksum of the referenced file. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/amdSec/digiprovMD/mdRef/@CHECKSUMTYPE` |
|-----------------------|-----------|
| Name | File checksum type |
| Description | A value from the METS-standard which identifies the algorithm used to calculate the checksum for the referenced file. This MUST be set to `MD5`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/amdSec/rightsMD` |
|-----------------------|-----------|
| Name | Rights metadata |
| Description | A simple rights statement may be used to describe general permissions for the package.<br><br>Individual representations SHOULD state their specific rights in their representation `mets.xml` file.<br>Standards for rights metadata include [RightsStatements.org](http://rightsstatements.org/), [Europeana rights statements info](https://pro.europeana.eu/page/available-rights-statements), [METS Rights Schema](https://github.com/mets/METS-Rights-Schema) and [PREMIS Rights Entities](https://www.loc.gov/standards/premis/v3/premis-3-0-final.pdf#page=188).|
| Cardinality | 0..* |
| Obligation | MAY |

| Attribute | `mets/amdSec/rightsMD/@ID` |
|-----------------------|-----------|
| Name | Rights metadata identifier |
| Description | A unique identifier used for internal package references.<br>It MUST be unique within the SIP. |
| Datatype | UUID |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/amdSec/rightsMD/@STATUS` |
|-----------------------|-----------|
| Name | Status of the rights metadata |
| Description | Describes the status of the `digiprovMD` which is supported by the profile.<br>Meemoo investigates the use of the `@STATUS` attribute for future use cases such as e.g. a rights metadata update (i.e. ingest of metadata only with the goal of updating, adding or deleting existing metadata in meemoo's archive system). |
| Datatype | String; fixed vocabulary |
| Vocabulary | `CURRENT`<br>`SUPERSEDED` |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Element | `mets/amdSec/rightsMD/mdRef` |
|-----------------------|-----------|
| Name | Reference to the document with the rights metadata (when not embedded within the mets.xml file). |
| Description | Reference to the rights metadata file(s) when located in the `/metadata/preservation` directory. |
| Cardinality | 0..1 |
| Obligation | MUST |

| Attribute | `mets/amdSec/rightsMD/mdRef[@LOCTYPE='URL']` |
|-----------------------|-----------|
| Name | Type of locator |
| Description | Indication of the locator type used to refer to the rights metadata file in the `/metadata/preservation` directory.<br>It MUST always be used with the value `URL`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/amdSec/rightsMD/mdRef[@xlink:type='simple']` |
|-----------------------|-----------|
| Name | Type of link |
| Description | This attribute's value MUST be set to `simple`, in order to indicate a simple 'HTML-like' link. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/amdSec/rightsMD/mdRef/@xlink:href` |
|-----------------------|-----------|
| Name | Resource location |
| Description | Indication of the actual location of the rights metadata file.<br>As indicated by the `@LOCTYPE` attribute, this filepath MUST be a URL type filepath. |
| Datatype | URL |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/amdSec/rightsMD/mdRef/@MDTYPE` |
|-----------------------|-----------|
| Name | Type of preservation metadata |
| Description | Specification of the type of metadata that is used in the externally located rights metadata file in the `/metadata/preservation` directory. |
| Datatype | String; fixed vocabulary |
| Vocabulary | `PREMIS`<br>`METSRIGHTS`<br>`OTHER` |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/amdSec/rightsMD/mdRef/@MIMETYPE` |
|-----------------------|-----------|
| Name | File mime type |
| Description | The media/mime type of the referenced file. |
| Datatype | IANA mime type |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/amdSec/rightsMD/mdRef/@SIZE` |
|-----------------------|-----------|
| Name | File size |
| Description | Size of the referenced file; this MUST be in bytes. |
| Datatype | Integer |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/amdSec/rightsMD/mdRef/@CREATED` |
|-----------------------|-----------|
| Name | File creation datetime |
| Description | The creation date and time of the referenced file. |
| Datatype | EDTF |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/amdSec/rightsMD/mdRef/@CHECKSUM` |
|-----------------------|-----------|
| Name | File checksum |
| Description | The checksum of the referenced file. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/amdSec/rightsMD/mdRef/@CHECKSUMTYPE` |
|-----------------------|-----------|
| Name | File checksum type |
| Description | A value from the METS-standard which identifies the algorithm used to calculate the checksum for the referenced file. This MUST be set to `MD5`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

### \<fileSec\> section

The `fileSec` element (short for 'file section') lists all files of the package level in the SIP.
It contains references to the representation `mets.xml` files of the different representations, but does not list other files of those representations.
The listing of other representation files (i.e. metadata files and media files) is left to the respective representation `mets.xml` files.

***Example***

```xml
<fileSec ID="uuid-0c53fd9b-f640-4def-a872-2e4622f691d9">
    <fileGrp USE="root" ID="uuid-6c78980c-bdfc-4e2e-b19a-579e5b285055">
        <fileGrp USE="metadata" ID="uuid-bd087c44-ee3f-48e9-9031-9190a60c8e13">
            <fileGrp USE="metadata/descriptive" ID="uuid-5194aca6-97b6-448c-b385-b892bc0c362c">
                <file ID="uuid-c6a678a7-b4b0-45af-a7d4-33123d9f0911" MIMETYPE="text/xml" SIZE="2655" CREATED="2022-02-16T10:01:15.014+02:00" CHECKSUM="7c513b9cb8848860ddcb4d4b680171bc" CHECKSUMTYPE="MD5">
                    <FLocat LOCTYPE="URL" xlink:type="simple" xlink:href="./metadata/descriptive/descriptive.xml" />
                </file>
            </fileGrp>
            <fileGrp USE="metadata/preservation" ID="uuid-caea98b8-ae09-412d-8f25-dd50ba6a30cd">
                <file ID="uuid-4ac13924-fe19-4711-b51f-6b5acc692ec0" MIMETYPE="text/xml" SIZE="6277" CREATED="2022-02-16T10:01:15.014+02:00" CHECKSUM="8c2914e1df1e2827c9c4059804075120" CHECKSUMTYPE="MD5">
                    <FLocat LOCTYPE="URL" xlink:type="simple" xlink:href="./metadata/preservation/preservation.xml" />
                </file>
            </fileGrp>
        </fileGrp>
        <fileGrp USE="representations" ID="uuid-779319d9-cc1f-41b3-a49e-28d169e0d066">
            <fileGrp USE="representations/representation_1" ID="uuid-700c97da-3164-4863-9e58-d6d62156052e">
                <file ID="uuid-0fe40ffc-b5f3-465e-af3a-d266d94453b7" MIMETYPE="text/xml" SIZE="4295" CREATED="2022-02-16T10:01:15.014+02:00" CHECKSUM="b31b2224cef22b22d29f62a03f30aaa3" CHECKSUMTYPE="MD5">
                    <FLocat LOCTYPE="URL" xlink:type="simple" xlink:href="./representations/representation_1/mets.xml" />
                </file>
            </fileGrp>
            <fileGrp USE="representations/representation_2" ID="uuid-c0fed1c6-96c8-4f15-9e82-abc7be2e981c">
                <file ID="uuid-625629a4-e5f8-4087-9114-66e4a943bf50" MIMETYPE="text/xml" SIZE="3896" CREATED="2022-02-16T10:01:15.014+02:00" CHECKSUM="2f3f71fadf038f86ba512c16702af864" CHECKSUMTYPE="MD5">
                    <FLocat LOCTYPE="URL" xlink:type="simple" xlink:href="./representations/representation_2/mets.xml" />
                </file>
            </fileGrp>
        </fileGrp>
    </fileGrp>
</fileSec>
```

***Requirements***

- There MUST NOT be more than one `fileSec` element in the `mets.xml` file.
- The `fileSec` element of the package `mets.xml` file MUST NOT reference anything from the different representation levels, EXCEPT the representation `mets.xml` files.
- Each representation `mets.xml` MUST be referenced within its own `fileGrp` element within the `fileSec` element of the package `mets.xml`.

| Element | `mets/fileSec` |
|-----------------------|-----------|
| Name | mets/fileSec |
| Description | Wrapper element for the file section of the METS which contains different `fileGrp` elements which acts as an inventory of the package level and its content.<br>Only a single `fileSec` element should be present. |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Attribute | `mets/fileSec/@ID` |
|-----------------------|-----------|
| Name | File section identifier |
| Description | A unique identifier for the file section used for internal package references.<br>It MUST be unique within the SIP. |
| Datatype | UUID |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/fileSec/fileGrp[@USE='Documentation']` |
|-----------------------|-----------|
| Name | Documentation file group |
| Description | All documentation pertaining to the transferred content is placed in one or more file group elements with `mets/fileSec/fileGrp/@USE` attribute value “Documentation”. The content of this element MAY be empty. |
| Cardinality | 1..* |
| Obligation | MUST |

| Attribute | `mets/fileSec/fileGrp[@USE='Schemas']` |
|-----------------------|-----------|
| Name | Schema file group |
| Description | XML schemas used in the information package can be included in one or more file groups with `mets/fileSec/fileGrp/@USE` attribute value “Schemas”. The content of this element MAY be empty. |
| Cardinality | 1..* |
| Obligation | MUST |

| Attribute | `mets/fileSec/fileGrp[@USE=[starts-with('Representations')]]` |
|-----------------------|-----------|
| Name | Representations file group |
| Description | A pointer to the METS document describing the representation or pointers to the content being transferred must be present in one or more file groups with `mets/fileSec/fileGrp/@USE` attribute value starting with `Representations` followed by the path to the folder where the _representation level_ `mets.xml` file is placed. |
| Cardinality | 1..* |
| Obligation | MUST |

| Attribute | `mets/fileSec/fileGrp/@ADMID` |
|-----------------------|-----------|
| Name | Reference to administrative metadata |
| Description | Reference to the ID of the corresponding administrative metadata section, in case an `amdSec` was used. |
| Datatype | UUID |
| Cardinality | 0..1 |
| Obligation | MAY |

| Attribute | `mets/@csip:CONTENTINFORMATIONTYPE="MIXED"|mets/fileSec/fileGrp[@USE=[starts-with('Representations')]]/@csip:CONTENTINFORMATIONTYPE` |
|-----------------------|-----------|
| Name | Content Information Type Specification |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Attribute | `mets/fileSec/fileGrp[@csip:CONTENTINFORMATIONTYPE='OTHER']/@csip:OTHERCONTENTINFORMATIONTYPE` |
|-----------------------|-----------|
| Name | Other Content Information Type Specification |
| Description | When the `mets/fileSec/fileGrp/@csip:CONTENTINFORMATIONTYPE` attribute has the value `OTHER` the attribute `mets/fileSec/fileGrp/@csip:OTHERCONTENTINFORMATIONTYPE` must state a value for the Content Information Type Specification used. |
| Cardinality | 0..1 |
| Obligation | MAY |

| Attribute | `mets/fileSec/fileGrp/@USE` |
|-----------------------|-----------|
| Name | Description of the use of the file group |
| Description | The value in the `mets/fileSec/fileGrp/@USE` attribute is the name of the whole folder structure to the data, e.g. `representations/representation_1` or `documentation`. |
| Datatype | URL |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/fileSec/fileGrp/@ID` |
|-----------------------|-----------|
| Name | File group identifier |
| Description | A unique identifier for the file group. This is used for internal package references.<br>It MUST be unique within the SIP. |
| Datatype | UUID |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/fileSec/fileGrp/file` |
|-----------------------|-----------|
| Name | File |
| Description | The `file` elements contain descriptions of the media files. |
| Cardinality | 1..* |
| Obligation | MUST |

| Attribute | `mets/fileSec/fileGrp/file/@ID` |
|-----------------------|-----------|
| Name | File identifier |
| Description | A unique identifier for the file. This is used for internal package references.<br>It MUST be unique within the SIP. |
| Datatype | UUID |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/fileSec/fileGrp/file/@MIMETYPE` |
|-----------------------|-----------|
| Name | File mimetype |
| Description | The media/mime type of the referenced file. |
| Datatype | IANA mime type |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/fileSec/fileGrp/file/@SIZE` |
|-----------------------|-----------|
| Name | File size |
| Description | Size of the referenced file; this MUST be in bytes. |
| Datatype | Integer |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/fileSec/fileGrp/file/@CREATED` |
|-----------------------|-----------|
| Name | File creation datetime |
| Description | The creation date and time of the referenced file. |
| Datatype | EDTF |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/fileSec/fileGrp/file/@CHECKSUM` |
|-----------------------|-----------|
| Name | File checksum |
| Description | The checksum of the referenced file. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/fileSec/fileGrp/file/@CHECKSUMTYPE` |
| Name | File checksum type |
| Description | A value from the METS-standard which identifies the algorithm used to calculate the checksum for the referenced file. This MUST be set to `MD5`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/fileSec/fileGrp/file/@OWNERID` |
|-----------------------|-----------|
| Name | File original identification |
| Description | If an identifier for the file was supplied by the CP it can be recorded in this attribute. |
| Datatype | String |
| Cardinality | 0..1 |
| Obligation | MAY |

| Attribute | `mets/fileSec/fileGrp/file/@ADMID` |
|-----------------------|-----------|
| Name | File reference to administrative metadata |
| Description | If an `amdSec` (with `@ID` attribute) was provided, this attribute allows to reference it. |
| Datatype | UUID |
| Cardinality | 0..1 |
| Obligation | MAY |

| Attribute | `mets/fileSec/fileGrp/file/@DMDID` |
|-----------------------|-----------|
| Name | File reference to descriptive metadata |
| Description | If a `dmdSec` (with `@ID` attribute) was provided, this attribute allows to reference it. |
| Datatype | UUID |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `mets/fileSec/fileGrp/file/FLocat` |
|-----------------------|-----------|
| Name | File locator reference |
| Description | Element that allows for referencing the location of each external file. |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/fileSec/fileGrp/file/FLocat[@LOCTYPE='URL']` |
|-----------------------|-----------|
| Name | Type of locator |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/fileSec/fileGrp/file/FLocat[@xlink:type='simple']` |
|-----------------------|-----------|
| Name | Type of link |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/fileSec/fileGrp/file/FLocat/@xlink:href` |
|-----------------------|-----------|
| Name | Resource location |
| Description | One SHOULD use the relative location of the file in this URL. |
| Datatype | URL |
| Cardinality | 1..1 |
| Obligation | MUST |

### \<structMap\> section

The `structMap` element outlines the hierarchical structure of the package level of the SIP.
It provides links between elements and metadata files located elsewhere in the package level.

***Example***

```xml
<structMap ID="uuid-1ce2cef4-cb9a-4649-8983-c916870cf2b4" TYPE="PHYSICAL" LABEL="CSIP">
    <div ID="uuid-33cd69c8-b297-40e1-9491-1b5db58890bd" LABEL="">
        <div ID="uuid-c0a73bbc-d6f3-42a0-b5e1-f53a4601101b" LABEL="metadata">
            <div ID="uuid-9aae35c0-9d17-43c7-824a-4722ef3039cd" LABEL="descriptive">
                <fptr FILEID="uuid-c6a678a7-b4b0-45af-a7d4-33123d9f0911" />
            </div>
            <div ID="uuid-ee9ce21e-8264-45cc-b877-7e266647a335" LABEL="preservation">
                <fptr FILEID="uuid-4ac13924-fe19-4711-b51f-6b5acc692ec0" />
            </div>
        </div>
        <div ID="uuid-17ff6cea-cd84-46ad-b9a8-250809f9e2c7" LABEL="representations">
            <div ID="uuid-c5cab13b-aced-4024-bbc3-d38c682602d2" LABEL="representation_1">
                <mptr xlink:type="simple" xlink:href="./representations/representation_1/mets.xml" LOCTYPE="URL" />
            </div>
            <div ID="uuid-daeba358-46ee-4363-b2a2-bd745c128f6f" LABEL="representation_2">
                <mptr xlink:type="simple" xlink:href="./representations/representation_2/mets.xml" LOCTYPE="URL" />
            </div>
        </div>
    </div>
</structMap>
```

***Requirements***

| Element | `mets/structMap` |
|-----------------------|-----------|
| Name | Structural description of the package |
| Description | The `structMap` describes the highest logical structure of the IP. |
| Cardinality | 1..* |
| Obligation | MUST |

| Attribute | `mets/structMap[@TYPE='PHYSICAL']` |
|-----------------------|-----------|
| Name | Type of structural description |
| Description | The `mets/structMap/@TYPE` attribute MUST take the value `PHYSICAL`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/structMap[@LABEL='CSIP']` |
|-----------------------|-----------|
| Name | Name of the structural description |
| Description | This value MUST be set to `CSIP` in order to be compliant with the E-ARK Common Specification for Information Packages. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/structMap[@LABEL='CSIP']/@ID` |
|-----------------------|-----------|
| Name | Structural description identifier |
| Description | A unique identifier for the structural description. This can be used for internal package references. |
| Datatype | UUID |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/structMap[@LABEL='CSIP']/div` |
|-----------------------|-----------|
| Name | Main structural division |
| Description | The division element. Each `structMap` element MUST contain one `div` element that contains possible further `div` elements of the `structMap` elements. |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/structMap[@LABEL='CSIP']/div/@ID` |
|-----------------------|-----------|
| Name | Main structural division identifier |
| Description | A unique identifier for the main `div` element. This can be used for internal package references.<br>It MUST be unique within the SIP. |
| Datatype | UUID |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Metadata']` |
|-----------------------|-----------|
| Name | Metadata division |
| Description | The metadata referenced in the administrative and/or descriptive metadata section is described in the structural map with one sub division. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Metadata']/@ID` |
|-----------------------|-----------|
| Name | Metadata division identifier |
| Description | A unique identifier for the metadata `div` element. This can be used for internal package references.<br>It MUST be unique within the SIP. |
| Datatype | UUID |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Metadata']` |
|-----------------------|-----------|
| Name | Metadata division label |
| Description | The metadata `div` element’s `@LABEL` attribute value MUST be `Metadata`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Metadata']/@ADMID` |
|-----------------------|-----------|
| Name | Metadata division references administrative metadata |
| Description | The administrative metadata division should reference all current administrative metadata sections.<br>All `amdSec` elements with `@STATUS='CURRENT'` SHOULD be referenced by their identifier, `@ID`. <br> The current `amdSec` elements' `@ID`s are recorded in the `div[@LABEL='Metadata']/@ADMID` attribute in a space delimited list. |
| Datatype | UUID |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Attribute | `mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Metadata']/@DMDID` |
|-----------------------|-----------|
| Name | Metadata division references descriptive metadata |
| Description | The descriptive metadata division should reference all current descriptive metadata sections.<br>All `dmdSec` elements with `@STATUS='CURRENT'` SHOULD be referenced by their identifier, `@ID`. <br> The current `dmdSec` elements' `@ID`s are recorded in the `div[@LABEL='Metadata']/@DMDID` attribute in a space delimited list. |
| Datatype | UUID |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Attribute | `mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Documentation']` |
|-----------------------|-----------|
| Name | Documentation division |
| Description | The documentation referenced in the file section file groups is described in the structural map with one sub division. |
| Datatype | String |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Attribute | `mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Documentation']/@ID` |
|-----------------------|-----------|
| Name | Documentation division identifier |
| Description | A unique identifier for the documentation `div` element. This can be used for internal package references. |
| Datatype | UUID |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Documentation']` |
|-----------------------|-----------|
| Name | Documentation division label |
| Description | The documentation `div` element’s `@LABEL` attribute value MUST be `Documentation`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Documentation']/fptr` |
|-----------------------|-----------|
| Name | Documentation file references |
| Description | All file groups containing documentation described in the package are referenced via the relevant file group identifiers. <br>There MUST be one file group reference per `fptr` element. |
| Cardinality | 0..* |
| Obligation | MUST |

| Attribute | `mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Documentation']/fptr/@FILEID` |
|-----------------------|-----------|
| Name | Documentation file group reference pointer |
| Description | A unique identifier to the `Documentation` file group. This can be used for internal package references. |
| Datatype | UUID |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Schemas']` |
|-----------------------|-----------|
| Name | Schema division |
| Description | The schemas referenced in the file section file groups are described in the structural map within a single sub-division. |
| Datatype | String |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Attribute | `mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Schemas']/@ID` |
|-----------------------|-----------|
| Name | Schema division identifier |
| Description | A unique identifier to the `Schemas` file group. This can be used for internal package references. |
| Datatype | UUID |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Schemas']` |
|-----------------------|-----------|
| Name | Schema division label |
| Description | The schemas `div` element’s `@LABEL` attribute value MUST be `Schemas`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Schemas']/fptr` |
|-----------------------|-----------|
| Name | Schema file reference |
| Description | All file groups containing schemas described in the package are referenced via the relevant file group identifiers. <br>There MUST be one file group reference per `fptr` element. |
| Cardinality | 0..* |
| Obligation | MUST |

| Attribute | `mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Schemas']/fptr/@FILEID` |
|-----------------------|-----------|
| Name | Schema file group reference |
| Description | A unique identifier to the `Schemas` file group. This can be used for internal package references. |
| Datatype | UUID |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Representations']` |
|-----------------------|-----------|
| Name | Content division |
| Description | When no representations are present the content referenced in the file section file group with `@USE` attribute value, `Representations` is described in the structural map as a single sub division. |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Attribute | `mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Representations']/@ID` |
|-----------------------|-----------|
| Name | Content division identifier |
| Description | A unique identifier to the `Representations` file group. This can be used for internal package references. |
| Datatype | UUID |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Representations']` |
|-----------------------|-----------|
| Name | Content division label |
| Description | The representations `div` element’s `@LABEL` attribute value MUST be `Representations`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Representations']/fptr` |
|-----------------------|-----------|
| Name | Content division file references |
| Description | All file groups containing content described in the package are referenced via the relevant file group identifiers.<br>There MUST be one file group reference per `fptr` element. |
| Cardinality | 0..* |
| Obligation | MUST |

| Attribute | `mets/structMap[@LABEL='CSIP']/div/div[@LABEL='Representations']/fptr/@FILEID` |
|-----------------------|-----------|
| Name | Content division file group references |
| Description | The pointer to the identifier for the `Representations` file group. |
| Datatype | UUID |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/structMap[@LABEL='CSIP']/div/div` |
|-----------------------|-----------|
| Name | Representation division |
| Description | When a package consists of multiple representations, each described by a representation level mets.xml file, there should be a discrete representation `\div` element for each representation. <br> Each representation `div` references the representation level `mets.xml` file, documenting the structure of the representation and its content. |
| Cardinality | 0..* |
| Obligation | SHOULD |

| Attribute | `mets/structMap[@LABEL='CSIP']/div/div/@ID` |
|-----------------------|-----------|
| Name | Representations division identifier |
| Description | A unique identifier that can be used for internal package references. |
| Datatype | UUID |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/structMap[@LABEL='CSIP']/div/div/@LABEL` |
|-----------------------|-----------|
| Name | Representations division label |
| Description | The package’s representation division `div` element `@LABEL` attribute value must be the path to the representation level mets.xml file starting with the value `Representations` followed by the main folder name, e.g. `Representations/representation_1`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/structMap[@LABEL='CSIP']/div/div/mptr/@xlink:title` |
|-----------------------|-----------|
| Name | Representations division file references |
| Description | The file group containing the files described in the package are referenced via the relevant file group identifier. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mets/structMap[@LABEL='CSIP']/div/div/mptr` |
|-----------------------|-----------|
| Name | Representation METS pointer |
| Description | The division `div` of the specific representation includes one occurrence of the METS pointer `mptr` element, pointing to the appropriate representation `mets.xml` file. |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/structMap/div/div/mptr/@xlink:href` |
|-----------------------|-----------|
| Name | Resource location |
| Description | Indication of the actual location of the `mets.xml` file.<br>As indicated by the `@LOCTYPE` attribute, this filepath MUST be a URL type filepath.<br>One SHOULD use the relative location of the file in this URL. |
| Datatype | URL |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/structMap/div/div/mptr[@xlink:type='simple']` |
|-----------------------|-----------|
| Name | Type of link |
| Description | This attribute's value MUST be set to `simple`, in order to indicate a simple 'HTML-like' link. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mets/structMap/div/div/mptr[@LOCTYPE='URL']` |
|-----------------------|-----------|
| Name | Type of locator |
| Description | Indication of the locator type used to refer to the representation mets.xml files of the different representation levels.<br>It MUST always be used with the value `URL`. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

## /metadata (directory)

The `/metadata` directory contains both descriptive and preservation metadata about the (sub-)IE(s) at the package level.
It also contains preservation metadata about the SIP as a whole.

***Requirements***

- The `/metadata` directory MUST contain exactly two subdirectories: `/descriptive` and `/preservation`.

### /descriptive (directory)

The `/descriptive` directory contains descriptive metadata about the (sub-)IE(s) at the package level.

***Requirements***

- The `/descriptive` directory MUST contain exactly one file: `descriptive.xml`.

The `descriptive.xml` file at the package-level contains descriptive metadata about the (sub-)IE(s) of the SIP.
It relies on the [PREMIS for Preservation Metadata](https://www.loc.gov/standards/premis/v3/) schema and the [Dublin Core Metadata Initiative Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) schema in order to facilitate a basic description with a limited number of descriptive metadata elements.

Descriptive metadata about one or more (sub-)IEs is divided into separate `<premis:object>` elements with unique identifiers.
This allows for describing all (sub-)IEs in one and the same descriptive metadata file, using multiple `<premis:object>` elements.
The link between the `<premis:object>` elements in the descriptive metadata and the `<premis:object>` elements in the preservation metadata (in the `preservation.xml` in `/data/metadata/preservation`) is made using shared UUIDs in the `<premis:objectIdentifier>` elements of both files.

***Example***

```xml
<?xml version='1.0' encoding='UTF-8'?>
<premis:premis xmlns:dcterms="http://purl.org/dc/terms/" xmlns:premis="http://www.loc.gov/premis/v3" xmlns:xs="http://www.w3.org/2001/XMLSchema/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance/">

  <premis:object>

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-b21a86aa-97a3-4f7b-a9f5-4d330af641c0</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- general title for the resource -->
    <dcterms:title>Felis Catus Flamens</dcterms:title>

    <!-- id for the FCF in an imaginary cat database -->
    <dcterms:identifier>FCatus_FelisCatusFlamens_01</dcterms:identifier>

    <!-- date unknown -->
    <dcterms:created xsi:type="edtf">XXXX</dcterms:created>

    <!-- multiple keywords about the resource -->
    <dcterms:subject>Cat</dcterms:subject>
    <dcterms:subject>Felis Catus Flamens</dcterms:subject>

  </premis:object>

  <premis:object>

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-948e2213-ca54-459c-8c87-5818adeb9444</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- general title for the resource -->
    <dcterms:title>Felis Catus Flamens lying on a sofa</dcterms:title>

    <!-- id for the FCF in an imaginary cat database -->
    <dcterms:identifier>FCatus_FelisCatusFlamens_Sofa_01</dcterms:identifier>

    <!-- date unknown -->
    <dcterms:created xsi:type="edtf">XXXX</dcterms:created>

    <!-- multiple keywords about the resource -->
    <dcterms:subject>Cat</dcterms:subject>
    <dcterms:subject>Felis Catus Flamens</dcterms:subject>
    <dcterms:subject>Sofa</dcterms:subject>

  </premis:object>

  <premis:object>

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-01d59d41-f523-4d06-a549-4bf6f7cef853</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- general title for the resource -->
    <dcterms:title>Felis Catus Flamens sitting on a cat tree</dcterms:title>

    <!-- id for the FCF in an imaginary cat database -->
    <dcterms:identifier>FCatus_FelisCatusFlamens_CatTree_01</dcterms:identifier>

    <!-- date unknown -->
    <dcterms:created xsi:type="edtf">XXXX</dcterms:created>

    <!-- multiple keywords about the resource -->
    <dcterms:subject>Cat</dcterms:subject>
    <dcterms:subject>Felis Catus Flamens</dcterms:subject>
    <dcterms:subject>Cat tree</dcterms:subject>

  </premis:object>

</premis:premis>  
```

***Requirements***

- The `descriptive.xml` file MUST only use the [PREMIS for Preservation Metadata](https://www.loc.gov/standards/premis/v3/) and [Dublin Core Metadata Initiative Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) schemas and MUST NOT use any other metadata schemas.
- The `descriptive.xml` file MUST declare the PREMIS and DC Terms namespaces in its root element.
- The `descriptive.xml` file MUST use the `<premis:premis/>` tag as its root element.
- The `descriptive.xml` file MUST use `<premis:object/>` elements for each separate (sub-)IE that is described.
- All descriptive metadata in the `descriptive.xml` file MUST be embedded in `<premis:object/>` elements.
- The `descriptive.xml` file MUST include the DC Terms elements outlined in the table below; besides these mandatory elements it MAY use all other terms from the DC Terms schema.
- The `descriptive.xml` file MUST adhere to the restrictions on cardinality of terms outlined in the table below; if a term is not listed with a restriction on cardinality, it MAY be used multiple times.

| Element | `premis:premis` |
|-----------------------|-----------|
| Name | DC root element |
| Description | This root element MUST contain [the XML schema namespace of DCMI Metadata Terms](https://www.dublincore.org/schemas/xmls/qdc/dcterms.xsd).<br>It MUST NOT contain any other XML schema namespaces besides DCMI Metadata Terms.<br>It MUST NOT contain any attributes. |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object/dcterms:identifier` |
|-----------------------|-----------|
| Name | Identifier |
| Description | An unambiguous and unique reference to the Intellectual Entity/Entities and/or Representation(s) present in the SIP.<br>This identifier stems from the local identification system of the content partner. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object/dcterms:created` |
|-----------------------|-----------|
| Name | Creation date |
| Description | Creation date of the resource. |
| Datatype | EDTF |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object/dcterms:description` |
|-----------------------|-----------|
| Name | Description |
| Description | An account of the resource.<br>The `description` term MAY be used multiple times when it uses a different language.<br>The language of the description MUST be provided by a `@XML:LANG` attribute. This attribute MUST use a controlled vocabulary such as [ISO 639-2](https://www.loc.gov/standards/iso639-2/php/code_list.php) or [ISO 639-3](https://www.iso.org/standard/39534.html). |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `premis:premis/premis:object/dcterms:issued` |
|-----------------------|-----------|
| Name | Date issued |
| Description | Date of formal issuance of the resource. |
| Datatype | EDTF |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `premis:premis/premis:object/dcterms:title` |
|-----------------------|-----------|
| Name | Title |
| Description | A name given to the resource. |
| Datatype | String |
| Cardinality | 1..1 |
| Obligation | MUST |

### /preservation (directory)

The `/preservation` directory contains preservation metadata about the (sub-)IE(s) at package level.

***Requirements***

- The `/preservation` directory MUST contain exactly one file: `preservation.xml`.

The `preservation.xml` file at the package-level contains preservation metadata about the (sub-)IE(s) of the SIP, and about the SIP as a whole.
It relies on the [Preservation Metadata: Implementation Strategies (PREMIS)](https://www.loc.gov/standards/premis/) standard in order to provide basic preservation information.
More detailed preservation information can be described using PREMIS events and PREMIS agents.

***Example***

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3">

  <!-- IE about the Felis Catus Flamens -->
  <premis:object>
    <premis:objectCategory>intellectual entity</premis:objectCategory>

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-b21a86aa-97a3-4f7b-a9f5-4d330af641c0</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship between the main IE and its subIEs -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/log">logical</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/gen">generalizes</premis:relationshipSubType>
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

  <!-- subIE about the Felis Catus Flamens lying on the sofa -->
  <premis:object>
    <premis:objectCategory>intellectual entity</premis:objectCategory>

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-948e2213-ca54-459c-8c87-5818adeb9444</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship between the subIE and the main IE -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/log">logical</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/spe">specializes</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-b21a86aa-97a3-4f7b-a9f5-4d330af641c0</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship between the subIE and its representation -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isr">is represented by</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-541292c3-223a-4b80-b747-66bc86ff4a89</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>

  <!-- subIE about the Felis Catus Flamens sitting on its cat tree -->
  <premis:object>
    <premis:objectCategory>intellectual entity</premis:objectCategory>

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-01d59d41-f523-4d06-a549-4bf6f7cef853</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship between the subIE and the main IE -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/log">logical</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/spe">specializes</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-b21a86aa-97a3-4f7b-a9f5-4d330af641c0</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship between the subIE and its representation -->
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

***Requirements***

- The `preservation.xml` file MUST contain a PREMIS object for each IE and sub-IE in the SIP.
- Each PREMIS object in the `preservation.xml` MUST contain a unique identifier.
- The `preservation.xml` file SHOULD contain PREMIS events detailing, a.o., the creation and each modification of the SIP as a whole.

## /representations (directory)

The `/representations` directory contains a separate `/representation_*` (where `*` is a positive integer) directory for each representation of the (sub-)IE(s) of the package level.

***Requirements***

- The `/representations` directory MUST at least contain one `/representation_*` directory.
- The different subdirectories in the `/representations` directory MUST be named `/representation_*`, with `*` being a positive integer that is incremented by 1 for each additional representation in the `/representations` directory.

<small>
Continue to [Representation Level]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/sip_structure/6_structure_representation.md %}).
</small>
