---
layout:       default
title:        Scan of a three-dimensional artwork
parent:       Use cases
grand_parent:  SIP Specification 1.1
nav_order:    7
nav_exclude:  false
has_children: false
sip_profile:  Material artwork
---
Editor's Draft
{: .label .label-yellow }
# Use Case: a digitization of a three-dimensional artwork

The following use case describes how to package a reproduction of a three-dimensional artwork such as a statue or sculpture. 
The reproduction contains multiple flavours of a 3D scan: high-poly, low-poly, container format and a scanner calibration result.
It includes:

- STL files;
- OBJ files;
- MTL files;
- TIFF files;
- BMP files;
- basic descriptive metadata;
- basic preservation metadata.

It uses the [**material-artwork SIP profile**]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/profiles/material-artwork.md %}).

A full sample SIP can be viewed [here]({{ site.baseurl }}{% link assets/sip_samples/3d4bd7ca-38c6-11ed-95f2-7e92631d7d28.zip %}).

## The content

The following content is provided for packaging:

| `qv3bz95m19_ARCH_STL.STL` | A binary 3D model of the sculpture 'The Roman She-Wolf with Romulus and Remus' targeted at 3D printing.  |
| `qv3bz95m19_ARCH_OBJ.OBJ` | A high-resolution polygon file containing a scan of the sculpture 'The Roman She-Wolf with Romulus and Remus'. |
| `qv3bz95m19_ARCH_MTL.MTL` | A companion file for the high-resolution OBJ file.  |
| `qv3bz95m19_ARCH_TIFF_COLOR.TIFF` | The texture map in TIFF format for the high-resolution OBJ file. |
| `qv3bz95m19_VER_OBJ.OBJ` | A low-resolution polygon file containing a scan of the sculpture 'The Roman She-Wolf with Romulus and Remus'. |
| `qv3bz95m19_VER_MTL.MTL` | A companion file for the low-resolution OBJ file |
| `qv3bz95m19_VER_COLOR_BMP.BMP` | The texture map in Windows Bitmap for the high-resolution OBJ file. |
| `qv3bz95m19_REF_OBJ.OBJ` | A polygon file of scanner calibration object. |
| `qv3bz95m19_REF_MTL.MTL` | A companion file for the OBJ file of scanner calibration object. |
| `qv3bz95m19_REF_BMP.BMP` | The texture map in Windows Bitmap for the calibration OBJ file.  |
| `qv3bz95m19_REF_IJK_BMP.BMP` | An additional texture map in Windows Bitmap of scanner calibration object combined with the sculpture 'The Roman She-Wolf with Romulus and Remus'. |
| `qv3bz95m19_FOTO1_TIFF.TIFF`, ..., `qv3bz95m19_FOTO3_TIFF.TIFF` | Additional photography of the sculpture 'The Roman She-Wolf with Romulus and Remus'. |
| `metadata.xml` | A metadata record describing the sculpture 'The Roman She-Wolf with Romulus and Remus'. |

The metadata record can contain the following information:

- the title of the sculpture;
- a description of the sculpture;
- the date the sculpture was created;
- the dimensions of the sculpture;
- the name, birthdate and deathdate of the author;
- a list of meemoo licenses;
- some keywords
- the md5 checksums of the media files;
- rights credits
- ...

Some of the metadata above is supplied in English and Dutch.

## Applying the core concepts

Since the metadata only describes a single artwork, we can consider it as the single Intellectual Entity in the SIP.

We can distinguish a couple of file sets that represent the sculpture in some manner: an model for 3D printing, a high-polygon scan, a low-polygon scan, a scanner calibration target recording, and some additional photos..

Since each set of files can have a meaning on its own, they are split into separate representations. This results in the following application of the [core concepts]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/3_core-concepts.md %}):

