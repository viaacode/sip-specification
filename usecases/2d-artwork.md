---
layout:       default
title:        Two-dimensional artwork
parent:       Use cases
nav_order:    4
nav_exclude:  false
has_children: false
sip_profile:  2d
---
# Use Case: a digitization of a two-dimensional artwork

The following use case describes how to package a reproduction of a two-dimensional artwork such as a painting. 
The reproduction contains multiple flavours of photoregistration: with frame, without frame, stitched, or as partial captures. 
It includes:

- TIFF files;
- basic descriptive metadata;
- basic preservation metadata.

It uses the [**2D SIP profile**]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/profiles/2D.md %}).

A full sample SIP can be viewed [here]({{ site.baseurl }}{% link assets/sip_samples/fa307608-35c3-11ed-9243-7e92631d7d27.zip %}).

## The content

The following content is provided for packaging:

| `7m03z1634f_overzichtsopname_metlijst_tiff.tiff` | An image file in the TIFF file format containing a photoregistration of the painting 'The lamentation over the Dead Christ' with the frame included. |
| `7m03z1634f_overzichtsopname_zonderlijst_tiff.tif` | An image file in the TIFF file format containing a photoregistration of the painting 'The lamentation over the Dead Christ' without the frame. |
| `7m03z1634f_stitch_tiff.tif` | A stitched very high-resolution image file in the TIFF file format containing a photoregistration of the painting 'The lamentation over the Dead Christ'. |
| `7m03z1634f_target_tiff.tif` | A reference image file in the TIFF file format for calibrating the photoregistration hardware. |
| `7m03z1634f_deelopname1_tiff.tif`<br>`7m03z1634f_deelopname2_tiff.tif`<br>`...`<br>`7m03z1634f_deelopname9_tiff.tif` | A very high-resolution image split into multiple files in the TIFF file format containing a photoregistration of the painting 'The lamentation over the Dead Christ'. |
| `metadata.xml` | A metadata record describing the painting 'The lamentation over the Dead Christ'. |

The metadata record can contain the following information:

- the title of the painting;
- a description of the painting;
- the date the painting was created;
- the dimensions of the painting;
- the name, birthdate and deathdate of the artist;
- a list of meemoo licenses;
- some keywords;
- the md5 checksums of the media files;
- rights credits;
- ...

Some of the metadata above is supplied in both English and Dutch.

## Applying the core concepts

Since the metadata only describes a single artwork, we can consider it as the single Intellectual Entity in the SIP.

We can distinguish a couple of file sets (in the TIFF file format) that represent the painting in some manner: an overview with frame, an overview without frame, a stitched high-resolution image, a high-resolution image in parts, and a camera calibration target recording.

Since each set of files can have a meaning on its own (i.e. one could focus on one of the TIFF files to get an idea of what the painting looks like), they are split into separate representations. This results in the following application of the [core concepts]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/3_core-concepts.md %}):

|_Intellectual Entity_|the painting 'The lamentation over the Dead Christ' |
|_Representation 1_| the access copy of the painting with frame |
|_Representation 2_| the access copy of the painting without frame |
|_Representation 3_| the first archive master: a high-resolution stitched representation |
|_Representation 4_| the second archive master: a high-resolution non-stitched representation|
|_Representation 5_| the calibration result|
|_Files (rep. 1)_|the TIFF file: `7m03z1634f_overzichtsopname_metlijst_tiff.tiff`|
|_Files (rep. 2)_|the TIFF file: `7m03z1634f_overzichtsopname_zonderlijst_tiff.tif`|
|_Files (rep. 3)_|the TIFF file: `7m03z1634f_stitch_tiff.tif`|
|_Files (rep. 4)_|the TIFF files: `7m03z1634f_deelopname1_tiff.tif`, `7m03z1634f_deelopname2_tiff.tif`, ..., `7m03z1634f_deelopname9_tiff.tif`|
|_Files (rep. 5)_|the TIFF file: `7m03z1634f_target_tiff`|

This case relies on the 2D profile because:

- there is one IE and multiple representations;
- the painting can be described using a combination of the [DCTERMS](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) and [Schema](schema.org/) metadata models;

## Directory structure

