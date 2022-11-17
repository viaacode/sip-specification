---
layout:       default
title:        Gigapixel artwork
parent:       Use cases
grand_parent:  SIP Specification 1.1
nav_order:    6
nav_exclude:  false
has_children: false
sip_profile:  Material artwork
---
Editor's Draft
{: .label .label-yellow }
# Use Case: a gigapixel digitization of a two-dimensional artwork

The following use case describes how to package a gigapixel reproduction of a two-dimensional artwork such as a drawing or painting. 
The reproduction contains multiple flavours of photoregistration: with frame, without frame, stitched, or as partial captures. 
It includes:

- TIFF files;
- an Adobe Photoshop PSB file
- basic descriptive metadata;
- basic preservation metadata.

It uses the [**material-artwork SIP profile**]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/profiles/material-artwork.md %}).

## The content

The following content is provided for packaging:

| `cf9j41p15z_overzichtsopname_metlijst_tiff.tiff` | An image file in the TIFF file format containing a photoregistration of an 'Uur- en kalenderwijzerplaat' with the frame included. |
| `cf9j41p15z_overzichtsopname_zonderlijst_tiff.tiff` | An image file in the TIFF file format containing a photoregistration of the 'Uur- en kalenderwijzerplaat' without the frame. |
| `cf9j41p15z_stitch_bigtiff.tiff` | A stiched very high-resolution image file in the TIFF file format containing a photoregistration of the 'Uur- en kalenderwijzerplaat'. |
| `cf9j41p15z_stitch_psb.psb` | A stitched very high-resolution image file in the Adobe Photoshop Large Document Format containing a photoregistration of the 'Uur- en kalenderwijzerplaat'. |
| `cf9j41p15z_target_tiff.tiff` | A reference image file in the TIFF file format for calibrating the photoregistration hardware. |
| `cf9j41p15z_Kolom1_deelopname1_tiff.tiff`<br>`cf9j41p15z_Kolom1_deelopname2_tiff.tiff`<br>`...`<br>`cf9j41p15z_Kolom5_deelopname6_tiff.tiff` | A very high-resolution image split into multiple files in the TIFF file format containing a photoregistration of the 'Uur- en kalenderwijzerplaat'. |
| `metadata.xml` | A metadata record describing the 'Uur- en kalenderwijzerplaat'. |

The metadata record can contain the following information:

- the title of the work;
- a description of the work;
- a local identifier (e.g. Inventarisnummer)
- the date the work was created;
- the dimensions of the work;
- the name, birthdate and deathdate of the artist;
- a list of meemoo licenses;
- some keywords;
- the md5 checksums of the media files;
- rights credits;
- ...

Some of the metadata above is supplied in both English and Dutch.

## Applying the core concepts

Since the metadata only describes a single artwork, we can consider it as the single Intellectual Entity in the SIP.

We can distinguish a couple of file sets (in the TIFF or PSB file format) that represent the work in some manner: an overview with frame, an overview without frame, a stitched high-resolution image, a high-resolution image in parts, and a camera calibration target recording.

Since each set of files can have a meaning on its own (i.e. one could focus on one of the TIFF files to get an idea of what the painting looks like), they are split into separate representations. This results in the following application of the [core concepts]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/3_core-concepts.md %}):

|_Intellectual Entity_|the 'Uur- en kalenderwijzerplaat' |
|_Representation 1_| the access copy of the painting with frame |
|_Representation 2_| the access copy of the painting without frame |
|_Representation 3_| the first archive master: a high-resolution stitched representation in TIFF format |
|_Representation 4_| the second archive master: a high-resolution stitched representation in Adobe Photoshop Large Document Format |
|_Representation 5_| the second archive master: a high-resolution non-stitched representation|
|_Representation 6_| the calibration result|
|_Files (rep. 1)_|the TIFF file: `cf9j41p15z_overzichtsopname_metlijst_tiff.tiff`|
|_Files (rep. 2)_|the TIFF file: `cf9j41p15z_overzichtsopname_zonderlijst_tiff.tiff`|
|_Files (rep. 3)_|the TIFF file: `cf9j41p15z_stitch_bigtiff.tiff` |
|_Files (rep. 4)_|the PSB file: `cf9j41p15z_stitch_psb.psb`|
|_Files (rep. 5)_|the TIFF files: `cf9j41p15z_Kolom1_deelopname1_tiff.tiff`, `cf9j41p15z_Kolom1_deelopname2_tiff.tiff`, ..., `cf9j41p15z_Kolom5_deelopname6_tiff.tiff`|
|_Files (rep. 6)_|the TIFF file: `cf9j41p15z_target_tiff.tiff`|