|_Intellectual Entity_| the sculpture 'The Roman She-Wolf with Romulus and Remus' |
|_Representation 1_| the model of the sculpture for 3D printing |
|_Representation 2_| the archive master: a high-polygon representation of the sculpture |
|_Representation 3_| the access copy: a low-polygon representation of the sculpture |
|_Representation 4_| the scanner calibration result |
|_Representation 5_| an additional photographic representation |
|_Files (rep. 1)_| the STL file: `qv3bz95m19_ARCH_STL.STL` |
|_Files (rep. 2)_| the files: `qv3bz95m19_ARCH_OBJ.OBJ`, `qv3bz95m19_ARCH_MTL.MTL`, `qv3bz95m19_ARCH_TIFF_COLOR.TIFF` |
|_Files (rep. 3)_| the files: `qv3bz95m19_VER_OBJ.OBJ`, `qv3bz95m19_VER_MTL.MTL`, `qv3bz95m19_VER_COLOR_BMP.BMP` |
|_Files (rep. 4)_| the files:  `qv3bz95m19_REF_OBJ.OBJ`, `qv3bz95m19_REF_MTL.MTL`, `qv3bz95m19_REF_BMP.BMP`, `qv3bz95m19_REF_IJK_BMP.BMP` |
|_Files (rep. 5)_| the TIFF files: `qv3bz95m19_FOTO1_TIFF.TIFF`, `qv3bz95m19_FOTO2_TIFF.TIFF`, `qv3bz95m19_FOTO3_TIFF.TIFF`|

This case relies on the material-artwork profile because:

- there is one IE and multiple representations containing one or more files;
- the sculpture can be described using a combination of DCTERMS and a Schema.org;

## Directory structure

We package the above in a meemoo SIP named `3d4bd7ca-38c6-11ed-95f2-7e92631d7d28.zip`.
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
        |── representation_1       # high-poly capture for print
        |   │── mets.xml
        |   └── data  
        |   │   └── qv3bz95m19_ARCH_STL.STL              
        |   │
        |   └── metadata
        |       |── descriptive  
        |       |   └── dc+schema.xml
        |       └── preservation
        |           └── premis.xml
        |── representation_2       # high-poly capture
        |   │── mets.xml
        |   |── data
        |   |   |── qv3bz95m19_ARCH_OBJ.OBJ       # polygon file    
        |   |   |── qv3bz95m19_ARCH_TIFF_COLOR.TIFF      # texture image       
        |   │   └── qv3bz95m19_ARCH_MTL.MTL              # texture mapping file
        |   │
        |   └── metadata
        |       |── descriptive   
        |       |   └── dc+schema.xml
        |       └── preservation
        |           └── premis.xml
        └──representation_3       # low-poly capture
        |   │── mets.xml
        |   |── data
        |   |   |── qv3bz95m19_VER_OBJ.OBJ       # polygon file    
        |   |   |── qv3bz95m19_VER_COLOR_BMP.BMP             # texture image       
        |   │   └── qv3bz95m19_VER_MTL.MTL                   # texture mapping file
        |   │
        |   └── metadata
        |       |── descriptive   
        |       |   └── dc+schema.xml    
        |       └──preservation
        |          └── premis.xml
        └── representation_4       # quality assessment reference
        |    │── mets.xml
        |    |──data
        |    |  |── qv3bz95m19_REF_OBJ.OBJ               # polygon file    
        |    |  |── qv3bz95m19_REF_BMP.BMP               # texture image      
        |    |  |── qv3bz95m19_REF_IJK_BMP.BMP           # UV image     
        |    │  └── qv3bz95m19_REF_MTL.MTL               # texture mapping file
        |    │
        |    └── metadata
        |       |── descriptive
        |       |   └── dc+schema.xml    
        |       └── preservation
        |           └── premis.xml
        └── representation_5       # additional photography
            │── mets.xml
            |── data
            |   |── qv3bz95m19_FOTO1_TIFF.TIFF
            |   |── qv3bz95m19_FOTO2_TIFF.TIFF                   
            │   └── qv3bz95m19_FOTO3_TIFF.TIFF               
            │
            └── metadata
                |── descriptive
                |   └── dc+schema.xml    
                └── preservation
                    └── premis.xml