We package the above in a meemoo SIP named `fa307608-35c3-11ed-9243-7e92631d7d27.zip`.
It has the following directory structure:

```plaintext
root_directory
│── manifest-md5.txt
│── bagit.txt
└── data
    │── mets.xml
    │── metadata
    |   |── descriptive
    |   |   |── dc.xml
    |   |   └── schema.xml
    |   └── preservation
    |       └── premis.xml
    │
    └── representations
        |── representation_1       # overview with frame
        |   │── mets.xml
        |   |── data
        |   │   └── 7m03z1634f_overzichtsopname_metlijst_tiff.tiff
        |   └──metadata
        |      |── descriptive    
        |      |   └── dc.xml   
        |      └── preservation
        |          └── premis.xml
        |── representation_2       # overview without frame
        |   │── mets.xml
        |   |── data
        |   │   └── 7m03z1634f_overzichtsopname_zonderlijst_tiff.tif
        |   └──metadata
        |      |── descriptive     
        |      |   └── dc.xml   
        |      └── preservation
        |          └── premis.xml
        |── representation_3       # composed stitch 
        |   │── mets.xml
        |   |── data
        |   │   └── 7m03z1634f_stitch_tiff.tif
        |   └──metadata    
        |      └── preservation
        |          └── premis.xml
        |── representation_4       # stitch 
        |   │── mets.xml
        |   |── data
        |   |   |── 7m03z1634f_deelopname1_tiff.tif
        |   |   |── 7m03z1634f_deelopname2_tiff.tif
        |   |   |── ...
        |   │   └── 7m03z1634f_deelopname9_tiff.tif
        |   └── metadata
        |       └── preservation
        |           └── premis.xml
        └── representation_5       # target 
           │── mets.xml
           |── data
           │   └── 7m03z1634f_target_tiff.tif
           └── metadata
               └── preservation
                   └── premis.xml

```

## The metadata

In total, the SIP contains 13 metadata files:

|`data/metadata/descriptive/dc.xml`| Descriptive metadata about the IE residing at the _package level_ using the [DCTERMS](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) metadata schema. |
|`data/metadata/descriptive/schema.xml`| Descriptive metadata about the IE residing at the _package level_ using the [Schema](schema.org/) metadata schema. |
|`data/metadata/preservation/premis.xml`| Preservation metadata about the IE residing at the _package level_, including any PREMIS events related to the SIP/package/representations. |
|`data/representations/representation_*/metadata/preservation/premis.xml`| Preservation metadata about the representation and TIFF files residing at the _representation level_. |

### /data/metadata/descriptive/dc.xml

The `dc.xml` of the package level describes the IE using [the DCTERMS]((https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)) and the [Schema](schema.org/) metadata models.
It contains minimal metadata such as a title, a description, an identifier, a date of creation and of issuance...

The identifier is used to link the `dc.xml` file to the corresponding PREMIS object in the `preservation/premis.xml` file of the package level (see [here]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/sip_structure/5_structure_package.md %}#shareduuidinfo) for more information).

```xml
<?xml version='1.0' encoding='UTF-8'?>
<metadata xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xs="http://www.w3.org/2001/XMLSchema/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance/" xmlns:edtf="http://id.loc.gov/datatypes/edtf/" xmlns:schema="https://schema.org/">

  <!-- general title for the resource -->
  <dcterms:title xml:lang="nl">Bewening van Christus</dcterms:title>
  <dcterms:title xml:lang="en">The lamentation over the Dead Christ</dcterms:title>

  <!-- general description for the resource -->
  <dcterms:description xml:lang="nl">Rond 1629 geschilderd voor het hoogaltaar van de Begijnhofkerk te Antwerpen. Een tweede exemplaar wordt bewaard te Madrid (Prado); schetsen te Leningrad (Hermitage) een kleinere herhaling te Hagley (Lord Littleton) een tekening in Atger Museum te Montpellier en een grisaille studie tenslotte bevond zich in 1776 in de veiling Randon de Boisset. Het schilderij werd gegraveerd door Paul Pontius en Andreas van Rymsdyck.</dcterms:description>
  <dcterms:description xml:lang="en">Painted around 1629 for the high altar of the Beguinage Church in Antwerp. A second copy is kept in Madrid (Prado); sketches at Leningrad (Hermitage) a smaller repetition at Hagley (Lord Littleton) a drawing in the Atger Museum in Montpellier and finally a grisaille study was in the Randon de Boisset auction in 1776. The painting was engraved by Paul Pontius and Andreas van Rymsdyck.</dcterms:description>

  <!-- linking id between dc and premis -->
  <dcterms:identifier>7m03z1634f</dcterms:identifier>

  <!-- creationdate -->
  <dcterms:created xsi:type="edtf:EDTF-level1">1628/1629</dcterms:created>

  <dcterms:subject xml:lang="nl">topstukken</dcterms:subject>
  <dcterms:subject xml:lang="nl">religie</dcterms:subject>
  <dcterms:subject xml:lang="nl">Christus</dcterms:subject>

  <!-- rights note -->
  <dcterms:rights xml:lang="en">public domain</dcterms:rights>

</metadata>
```

