---
layout:       default
title:        Basic
parent:       Profiles
grand_parent:  1.2
nav_order:    1
nav_exclude:  false
---
Release Candidate
{: .label .label-blue }
# Profile: Basic 

The basic profile supports simple cases consisting of a single media file accompanied by limited metadata.

**Permalink:** <https://data.hetarchief.be/id/sip/1.2/basic>

## Example Directory structure

```plaintext
root_directory
│── manifest-md5.txt
│── bagit.txt
│
└── data
    │── mets.xml
    │── metadata
    |   |── descriptive
    |   |   └── dc+schema.xml
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
- Only the MD5 hashing algorithm is allowed to compute the fixity, thus:
  - The value of element `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:fixity/premis:messageDigestAlgorithm` MUST be set to `MD5`.
  - The value of attribute `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:fixity/premis:messageDigestAlgorithm/@valueURI` MUST be set to `"http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5"`.

### Package METS

- The `csip:CONTENTINFORMATIONTYPE` attribute MUST be set to `OTHER` and the `csip:OTHERCONTENTINFORMATIONTYPE` attribute MUST be set to `https://data.hetarchief.be/id/sip/1.2/basic`.
- The `mets/dmdSec/mdRef/@MDTYPE` attribute MUST be set to `OTHER` and `mets/dmdSec/mdRef/@OTHERMDTYPE` attribute must be set to `DC+SCHEMA`.

### <span id="dc-requirements"></span>Descriptive metadata