This case relies on the material-artwork profile because:

- there is one IE and multiple representations;
- the artwork can be described using a combination of DCTERMS and a Schema.org;

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
    |   |   └── dc+schema.xml
    |   └── preservation
    |       └── premis.xml
    │
    └── representations
        |── representation_1       # overview with list
        |   │── mets.xml
        |   |── data
        |   │   └── cf9j41p15z_overzichtsopname_metlijst_tiff.tiff
        |   └──metadata
        |      |── descriptive    
        |      |   └── dc+schema.xml   
        |      └── preservation
        |          └── premis.xml
        |── representation_2       # overview without list
        |   │── mets.xml
        |   |── data
        |   │   └── cf9j41p15z_overzichtsopname_zonderlijst_tiff.tiff
        |   └──metadata
        |      |── descriptive     
        |      |   └── dc+schema.xml   
        |      └── preservation
        |          └── premis.xml
        |── representation_3       # composed stitch 
        |   │── mets.xml
        |   |── data
        |   │   └── cf9j41p15z_stitch_bigtiff.tiff
        |   └──metadata
        |      |── descriptive   
        |      |   └── dc+schema.xml         
        |      └── preservation
        |          └── premis.xml
        |── representation_4       # composed stitch in PSB
        |   │── mets.xml
        |   |── data
        |   │   └── cf9j41p15z_stitch_psb.psb
        |   └──metadata
        |      |── descriptive   
        |      |   └── dc+schema.xml         
        |      └── preservation
        |          └── premis.xml
        |── representation_5       # stitch 
        |   │── mets.xml
        |   |── data
        |   |   |── cf9j41p15z_Kolom1_deelopname1_tiff.tiff
        |   |   |── cf9j41p15z_Kolom1_deelopname2_tiff.tiff
        |   |   |── ...
        |   │   └── cf9j41p15z_Kolom5_deelopname6_tiff.tiff`
        |   └── metadata
        |       |── descriptive     
        |       |   └── dc+schema.xml    
        |       └── preservation
        |           └── premis.xml
        └── representation_6       # target 
           │── mets.xml
           |── data
           │   └── cf9j41p15z_target_tiff.tiff
           └── metadata
               |── descriptive     
               |   └── dc+schema.xml    
               └── preservation
                   └── premis.xml

```

## The metadata

In total, the SIP contains 13 metadata files:

|`data/metadata/descriptive/dc+schema.xml`| Descriptive metadata about the IE residing at the _package level_ using the [DCTERMS](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) and [Schema](schema.org/) metadata schema. |
|`data/metadata/preservation/premis.xml`| Preservation metadata about the IE residing at the _package level_, including any PREMIS events related to the SIP/package/representations. |
|`data/representations/representation_1/metadata/preservation/premis.xml`| Preservation metadata about the first representation and TIFF file residing at the _representation level_. |
|`data/representations/representation_2/metadata/preservation/premis.xml`| Preservation metadata about the second representation and TIFF file residing at the _representation level_. |
|`data/representations/representation_3/metadata/preservation/premis.xml`| Preservation metadata about the third representation and TIFF file residing at the _representation level_. |
|`data/representations/representation_4/metadata/preservation/premis.xml`| Preservation metadata about the fourth representation and PSB file residing at the _representation level_. |
|`data/representations/representation_5/metadata/preservation/premis.xml`| Preservation metadata about the fifth representation and TIFF files residing at the _representation level_. |
|`data/representations/representation_6/metadata/preservation/premis.xml`| Preservation metadata about the sixth representation and TIFF file residing at the _representation level_. |

### /data/metadata/descriptive/dc+schema.xml

The `dc+schema.xml` of the package level describes the IE using [the DCTERMS]((https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)) and the [Schema](schema.org/) metadata models.
It contains minimal metadata such as a title, a description, an identifier, a date of creation and of issuance, and additional metadata such as the dimensions of the artwork, information about the artist, the art medium and the type of artwork.

