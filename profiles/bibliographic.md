---
layout:       default
title:        Bibliographic
parent:       Profiles
grand_parent:  1.2
nav_order:    2
nav_exclude:  false
---
Release Candidate
{: .label .label-blue }
# Profile: Bibliographic 

The bibliographic profile supports the ingest of digitised written works consisting of multiple bounded or unbounded pages predominately containing handwritten or printed text, such as books, magazines, manuscripts, letters or newspapers. They are often described and maintained by libraries.
This profile dictates how the media files (in formats such as TIFF, ALTO XML and PDF), their metadata, and the relationships between them, should be expressed and organized.
It applies the [MODS XML metadata schema](https://www.loc.gov/standards/mods/) for descriptive metadata.

**Permalink:** <https://data.hetarchief.be/id/sip/1.2/bibliographic>

## Example Directory structure

```plaintext
root_directory
│──manifest-md5.txt
│──bagit.txt
│
└──data
    │──mets.xml
    │──metadata
    |   |──descriptive      (at least one of both files must be present)
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

- A SIP MUST contain content of exactly one written work of type
  - newspaper edition;
  - book;
  - letter;
  - magazine issue; or
  - manuscript.
- The content MUST be digitised per page, i.e. each TIFF and/or ALTO XML file contained in their respective representation directories MUST represent exactly one page.
  - <a id="pdf"></a>An exception to this requirement MAY be made with regards to a PDF file: it is RECOMMENDED to only use a single PDF that contains the entire contents (i.e. all pages are present in one single PDF file).
- There MUST be exactly one IE present in the SIP, i.e. the written work.
- There MUST be preservation metadata at the package level in the `preservation/premis.xml` file.
- There MUST be preservation metadata at the representation level in the respective `preservation/premis.xml` files.
- Preservation metadata in the SIP MUST be limited to the PREMIS metadata schema.
- Only the MD5 hashing algorithm is allowed to compute the fixity, thus:
  - The value of element `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:fixity/premis:messageDigestAlgorithm` MUST be set to `MD5`.
  - The value of attribute `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:fixity/premis:messageDigestAlgorithm/@valueURI` MUST be set to `"http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5"`.
- There MAY be descriptive metadata at the representation level (e.g. information about the representations, such as a title or a description).

### Package METS

- The `csip:CONTENTINFORMATIONTYPE` attribute MUST be set to `https://data.hetarchief.be/id/sip/1.2/bibliographic`.
- The `mets/dmdSec/mdRef/@MDTYPE` attribute MUST be set to `MODS`.

### Package Descriptive Metadata

- Either a `descriptive/mods.xml` or a `descriptive/dc.xml` descriptive metadata file MUST be present at the package level. In case they both occur, the `descriptive/dc.xml` file is ignored. 
- The `descriptive/dc.xml` file MUST follow the [DCTERMS](https://www.dublincore.org/schemas/xmls/qdc/dcterms.xsd) metadata schema in accordance with the [basic profile requirements]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/profiles/basic.md %}#dc-requirements).
- The `descriptive/mods.xml` file MUST follow the [MODS](https://www.loc.gov/standards/mods/v3/mods-3-7.xsd) metadata schema (v3.7.).
- The `descriptive/mods.xml` file MUST contain a shared identifier with the `preservation/premis.xml` to indicate which PREMIS object is being described in the `descriptive/mods.xml` file.
- The MODS metadata in `descriptive/mods.xml` MUST be limited to the elements and attributes outlined below.

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

| Element | `mods:mods/mods:recordInfo/mods:recordIdentifier` |
|-----------------------|-----------|
| Name | MODS record identifier |
| Description | This element contains the title of the written work. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 0..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:titleInfo` |
|-----------------------|-----------|
| Name | MODS titleInfo element |
| Description | This element contains information about the title of the written work.<br>There MUST be at least one `<mods:titleInfo/>` element that does not contain any attributes to designate the main title and differentiate it from other optional `<mods:titleInfo/>` elements which, if present, MUST contain `@type` attributes to indicate e.g. alternative titles for the newspaper. |
| Cardinality | 1..* |
| Obligation | MUST |

| Attribute | `mods:mods/mods:titleInfo/@type` |
|-----------------------|-----------|
| Name | MODS title type attribute |
| Description | This attribute indicates the type of title. If present, its value MUST be set to `alternative` and the attribute `@otherType` MUST be present.  |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Vocabulary | `alternative` |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Attribute | `mods:mods/mods:titleInfo[@type="alternative"]/@otherType` |
|-----------------------|-----------|
| Name | MODS alternative title other type attribute |
| Description | This attribute contains the subtype for any alternative title. This attribute MUST be present if `@type` is set to `alternative`. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Vocabulary | `incipit`, `incipit brief`, `correspondenten` |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:titleInfo[not(@*)]/mods:title` |
|-----------------------|-----------|
| Name | MODS title element |
| Description | This element contains the title of the written work.<br>Its parent element (`<mods:titleInfo/>`) MUST NOT contain any attributes in order to differentiate from other optional `<mods:titleInfo/>` elements which, if present, MUST contain `@type` attributes to indicate e.g. alternative titles for the newspaper. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:titleInfo[@type="alternative"]/mods:title` |
|-----------------------|-----------|
| Name | MODS title element |
| Description | This element contains an alternative title of the written work.<br>Its parent element (`<mods:titleInfo/>`) MUST contain the `@type` attribute set to `alternative`. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:identifier[not(@*)]` |
|-----------------------|-----------|
| Name | MODS identifier element |
| Description | A unique identifier for the written work.<br>This identifier MUST be shared with the relevant PREMIS object in the `preservation/premis.xml` file.<br>This metadata element MUST NOT contain any attributes.  |
| Datatype | [ID]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#id) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:language` |
|-----------------------|-----------|
| Name | MODS language element |
| Description |   |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `mods:mods/mods:language/mods:languageTerm` |
|-----------------------|-----------|
| Name | MODS language element |
| Description |   |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

<!-- | Element | `mods:mods/mods:identifier[@type="uri"]` |
|-----------------------|-----------|
| Name | Abraham ID |
| Description | This element contains the Abraham identifier taken from the [Abraham Belgian Newspaper Catalog](https://krantencatalogus.be). Note that an Abraham identifier refers to newspaper titles rather than newspaper editions; multiple editions can therefore share the same Abraham identifier.<br><br>This element MUST contain the `@type` attribute, with its value set to `abraham_id`. The `@type` attribute of its parent element (i.e. `<mets:relatedItem/>`) MUST be set to `series`. |
| Datatype | [ID]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#id) |
| Cardinality | 0..1 |
| Obligation | SHOULD | -->

| Element | `mods:mods/mods:typeOfResource` |
|-----------------------|-----------|
| Name | MODS type of resource element |
| Description | This element indicates which type of resource is being described. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Vocabulary | `newspaper edition`, `Notated music`, `Text` |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mods:mods/mods:typeOfResource/@manuscript` |
|-----------------------|-----------|
| Name | MODS type manuscript |
| Description | When present and its value is set to `yes`, this attribute indicates that the resource is handwritten. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Vocabulary | `yes` |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `mods:mods/mods:abstract` |
|-----------------------|-----------|
| Name | MODS abstract element |
| Description | This element contains a summary or description of the content of the written work. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Element | `mods:mods/mods:genre` |
|-----------------------|-----------|
| Name | MODS genre element |
| Description | This element contains a term or terms that designate a category characterizing a particular style, form, or content of the written work, such as artistic, musical, literary composition, etc. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | SHOULD |

| Element | `mods:mods/mods:subject/mods:topic` |
|-----------------------|-----------|
| Name | MODS topic element |
| Description | A term or phrase representing the primary topic(s) on which the written work is focused. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `mods:mods/mods:name` |
|-----------------------|-----------|
| Name | MODS name element |
| Description | A person or company associated with the written work.  |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Attribute | `mods:mods/mods:name/@type` |
|-----------------------|-----------|
| Name | MODS name type attribute |
| Description | This attributed indicates wheter the name belongs to a person (`personal`) or to an organization or company (`corporate`).  |
| Vocabulary | `personal`, `corporate` |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:name[@type="personal"]/mods:namePart[@type="family"]` |
|-----------------------|-----------|
| Name | Family name of a person |
| Description | The family name of a person associated with the written work.  |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:name[@type="personal"]/mods:namePart[@type="given"]` |
|-----------------------|-----------|
| Name | Given name of a person |
| Description | The given name of a person associated with the written work.  |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:name[@type="corporate"]/mods:namePart` |
|-----------------------|-----------|
| Name | Name of a company or organization |
| Description | The name of a company or organization associated with the written work.  |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:name/mods:role/mods:roleTerm[@type="text"]` |
|-----------------------|-----------|
| Name | Role of a person |
| Description | Designates the relationship (role) of the person or organization to the written work.  |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

{: .bg-green-000 }

| Element | `mods:mods/mods:originInfo` |
|-----------------------|-----------|
| Name | MODS originInfo element |
| Description | This element contains information about the written work's origin, e.g., when and where it was created or published  |
| Cardinality | 1..* |
| Obligation | MUST |

| Attribute | `mods:mods/mods:originInfo/@eventType` |
|-----------------------|-----------|
| Name | MODS issuance date element |
| Description | This attribute specifies the type of event that should be associated with the originInfo. This attribute is not required, but if present, its value MUST be set to `publication, meaning that the origin info is about when the written work was published. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Vocabulary | `publication` |
| Cardinality | 0..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:originInfo/mods:publisher` |
|-----------------------|-----------|
| Name | MODS publisher element |
| Description | The publisher of the written work, e.g., when and where it was created or published  |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `mods:mods/mods:originInfo/mods:dateCreated[@encoding="edtf"]` |
|-----------------------|-----------|
| Name | MODS creation date element |
| Description | This element contains the date the written work was created. Its value MUST be EDTF-compliant, as indicated by the `@encoding` attribute which MUST be set to `edtf`.  |
| Datatype | [EDTF]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#edtf) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:originInfo/mods:dateIssued[@encoding="edtf"]` |
|-----------------------|-----------|
| Name | MODS issuance date element |
| Description | This element contains the date the written work was issued. Its value MUST be EDTF-compliant, as indicated by the `@encoding` attribute which MUST be set to `edtf`.  |
| Datatype | [EDTF]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#edtf) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:originInfo/mods:issuance` |
|-----------------------|-----------|
| Name | MODS issuance element |
| Description | This element contains a term that designates how the written work was issued. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `mods:mods/mods:originInfo/mods:place` |
|-----------------------|-----------|
| Name | MODS place element |
| Description | This element contains the place the written work was issued. |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `mods:mods/mods:originInfo/mods:place/mods:placeTerm[@type="text"]` |
|-----------------------|-----------|
| Name | MODS place term text element |
| Description | This element is used to express place in a textual form.  |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | SHOULD |

| Element | `mods:mods/mods:originInfo/mods:place/mods:placeTerm[@type="code"]` |
|-----------------------|-----------|
| Name | MODS place term code element |
| Description | This element is used to express place in a coded form.  |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | SHOULD |

| Element | `mods:mods/mods:physicalDescription` |
|-----------------------|-----------|
| Name | MODS physical description element |
| Description | This element is used to express physical characteristics of the written work.  |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `mods:mods/mods:physicalDescription/mods:note` |
|-----------------------|-----------|
| Name | MODS physical description note element  |
| Description |  This element containes a description of the condition of the written work or the statement of responsibility of the written work.  |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `mods:mods/mods:physicalDescription/mods:note/@type` |
|-----------------------|-----------|
| Name | MODS physical description note type attribute  |
| Description |  This attribute indicates whether the note describes the condition of the written work of dictates the statement of responsibility. Its value MUST be either `statement of responsibility` or `condition`.  |
| Vocabulary | `statement of responsibility`, `condition` |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `mods:mods/mods:physicalDescription/mods:extent` |
|-----------------------|-----------|
| Name | MODS extent element |
| Description | This element is used to express a physical dimension of the written work indicated by the `@unit` attribute, such as the number of pages, the number of sheets, or its physical measurements .  |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | MAY |

| Attribute | `mods:mods/mods:physicalDescription/mods:extent/@unit` |
|-----------------------|-----------|
| Name | MODS extent element |
| Description | This attribute indicates the physical dimension that is described. For expressing the physical size of the written work, the metric unit `cm` (centimeter) or `mm` (millimeter) is used; the value MUST be in the form `<width> X <height>`, with `<width>` and `<height>` being values of type [Integer]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#integer). |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Vocabulary | `cm`, `mm`, `sheets`, `pages` |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `mods:mods/mods:physicalDescription/mods:form` |
|-----------------------|-----------|
| Name | MODS form element |
| Description | This element denotes the physical presentation of the written work, including the physical form, medium or material.  |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | MAY |

| Attribute | `mods:mods/mods:physicalDescription/mods:form/@type` |
|-----------------------|-----------|
| Name | MODS form type attribute |
| Description | This attribute denotes the particular type of physical presentation that is being described, such as the physical form, the medium or the material.  |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 0..1 |
| Obligation | MAY |

| Attribute | `mods:mods/(mods:genre|mods:mods/mods:originInfo/mods:place/mods:placeTerm[@type="code"]|mods:physicalDescription/mods:form)/@authority` |
|-----------------------|-----------|
| Name | MODS authority attribute |
| Description | The name of an authoritative list of terms whose values are controlled. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Attribute | `mods:mods/(mods:genre|mods:mods/mods:originInfo/mods:place/mods:placeTerm[@type="code"]|mods:physicalDescription/mods:form)/@authorityURI` |
|-----------------------|-----------|
| Name | MODS authority uri attribute |
| Description | The URI for the authoritative list (as described above for `@authority`). |
| Datatype | [URI]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#uri) |
| Cardinality | 0..1 |
| Obligation | SHOULD |

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

| Element | `mods:mods/mods:relatedItem[@type="series"]/mods:identifier[@type="number"]` |
|-----------------------|-----------|
| Name | series number |
| Description | This element contains the number of the series in which the written work was published. The `@type` attribute of its parent element (i.e. `<mets:relatedItem/>`) MUST be set to `series`.  |
| Datatype | [Integer]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#integer) |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `mods:mods/mods:relatedItem[@type="series"]/mods:identifier[@type="page"]` |
|-----------------------|-----------|
| Name | page number |
| Description | This element contains the number of the series in which the written work was published. The `@type` attribute of its parent element (i.e. `<mets:relatedItem/>`) MUST be set to `series`.  |
| Datatype | [Integer]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#integer) |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `mods:mods/mods:relatedItem[@type="series"]/mods:title` |
|-----------------------|-----------|
| Name | MODS relatedItem title element |
| Description | This element contains the title of the series.<br>Its parent element (`<mods:titleInfo/>`) MUST NOT contain any attributes in order to differentiate from other optional `<mods:titleInfo/>` elements which, if present, MUST contain `@type` attributes to indicate e.g. alternative titles for the newspaper. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#string) |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `mods:mods/mods:relatedItem[@type="series"]/mods:originInfo/mods:dateIssued[@encoding="edtf"]` |
|-----------------------|-----------|
| Name | MODS relatedItem issuance date element |
| Description | This element contains the date the series was issued. Its value MUST be EDTF-compliant, as indicated by the `@encoding` attribute which MUST be set to `edtf`.  |
| Datatype | [EDTF]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/2_terminology.md %}#edtf) |
| Cardinality | 0..1 |
| Obligation | MAY |

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
- If the SIP contains a PDF file (which SHOULD contain all pages of the written work, cf. [supra](#pdf), the `preservation/premis.xml` file MUST contain a PREMIS event of type `creation` to link the TIFF and ALTO XML files to the PDF file. With this event, the two representations containing the TIFF and the ALTO XML files MUST receive the PREMIS linking object role `source` and the representation containing the PDF file MUST receive the PREMIS linking object role `outcome`. See the [section about PREMIS events]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/sip_structure/5_structure_package.md %}#adding-provenance-of-representations) and [example 1 below](#example-transcription-event) for more information about the structure of PREMIS events.

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

- If the files in a representation each correspond with a single page (e.g. the TIFF and ALTO XML files, since each of these files MUST correspond to a single page), the corresponding `<div/>` elements in the structural map MUST contain an `@ORDER` attribute that indicates the sequence of the pages. Additionally, each `<div/>` element that corresponds to a file representing a page MUST have a `@TYPE` attribute that is set to `page`. See [example 3 below](#example-representation-mets) for more information.

<a id="example-representation-mets"></a>_Example 3: the structural map of a representation METS, with `@TYPE` and `@ORDER` attributes_

```xml
<mets xmlns="http://www.loc.gov/METS/" xmlns:csip="https://DILCIS.eu/XML/METS/CSIPExtensionMETS"  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xlink="http://www.w3.org/1999/xlink" OBJID="representation_1" TYPE="Textual works - Print" PROFILE="https://earksip.dilcis.eu/profile/E-ARK-SIP.xml" xsi:schemaLocation="https://www.w3.org./1999/xlink http://www.loc.gov/standards/xlink/xlink.xsd  http://www.loc.gov/METS/ https://www.loc.gov/standards/mets/mets.xsd https://dilcis.eu/XML/METS/CSIPExtensionMETS https://earkcsip.dilcis.eu/schema/DILCISExtensionMETS.xsd ">
    
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

### Validation

The XML files that are required by this profile can be validated using the following XML schema definitions:

| File | Format | XML Schema |
| `mets.xml` | METS v1.12.1 | [mets.xsd](https://www.loc.gov/standards/mets/mets.xsd) |
| `premis.xml` | PREMIS v3.0 | [premis-v3-0.xsd](https://www.loc.gov/standards/premis/v3/premis-v3-0.xsd) |
| `mods.xml` | MODS v3.8 | [mods-3-8.xsd](https://www.loc.gov/standards/mods/v3/mods-3-8.xsd) |
| `dc.xml` (if no MODS) | Dublin Core (custom schema) | [dc_basic.xsd](https://raw.githubusercontent.com/viaacode/sipin-sip-validator/main/app/resources/xsd/dc_basic.xsd)<br>_depends on: [edtf.xsd](https://raw.githubusercontent.com/viaacode/sipin-sip-validator/main/app/resources/xsd/edtf.xsd), [dcterms.xsd](https://github.com/viaacode/sipin-sip-validator/blob/main/app/resources/xsd/dcterms.xsd), [dcmitype.xsd](https://raw.githubusercontent.com/viaacode/sipin-sip-validator/main/app/resources/xsd/dcmitype.xsd), [dc.xsd](https://raw.githubusercontent.com/viaacode/sipin-sip-validator/main/app/resources/xsd/dc.xsd)_ |

## Use Cases

Some use cases that implement this profile are:

{% include _usecases.liquid  %}