```

## The metadata

In total, the SIP contains 12 metadata files:

|`data/metadata/descriptive/dc+schema.xml`| Descriptive metadata about the IE residing at the _package level_ using the DCTERMS metadata schema. |
|`data/metadata/preservation/premis.xml`| Preservation metadata about the IE residing at the _package level_, including any PREMIS events related to the SIP/package/representations. |
|`data/representations/representation_*/metadata/descriptive/dc+schema.xml`| Descriptive metadata about about each of the 5 representations at the _representation level_. |
|`data/representations/representation_*/metadata/preservation/premis.xml`| Preservation metadata about each of the 5 representations and 14 files residing at the _representation level_. |

### /data/metadata/descriptive/dc+schema.xml

The `dc+schema.xml` of the package level describes the IE using [the DCTERMS]((https://www.dublincore.org/specifications/dublin-core/dcmi-terms/)) and the [Schema](schema.org/) metadata models.
It contains minimal metadata such as a title, a description, an identifier, a date of creation and of issuance, and additional metadata such as the dimensions of the artwork, information about the artist, the art medium and the type of artwork.

The identifier is used to link the `dc+schema.xml` file to the corresponding PREMIS object in the `preservation/premis.xml` file of the package level (see [here]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/sip_structure/5_structure_package.md %}#shareduuidinfo) for more information).

```xml
<?xml version='1.0' encoding='UTF-8'?>
<metadata xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xs="http://www.w3.org/2001/XMLSchema/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance/" xmlns:edtf="http://id.loc.gov/datatypes/edtf/" xmlns:schema="">


  <!-- general title for the resource -->
  <dcterms:title xml:lang="nl">De Romeinse wolvin met Romulus en Remus</dcterms:title>
  <dcterms:title xml:lang="en">The Roman She-Wolf with Romulus and Remus</dcterms:title>

  <!-- general description for the resource -->
  <dcterms:description xml:lang="nl">onderdeel van de Van Herck collectie terracottabeelden</dcterms:description>
  <dcterms:description xml:lang="en">part of the Van Herck collection of terracotta sculptures.</dcterms:description>

  <!-- linking id between dc and premis -->
  <dcterms:identifier>7m03z1634f</dcterms:identifier>

  <!-- creationdate -->
  <dcterms:created xsi:type="edtf:EDTF-level1">1701/1800</dcterms:created>

  <dcterms:subject xml:lang="nl">topstukken</dcterms:subject>
  <dcterms:subject xml:lang="nl">collectie Van Herck</dcterms:subject>
  <dcterms:subject xml:lang="nl">terracotta</dcterms:subject>
  <dcterms:subject xml:lang="nl">3D</dcterms:subject>
  <dcterms:subject xml:lang="nl">scan</dcterms:subject>
  <dcterms:subject xml:lang="nl">beeldhouwwerk</dcterms:subject>

  <dcterms:subject xml:lang="en">collection Van Herck</dcterms:subject>
  <dcterms:subject xml:lang="en">terracotta</dcterms:subject>
  <dcterms:subject xml:lang="en">3D</dcterms:subject>
  <dcterms:subject xml:lang="en">scan</dcterms:subject>
  <dcterms:subject xml:lang="en">sculpture</dcterms:subject>

  <!-- rights note -->
  <dcterms:rights xml:lang="en">public domain</dcterms:rights>

  <!-- creator -->
  <schema:creator schema:roleName="auteur">
    <schema:name>Walter Pompe</schema:name>
    <schema:birthDate xsi:type="xsd:dateTime">1703</schema:birthDate>
    <schema:deathDate xsi:type="xsd:dateTime">1777</schema:deathDate>
  </schema:creator>

  <!-- dimensions -->
  <schema:height>
    <schema:value>116</schema:value>
    <schema:unitText>mm</schema:unitText>
    <schema:unitCode>MMT</schema:unitCode>
  </schema:height>
  <schema:width>
    <schema:value>220</schema:value>
    <schema:unitText>mm</schema:unitText>
    <schema:unitCode>MMT</schema:unitCode>
  </schema:width>
  <schema:depth>
    <schema:value>130</schema:value>
    <schema:unitText>mm</schema:unitText>
    <schema:unitCode>MMT</schema:unitCode>
  </schema:depth>
  <schema:weight>
    <schema:value>2,3</schema:value>
    <schema:unitText>kg</schema:unitText>
    <schema:unitCode>KGM</schema:unitCode>
  </schema:weight>
  <schema:artMedium xml:lang="nl">terracotta</schema:artMedium>
  <schema:artMedium xml:lang="en">terracotta</schema:artMedium>
  <schema:artform xml:lang="nl">beeldhouwwerk</schema:artform>
  <schema:artform xml:lang="en">sculpture</schema:artform>