The identifier in the `<dcterms:identifier/>` element is used to link the `dc+schema.xml` file to the corresponding PREMIS object in the `preservation/premis.xml` file of the package level (see [here]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/sip_structure/5_structure_package.md %}#shareduuidinfo) for more information).

```xml
<?xml version='1.0' encoding='UTF-8'?>
<metadata xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xs="http://www.w3.org/2001/XMLSchema/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance/" xmlns:edtf="http://id.loc.gov/datatypes/edtf/" xmlns:schema="https://schema.org/">

  <!-- general title for the resource -->
  <dcterms:title xml:lang="nl">Uur- en kalenderwijzeplaat</dcterms:title>

  <!-- general description for the resource -->
  <dcterms:description xml:lang="nl">De unieke Brabantse uur- en kalenderwijzerplaat van circa 1500 vertelt als een groot en minitieus geschilderd prentenboek de verhalen van de dierenriem de maanden en de planetenkinderen.</dcterms:description>

  <!-- linking id between dc and premis -->
  <dcterms:identifier>cf9j41p15z</dcterms:identifier>

  <!-- creationdate -->
  <dcterms:created xsi:type="edtf:EDTF">1500</dcterms:created>

  <dcterms:subject xml:lang="nl">topstukken</dcterms:subject>
  <dcterms:subject xml:lang="nl">religie</dcterms:subject>
  <dcterms:subject xml:lang="nl">Christus</dcterms:subject>

  <!-- creator -->
  <dcterms:creator schema:roleName="auteur">
    Anoniem (Anoniem Leuvens Meester)
  </dcterms:creator>

  <!-- rights note -->
  <dcterms:rights xml:lang="en">public domain</dcterms:rights>

  <!-- dimensions -->
  <schema:height>
    <schema:value>123,4</schema:value>
    <schema:unitText>cm</schema:unitText>
    <schema:unitCode>CMT</schema:unitCode>
  </schema:height>
  <schema:width>
    <schema:value>125,6</schema:value>
    <schema:unitText>cm</schema:unitText>
    <schema:unitCode>CMT</schema:unitCode>
  </schema:width>
  <schema:artMedium xml:lang="nl">olieverf op doek</schema:artMedium>
  <schema:artMedium xml:lang="en">oil on canvas</schema:artMedium>
  <schema:artform xml:lang="en">painting</schema:artform>
  <schema:artform xml:lang="nl">schilderij</schema:artform>
</metadata>
```

### data/metadata/preservation/premis.xml

The `premis.xml` of the package level describes the IE and the relationships with its representations.
It also contains a digitization event that details how the TIFF files were created and by whom.

Note that the identifier in the `<premis:objectIdentifier>` element is shared with the `<dcterms:identifier/>` (in the `descriptive/dc+schema.xml` file) element in order to link the PREMIS IE object to its description.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:schema="http://schema.org/" xmlns:premis="http://www.loc.gov/premis/v3" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

    <!-- IE about the artwork -->
    <premis:object xsi:type="premis:intellectualEntity">
        <premis:objectIdentifier>
            <premis:objectIdentifierType>VIAA PID</premis:objectIdentifierType>
            <premis:objectIdentifierValue>cf9j41p15z</premis:objectIdentifierValue>
        </premis:objectIdentifier>

        <premis:objectIdentifier>
            <premis:objectIdentifierType>Topstuk_ID</premis:objectIdentifierType>
            <premis:objectIdentifierValue>222</premis:objectIdentifierValue>
        </premis:objectIdentifier>

        <premis:objectIdentifier>
            <premis:objectIdentifierType>Inventarisnummer</premis:objectIdentifierType>
            <premis:objectIdentifierValue>S/4/O</premis:objectIdentifierValue>
        </premis:objectIdentifier>

        <premis:relationship>
            <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
            <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isr">is represented by</premis:relationshipSubType>
            <premis:relatedObjectIdentifier>
                <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
                <premis:relatedObjectIdentifierValue>uuid-7507ec4a-39e0-4ddd-8c7e-95bdaa7bbbc6</premis:relatedObjectIdentifierValue>
            </premis:relatedObjectIdentifier>
        </premis:relationship>

        <!-- relationship between nested IE and its representation -->
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
                <premis:relatedObjectIdentifierValue>uuid-70dd6ae0-37fe-11ed-9b20-7e92631d7d28</premis:relatedObjectIdentifierValue>
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
        <premis:eventDateTime>03-08-2022T00:00:00Z</premis:eventDateTime>

        <premis:eventOutcomeInformation>
            <premis:eventOutcome>success</premis:eventOutcome>
        </premis:eventOutcomeInformation>

        <premis:linkingAgentIdentifier>
            <premis:linkingAgentIdentifierType>VIAA SP Agent ID</premis:linkingAgentIdentifierType>
            <premis:linkingAgentIdentifierValue>OR-319s272</premis:linkingAgentIdentifierValue>
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
            <premis:linkingObjectIdentifierValue>uuid-70dd6ae0-37fe-11ed-9b20-7e92631d7d28</premis:linkingObjectIdentifierValue>
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
            <premis:agentIdentifierValue>OR-319s272</premis:agentIdentifierValue>
        </premis:agentIdentifier>
        <premis:agentName>Rik Klein Gotink</premis:agentName>
        <premis:agentType>person</premis:agentType>
        <premis:agentExtension>
            <schema:affiliation>Rik Klein Gotink fotografie</schema:affiliation>
        </premis:agentExtension>
    </premis:agent>