### /data/metadata/descriptive/schema.xml

The `schema.xml` of the package level describes the IE using [Schema metadata schema](schema.org/).
It contains additional metadata such as the dimensions of the artwork, information about the artist, the art medium and the type of artwork.

Similar to `dc.xml`, the identifier is used to link the `schema.xml` file to the corresponding PREMIS object in the `preservation/premis.xml` file of the package level.

```xml
<?xml version='1.0' encoding='UTF-8'?>
<metadata xmlns:xs="http://www.w3.org/2001/XMLSchema/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance/" xmlns:edtf="http://id.loc.gov/datatypes/edtf/" xmlns:schema="https://schema.org/">

  <!-- linking id between dc and premis -->
  <schema:identifier>7m03z1634f</schema:identifier>

  <schema:creator schema:roleName="auteur">
    <schema:name>Anthony van Dyck</schema:name>
    <schema:birthDate xsi:type="xsd:dateTime">1599</schema:birthDate>
    <schema:deathDate xsi:type="xsd:dateTime">1641</schema:deathDate>
  </schema:creator>

  <!-- creator -->
  <schema:creator schema:roleName="auteur">
    <schema:name>Anthony van Dyck</schema:name>
    <schema:birthDate xsi:type="xsd:dateTime">1599</schema:birthDate>
    <schema:deathDate xsi:type="xsd:dateTime">1641</schema:deathDate>
  </schema:creator>

  <!-- dimensions -->
  <schema:height>
    <schema:value>3030</schema:value>
    <schema:unitText>mm</schema:unitText>
    <schema:unitCode>MMT</schema:unitCode>
  </schema:height>
  <schema:width>
    <schema:value>2250</schema:value>
    <schema:unitText>mm</schema:unitText>
    <schema:unitCode>MMT</schema:unitCode>
  </schema:width>
  <schema:artMedium xml:lang="nl">olieverf op doek</schema:artMedium>
  <schema:artMedium xml:lang="en">oil on canvas</schema:artMedium>
  <schema:artform xml:lang="en">painting</schema:artform>
  <schema:artform xml:lang="nl">schilderij</schema:artform>

</metadata>
```

### data/metadata/preservation/premis.xml

The `premis.xml` of the package level describes the IE and the relationships with its representations.
It also contains a digitization event that details how the TIFF files were created and by who.

Note that the identifier in the `<premis:objectIdentifier>` element is shared with the `<dcterms:identifier/>` (in the `descriptive/dc.xml` file) in order to link the PREMIS IE object to its descriptions in the two files.