</metadata>
```

### data/metadata/preservation/premis.xml

The `premis.xml` of the package level describes the IE and the relationships with its representations.
It also contains a digitization event that details how the differetn files were created and by who.

Note that the identifier in the `<premis:objectIdentifier>` element is shared with the `<dcterms:identifier/>` (in the `descriptive/dc+schema.xml` file) in order to link the PREMIS IE object to its descriptions in the two files.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:schema="http://schema.org/" xmlns:premis="http://www.loc.gov/premis/v3" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

    <!-- IE about the artwork -->
    <premis:object xsi:type="premis:intellectualEntity">
        <premis:objectIdentifier>
            <premis:objectIdentifierType>VIAA PID</premis:objectIdentifierType>
            <premis:objectIdentifierValue>qv3bz95m19</premis:objectIdentifierValue>
        </premis:objectIdentifier>

        <premis:objectIdentifier>
            <premis:objectIdentifierType>Topstuk_ID</premis:objectIdentifierType>
            <premis:objectIdentifierValue>213</premis:objectIdentifierValue>
        </premis:objectIdentifier>

        <premis:objectIdentifier>
            <premis:objectIdentifierType>Inventarisnummer</premis:objectIdentifierType>
            <premis:objectIdentifierValue>IB00.008</premis:objectIdentifierValue>
        </premis:objectIdentifier>

        <!-- relationship between nested IE and its representation -->
        <premis:relationship>
            <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
            <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isr">is represented by</premis:relationshipSubType>
            
            <premis:relatedObjectIdentifier>
                <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
                <premis:relatedObjectIdentifierValue>uuid-e3aff200-237b-11ed-8d32-7e92631d7d28</premis:relatedObjectIdentifierValue>
            </premis:relatedObjectIdentifier>            
            <premis:relatedObjectIdentifier>
                <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
                <premis:relatedObjectIdentifierValue>uuid-7f16cfda-21ff-11ed-a277-7e92631d7d27</premis:relatedObjectIdentifierValue>
            </premis:relatedObjectIdentifier>
            <premis:relatedObjectIdentifier>
                <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
                <premis:relatedObjectIdentifierValue>uuid-671f4eb6-21ff-11ed-9e92-7e92631d7d27</premis:relatedObjectIdentifierValue>
            </premis:relatedObjectIdentifier>
            <premis:relatedObjectIdentifier>
                <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
                <premis:relatedObjectIdentifierValue>uuid-5c430d70-21ff-11ed-baeb-7e92631d7d27</premis:relatedObjectIdentifierValue>
            </premis:relatedObjectIdentifier>
        </premis:relationship>

    </premis:object>

    <!-- Digitization event -->

    <premis:event>
        <premis:eventIdentifier>
            <premis:eventIdentifierType>UUID</premis:eventIdentifierType>
            <premis:eventIdentifierValue>uuid-7f16cfda-21ff-11ed-a277-7e92631d7d27</premis:eventIdentifierValue>
        </premis:eventIdentifier>
        <premis:eventType>digitization</premis:eventType>
        <premis:eventDateTime>2022-08-29T00:00:00Z</premis:eventDateTime>

        <premis:eventDetailInformation>
            <premis:eventDetail>GIVE</premis:eventDetail>
        </premis:eventDetailInformation>

        <premis:eventOutcomeInformation>
            <premis:eventOutcome>success</premis:eventOutcome>
        </premis:eventOutcomeInformation>

        <premis:linkingAgentIdentifier>
            <premis:linkingAgentIdentifierType>VIAA SP Agent ID</premis:linkingAgentIdentifierType>
            <premis:linkingAgentIdentifierValue>OR-x05xc4w</premis:linkingAgentIdentifierValue>
            <premis:linkingAgentRole valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedAgentRole/imp">implementer</premis:linkingAgentRole>
        </premis:linkingAgentIdentifier>
        
        <premis:linkingObjectIdentifier>
            <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
            <premis:linkingObjectIdentifierValue>uuid-e3aff200-237b-11ed-8d32-7e92631d7d28</premis:linkingObjectIdentifierValue>
            <premis:linkingObjectRole valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/out">outcome</premis:linkingObjectRole>
        </premis:linkingObjectIdentifier>
        <premis:linkingObjectIdentifier>
            <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
            <premis:linkingObjectIdentifierValue>uuid-7f16cfda-21ff-11ed-a277-7e92631d7d27</premis:linkingObjectIdentifierValue>
            <premis:linkingObjectRole valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/out">outcome</premis:linkingObjectRole>
        </premis:linkingObjectIdentifier>
        <premis:linkingObjectIdentifier>
            <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
            <premis:linkingObjectIdentifierValue>uuid-671f4eb6-21ff-11ed-9e92-7e92631d7d27</premis:linkingObjectIdentifierValue>
            <premis:linkingObjectRole valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/out">outcome</premis:linkingObjectRole>
        </premis:linkingObjectIdentifier>
        <premis:linkingObjectIdentifier>
            <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
            <premis:linkingObjectIdentifierValue>uuid-5c430d70-21ff-11ed-baeb-7e92631d7d27</premis:linkingObjectIdentifierValue>
            <premis:linkingObjectRole valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/out">outcome</premis:linkingObjectRole>
        </premis:linkingObjectIdentifier>
        <premis:linkingObjectIdentifier>
            <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
            <premis:linkingObjectIdentifierValue>uuid-0b6c68e2-3a7d-11ed-97b8-7e92631d7d28</premis:linkingObjectIdentifierValue>
            <premis:linkingObjectRole valueURI="http://id.loc.gov/vocabulary/preservation/eventRelatedObjectRole/out">outcome</premis:linkingObjectRole>
        </premis:linkingObjectIdentifier>
    </premis:event>

    <premis:agent>
        <premis:agentIdentifier>
            <premis:agentIdentifierType>VIAA SP Agent ID</premis:agentIdentifierType>
            <premis:agentIdentifierValue>OR-x05xc4w</premis:agentIdentifierValue>
        </premis:agentIdentifier>
        <premis:agentName>De Logi &amp; Hoorne - Erfgo3D</premis:agentName>
        <premis:agentType>organization</premis:agentType>
    </premis:agent>

</premis:premis>
```