</premis:premis>
```

### data/representations/representation_4/metadata/preservation/premis.xml

The `premis.xml` file of the fourth representation describes two PREMIS objects:

1. the representation;
2. the PSB file `cf9j41p15z_stitch_psb.psb`;

It also describes the various relationships between these objects:

1. the relation between the representation and the IE at the package level;
2. the relations between the representation and the PSB file;

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

  <premis:object xsi:type="premis:representation">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-70dd6ae0-37fe-11ed-9b20-7e92631d7d28</premis:objectIdentifierValue>
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
        <premis:relatedObjectIdentifierValue>cf9j41p15z</premis:relatedObjectIdentifierValue>
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
          <premis:formatRegistryKey>fmt/996</premis:formatRegistryKey>
          <premis:formatRegistryRole authority="http://id.loc.gov/vocabulary/preservation/formatRegistryRole" valueURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole/spe">specification</premis:formatRegistryRole>
        </premis:formatRegistry>
        <premis:formatNote></premis:formatNote>
      </premis:format>
    </premis:objectCharacteristics>

    <premis:originalName>cf9j41p15z_stitch_psb</premis:originalName>

    <!-- relationship between file and its representation -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isi">is included in</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-70dd6ae0-37fe-11ed-9b20-7e92631d7d28</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>

</premis:premis>
```

The `premis.xml` file of representation 1, 2, 3 have an identical structure.


### data/representations/representation_5/metadata/preservation/premis.xml

The `premis.xml` file of the fifth representation describes 30 PREMIS objects (of which the first two are shown in the example below):

1. the representation;
2. the nine TIFF files `cf9j41p15z_Kolom1_deelopname1_tiff.tiff`, `cf9j41p15z_Kolom1_deelopname2_tiff.tiff`, ..., `cf9j41p15z_Kolom5_deelopname6_tiff.tiff`;

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
      <!-- ( there is a premis:relatedObjectIdentifier all 30 files) -->
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
        <premis:relatedObjectIdentifierValue>cf9j41p15z</premis:relatedObjectIdentifierValue>
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
        <premis:messageDigest>d41d8cd98f00b204e9800998ecf8427e</premis:messageDigest>
      </premis:fixity>
      <premis:size>1735648</premis:size>
      <premis:format>
        <premis:formatRegistry>
          <premis:formatRegistryName>PRONOM</premis:formatRegistryName>
          <premis:formatRegistryKey>fmt/154</premis:formatRegistryKey>
          <premis:formatRegistryRole authority="http://id.loc.gov/vocabulary/preservation/formatRegistryRole" valueURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole/spe">specification</premis:formatRegistryRole>
        </premis:formatRegistry>
        <premis:formatNote></premis:formatNote>
      </premis:format>
    </premis:objectCharacteristics>

    <premis:originalName>cf9j41p15z_Kolom1_deelopname1_tiff.tiff</premis:originalName>

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
