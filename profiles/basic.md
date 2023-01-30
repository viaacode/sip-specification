---
layout:       default
title:        Basic
parent:       Profiles
grand_parent:  1.0
nav_order:    1
nav_exclude:  false
---
# Profile: Basic 

The basic profile supports simple cases consisting of a single media file accompanied by limited metadata.

**Permalink:** <https://data.hetarchief.be/id/sip/1.0/basic>

**Directory structure:**

```plaintext
root_directory
│── manifest-md5.txt
│── bagit.txt
│
└── data
    │── mets.xml
    │── metadata
    |   |── descriptive
    |   |   └── dc.xml
    |   └── preservation
    |       └── premis.xml
    │
    └── representations
        └──representation_1
           │── mets.xml
           └──data
           |  |── file_1.xyz
           │  └── ...
           │
           └──metadata
              └──preservation
                 └── premis.xml
```

## Requirements

### General

- There MUST be exactly one IE.
- The IE MUST be represented by exactly one representation.
- The representation MUST contain at least one file. 
- Preservation metadata MUST be limited to the PREMIS metadata schema.
- There MUST be preservation metadata at the package level in the `preservation/premis.xml` file.
- There MUST be preservation metadata at the representation level in the `preservation/premis.xml` file.

### Package METS

- The `csip:CONTENTINFORMATIONTYPE` attribute MUST be set to `https://data.hetarchief.be/id/sip/1.0/basic`.
- The `mets/dmdSec/mdRef/@MDTYPE` attribute MUST be set to `DC`.

### <span id="dc-requirements"></span>Descriptive metadata