```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:schema="http://schema.org/" xmlns:premis="http://www.loc.gov/premis/v3" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

    <!-- IE about the artwork -->
    <premis:object xsi:type="premis:intellectualEntity">
        <premis:objectIdentifier>
            <premis:objectIdentifierType>VIAA PID</premis:objectIdentifierType>
            <premis:objectIdentifierValue>7m03z1634f</premis:objectIdentifierValue>
        </premis:objectIdentifier>

        <premis:objectIdentifier>
            <premis:objectIdentifierType>Topstuk_ID</premis:objectIdentifierType>
            <premis:objectIdentifierValue>213</premis:objectIdentifierValue>
        </premis:objectIdentifier>

        <premis:objectIdentifier>
            <premis:objectIdentifierType>Inventarisnummer</premis:objectIdentifierType>
            <premis:objectIdentifierValue>IB00.008</premis:objectIdentifierValue>
        </premis:objectIdentifier>

        <!-- relationship between IE and its representations -->
        <premis:relationship>
            <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
            <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isr">is represented by</premis:relationshipSubType>
            <premis:relatedObjectIdentifier>
                <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
                <premis:relatedObjectIdentifierValue>uuid-187DA428-6BA1-4EB7-B786-CD4AF85A02B1</premis:relatedObjectIdentifierValue>
            </premis:relatedObjectIdentifier>
            <premis:relatedObjectIdentifier>
                <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
                <premis:relatedObjectIdentifierValue>uuid-8DA0F75B-1031-4F20-B26C-184B919B1A43</premis:relatedObjectIdentifierValue>
            </premis:relatedObjectIdentifier>
            <premis:relatedObjectIdentifier>
                <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
                <premis:relatedObjectIdentifierValue>uuid-51F2C0F1-CA06-4B59-9605-54F7C91BA53F</premis:relatedObjectIdentifierValue>
            </premis:relatedObjectIdentifier>
            <premis:relatedObjectIdentifier>
                <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
                <premis:relatedObjectIdentifierValue>uuid-4e475706-2752-4f77-9069-1f71c0e22572</premis:relatedObjectIdentifierValue>
            </premis:relatedObjectIdentifier>
            <premis:relatedObjectIdentifier>
                <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
                <premis:relatedObjectIdentifierValue>uuid-ddcf9e36-35ae-11ed-b866-7e92631d7d27</premis:relatedObjectIdentifierValue>
            </premis:relatedObjectIdentifier>
        </premis:relationship>

    </premis:object>

    <!-- Digitization event -->

    <premis:event>
        <premis:eventIdentifier>
            <premis:eventIdentifierType>UUID</premis:eventIdentifierType>
            <premis:eventIdentifierValue>uuid-187DA428-6BA1-4EB7-B786-CD4AF85A02B1</premis:eventIdentifierValue>
        </premis:eventIdentifier>
        <premis:eventType>digitization</premis:eventType>
        <premis:eventDateTime>2022-06-15T00:00:00Z</premis:eventDateTime>

        <premis:eventOutcomeInformation>
            <premis:eventOutcome>success</premis:eventOutcome>
        </premis:eventOutcomeInformation>

        <premis:linkingAgentIdentifier>
            <premis:linkingAgentIdentifierType>VIAA SP Agent ID</premis:linkingAgentIdentifierType>
            <premis:linkingAgentIdentifierValue>OR-xg9fb0b</premis:linkingAgentIdentifierValue>
            <premis:linkingAgentRole valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp">implementer</premis:linkingAgentRole>
        </premis:linkingAgentIdentifier>

        <premis:linkingObjectIdentifier>
            <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
            <premis:linkingObjectIdentifierValue>uuid-187DA428-6BA1-4EB7-B786-CD4AF85A02B1</premis:linkingObjectIdentifierValue>
            <premis:linkingObjectRole valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/out">outcome</premis:linkingObjectRole>
        </premis:linkingObjectIdentifier>
        <premis:linkingObjectIdentifier>
            <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
            <premis:linkingObjectIdentifierValue>uuid-51F2C0F1-CA06-4B59-9605-54F7C91BA53F</premis:linkingObjectIdentifierValue>
            <premis:linkingObjectRole valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/out">outcome</premis:linkingObjectRole>
        </premis:linkingObjectIdentifier>
        <premis:linkingObjectIdentifier>
            <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
            <premis:linkingObjectIdentifierValue>uuid-187DA428-6BA1-4EB7-B786-CD4AF85A02B1</premis:linkingObjectIdentifierValue>
            <premis:linkingObjectRole valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/out">outcome</premis:linkingObjectRole>
        </premis:linkingObjectIdentifier>
        <premis:linkingObjectIdentifier>
            <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
            <premis:linkingObjectIdentifierValue>uuid-4e475706-2752-4f77-9069-1f71c0e22572</premis:linkingObjectIdentifierValue>
            <premis:linkingObjectRole valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/out">outcome</premis:linkingObjectRole>
        </premis:linkingObjectIdentifier>
        <premis:linkingObjectIdentifier>
            <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
            <premis:linkingObjectIdentifierValue>uuid-ddcf9e36-35ae-11ed-b866-7e92631d7d27</premis:linkingObjectIdentifierValue>
            <premis:linkingObjectRole valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/out">outcome</premis:linkingObjectRole>
        </premis:linkingObjectIdentifier>

    </premis:event>

    <premis:agent>
        <premis:agentIdentifier>
            <premis:agentIdentifierType>VIAA SP Agent ID</premis:agentIdentifierType>
            <premis:agentIdentifierValue>OR-xg9fb0b</premis:agentIdentifierValue>
        </premis:agentIdentifier>
        <premis:agentName>Cedric Verhelst</premis:agentName>
        <premis:agentType>person</premis:agentType>
        <premis:agentExtension>
            <schema:affiliation>Cedric Verhelst bv</schema:affiliation>
        </premis:agentExtension>
    </premis:agent>

</premis:premis>
```