- There MUST NOT be any descriptive metadata at the representation level.
- The `/descriptive` directory at the package level MUST contain exactly one metadata file `dc+schema.xml` that describes the IE.
- The `dc+schema.xml` file MUST use the `<metadata/>` tag as its root element.
- The `dc+schema.xml` file MUST declare the `http://purl.org/dc/terms/` (dcterms), `https://schema.org/` (schema), `http://www.w3.org/2001/XMLSchema-instance` (xsi) and `http://id.loc.gov/datatypes/edtf/` (edtf) namespaces in its root element.
- The `dc+schema.xml` file MUST declare `https://data.hetarchief.be/id/sip/1.2/basic` as default namespace in its root element.
- Descriptive metadata in `dc+schema.xml` MUST be limited to the [DCTERMS](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) and [SCHEMA](http://schema.org) elements outlined in the table below.
- The `dc+schema.xml` file MUST adhere to the restrictions on cardinality of terms outlined in the table below; if a term is not listed with a restriction on cardinality, it MAY be used multiple times.
- The `dc+schema.xml` file MUST contain a shared ID with a PREMIS object in the `preservation/premis.xml` file, stored in the `<dcterms:identifier>` element (see [next section](#connecting-the-descriptive-metadata-to-premis)).
- The `dc+schema.xml` file MUST NOT contain additional IDs besides the shared ID in the `<dcterms:identifier>`; these MUST be added in the `preservation/premis.xml` file.
- Some descriptive metadata elements of datatype [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) MUST contain an attribute `@xml:lang` that indicates the language of the metadata element's value (in order to, for example, specify a title or description in multiple languages); these are indicated with `[@xml:lang=*]` in the table below. Other elements MUST NOT contain this attribute.
- The value of the `@xml:lang` attribute MUST be a valid [IETF BCP 47 language tag](https://www.rfc-editor.org/info/bcp47)(see [here](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) for a list). 

{: .important }
For elements that require the `@xml:lang` attribute, it is still necessary to supply an element with `@xml:lang` set to `nl` even if there is no Dutch content available (e.g., the original title is in English or French and no translation was ever made, or the title is the same in both languages). In that case, a title in another language can be copied as it it were Dutch. 

#### Root element

| Element | `metadata` |
|-----------------------|-----------|
| Name | DCTERMS root element |
| Description | The root element for descriptive metadata in [DCTERMS](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/). This root element MUST declare the XML schema namespaces `http://purl.org/dc/terms/` (dcterms), `http://www.w3.org/2001/XMLSchema-instance` (xsi) and `http://id.loc.gov/datatypes/edtf/` (edtf), and the default namespace `https://data.hetarchief.be/id/sip/1.2/basic`. |
| Cardinality | 1..1 |
| Obligation | MUST |

#### DCMI Terms elements

| Element | `metadata/dcterms:title[@xml:lang=*]` |
|-----------------------|-----------|
| Name | Title |
| Description | A name given to the Intellectual Entity. <br>The `title` term MAY only be used multiple times when it uses a different language. The applied language MUST be provided by a `@xml:lang` attribute (see requirements above). There MUST always be an entry in Dutch with `@xml:lang` set to `nl`. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `metadata/dcterms:alternative[@xml:lang=*]` |
|-----------------------|-----------|
| Name | Alternative title |
| Description | An alternative to the main title given to the Intellectual Entity.<br>The `alternative` term MAY only be used multiple times when it uses a different language. The applied language MUST be provided by a `@xml:lang` attribute (see requirements above). There MUST always be an entry in Dutch with `@xml:lang` set to `nl`. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `metadata/dcterms:identifier` |
|-----------------------|-----------|
| Name | Identifier |
| Description | An unambiguous and unique reference to the Intellectual Entity/Entities present in the SIP.<br>This identifier MUST be used to establish a link between the `dc+schema.xml` file and the relevant PREMIS object in the `preservation/premis.xml` file. |
| Datatype | [ID]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#id) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `metadata/dcterms:extent` |
|-----------------------|-----------|
| Name | Duration |
| Description | Duration in time of the Intellectual Entity. |
| Datatype | [XML Schema duration]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#xsd-duration) |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `metadata/dcterms:available` |
|-----------------------|-----------|
| Name | Available |
| Description | The moment that the Intellectual Entity became available. |
| Datatype | [XML Schema datetime]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#xsd-datetime) |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `metadata/dcterms:description[@xml:lang=*]` |
|-----------------------|-----------|
| Name | Description |
| Description | An account of the Intellectual Entity.<br>The `description` term MAY only be used multiple times when it uses a different language. The applied language MUST be provided by a `@xml:lang` attribute (see requirements above). There MUST always be an entry in Dutch with `@xml:lang` set to `nl`. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `metadata/dcterms:abstract[@xml:lang=*]` |
|-----------------------|-----------|
| Name | Abstract |
| Description | A long description of the Intellectual Entity.<br>The `abstract` term MAY only be used multiple times when it uses a different language. The applied language MUST be provided by a `@xml:lang` attribute (see requirements above). If the element is present, there MUST always be an entry in Dutch with `@xml:lang` set to `nl`. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `metadata/dcterms:created` |
|-----------------------|-----------|
| Name | Creation date |
| Description | Creation date of the Intellectual Entity. |
| Datatype | [EDTF]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#edtf) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `metadata/dcterms:issued` |
|-----------------------|-----------|
| Name | Date issued |
| Description | Date of formal issuance of the Intellectual Entity. |
| Datatype | [EDTF]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#edtf) |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `metadata/dcterms:publisher` |
|-----------------------|-----------|
| Name | Publisher |
| Description | A publisher of the Intellectual Entity. This element is an alias for `metadata/schema:creator` without the attribute `@roleName`. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `metadata/dcterms:contributor` |
|-----------------------|-----------|
| Name | Contributor |
| Description | A contributor to the Intellectual Entity. This element is an alias for `metadata/schema:creator` without the attribute `@roleName`. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `metadata/dcterms:creator` |
|-----------------------|-----------|
| Name | Creator |
| Description | An author or creator of the Intellectual Entity. This element is an alias for `metadata/schema:creator` without the attribute `@roleName`. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `metadata/dcterms:spatial` |
|-----------------------|-----------|
| Name | Spatial |
| Description | Spatial coverage information on the Intellectual Entity |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `metadata/dcterms:temporal` |
|-----------------------|-----------|
| Name | Temporal |
| Description | Temporal coverage information on the Intellectual Entity |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `metadata/dcterms:subject[@xml:lang=*]` |
|-----------------------|-----------|
| Name | Subject |
| Description | Subjects or keywords related to the Intellectual Entity.<br> If the element is present, the applied language MUST be provided by a `@xml:lang` attribute (see requirements above) and there MUST always be an entry in Dutch with `@xml:lang` set to `nl`. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | SHOULD |

| Element | `metadata/dcterms:language` |
|-----------------------|-----------|
| Name | Language |
| Description | The language that the Intellectual Entity is in. |
| Datatype | [BCP47]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#bcp47) |
| Cardinality | 0..* |
| Obligation | SHOULD |

| Element | `metadata/dcterms:license` |
|-----------------------|-----------|
| Name | License |
| Description | A legal document giving official permission to meemoo, end users of the meemoo platforms, or any other user, to do something with the Intellectual Entity. |
| Vocabulary | See the lists of [licenses](https://developer.meemoo.be/docs/metadata/viaa/licenties.html)  |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | SHOULD |

| Element | `metadata/dcterms:rightsHolder` |
|-----------------------|-----------|
| Name | Rights holder |
| Description | The person or ogranization that holds the copyright to the Intellectual Entity. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Element | `metadata/dcterms:rights[@xml:lang=*]` |
|-----------------------|-----------|
| Name | Rights |
| Description | A copyright notice on the Intellectual Entity. The `rights` term MAY only be used multiple times when it uses a different language. The applied language MUST be provided by a `@xml:lang` attribute (see requirements above). If the element is present, there MUST always be an entry in Dutch with `@xml:lang` set to `nl`. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Element | `metadata/dcterms:type` |
|-----------------------|-----------|
| Name | Type |
| Description | The classification of this Intellectual Entity . |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | MAY |

#### Schema.org elements

| Element | `metadata/schema:creator` |
|-----------------------|-----------|
| Name | Creator artwork |
| Description | The creator/author of the digitally reproduced artwork. This element is an alias for `metadata/dcterms:creator`.  |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `metadata/schema:contributor` |
|-----------------------|-----------|
| Name | Creator artwork |
| Description | An agent that has contributed to the digitally reproduced artwork. This element is an alias for `metadata/dcterms:contributor`.  |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `metadata/schema:publisher` |
|-----------------------|-----------|
| Name | Creator artwork |
| Description | The publisher of the digitally reproduced artwork. This element is an alias for `metadata/dcterms:publisher`.  |
| Cardinality | 0..* |
| Obligation | MAY |

| Attribute | `metadata/(schema:creator|schema:publisher|schema:contributor)/@roleName` |
|-----------------------|-----------|
| Name | Role creator, publisher, or contributor |
| Description | The role with which the creator, publisher, or contributor was involved in creating, publishing or contributing to the digitally reproduced artwork.  |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Vocabulary | See the lists of roles for [makers](https://developer.meemoo.be/docs/metadata/viaa/algemeen.html#mogelijke-sleutels-1), [contributors](https://developer.meemoo.be/docs/metadata/viaa/algemeen.html#bijdrager), and [publisher](https://developer.meemoo.be/docs/metadata/viaa/algemeen.html#mogelijke-sleutels-3).  |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Element | `metadata/(schema:creator|schema:publisher|schema:contributor)/schema:name` |
|-----------------------|-----------|
| Name | Name creator, publisher, or contributor |
| Description | The name of the creator, publisher, or contributor.  |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `metadata/(schema:creator|schema:publisher|schema:contributor)/schema:birthDate` |
|-----------------------|-----------|
| Name | Birth date creator, publisher, or contributor |
| Description | The creator, publisher, or contributor's date of birth.  |
| Datatype | [EDTF]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#edtf) |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `metadata/(schema:creator|schema:publisher|schema:contributor)/schema:deathDate` |
|-----------------------|-----------|
| Name | Death date creator, publisher, or contributor |
| Description | The creator, publisher, or contributor's date of death.  |
| Datatype | [EDTF]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#edtf) |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `metadata/schema:height` |
|-----------------------|-----------|
| Name | Height artwork |
| Description | The measured height of the physical artwork.  |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `metadata/schema:width` |
|-----------------------|-----------|
| Name | Width artwork |
| Description | The measure width of the physical artwork. |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Element | `metadata/schema:depth` |
|-----------------------|-----------|
| Name | Depth artwork |
| Description | The measured depth of the physical artwork. |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Element | `metadata/schema:weight` |
|-----------------------|-----------|
| Name | Depth artwork |
| Description | The measured weight of the physical artwork. |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Element | `metadata/(schema:height|schema:width|schema:depth|schema:weight)/schema:value` |
|-----------------------|-----------|
| Name | Value |
| Description | The height, width, depth, or weight measurement value. |
| Cardinality | 1..1 |
| Datatype | [Float]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#float) |
| Obligation | MUST |

| Element | `metadata/(schema:height|schema:width|schema:depth)/schema:unitCode` |
|-----------------------|-----------|
| Name | Unit Code |
| Description | The unit of length measurement given using the [UN/CEFACT Common Code (3 characters)](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes). |
| Vocabulary | `MMT`, `CMT`, `MTR` |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Element | `metadata/schema:weight/schema:unitCode` |
|-----------------------|-----------|
| Name | Unit Code |
| Description | The unit of weight measurement given using the [UN/CEFACT Common Code (3 characters)](http://wiki.goodrelations-vocabulary.org/Documentation/UN/CEFACT_Common_Codes), which MUST be set to `KGM` (kilograms). |
| Vocabulary | `KGM` |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 0..1 |
| Obligation | SHOULD |

| Element | `metadata/(schema:height|schema:width|schema:depth)/schema:unitText` |
|-----------------------|-----------|
| Name | Unit Text |
| Description | A string or text indicating the unit of the height or width measurement value. Useful if you cannot provide a standard unit code for `schema:unitCode`.  |
| Vocabulary | `mm`, `cm`, `m` |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `metadata/schema:weight/schema:unitText` |
|-----------------------|-----------|
| Name | Unit Text |
| Description | A string or text indicating the unit of the weight measurement value, which MUST be set to `kg` (kilograms). Useful if you cannot provide a standard unit code for `schema:unitCode`.  |
| Vocabulary | `kg` |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `metadata/schema:artMedium[@xml:lang=*]` |
|-----------------------|-----------|
| Name | Art medium |
| Description | The material used to create the physical artwork, e.g. Oil, Watercolour, Acrylic, Linoprint, Marble, Cyanotype, Digital, Lithograph, DryPoint, Intaglio, Pastel, Woodcut, Pencil, Mixed Media, etc. The applied language MUST be provided by a `@xml:lang` attribute (see requirements above). There MUST always be an entry in Dutch with `@xml:lang` set to `nl`. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `metadata/schema:artform[@xml:lang=*]` |
|-----------------------|-----------|
| Name | Artform |
| Description | The type of artform, e.g. Painting, Drawing, Sculpture, Print, Photograph, Assemblage, Collage, etc. The applied language MUST be provided by a `@xml:lang` attribute (see requirements above). There MUST always be an entry in Dutch with `@xml:lang` set to `nl`. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `metadata/schema:isPartOf[@xsi:type=schema:Episode]` |
|-----------------------|-----------|
| Name | Is part of episode |
| Description | Indicates an episode that this item is part of.  |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `metadata/schema:isPartOf[@xsi:type=schema:Episode]/schema:name` |
|-----------------------|-----------|
| Name | Name episode |
| Description | The name of the episode. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `metadata/schema:isPartOf[@xsi:type=schema:ArchiveComponent]` |
|-----------------------|-----------|
| Name | Is part of archive |
| Description |  Indicates an archive that this item is part of.  |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `metadata/schema:isPartOf[@xsi:type=schema:ArchiveComponent]/schema:name` |
|-----------------------|-----------|
| Name | Name archive |
| Description | The name of the archive.  |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `metadata/schema:isPartOf[@xsi:type=schema:CreativeWorkSeries]` |
|-----------------------|-----------|
| Name | Is part of series |
| Description |   Indicates a series that this item is part of. |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `metadata/schema:isPartOf[@xsi:type=schema:CreativeWorkSeries]/schema:name` |
|-----------------------|-----------|
| Name | Name series |
| Description | The name of the series.  |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `metadata/schema:isPartOf[@xsi:type=schema:CreativeWorkSeries]/schema:position` |
|-----------------------|-----------|
| Name | Number series |
| Description | The number of the series.  |
| Datatype | [Integer]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#integer) |
| Cardinality | 0..1 |
| Obligation | MAY |

| Element | `metadata/schema:isPartOf[@xsi:type=schema:CreativeWorkSeries]/schema:hasPart` |
|-----------------------|-----------|
| Name | Has subseries |
| Description | Indicates a creative work that is part of this series.  |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `metadata/schema:isPartOf[@xsi:type=schema:CreativeWorkSeries]/schema:hasPart/schema:name` |
|-----------------------|-----------|
| Name | Name subseries  |
| Description | The name of the subseries.  |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `metadata/schema:isPartOf[@xsi:type=schema:BroadcastEvent]` |
|-----------------------|-----------|
| Name | Is part of broadcast event|
| Description | Indicates a broadcast that this item is part of.   |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `metadata/schema:isPartOf[@xsi:type=schema:BroadcastEvent]/schema:name` |
|-----------------------|-----------|
| Name | Name broadcast event |
| Description |  The name of the broadcast. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `metadata/schema:isPartOf[@xsi:type=schema:CreativeWorkSeason]` |
|-----------------------|-----------|
| Name | Is part of season |
| Description |  Indicates a season that this item is part of.  |
| Cardinality | 0..* |
| Obligation | MAY |

| Element | `metadata/schema:isPartOf[@xsi:type=schema:CreativeWorkSeason]/schema:name` |
|-----------------------|-----------|
| Name | Name season |
| Description |  The name of the season. |
| Datatype | [String]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#string) |
| Cardinality | 1..1 |
| Obligation | MUST |

| Element | `metadata/schema:isPartOf[@xsi:type=schema:CreativeWorkSeason]/schema:seasonNumber` |
|-----------------------|-----------|
| Name | Number season |
| Description |  Position of the season within an ordered group of seasons. |
| Datatype | [Integer]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/2_terminology.md %}#integer) |
| Cardinality | 0..1 |
| Obligation | MAY |

### Validation

The XML files that are required by this profile can be validated using the following XML schema definitions:

| File | Format | XML Schema |
| `mets.xml` | METS v1.22.1 | [mets.xsd](https://www.loc.gov/standards/mets/mets.xsd) |
| `premis.xml` | PREMIS v3.0 | [premis-v3-0.xsd](https://www.loc.gov/standards/premis/v3/premis-v3-0.xsd) |
| `dc+schema.xml` | Dublin Core (custom schema) | [dc_basic.xsd](https://raw.githubusercontent.com/viaacode/sipin-sip-validator/main/app/resources/xsd/dc_basic.xsd)<br>_depends on: [edtf.xsd](https://raw.githubusercontent.com/viaacode/sipin-sip-validator/main/app/resources/xsd/edtf.xsd), [dcterms.xsd](https://github.com/viaacode/sipin-sip-validator/blob/main/app/resources/xsd/dcterms.xsd), [dcmitype.xsd](https://raw.githubusercontent.com/viaacode/sipin-sip-validator/main/app/resources/xsd/dcmitype.xsd), [dc.xsd](https://raw.githubusercontent.com/viaacode/sipin-sip-validator/main/app/resources/xsd/dc.xsd)_|

## Connecting the descriptive metadata to PREMIS

The `dc+schema.xml` file at the package-level contains descriptive metadata about the IE(s) of the SIP.
It relies on the [DCTERMS](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) and [SCHEMA](http://schema.org) metadata schema in order to facilitate a basic description with a limited number of descriptive metadata elements.

There is a link present between each `dc+schema.xml` file and the PREMIS Intellectual Entity in the `preservation/premis.xml` file via a shared ID.
This shared ID is stored in the `<dcterms:identifier>` element of each `dc+schema.xml` file and in a `<premis:objectIdentifier>` element of each PREMIS object in the `preservation/premis.xml` file.

Please note that additional IDs must be dealt with in the `preservation/premis.xml` file via `<premis:objectIdentifier>` elements in which the type of ID is specified using the `<premis:objectIdentifierType>` element.

***Example***

```xml
<?xml version='1.0' encoding='UTF-8'?>
<metadata xmlns="https://data.hetarchief.be/id/sip/1.2/basic" 
      xmlns:dcterms="http://purl.org/dc/terms/" 
      xmlns:xs="http://www.w3.org/2001/XMLSchema/" 
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xmlns:edtf="http://id.loc.gov/datatypes/edtf/">


  <!-- general title for the resource -->
  <dcterms:title xml:lang="nl">Felis Catus Flamens</dcterms:title>

  <!-- linking id between dc and premis -->
  <dcterms:identifier>uuid-b21a86aa-97a3-4f7b-a9f5-4d330af641c0</dcterms:identifier>

  <!-- date unknown -->
  <dcterms:created xsi:type="edtf:EDTF-level1">XXXX</dcterms:created>

  <!-- multiple keywords about the resource -->
  <dcterms:subject xml:lang="nl">Cat</dcterms:subject>
  <dcterms:subject xml:lang="nl">Felis Catus Flamens</dcterms:subject>


</metadata>   
```

## Use Cases

Some use cases that implement this profile are:

{% include _usecases.liquid  %}
