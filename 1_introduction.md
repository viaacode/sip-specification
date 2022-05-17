---
layout:       default
title:        Introduction
parent:       SIP Specification
grand_parent:  Digitale instroom
nav_order:    1
nav_exclude:  false
---
Status: WIP
{: .label .label-yellow }
# Introduction

This document specifies the meemoo Submission Information Package (SIP), which describes how data and metadata should be packaged when delivered to meemoo for ingest.
As a digital archive for over 160 content partners, meemoo ingests and disseminates an ever-growing number of digital objects.
These collections contain a wealth of content and information stored in various types of digital file formats.
They are accompanied by metadata that is described in a variety of formats.
Therefore, the current SIP specification was developed to standardize the delivery of (media) content and metadata by meemoo's content partners and increase scalability and sustainability.

The meemoo SIP uses a three-level hierarchical directory structure (_bag - package - representation_) to aggregate and describe media assets, including video, audio, images, captions...
A meemoo SIP is a valid [BagIt bag](https://www.rfc-editor.org/rfc/rfc8493.html) that contains a valid [E-ARK SIP](https://earksip.dilcis.eu/).

At the lowest directory level, the _representation level_, these assets are described in aggregate as digital representations.
One level higher, the _package_ directory _level_, embodies the represented content or [_intellectual entity_](./3_core-concepts.html), such as the work that is being depicted.
Finally, the _bag_ directory _level_ bundles everything together for transport.

Metadata can occur at every SIP level to add administrative, structural, descriptive, and preservation information about the data and its context.
Examples are the author of a representation, the author of what the representation represents (i.e. the intellectual entity), or the creation date of a reprentation.
Metadata are written down in XML files using the common vocabularies [METS](https://www.loc.gov/standards/mets), [DCMI Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/), and [PREMIS](https://www.loc.gov/standards/premis/).

## How to Read this Specification

This document is primarily intended for the following audiences:

- Archivists delivering media resources with accompanying metadata to meemoo for long-term preservation;
- Service providers such as digitization companies that integrate with the ingest flow of meemoo;
- Partners of meemoo publishing software tenders that aim at integrating with the meemoo ingest flow.

To fully understand the basics of this specification, it is advised to be familiar with the [XML](https://www.w3.org/XML/) format, as well as the following standards and metadata schemas this specification adheres to:

| Abbreviation | Standard/schema|
| ------------ | -------------- |
| BagIt        | [BagIt File Packaging Format](https://www.rfc-editor.org/rfc/rfc8493.html)|
| E-ARK CSIP   | [E-ARK Common Specification for Information Packages](https://earkcsip.dilcis.eu/)|
| E-ARK SIP    | [E-ARK Specification for Submission Information Packages](https://earksip.dilcis.eu/)|
| METS         | [Metadata Encoding & Transmission Standard](https://www.loc.gov/standards/mets/mets.xsd)|
| DC           | [Dublin Core Metadata Initiative Metadata Terms](http://dublincore.org/schemas/xmls/qdc/2008/02/11/dcterms.xsd)|
| PREMIS       | [PREMIS for Preservation Metadata](https://www.loc.gov/standards/premis/v3/premis-v3-0.xsd)|

Metadata elements from these standards are described throughout this specification using tables such as the one below. 

| Element/Attribute | `Metadata/element/XPath` |
|-----------------------|-----------|
| Name | Metadata element name |
| Description | Metadata element description |
| Datatype | Metadata element datatype |
| Vocabulary | `Vocabulary term 1`<br>`Vocabulary term 2`<br>`...` |
| Cardinality | `Metadata element cardinality` |
| Obligation | MAY/SHOULD/MUST |

Each table contains the following information about a metadata element:

- whether the tag is an XML element or an XML attribute;
- an XPath expression to select the relevant element from the relevant file;
- the name of the metadata element;
- a description of the metadata element (including relevant requirements about its value);
- the expected datatype of the value for this metadata element (if applicable);
- vocabularies of possible values (if applicable);
- the cardinality of the metadata element, i.e. if and how many times the element is allowed to occur;
- whether the metadata element may/should/must be used.

The cardinality is expressed with syntax from the [Unified Modeling Language](https://www.omg.org/spec/UML/2.5.1/PDF), outlined in the table below.

| UML Syntax | Cardinality                                                                      |
| ---------- | -------------------------------------------------------------------------------- |
| `0..1`       | The element can either not occur or occur at most exactly once.                  |
| `0..*`       | The element can either not occur or can occur an unlimited number of times.      |
| `1..1`       | The element must occur exactly once.                                             |
| `1..*`       | The element must occur at least once and can occur an unlimited number of times. |
| `m..n`       | At least m but no more than n instances.                                         |

<small>
Continue to [Terminology]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}).
</small>