### data/representations/representation_1/metadata/descriptive/dc.xml

The `dc.xml` of the representation level describes the representation using [the DCTERMS metadata schema](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/).
It contains minimal metadata about licenses that might divert from the IE's license.

The identifier is used to link the `dc.xml` file to the corresponding PREMIS object in the `preservation/premis.xml` file of the package level (see [here]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/sip_structure/5_structure_package.md %}#shareduuidinfo) for more information).

```xml
<?xml version='1.0' encoding='UTF-8'?>
<metadata xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xs="http://www.w3.org/2001/XMLSchema/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance/" xmlns:edtf="http://id.loc.gov/datatypes/edtf/" xmlns:schema="https://schema.org">

    <!-- linking id between dc and premis -->
    <dcterms:identifier>uuid-187DA428-6BA1-4EB7-B786-CD4AF85A02B1</dcterms:identifier>

    <!-- licenses -->
    <dcterms:license>CCBY-NC-ND-CONTENT</dcterms:license>
    <dcterms:license>CP-website</dcterms:license>

</metadata>
```

### data/representations/representation_1/metadata/preservation/premis.xml

The `premis.xml` file of the first representation describes two PREMIS objects:

1. the representation;
2. the TIFF file `7m03z1634f_overzichtsopname_metlijst_tiff.tiff`;

It also describes the various relationships between these objects:

1. the relation between the representation and the IE at the package level;
2. the relations between the representation and the TIFF file;

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

  <premis:object xsi:type="premis:representation">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-187DA428-6BA1-4EB7-B786-CD4AF85A02B1</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship between representation and its files -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/inc">includes</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-6A07B2FE-3363-4B46-953E-59A30BE67F9B</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship between representation and its IE/subIE -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/rep">represents</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>VIAA PID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>7m03z1634f</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>
  </premis:object>

  <premis:object xsi:type="premis:file">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-6A07B2FE-3363-4B46-953E-59A30BE67F9B</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:objectCharacteristics>
      <premis:fixity>
        <premis:messageDigestAlgorithm authority="cryptographicHashFunctions" authorityURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions" valueURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5">
                MD5
        </premis:messageDigestAlgorithm>
        <premis:messageDigest>08d339fdc35d17620992cbeeecaca8eb</premis:messageDigest>
      </premis:fixity>
      <premis:size>558891008</premis:size>
      <premis:format>
        <premis:formatRegistry>
          <premis:formatRegistryName>PRONOM</premis:formatRegistryName>
          <premis:formatRegistryKey>fmt/154</premis:formatRegistryKey>
          <premis:formatRegistryRole authority="http://id.loc.gov/vocabulary/preservation/formatRegistryRole" valueURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole/spe">specification</premis:formatRegistryRole>
        </premis:formatRegistry>
        <premis:formatNote></premis:formatNote>
      </premis:format>
    </premis:objectCharacteristics>

    <premis:originalName>7m03z1634f_overzichtsopname_metlijst_tiff</premis:originalName>

    <!-- relationship between file and its representation -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isi">is included in</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-187DA428-6BA1-4EB7-B786-CD4AF85A02B1</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>