### data/representations/representation_1/metadata/preservation/premis.xml

The `premis.xml` file of the first representation describes a couple of PREMIS objects:

1. the representation;
2. the STL file `qv3bz95m19_ARCH_STL.STL`;

It also describes the various relationships between these objects:

1. the relation between the representation and the IE at the package level;
2. the relations between the representation and the STL file;

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

  <premis:object xsi:type="premis:representation">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-e3aff200-237b-11ed-8d32-7e92631d7d28</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship between representation and its files -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/inc">includes</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-de990ee6-237b-11ed-a484-7e92631d7d28</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship between representation and its IE/subIE -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/rep">represents</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>VIAA PID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>qv3bz95m19</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>
  </premis:object>

  <premis:object xsi:type="premis:file">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-de990ee6-237b-11ed-a484-7e92631d7d28</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:objectCharacteristics>
      <premis:fixity>
        <premis:messageDigestAlgorithm authority="cryptographicHashFunctions" authorityURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions" valueURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5">
                MD5
        </premis:messageDigestAlgorithm>
        <premis:messageDigest>9b7dd51ee94d1cc666392f5fbb6d9ea2</premis:messageDigest>
      </premis:fixity>
      <premis:size>558891008</premis:size>
      <premis:format>
        <premis:formatRegistry>
          <premis:formatRegistryName>PRONOM</premis:formatRegistryName>
          <premis:formatRegistryKey>fmt/865</premis:formatRegistryKey>
          <premis:formatRegistryRole authority="http://id.loc.gov/vocabulary/preservation/formatRegistryRole" valueURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole/spe">specification</premis:formatRegistryRole>
        </premis:formatRegistry>
      </premis:format>
    </premis:objectCharacteristics>

    <premis:originalName>PID_ARCH_STL</premis:originalName>

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

### data/representations/representation_2/metadata/descriptive/dc+schema.xml

The `dc+schema.xml` of the representation level describes the Representation using [the DCTERMS metadata schema](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/).
It contains minimal metadata such as a title and some licenses.

The identifier is used to link the `dc+schema.xml` file to the corresponding PREMIS object in the `preservation/premis.xml` file in the representaion folder (see [here]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/sip_structure/6_structure_representation.md %}#shareduuidinfo) for more information).

```xml
<?xml version='1.0' encoding='UTF-8'?>
<metadata xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xs="http://www.w3.org/2001/XMLSchema/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance/" xmlns:edtf="http://id.loc.gov/datatypes/edtf/" xmlns:schema="https://schema.org/">

    <!-- linking id between dc and premis -->
    <dcterms:identifier>uuid-7f16cfda-21ff-11ed-a277-7e92631d7d27</dcterms:identifier>

    <dcterms:title>ARCHIVERINGSCOPIE OBJ</dcterms:title>

    <!-- licenses -->
    <dcterms:license>CCBY-NC-ND-CONTENT</dcterms:license>
    <dcterms:license>CP-website</dcterms:license>

</metadata>
```


### data/representations/representation_2/metadata/preservation/premis.xml

The `premis.xml` file of the second representation describes a couple of PREMIS objects:

