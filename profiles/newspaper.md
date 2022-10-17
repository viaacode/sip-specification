---
layout:       default
title:        Newspaper
parent:       Profiles
grand_parent:  SIP Specification 1.1
nav_order:    2
nav_exclude:  false
---
Editor's Draft
{: .label .label-yellow }
# Profile: Newspaper 

The newspaper profile supports the ingest of digitised newspaper content.
It shows how to deal with multiple media files (in formats such as TIFF, ALTO XML and PDF) and the relationships between them and their metadata.
It also allows to use the [MODS metadata schema](https://www.loc.gov/standards/mods/) for descriptive metadata, which is the default for describing newspaper content.

**Permalink:** <https://data.hetarchief.be/id/sip/1.1/newspaper>

## Example Directory structure

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
- There MUST be preservation metadata at the package level in the `preservation/premis.xml` file.
- There MUST be preservation metadata at the representation level in the respective `preservation/premis.xml` files.
- Preservation metadata in the SIP MUST be limited to the PREMIS metadata schema.
- There MAY be descriptive metadata at the representation level (e.g. information about the representations, such as a title or a description).

### Package METS

- The `csip:CONTENTINFORMATIONTYPE` attribute MUST be set to `https://data.hetarchief.be/id/sip/1.1/newspaper`.

### Package Descriptive Metadata

- A descriptive metadata file `descriptive/mods.xml` MUST be present at the package level; this file MUST follow the [MODS](https://www.loc.gov/standards/mods/v3/mods-3-7.xsd) metadata schema (v3.7.).
- A descriptive metadata file `descriptive/dc.xml` MAY be present at the package level; if present, this file MUST follow the [DCTERMS](https://www.dublincore.org/schemas/xmls/qdc/dcterms.xsd) metadata schema.
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
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:titleInfo[not(@*)]/mods:title` |
|-----------------------|-----------|
| Name | MODS title element |
| Description | This element contains the title of the newspaper.<br>Its parent element (`<mods:titleInfo/>`) MUST NOT contain any attributes in order to differentiate from other optional `<mods:titleInfo/>` elements which, if present, MUST contain `@type` attributes to indicate e.g. alternative titles for the newspaper. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:identifier[not(@*)]` |
|-----------------------|-----------|
| Name | MODS identifier element |
| Description | A unique identifier for the newspaper edition.<br>This identifier MUST be shared with the relevant PREMIS object in the `preservation/premis.xml` file.<br>This metadata element MUST NOT contain any attributes.  |
| Datatype | [ID]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#id) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:typeOfResource` |
|-----------------------|-----------|
| Name | MODS type of resource element |
| Description | This element indicates which type of resource is being described. Its value MUST be set to `newspaper edition`. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:originInfo/mods:dateIssued[@encoding="edtf"]` |
|-----------------------|-----------|
| Name | MODS issuance date element |
| Description | This element contains the date the newspaper edition was issued. Its value MUST be EDTF-compliant, as indicated by the `@encoding` attribute which MUST be set to `edtf`.  |
| Datatype | [EDTF]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#edtf) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:relatedItem[@type="series"]/mods:identifier[@type="abraham_id"]` |
|-----------------------|-----------|
| Name | Abraham ID |
| Description | This element contains the Abraham identifier taken from the [Abraham Belgian Newspaper Catalog](https://krantencatalogus.be). Note that an Abraham identifier refers to newspaper titles rather than newspaper editions; multiple editions can therefore share the same Abraham identifier.<br><br>This element MUST contain the `@type` attribute, with its value set to `abraham_id`. The `@type` attribute of its parent element (i.e. `<mets:relatedItem/>`) MUST be set to `series`. |
| Datatype | [ID]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#id) |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Element | `mods:mods/mods:relatedItem[@type="series"]/mods:identifier[@type="abraham_uri"]` |
|-----------------------|-----------|
| Name | Abraham URI |
| Description | This element contains the Abraham URI taken from the [Abraham Belgian Newspaper Catalog](https://krantencatalogus.be). Note that an Abraham URI refers to newspaper titles rather than newspaper editions; multiple editions can therefore share the same Abraham URI.<br><br>This element MUST contain the `@type` attribute, with its value set to `abraham_uri`. The `@type` attribute of its parent element (i.e. `<mets:relatedItem/>`) MUST be set to `series`. Note that the Abraham URI contains the Abraham identifier. |
| Datatype | [URI]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#uri) |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Element | `mods:mods/mods:note[@type="license"]` |
|-----------------------|-----------|
| Name | License element |
| Description | This element MAY be used to add any licensing info needed. It MUST contain the `@type` attribute, with its value set to `license`. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | MAY |

### Package Preservation Metadata

- A preservation metadata file `preservation/premis.xml` MUST be present at the package level.
- The `preservation/premis.xml` file MUST follow the [PREMIS](https://www.loc.gov/standards/premis/v3/premis-v3-0.xsd) metadata schema (v3.0.).
- If the SIP contains ALTO XML files, the `preservation/premis.xml` file MUST contain a PREMIS event of type `transcription` to link the TIFF and ALTO XML files. With this event, the representation containing the TIFF files MUST receive the PREMIS linking object role `source` and the representation containing the ALTO XML files MUST receive the PREMIS linking object role `outcome`. See the [section about PREMIS events]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/sip_structure/5_structure_package.md %}#adding-provenance-of-representations) and [example 1 below](#example-transcription-event) for more information about the structure of PREMIS events.
- If the SIP contains a PDF file (which SHOULD contain all pages of the newspaper edition, cf. [supra](#pdf), the `preservation/premis.xml` file MUST contain a PREMIS event of type `creation` to link the TIFF and ALTO XML files to the PDF file. With this event, the two representations containing the TIFF and the ALTO XML files MUST receive the PREMIS linking object role `source` and the representation containing the PDF file MUST receive the PREMIS linking object role `outcome`. See the [section about PREMIS events]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/sip_structure/5_structure_package.md %}#adding-provenance-of-representations) and [example 1 below](#example-transcription-event) for more information about the structure of PREMIS events.

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

- If the files in a representation each correspond with a single page (e.g. the TIFF and ALTO XML files, since each of these files MUST correspond to a single page), the corresponding `<div/>` elements in the structural map MUST contain an `@ORDER` attribute that indicates the sequence of the pages of the newspaper edition. Additionally, each `<div/>` element that corresponds to a file representing a page MUST have a `@TYPE` attribute that is set to `page`. See [example 3 below](#example-representation-mets) for more information.

<a id="example-representation-mets"></a>_Example 3: the structural map of a representation METS, with `@TYPE` and `@ORDER` attributes_

```xml
<mets xmlns="http://www.loc.gov/METS/" xmlns:csip="https://DILCIS.eu/XML/METS/CSIPExtensionMETS" xmlns:sip="https://DILCIS.eu/XML/METS/SIPExtensionMETS" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xlink="http://www.w3.org/1999/xlink" OBJID="representation_1" TYPE="Textual works - Print" PROFILE="https://earksip.dilcis.eu/profile/E-ARK-SIP.xml">
    
    [...]
    
    <structMap ID="uuid-04647bb4-f524-435b-b4bf-5fe7a926b9d4" TYPE="PHYSICAL" LABEL="CSIP">
        <div ID="uuid-74e4335c-1d24-42bc-bbd0-864bd216d99c" LABEL="representation_1">
            <div ID="uuid-60d4a0db-769c-42a9-8ef8-c395bb555803" LABEL="metadata">
                <div ID="uuid-e96b8688-e811-4dd8-83dc-81ae263b9c2a" LABEL="preservation">
                    <fptr FILEID="uuid-4482555d-aed7-4066-a211-44429a60a49a" />
                </div>
            </div>
            <!-- order attributes for page order -->
            <div ID="uuid-41bacec1-1d6c-467a-8020-7114115562a8" LABEL="data">
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

- If ALTO XML files are present in the SIP, the `preservation/premis.xml` files of the representation containing the TIFF files and of the representation containing the ALTO XML files MUST contain a PREMIS relationship to establish a link between the two.
  - In the case of the representation with the TIFF files, this PREMIS relationship MUST be of type `derivation` and of subtype `is source of`. The `@valueURI` attribute of the `<premis:relationshipType>` element MUST be set to `http://id.loc.gov/vocabulary/preservation/relationshipType/der`. The `@valueURI` attribute of the `<premis:relationshipSubType>` element MUST be set to `http://id.loc.gov/vocabulary/preservation/relationshipSubType/iso`. Finally, a `<premis:relatedEventIdentifier/>` element MUST be present that refers to the relevant event (in this case a transcription event) defined in the `preservation/premis.xml` file of the package level. This is shown in [example 4 below](#example-premis-issourceof).
  - In the case of the representation with the ALTO XML files, this PREMIS relationship MUST be of type `derivation` and of subtype `has source`. The `@valueURI` attribute of the `<premis:relationshipType>` element MUST be set to `http://id.loc.gov/vocabulary/preservation/relationshipType/der`. The `@valueURI` attribute of the `<premis:relationshipSubType>` element MUST be set to `http://id.loc.gov/vocabulary/preservation/relationshipSubType/hss`. Finally, a `<premis:relatedEventIdentifier/>` element MUST be present that refers to the relevant event (in this case a transcription event) defined in the `preservation/premis.xml` file of the package level. This is shown in [example 5 below](#example-premis-hassource).
- If a PDF file is present in the SIP, the `preservation/premis.xml` files of all three representations (i.e. of the TIFF files, of the ALTO XML file and of the PDF file) MUST contain a PREMIS relationship to establish a link between the three.
  - In the case of the representations with the TIFF and ALTO XML files, this PREMIS relationship MUST be of type `derivation` and of subtype `is source of`. The `@valueURI` attribute of the `<premis:relationshipType>` element MUST be set to `http://id.loc.gov/vocabulary/preservation/relationshipType/der`. The `@valueURI` attribute of the `<premis:relationshipSubType>` element MUST be set to `http://id.loc.gov/vocabulary/preservation/relationshipSubType/iso`. Finally, a `<premis:relatedEventIdentifier/>` element MUST be present that refers to the relevant event (in this case a transcription event) defined in the `preservation/premis.xml` file of the package level. This is similar to [example 4 shown below](#example-premis-issourceof).
  - In the case of the representation with the PDF file, this PREMIS relationship MUST be of type `derivation` and of subtype `has source`. The `@valueURI` attribute of the `<premis:relationshipType>` element MUST be set to `http://id.loc.gov/vocabulary/preservation/relationshipType/der`. The `@valueURI` attribute of the `<premis:relationshipSubType>` element MUST be set to `http://id.loc.gov/vocabulary/preservation/relationshipSubType/hss`. Finally, a `<premis:relatedEventIdentifier/>` element MUST be present that refers to the relevant event (in this case a transcription event) defined in the `preservation/premis.xml` file of the package level. This is similar to [example 5 below](#example-premis-hassource), the difference being that the relationship will mostly entail multiple `<premis:relatedObjectIdentifier/>` elements since the PDF is derived from all TIFF and ALTO XML files together.

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

## Use Cases

Some use cases that implement this profile are:

{% include _usecases.liquid  %}