- There MUST NOT be any descriptive metadata at the representation level.
- The `/descriptive` directory at the package level MUST contain exactly one metadata file `dc*.xml` that describes the IE.
- The `dc*.xml` filename SHOULD apply the following naming convention: `dc*.xml` with `*` is any string of zero or more characters.
- The `dc*.xml` file MUST only use the [DCTERMS](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) schema and MUST NOT use any other metadata schemas.
- The `dc*.xml` file MUST declare the DCTERMS namespaces in its root element.
- The `dc*.xml` file MUST use the `<metadata/>` tag as its root element.
- The `dc*.xml` file MUST be limited to the DCTERMS elements outlined in the table below.
- The `dc*.xml` file MUST adhere to the restrictions on cardinality of terms outlined in the table below; if a term is not listed with a restriction on cardinality, it MAY be used multiple times.
- The `dc*.xml` file MUST contain a shared ID with a PREMIS object in the `preservation/premis.xml` file, stored in the `<dcterms:identifier>` element (see [next section](#connecting-the-descriptive-metadata-to-premis)).
- The `dc*.xml` file MUST NOT contain additional IDs besides the shared ID in the `<dcterms:identifier>`; these MUST be added in the `preservation/premis.xml` file.
- A descriptive metadata element of datatype [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) MAY contain an attribute `@xml:lang` that indicates the language of the metadata element's value (in order to, for example, specify a title or description in multiple languages). The value of this attribute MUST be a valid [IETF BCP 47 language tag](https://www.rfc-editor.org/info/bcp47)(see [here](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) for a list).

| Element | `metadata` |
|-----------------------|-----------|
| Name | DC root element |
| Description | This root element MUST contain the XML schema namespace of [DCTERMS](https://www.dublincore.org/schemas/xmls/qdc/dcterms.xsd).<br>It MUST NOT contain any other XML schema namespaces besides DCTERMS.<br>It MUST NOT contain any attributes besides namespaces. |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `metadata/dcterms:title` |
|-----------------------|-----------|
| Name | Title |
| Description | A name given to the Intellectual Entity. <br>The `title` term MAY be used multiple times when it uses a different language.<br>The language of the description MUST be provided by a `@xml:lang` attribute (see requirements above). |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `metadata/dcterms:alternative` |
|-----------------------|-----------|
| Name | Alternative title |
| Description | An alternative to the main title given to the Intellectual Entity.<br>The `alternative` term MAY be used multiple times when it uses a different language.<br>The language of the description MUST be provided by a `@xml:lang` attribute (see requirements above). |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `metadata/dcterms:identifier` |
|-----------------------|-----------|
| Name | Identifier |
| Description | An unambiguous and unique reference to the Intellectual Entity/Entities present in the SIP.<br>This identifier MUST be used to establish a link between the `dc*.xml` file and the relevant PREMIS object in the `preservation/premis.xml` file. |
| Datatype | [ID]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#id) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `metadata/dcterms:extent` |
|-----------------------|-----------|
| Name | Duration |
| Description | Duration in time of the Intellectual Entity. |
| Datatype | [XML Schema duration]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#xsd-duration) |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `metadata/dcterms:available` |
|-----------------------|-----------|
| Name | Available |
| Description | The moment that the Intellectual Entity became available. |
| Datatype | [XML Schema datetime]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#xsd-datetime) |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `metadata/dcterms:description` |
|-----------------------|-----------|
| Name | Description |
| Description | An account of the Intellectual Entity.<br>The `description` term MAY be used multiple times when it uses a different language.<br>The language of the description MUST be provided by a `@xml:lang` attribute (see requirements above). |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `metadata/dcterms:abstract` |
|-----------------------|-----------|
| Name | Abstract |
| Description | A long description of the Intellectual Entity.<br>The `abstract` term MAY be used multiple times when it uses a different language.<br>The language of the description MUST be provided by a `@xml:lang` attribute (see requirements above). |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `metadata/dcterms:created` |
|-----------------------|-----------|
| Name | Creation date |
| Description | Creation date of the Intellectual Entity. |
| Datatype | [EDTF]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#edtf) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `metadata/dcterms:issued` |
|-----------------------|-----------|
| Name | Date issued |
| Description | Date of formal issuance of the Intellectual Entity. |
| Datatype | [EDTF]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#edtf) |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `metadata/dcterms:publisher` |
|-----------------------|-----------|
| Name | Publisher |
| Description | A publisher of the Intellectual Entity |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `metadata/dcterms:contributor` |
|-----------------------|-----------|
| Name | Contributor |
| Description | A contributor to the Intellectual Entity |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `metadata/dcterms:creator` |
|-----------------------|-----------|
| Name | Creator |
| Description | An author or creator of the Intellectual Entity |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `metadata/dcterms:spatial` |
|-----------------------|-----------|
| Name | Spatial |
| Description | Spatial coverage information on the Intellectual Entity |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `metadata/dcterms:temporal` |
|-----------------------|-----------|
| Name | Temporal |
| Description | Temporal coverage information on the Intellectual Entity |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `metadata/dcterms:subject` |
|-----------------------|-----------|
| Name | Subject |
| Description | Subjects or keywords related to the Intellectual Entity. The `subject` term MAY be used multiple times when it uses a different language.<br>The language of the description MUST be provided by a `@xml:lang` attribute (see requirements above). |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | SHOULD |

| Element | `metadata/dcterms:language` |
|-----------------------|-----------|
| Name | Language |
| Description | The language that the Intellectual Entity is in. |
| Datatype | [BCP47]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#bcp47) |
| Cardinality | 0..* |
| Obligation | SHOULD |

| Element | `metadata/dcterms:rightsHolder` |
|-----------------------|-----------|
| Name | Rights holder |
| Description | The person or ogranization that holds the copyright to the Intellectual Entity. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Element | `metadata/dcterms:rights` |
|-----------------------|-----------|
| Name | Rights |
| Description | A copyright notice on the Intellectual Entity. The `rights` term MAY be used multiple times when it uses a different language.<br>The language of the description MUST be provided by a `@xml:lang` attribute (see requirements above). |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Element | `metadata/dcterms:type` |
|-----------------------|-----------|
| Name | Type |
| Description | The classification of this Intellectual Entity . |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/2_terminology.md %}#string) |
| Cardinality | 0..1 |
| Obligation | MAY |

### Validation

The XML files that are required by this profile can be validated using the following XML schema definitions:

| File | Format | XML Schema |
| `mets.xml` | METS v1.12.1 | [mets.xsd](https://www.loc.gov/standards/mets/mets.xsd) |
| `premis.xml` | PREMIS v3.0 | [premis-v3-0.xsd](https://www.loc.gov/standards/premis/v3/premis-v3-0.xsd) |
| `dc_*.xml` | Dublin Core (custom schema) | [dcterms.xsd](../../assets/xsd/dcterms.xsd) |

## Connecting the descriptive metadata to PREMIS

The `dc*.xml` file at the package-level contains descriptive metadata about the IE(s) of the SIP.
It relies on the [DCTERMS](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) schema in order to facilitate a basic description with a limited number of descriptive metadata elements.

There is a link present between each `dc*.xml` file and the PREMIS Intellectual Entity in the `preservation/premis.xml` file via a shared ID.
This shared ID is stored in the `<dcterms:identifier>` element of each `dc*.xml` file and in a `<premis:objectIdentifier>` element of each PREMIS object in the `preservation/premis.xml` file.

Please note that additional IDs must be dealt with in the `preservation/premis.xml` file via `<premis:objectIdentifier>` elements in which the type of ID is specified using the `<premis:objectIdentifierType>` element.

***Example***

```xml
<?xml version='1.0' encoding='UTF-8'?>
<metadata xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xs="http://www.w3.org/2001/XMLSchema/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">


  <!-- general title for the resource -->
  <dcterms:title>Felis Catus Flamens</dcterms:title>

  <!-- linking id between dc and premis -->
  <dcterms:identifier>uuid-b21a86aa-97a3-4f7b-a9f5-4d330af641c0</dcterms:identifier>

  <!-- date unknown -->
  <dcterms:created xsi:type="edtf">XXXX</dcterms:created>

  <!-- multiple keywords about the resource -->
  <dcterms:subject>Cat</dcterms:subject>
  <dcterms:subject>Felis Catus Flamens</dcterms:subject>


</metadata>   
```

## Use Cases

Some use cases that implement this profile are:

{% include _usecases.liquid  %}
