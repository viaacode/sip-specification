---
layout:       default
title:        Single file
parent:       Use cases
nav_order:    1
nav_exclude:  false
has_children: false
sip_profile: basic
---
Status: WIP
{: .label .label-yellow }
# Use Case: a single image

The following use case describes how to package a single image file with some basic descriptive metadata.
It illustrates the most minimal implementation that conforms to meemoo's SIP specification and the [**Basic content profile**]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/profiles/basic.md %}).

A full sample SIP can be downloaded [here]({{ site.baseurl }}{% link assets/sip_samples/deec5d89-3024-4cbd-afcd-e18af4ad33ec.zip %}).

## The content

The following content is provided for packaging:

| `D523F963.jpg` | The media file: an image in the JPEG media format containing a photo taken in January 2022 depicting a cat lying on a sofa. |
| `metadata.xml` | A metadata record describing the contents of the essence. |

The metadata record contains the following information:

- the title of the photo
- three keywords

## Applying the core concepts

Since the metadata record is only about one thing (i.e. the photograph), we can appoint it as the sole Intellectual Entity present.
Only one version of the image was supplied (i.e. the media file in the JPEG media format), hence there is only one representation.
This representation contains the `D523F963.jpg` file.

| _Intellectual Entity_ | photograph taken in January 2022 depicting a cat  |
| _Representation_ | the archive master |
| _File_ | the media file `D523F963.jpg` |

This case uses the Basic content profile because:

- there is only one IE and one Representation;
- the metadata can be mapped entirely to the Dublin Core and PREMIS metadata vocabularies.

## Directory structure

We package the above in a meemoo SIP named `deec5d89-3024-4cbd-afcd-e18af4ad33ec.zip`.
It has the following directory structure:

```plaintext
deec5d89-3024-4cbd-afcd-e18af4ad33ec.zip
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
           |  └── D523F963.jpg
           │
           └──metadata
              └──preservation
                 └── premis.xml
```

## The metadata

In total, the SIP contains 3 metadata files:

| `/data/metadata/descriptive/dc.xml` | Descriptive metadata about the IE residing on _Package level_. |
| `/data/metadata/preservation/premis.xml` | Preservation metadata about the IE residing on _Package level_. |
| `/data/representations/representation_1/metadata/preservation/premis.xml` | Preservation metadata about the representation and files residing on _Representation level_. |

### /data/metadata/descriptive/dc.xml

The `dc.xml` of the package level describes the IE using the DCTERMS metadata schema.
It contains minimal metadata such as a title, an identifier, a creation datetime (set to unknown) and a number of keywords.

Note that the identifier is used to link the `dc.xml` file to the corresponding PREMIS object in the `preservation/premis.xml` file of the package level (see [here]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/sip_structure/5_structure_package.md %}#shareduuidinfo)).

```xml
<?xml version='1.0' encoding='UTF-8'?>
<metadata xmlns:dcterms="http://purl.org/dc/terms/" xmlns:xs="http://www.w3.org/2001/XMLSchema/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance/">

  <!-- general title for the resource -->
  <dcterms:title>Felis Catus Flamens sitting on a cat tree</dcterms:title>

  <!-- linking id between dc and premis -->
  <dcterms:identifier>uuid-a0a5329c-4ad1-4607-9f6e-ce980d90b992</dcterms:identifier>

  <!-- date unknown -->
  <dcterms:created xsi:type="edtf">XXXX</dcterms:created>

  <!-- multiple keywords about the resource -->
  <dcterms:subject>Cat</dcterms:subject>
  <dcterms:subject>Felis Catus Flamens</dcterms:subject>
  <dcterms:subject>Cat tree</dcterms:subject>

</metadata>  
```

### /data/metadata/preservation/premis.xml

The `premis.xml` of the package level describes the IE and its relationship with its representation.

Note that the identifier in the `<premis:objectIdentifier>` element is shared with the `<dcterms:identifier>` in the `descriptive/dc.xml` file in order to link the two files together.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3">

  <!-- IE about the Felis Catus Flamens -->
  <premis:object>
    <premis:objectCategory>intellectual entity</premis:objectCategory>

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-a0a5329c-4ad1-4607-9f6e-ce980d90b992</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isr">is represented by</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-4e475706-2752-4f77-9069-1f71c0e22572</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>

</premis:premis>
```

### /data/representations/representation_1/metadata/preservation/premis.xml

The `premis.xml` of the representation level describes two PREMIS objects:

1. the representation
2. the media file `D523F963.jpg`

It also describes the various relationships between these objects:

1. the relation between the representation and the IE at the package level;
2. the relations between the representation and the media file;

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3">

  <!-- Representation: archive master -->
  <premis:object>
    <premis:objectCategory>representation</premis:objectCategory>

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
        <premis:relatedObjectIdentifierValue>uuid-945a16cd-eeb6-4a4c-95bb-4656a9f0909d</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship between representation and its IE/subIE -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/rep">represents</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-a0a5329c-4ad1-4607-9f6e-ce980d90b992</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>
  </premis:object>

  <!-- Image file: D523F963.jpg -->
  <premis:object>
    <premis:objectCategory>file</premis:objectCategory>

    <premis:originalName>D523F963.jpg</premis:originalName>

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-945a16cd-eeb6-4a4c-95bb-4656a9f0909d</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:objectCharacteristics>
      <premis:fixity>
        <premis:messageDigestAlgorithm authority="cryptographicHashFunctions" authorityURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions" valueURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5">
                MD5
        </premis:messageDigestAlgorithm>
        <premis:messageDigest>18513a8d61c6f2cbaaeeedd754b01d6b</premis:messageDigest>
      </premis:fixity>
    </premis:objectCharacteristics>

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

</premis:premis>
```

<small>
Continue to [Video file with subtitles]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/usecases/video-with-subtitles.md %}).
</small>