1. the representation;
2. the files `qv3bz95m19_ARCH_OBJ.OBJ`, `qv3bz95m19_ARCH_MTL.MTL`, `qv3bz95m19_ARCH_TIFF_COLOR.TIFF`;

It also describes the various relationships between these objects:

1. the relation between the representation and the IE at the package level;
2. the relations between the representation and the OBJ, MTL and TIFF file;

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

  <premis:object xsi:type="premis:representation">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-7f16cfda-21ff-11ed-a277-7e92631d7d27</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship between representation and its files -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/inc">includes</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-6A07B2FE-3363-4B46-953E-59A30BE67F9B</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-ECEB4181-5052-43C2-A3AD-D44AE5FB4D16</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-254F143D-85A3-4DB8-BFA4-53000DEA04C7</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship between representation and its IE -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/rep">represents</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>VIAA PID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>qv3bz95m19</premis:relatedObjectIdentifierValue>
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
        <premis:messageDigest>9b7dd51ee94d1cc666392f5fbb6d9ea2</premis:messageDigest>
      </premis:fixity>
      <premis:size>558891008</premis:size>
      <premis:format>
        <premis:formatRegistry>
          <premis:formatRegistryName>PRONOM</premis:formatRegistryName>
          <premis:formatRegistryKey>fmt/1210</premis:formatRegistryKey>
          <premis:formatRegistryRole authority="http://id.loc.gov/vocabulary/preservation/formatRegistryRole" valueURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole/spe">specification</premis:formatRegistryRole>
        </premis:formatRegistry>
      </premis:format>
    </premis:objectCharacteristics>

    <premis:originalName>qv3bz95m19_ARCH_OBJ</premis:originalName>

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

  <premis:object xsi:type="premis:file">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-ECEB4181-5052-43C2-A3AD-D44AE5FB4D16</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:objectCharacteristics>
      <premis:fixity>
        <premis:messageDigestAlgorithm authority="cryptographicHashFunctions" authorityURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions" valueURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5">
                MD5
        </premis:messageDigestAlgorithm>
        <premis:messageDigest>9b7dd51ee94d1cc666392f5fbb6d9ea2</premis:messageDigest>
      </premis:fixity>
      <premis:size>558891008</premis:size>
      <premis:format>
        <premis:formatRegistry>
          <premis:formatRegistryName>PRONOM</premis:formatRegistryName>
          <premis:formatRegistryKey>fmt/1211</premis:formatRegistryKey>
          <premis:formatRegistryRole authority="http://id.loc.gov/vocabulary/preservation/formatRegistryRole" valueURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole/spe">specification</premis:formatRegistryRole>
        </premis:formatRegistry>
        <premis:formatNote></premis:formatNote>
      </premis:format>
    </premis:objectCharacteristics>

    <premis:originalName>qv3bz95m19_ARCH_MTL</premis:originalName>

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

  <premis:object xsi:type="premis:file">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-254F143D-85A3-4DB8-BFA4-53000DEA04C7</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:objectCharacteristics>
      <premis:fixity>
        <premis:messageDigestAlgorithm authority="cryptographicHashFunctions" authorityURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions" valueURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5">
                MD5
        </premis:messageDigestAlgorithm>
        <premis:messageDigest>9b7dd51ee94d1cc666392f5fbb6d9ea2</premis:messageDigest>
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

    <premis:originalName>qv3bz95m19_ARCH_TIFF_COLOR</premis:originalName>

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



The folders of representation 3 and 4 have a identical structure.


### data/representations/representation_5/metadata/preservation/premis.xml

The `premis.xml` file of the fourth representation describes 4 PREMIS objects (of which the first two are shown in the example below):

1. the representation;
2. the three TIFF files `qv3bz95m19_FOTO1_TIFF.TIFF`, `qv3bz95m19_FOTO2_TIFF.TIFF`, `qv3bz95m19_FOTO3_TIFF.TIFF`;

It also describes the various relationships between these objects:

1. the relation between the representation and the IE at the package level;
2. the relations between the representation and the TIFF files;

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

  <premis:object xsi:type="premis:representation">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-0b6c68e2-3a7d-11ed-97b8-7e92631d7d28</premis:objectIdentifierValue>
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
    </premis:relationship>

    <!-- relationship between representation and its IE/subIE -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/rep">represents</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>VIAA PID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>qv3bz95m19</premis:relatedObjectIdentifierValue>
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

    <premis:originalName>qv3bz95m19_FOTO1_TIFF</premis:originalName>

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
