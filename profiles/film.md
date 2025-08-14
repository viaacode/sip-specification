---
layout:       default
title:        Film
parent:       Profiles
grand_parent:  2.1
nav_order:    4
nav_exclude:  false
---

# Profile: Film 

The film profile supports the ingest of digitised film stored on one or more image and/or audio reels. 
This profile dictates how the media files (in file formats such as MKV, MOV, JPEG and PDF), their metadata, and the relationships between them, should be expressed and organized.

It mainly applies the [DCTERMS metadata schema](https://www.dublincore.org/schemas/xmls/qdc/dcterms.xsd) for descriptive metadata and allows extensions using [Schema.org](https://schema.org), thereby resembling the [Basic profile](https://data.hetarchief.be/id/sip/2.1/basic). 

Its additions lie in the introduction of a separate PREMIS representation to denote the physical carrier(s) (a so-called 'carrier representation') and custom film-specific metadata (using a `<premis:significantPropertiesExtension>` element in the package PREMIS file) to describe physical aspects of this/these carrier(s).

This carrier representation was added to facilitate the description of the physical carrier(s), since the PREMIS metadata schema itself doesn't offer this possibility directly.
Please note that, as a result, the carrier representation as such is not reflected by a representation folder in the `representations` directory, given that it is used purely for the addition of descriptive metadata about the carrier(s) and does not contain any files itself. Use the relationship sub types `has carrier copy` and `is carrier copy of` between the IE and the carrier representation.

| Direction | Relationship type | Relationship subtype | Reciprocal/inverse relationship | Description |
|-------------------|----------------------|---------------------------------|-------------|
| From IE to carrier | [`structural`](http://id.loc.gov/vocabulary/preservation/relationshipType/str) | [`has carrier copy`](https://data.hetarchief.be/ns/object/hasCarrierCopy) | [`is carrier copy of`](https://data.hetarchief.be/ns/object/isCarrierCopyOf) | A IE is represented by a carrier representation. |


**Permalink:** <https://data.hetarchief.be/id/sip/2.1/film>

## Example Directory structure

```plaintext
root_directory
├── METS.xml
├── metadata
│   ├── descriptive
│   │   └── dc+schema.xml                               # descriptive metadata about the content of the film
│   └── preservation
│       └── premis.xml                                  # package PREMIS
│
└── representations
    │
    ├── representation_1
    │   ├── METS.xml
    │   ├── data
    │   │   └── master.mkv                              # archive master
    │   └── metadata
    │       └── preservation
    │           └── premis.xml
    │
    ├── representation_2
    │   ├── METS.xml
    │   ├── data
    │   │   └── mezzanine.mov                           # mezzanine
    │   └── metadata
    │       └── preservation
    │           └── premis.xml
    │
    ├── representation_3
    │   ├── METS.xml
    │   ├── data
    │   │   └── scan.jpeg                               # scan(s) of the reel's container (if present) in JPEG
    │   └── metadata
    │       └── preservation
    │           └── premis.xml
    │
    └── representation_4
        ├── METS.xml
        ├── data
        │   └── scan.pdf                                # scan(s) of the reel's container (if present) in PDF
        └── metadata
            └── preservation
                └── premis.xml
```

## Requirements

### General

{% assign constraints = site.data.2_1.FILM_PROFILE | where_exp: "c",
"c.Section == 'general'" %}

{% include_relative _list_constraints.liquid constraints = constraints %}

Only the MD5 hashing algorithm is allowed to compute the fixity, thus:

{% assign constraints = site.data.2_1.FILM_PROFILE | where_exp: "c",
"c.Section == 'md5'" %}

{% include_relative _list_constraints.liquid constraints = constraints %}

### Package METS

{% assign constraints = site.data.2_1.FILM_PROFILE | where_exp: "c",
"c.Section == 'mets'" %}

{% include_relative _list_constraints.liquid constraints = constraints %}

### Package Descriptive Metadata

{% assign constraints = site.data.2_1.FILM_PROFILE | where_exp: "c",
"c.Section == 'descriptive'" %}

{% include_relative _list_constraints.liquid constraints = constraints %}

### Package Preservation Metadata

The addition of a separate PREMIS representation for the carrier(s) (i.e. the carrier representation) leads to a number of additional requirements in the package `premis.xml` file.
The section below outlines the high level requirements, while the section [Describing a carrier within the carrier representation](#describing-a-carrier-within-the-carrier-representation) contains a more detailed discussion of the possibilities offered by the carrier representation.

{% assign constraints = site.data.2_1.FILM_PROFILE | where_exp: "c",
"c.Section == 'preservation'" %}

{% include_relative _list_constraints.liquid constraints = constraints %}

_Example 1: an example `<premis:object>` of a carrier representation together the relationships between the Intellectual Entity and the carrier representation_

```xml

<!-- IE for the film as a whole -->
<premis:object
    xsi:type="premis:intellectualEntity">

    <premis:objectIdentifier>
        <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
        <premis:objectIdentifierValue>uuid-intellectual-entity</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship between the IE and its carrier representation -->
    <premis:relationship>
        <premis:relationshipType>structural</premis:relationshipType>
        <premis:relationshipSubType>has carrier copy</premis:relationshipSubType>
        <premis:relatedObjectIdentifier>
            <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
            <premis:relatedObjectIdentifierValue>uuid-carrier-representation</premis:relatedObjectIdentifierValue>
        </premis:relatedObjectIdentifier>
    </premis:relationship>

</premis:object>

<!-- PREMIS object for the carrier representation -->
<premis:object xsi:type="premis:representation">
    <premis:objectIdentifier>
        <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
        <premis:objectIdentifierValue>uuid-carrier-representation</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship between the carrier representation and its IE -->
    <premis:relationship>
        <premis:relationshipType>structural</premis:relationshipType>
        <premis:relationshipSubType>is carrier copy of</premis:relationshipSubType>
        <premis:relatedObjectIdentifier>
            <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
            <premis:relatedObjectIdentifierValue>uuid-intellectual-entity</premis:relatedObjectIdentifierValue>
        </premis:relatedObjectIdentifier>
    </premis:relationship>
</premis:object>
```

### Describing a carrier within the carrier representation

The carrier representation is described using the `<premis:significantPropertiesExtension>` element. A custom schema is defined inside this extension to capture structural and descriptive metadata of the carrier. The schema uses the `hasip` namespace and is specified below.

| Prefix | URI                                |
| ------ | ---------------------------------- |
| hasip  | [https://data.hetarchief.be/ns/sip/](https://data.hetarchief.be/ns/sip/) |


_Example 2: hierarchical listing of a package `premis.xml` file with an Intellectual Entity and a Carrier Representation._

```text
premis:premis
│
├── premis:object xsi:type="premis:intellectualEntity"    # Intellectual Entity
│
└── premis:object xsi:type="premis:representation"        # Carrier Representation
    └── premis:significantProperties
        └── premis:significantPropertiesExtension
            └── ...                                       # Carrier representation description
```

#### General requirements

{% assign constraints = site.data.2_1.FILM_PROFILE | where_exp: "c",
"c.Section == 'summary'" %}

{% include_relative _list_constraints.liquid constraints = constraints %}

<!-- <inLanguage>Silent Movie</inLanguage> -->

#### Premis.xml

{% assign constraints = site.data.2_1.FILM_PROFILE | where_exp: "c",
"c.Section == 'premis'" %}

{% include_relative _constraints.liquid constraints = constraints %}                                                                                                                             

The following elements paths are relative to the `<premis:significantPropertiesExtension>` element.

{% assign constraints = site.data.2_1.FILM_PROFILE | where_exp: "c",
"c.Section == 'significantPropertiesExtension'" %}

{% include_relative _constraints.liquid constraints = constraints %}

_Example 4_ below contains an illustration of a simplified carrier representation (preceded by its intellectual entity) and a registration event involving the carrier representation in the package `premis.xml` file:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:premis="http://www.loc.gov/premis/v3" xmlns:haObj="https://data.hetarchief.be/ns/object/"
    xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

    <!-- IE for the film as a whole -->
    <premis:object
        xsi:type="premis:intellectualEntity">

        <premis:objectIdentifier>
            <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
            <premis:objectIdentifierValue>uuid-b1c5fa36-6bb6-460b-836b-ade5541fe89e</premis:objectIdentifierValue>
        </premis:objectIdentifier>

        <!-- relationship between the IE and its carrier representation -->
        <premis:relationship>
            <premis:relationshipType authority="relationshipType"
                authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
                valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
            <premis:relationshipSubType authority="relationshipSubType"
                authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType"
                valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isr">is
                represented
                by</premis:relationshipSubType>
            <premis:relatedObjectIdentifier>
                <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
                <premis:relatedObjectIdentifierValue>uuid-e2f092de-f800-486c-a291-3160ce740544</premis:relatedObjectIdentifierValue>
            </premis:relatedObjectIdentifier>
        </premis:relationship>

    </premis:object>

    <!-- PREMIS object for the carrier representation itself -->
    <premis:object xsi:type="premis:representation">

        <premis:objectIdentifier>
            <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
            <premis:objectIdentifierValue>uuid-e2f092de-f800-486c-a291-3160ce740544</premis:objectIdentifierValue>
        </premis:objectIdentifier>

        <!-- descriptive metadata in several <premis:significantProperties> elements -->
        <premis:significantProperties>
            <premis:significantPropertiesType>barcode_image_reels</premis:significantPropertiesType>
            <premis:significantPropertiesValue>AFLM_FEL_001392</premis:significantPropertiesValue>
        </premis:significantProperties>
        <premis:significantProperties>
            <premis:significantPropertiesType>material_type</premis:significantPropertiesType>
            <premis:significantPropertiesValue>Original positive</premis:significantPropertiesValue>
        </premis:significantProperties>
        <premis:significantProperties>
            <premis:significantPropertiesType>num_reels</premis:significantPropertiesType>
            <premis:significantPropertiesValue>1</premis:significantPropertiesValue>
        </premis:significantProperties>
        <premis:significantProperties>
            <premis:significantPropertiesType>film_base</premis:significantPropertiesType>
            <premis:significantPropertiesValue>acetate</premis:significantPropertiesValue>
        </premis:significantProperties>

        <!-- descriptive metadata using Schema in a nested <premis:significantPropertiesExtension> element -->
        <premis:significantProperties>
            <premis:significantPropertiesExtension xmlns:schema='https://schema.org'>
                <schema:duration>0:04:55</schema:duration>
                <schema:material>Original positive</schema:material>
                <schema:size>
                    <schema:unitCode>MTR</schema:unitCode>
                    <schema:QuantitativeValue>135</schema:QuantitativeValue>
                </schema:size>
            </premis:significantPropertiesExtension>
        </premis:significantProperties>

        <!-- indication of the carrier type -->
        <premis:storage>
            <premis:storageMedium>
                super8mmfilm
            </premis:storageMedium>
        </premis:storage>

        <!-- relationship between the carrier representation and its IE -->
        <premis:relationship>
            <premis:relationshipType authority="relationshipType"
                authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType"
                valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
            <premis:relationshipSubType authority="relationshipSubType"
                authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType"
                valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/rep">
                represents</premis:relationshipSubType>
            <premis:relatedObjectIdentifier>
                <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
                <premis:relatedObjectIdentifierValue>uuid-b1c5fa36-6bb6-460b-836b-ade5541fe89e</premis:relatedObjectIdentifierValue>
            </premis:relatedObjectIdentifier>
        </premis:relationship>

    </premis:object>

    <!-- registration event -->
    <premis:event>
        <premis:eventIdentifier>

            <premis:eventIdentifierType>UUID</premis:eventIdentifierType>
            <premis:eventIdentifierValue>uuid-aba62b7b-dd7a-43cf-b077-45f8b96deae8</premis:eventIdentifierValue>

        </premis:eventIdentifier>
        <premis:eventType valueURI="https://data.hetarchief.be/id/event-type/registration">
      registration
    </premis:eventType>
        <premis:eventDateTime>
      2021-04-02T09:04:04
    </premis:eventDateTime>
        <premis:eventDetailInformation>
            <premis:eventDetail>Base Scratching remarks: Light scratches, lines and stripes. Some cables. vinegar date: 2021-06-30 pH value:PH 4.8</premis:eventDetail>
            <premis:eventDetailExtension xmlns:schema="https://schema.org/">
                <schema:name>estimate_preparation_time_for_digitisation</schema:name>
                <schema:value>1:30:00</schema:value>
            </premis:eventDetailExtension>
            <premis:eventDetailExtension xmlns:schema="https://schema.org/">
                <schema:name>estimate_manual_cleaning_time</schema:name>
                <schema:value>0:00:00</schema:value>
            </premis:eventDetailExtension>
            <premis:eventDetailExtension xmlns:schema="https://schema.org/">
                <schema:name>physical_state_film</schema:name>
                <schema:value>film in good state</schema:value>
            </premis:eventDetailExtension>
        </premis:eventDetailInformation>

        <premis:eventOutcomeInformation>
            <premis:eventOutcome
                valueURI="http://id.loc.gov/vocabulary/preservation/eventOutcome/suc">success</premis:eventOutcome>
        </premis:eventOutcomeInformation>
        
        <premis:linkingAgentIdentifier>
            <premis:linkingAgentIdentifierType>MEEMOO-OR-ID</premis:linkingAgentIdentifierType>
            <premis:linkingAgentIdentifierValue>OR-jw86m54</premis:linkingAgentIdentifierValue>
            <premis:linkingAgentRole
                valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp">implementer</premis:linkingAgentRole>
        </premis:linkingAgentIdentifier>

        <!-- reference to the premis:Representation object of the carrier representation -->
        <premis:linkingObjectIdentifier>
            <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
            <premis:linkingObjectIdentifierValue>uuid-e2f092de-f800-486c-a291-3160ce740544</premis:linkingObjectIdentifierValue>
            <premis:linkingObjectRole
                valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/sou">source</premis:linkingObjectRole>
        </premis:linkingObjectIdentifier>
    </premis:event>

</premis:premis>
```

### Validation

The XML files that are required by this profile can be validated using the following XML schema definitions:

| File | Format | XML Schema |
| `METS.xml` | METS v1.12.1 | [mets.xsd](https://www.loc.gov/standards/mets/mets.xsd) |
| `premis.xml` | PREMIS v3.0 | [premis-v3-0.xsd](https://www.loc.gov/standards/premis/v3/premis-v3-0.xsd) |
| `dc+schema.xml` | Dublin Core with Schema.org | dc+schema.xsd (not yet available) |

## Use Cases

Some use cases that implement this profile are:

{% include _usecases.liquid  %}