</premis:premis>
```

The folders of representation 2, 3, and 5 have a identical structure.


### data/representations/representation_4/metadata/preservation/premis.xml

The `premis.xml` file of the fourth representation describes 10 PREMIS objects (of which the first two are shown in the example below):

1. the representation;
2. the nine TIFF files `7m03z1634f_deelopname1_tiff`, ... , `7m03z1634f_deelopname9_tiff`;

It also describes the various relationships between these objects:

1. the relation between the representation and the IE at the package level;
2. the relations between the representation and the TIFF files;

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

  <premis:object xsi:type="premis:representation">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-4e475706-2752-4f77-9069-1f71c0e22572</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship between representation and its files -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/inc">includes</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-075BF4BB-559A-497E-AA58-EEF7287F0A39</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-94F620EB-C269-45F0-A276-1C0319E5330F</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-75360EDC-A6D7-47BF-86D7-476EE59AF4A0</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-D22C8951-2A17-4856-9006-5F8613BD52C0</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-8E6174A1-FD31-432E-A780-8DC15BA4B0DD</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-1A40CBB1-C36A-4CAD-BEA0-7474BA96DD24</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-A5C4CCEE-A034-416E-B3D2-8EBE949C2F01</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-F64294B9-1224-40D3-AF63-29B9E26028AC</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-B15A7521-92A6-42DB-BCA4-8F16ABC7FCF9</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship between representation and its IE/subIE -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/rep">represents</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>VIAA PID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>7m03z1634f</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>
  </premis:object>

    <!-- relationship between file and its representation -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isi">is included in</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-4e475706-2752-4f77-9069-1f71c0e22572</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>
  <premis:object xsi:type="premis:file">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-075BF4BB-559A-497E-AA58-EEF7287F0A39</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:objectCharacteristics>
      <premis:fixity>
        <premis:messageDigestAlgorithm authority="cryptographicHashFunctions" authorityURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions" valueURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5">
                MD5
        </premis:messageDigestAlgorithm>
        <premis:messageDigest>6f556d6b193a0af3eca85a2b382273bc</premis:messageDigest>
      </premis:fixity>
      <premis:size>605028352</premis:size>
      <premis:format>
        <premis:formatRegistry>
          <premis:formatRegistryName>PRONOM</premis:formatRegistryName>
          <premis:formatRegistryKey>fmt/154</premis:formatRegistryKey>
          <premis:formatRegistryRole authority="http://id.loc.gov/vocabulary/preservation/formatRegistryRole" valueURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole/spe">specification</premis:formatRegistryRole>
        </premis:formatRegistry>
        <premis:formatNote></premis:formatNote>
      </premis:format>
    </premis:objectCharacteristics>

    <premis:originalName>7m03z1634f_deelopname1_tiff</premis:originalName>

    <!-- relationship between file and its representation -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isi">is included in</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-4e475706-2752-4f77-9069-1f71c0e22572</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>

  <premis:object xsi:type="premis:file">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-94F620EB-C269-45F0-A276-1C0319E5330F</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:objectCharacteristics>
      <premis:fixity>
        <premis:messageDigestAlgorithm authority="cryptographicHashFunctions" authorityURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions" valueURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5">
                MD5
        </premis:messageDigestAlgorithm>
        <premis:messageDigest>e1f53063d78e0a3f399d41ef764775f1</premis:messageDigest>
      </premis:fixity>
      <premis:size>605028352</premis:size>
      <premis:format>
        <premis:formatRegistry>
          <premis:formatRegistryName>PRONOM</premis:formatRegistryName>
          <premis:formatRegistryKey>fmt/154</premis:formatRegistryKey>
          <premis:formatRegistryRole authority="http://id.loc.gov/vocabulary/preservation/formatRegistryRole" valueURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole/spe">specification</premis:formatRegistryRole>
        </premis:formatRegistry>
        <premis:formatNote></premis:formatNote>
      </premis:format>
    </premis:objectCharacteristics>

    <premis:originalName>7m03z1634f_deelopname2_tiff</premis:originalName>

    <!-- relationship between file and its representation -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isi">is included in</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-4e475706-2752-4f77-9069-1f71c0e22572</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>

  [similar to above for the other TIFF files]

</premis:premis>
```
