---
title:        Bibliographic
nav_order:    2
---
{% from "docs/diginstroom/sip/2.1/profiles/_constraints.j2" import render_constraints as render_constraint_details %}
{% from "docs/diginstroom/sip/2.1/profiles/_list_constraints.j2" import render_constraints as render_constraint_list %}

{% set bib_constraints = sip_2_1_bibliographic %}

# Profile: Bibliographic 

The bibliographic profile supports the ingest of digitised written works consisting of multiple bounded or unbounded pages predominately containing handwritten or printed text, such as books, magazines, manuscripts, letters, notated music or newspapers. They are often described and maintained by libraries.
This profile dictates how the media files (in formats such as TIFF, ALTO XML and PDF), their metadata, and the relationships between them, should be expressed and organized.
It applies the [MODS XML metadata schema](https://www.loc.gov/standards/mods/) for descriptive metadata.

**Permalink:** <https://data.hetarchief.be/id/sip/2.1/bibliographic>

## Example Directory structure

```plaintext
root_directory
│──METS.xml
│──metadata
|   |──descriptive
|   |  └──mods.xml
|   └──preservation
|       └──premis.xml
│
└──representations
│──representation_1
│    │──METS.xml
│    │──data
│    |   |──file_1.tiff
│    │   └──...
│    │
│    └──metadata
│        └──preservation
│            └──premis.xml
│
│──representation_2
│    │──METS.xml
│    │──data
│    |   |──file_1.xml
│    │   └──...
│    │
│    └──metadata
│       └──preservation
│          └──premis.xml
│
└──representation_3
    │──METS.xml
    │──data
    |  └── file_1.pdf
    │
    └──metadata
        └──preservation
            └── premis.xml
```

## Requirements

{% set package_constraints = bib_constraints | selectattr("Level", "equalto", "Package") | list %}

{% set rep_constraints = bib_constraints | selectattr("Level", "equalto", "Representation") | list %}

### General

{% set constraints = package_constraints | selectattr("Section", "equalto", "general") | list %}

{{ render_constraint_list(constraints) }}

Only the MD5 hashing algorithm is allowed to compute the fixity, thus:

{% set constraints = package_constraints | selectattr("Section", "equalto", "md5") | list %}

{{ render_constraint_list(constraints) }}

### Package METS

{% set constraints = package_constraints | selectattr("Section", "equalto", "mets") | list %}

{{ render_constraint_list(constraints) }}

### Package Descriptive Metadata

{% set constraints = package_constraints | selectattr("Section", "equalto", "descriptive") | list %}

{{ render_constraint_list(constraints) }}

#### General information

{% set constraints = package_constraints | selectattr("Section", "equalto", "mods") | list %}

{{ render_constraint_details(constraints) }}

#### The main identifiers

{% set constraints = package_constraints | selectattr("Section", "equalto", "modsIdentifier") | list %}

{{ render_constraint_details(constraints) }}

#### Information on the main title 

{% set constraints = package_constraints | selectattr("Section", "equalto", "modsTitle") | list %}

{{ render_constraint_details(constraints) }}

#### Information on alternative titles

{% set constraints = package_constraints | selectattr("Section", "equalto", "modsAlternativeTitle") | list %}

{{ render_constraint_details(constraints) }}

#### Information on language

{% set constraints = package_constraints | selectattr("Section", "equalto", "modsLanguage") | list %}

{{ render_constraint_details(constraints) }}

#### General description of the written work

{% set constraints = package_constraints | selectattr("Section", "equalto", "modsDescription") | list %}

{{ render_constraint_details(constraints) }}

#### Information on people or organizations related to the written work

{% set constraints = package_constraints | selectattr("Section", "equalto", "modsName") | list %}

{{ render_constraint_details(constraints) }}

#### Information on the written work's origin

{% set constraints = package_constraints | selectattr("Section", "equalto", "modsOrigin") | list %}

{{ render_constraint_details(constraints) }}

#### Information on the written work's physical characteristics

{% set constraints = package_constraints | selectattr("Section", "equalto", "modsPhysical") | list %}

{{ render_constraint_details(constraints) }}

#### Related items

{% set constraints = package_constraints | selectattr("Section", "equalto", "modsRelated") | list %}

{{ render_constraint_details(constraints) }}

#### Information on the work series

{% set constraints = package_constraints | selectattr("Section", "equalto", "modsSeries") | list %}

{{ render_constraint_details(constraints) }}

### Package Preservation Metadata

{% set constraints = package_constraints | selectattr("Section", "equalto", "preservation") | list %}

{{ render_constraint_list(constraints) }}

<a id="example-transcription-event"></a>_Example 1: a PREMIS transcription event (linking the TIFF and ALTO XML files)_

```xml
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">
    
    [...]

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

    [...]

</premis:premis>
```

<a id="example-creation-event"></a>_Example 2: a PREMIS creation event (linking the TIFF, ALTO XML and PDF files)_

```xml
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">
    
    [...]

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
    
    [...]

<premis:premis>
```

### Representation METS

{% set constraints = rep_constraints | selectattr("Section", "equalto", "mets") | list %}

{{ render_constraint_list(constraints) }}

<a id="example-representation-mets"></a>_Example 3: the structural map of a representation METS, with `@TYPE` and `@ORDER` attributes_

```xml
<mets xmlns="http://www.loc.gov/METS/" xmlns:csip="https://DILCIS.eu/XML/METS/CSIPExtensionMETS"  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xlink="http://www.w3.org/1999/xlink" OBJID="representation_1" TYPE="Textual works - Print" PROFILE="https://earksip.dilcis.eu/profile/E-ARK-SIP-v2-2-0.xml" xsi:schemaLocation="https://www.w3.org./1999/xlink http://www.loc.gov/standards/xlink/xlink.xsd  http://www.loc.gov/METS/ https://www.loc.gov/standards/mets/mets.xsd https://DILCIS.eu/XML/METS/CSIPExtensionMETS https://earkcsip.dilcis.eu/schema/DILCISExtensionMETS.xsd ">
    
    [...]
    
    <structMap ID="uuid-04647bb4-f524-435b-b4bf-5fe7a926b9d4" TYPE="PHYSICAL" LABEL="CSIP">
        <div ID="uuid-74e4335c-1d24-42bc-bbd0-864bd216d99c" LABEL="representation_1">
            <div ID="uuid-60d4a0db-769c-42a9-8ef8-c395bb555803" LABEL="Metadata">
                <div ID="uuid-e96b8688-e811-4dd8-83dc-81ae263b9c2a" LABEL="preservation">
                    <fptr FILEID="uuid-4482555d-aed7-4066-a211-44429a60a49a" />
                </div>
            </div>
            <!-- order attributes for page order -->
            <div ID="uuid-41bacec1-1d6c-467a-8020-7114115562a8" LABEL="Representations">
                <div ID="uuid-47e52361-8508-4ae1-ad8c-0e1f5382065e" TYPE="page" ORDER="1">
                    <fptr FILEID="uuid-9850cb03-b1fd-4661-a4fb-e3dfcf25e9e5" />
                </div>
                <div ID="uuid-47e52361-8508-4ae1-ad8c-0e1f5382065e" TYPE="page" ORDER="2">
                    <fptr FILEID="uuid-3309e853-bf0f-4d19-ae6a-5e14911e3662" />
                </div>
                <div ID="uuid-eebd6f2a-f06e-4c5f-9c52-fd58e784eaff" TYPE="page" ORDER="3">
                    <fptr FILEID="uuid-4ef96979-4abf-4af0-8156-d04fdd2ff7c3" />
                </div>
            </div>
        </div>
    </structMap>
    
    [...]

</mets>
```  

### Representation Preservation Metadata

{% set constraints = rep_constraints | selectattr("Section", "equalto", "preservation") | list %}

{{ render_constraint_list(constraints) }}

<a id="example-premis-issourceof"></a>_Example 4: a PREMIS `is source of` relationship_

```xml
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

[...]

    <premis:relationship>
        <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/der">derivation</premis:relationshipType>
        <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/iso">is source of</premis:relationshipSubType>
        <premis:relatedObjectIdentifier>
            <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
            <premis:relatedObjectIdentifierValue>uuid-3d2dfddb-6348-43b7-865d-ba9a12ef5c79</premis:relatedObjectIdentifierValue>
        </premis:relatedObjectIdentifier>
        <premis:relatedEventIdentifier>
            <premis:relatedEventIdentifierType>UUID</premis:relatedEventIdentifierType>
            <premis:relatedEventIdentifierValue>uuid-34ae79f8-a8e7-4768-a269-4d6d895662d6</premis:relatedEventIdentifierValue>
        </premis:relatedEventIdentifier>
    </premis:relationship>

[...]

</premis:premis>
```

<a id="example-premis-hassource"></a>_Example 5: a PREMIS `has source` relationship_

```xml
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">
    
    [...]

    <premis:relationship>
        <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/der">derivation</premis:relationshipType>
        <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/hss">has source</premis:relationshipSubType>
        <premis:relatedObjectIdentifier>
            <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
            <premis:relatedObjectIdentifierValue>uuid-1711cd43-19d2-4d89-9259-17443fc7d75f</premis:relatedObjectIdentifierValue>
        </premis:relatedObjectIdentifier>
        <premis:relatedEventIdentifier>
            <premis:relatedEventIdentifierType>UUID</premis:relatedEventIdentifierType>
            <premis:relatedEventIdentifierValue>uuid-34ae79f8-a8e7-4768-a269-4d6d895662d6</premis:relatedEventIdentifierValue>
        </premis:relatedEventIdentifier>
    </premis:relationship>
    
    [...]

</premis:premis>
```

### Validation

The XML files that are required by this profile can be validated using the following XML schema definitions:

| File | Format | XML Schema |
| `METS.xml` | METS v1.12.1 | [mets.xsd](https://www.loc.gov/standards/mets/mets.xsd) |
| `premis.xml` | PREMIS v3.0 | [premis-v3-0.xsd](https://www.loc.gov/standards/premis/v3/premis-v3-0.xsd) |
| `mods.xml` | MODS v3.7 | [mods-3-7.xsd](https://www.loc.gov/standards/mods/v3/mods-3-7.xsd) |

## Use Cases

Some use cases that implement this profile are:

- [Newspaper edition (with PDF)](../usecases/newspaper-pdf.md)
- [Newspaper edition (without PDF)](../usecases/newspaper.md)
