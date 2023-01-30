---
layout:       default
title:        Video file with subtitles
parent:       Use cases
grand_parent:  1.1
nav_order:    2
nav_exclude:  false
has_children: false
sip_profile:  Basic
---
Editor's Draft
{: .label .label-yellow }
# Use Case: a video file with subtitles

The following use case describes how to package

- a video file;
- a subtitle file; and
- some basic descriptive metadata.

It uses the [**Basic SIP profile**]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/profiles/basic.md %}).

A full sample SIP can be downloaded [here]({{ site.baseurl }}{% link assets/sip_samples/subtitles_d3e1a978-3dd8-4b46-9314-d9189a1c94c6.zip %}).

## The content

The following content is provided for packaging:

| `broadcaster_news_20220516.mp4` | The essence: a video file in the MPEG4 media format containing a recording of a news episode on May 16th, 2022.  |
| `broadcaster_news_20220516.srt` | The collateral: a file containing subtitles in the [SubRip subtitle file format](https://www.matroska.org/technical/subtitles.html#srt-subtitles). |
| `metadata.xml` | A metadata record describing the contents of the media file. |

The metadata record can contain the following information:

- the title of the episode;
- the publisher of the episode;
- the description of the episode;
- a custom identifier by the CP;
- a list of keywords;
- the original filename;
- a list of meemoo licenses;
- the date the episode was created;
- the date the episode was aired;
- the md5 checksum of the media file.

Please note that one should use the future broadcaster profile (currently still in development) if one wants to include more detailed information such as the series the episode is part of, the audio transcript of the episode etc.

## Applying the core concepts

Since the metadata record only deals with the news episode, we can appoint it as the sole Intellectual Entity present in the SIP.
Only one version of the recording was supplied, hence there is only one representation of the episode, which in turn contains the `broadcaster_news_20220516.mp4` file. 
Because `broadcaster_news_20220516.srt` depends on `broadcaster_news_20220516.mp4` and has little meaning without it, it is not considered as a seperate representation, but included in the same representation.

| _Intellectual Entity_ | the news episode on May 16th, 2022  |
| _Representation_ | the archive master |
| _File_ | the files `broadcaster_news_20220516.mp4` and `broadcaster_news_20220516.srt` |

This case uses the Basic profile because:

- there is only one IE and one Representation;
- the metadata is limited and can thus be mapped entirely to the DCTERMS and PREMIS vocabularies.

## Directory structure

We package the above in a meemoo SIP named `subtitles_d3e1a978-3dd8-4b46-9314-d9189a1c94c6.zip`.
It has the following directory structure:

```plaintext
subtitles_d3e1a978-3dd8-4b46-9314-d9189a1c94c6.zip
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
           |  |── broadcaster_news_20220516.srt
           |  └── broadcaster_news_20220516.mp4
           │
           └──metadata
              └──preservation
                 └── premis.xml
```

## The metadata

In total, the SIP contains 3 metadata files:

| `/data/metadata/descriptive/dc.xml` | Descriptive metadata about the IE residing at the _Package level_. |
| `/data/metadata/preservation/premis.xml` | Preservation metadata about the IE residing at the _Package level_. |
| `/data/representations/representation_1/metadata/preservation/premis.xml` | Preservation metadata about the representation and files residing at the _Representation level_. |

### /data/metadata/descriptive/dc.xml

The `dc.xml` of the package level describes the IE using the DCTERMS metadata schema.
It contains minimal metadata such as a title, an identifier, a creation and an issued datetime...

Note that the identifier is used to link the `dc.xml` file to the corresponding PREMIS object in the `preservation/premis.xml` file of the package level (see [here]({{ site.baseurl }}{% link docs/diginstroom/sip/1.1/sip_structure/5_structure_package.md %}#shareduuidinfo)).

```xml
<?xml version='1.0' encoding='UTF-8'?>
<metadata xmlns:dcterms="http://purl.org/dc/terms/" xmlns:schema="https://schema.org/" xmlns:xs="http://www.w3.org/2001/XMLSchema/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">

  <dcterms:title>the title of the episode</dcterms:title>

  <dcterms:description>the description of the episode</dcterms:description>

  <!-- linking id between dc and premis -->
  <!-- matches the identifier of the premis:object defined in the preservation/premis.xml -->
  <dcterms:identifier>uuid-f58ece94-f050-4b5b-b383-bba83393eaff</dcterms:identifier>

  <dcterms:created xsi:type="edtf">the date the episode was created</dcterms:created>
  <dcterms:issued xsi:type="edtf">the date the episode was aired</dcterms:issued>

  <dcterms:license>VIAA-PUBLIEK-METADATA-LTD</dcterms:license>
  <dcterms:publisher>the publisher of the episode</dcterms:publisher>
  <dcterms:rightsHolder>the rights owner</dcterms:rightsHolder>

  <dcterms:subject>Keyword 1</dcterms:subject>
  <dcterms:subject>Keyword 2</dcterms:subject>

</metadata> 
```

### /data/metadata/preservation/premis.xml

The `premis.xml` of the package level describes the IE and its relationship with its representation.
It also contains an example of an additional identifier added by the CP.

Note that the identifier in the `<premis:objectIdentifier>` element is shared with the `<dcterms:identifier>` in the `descriptive/dc.xml` file in order to link the two files together.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

  <premis:object xsi:type="premis:intellectualEntity">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-f58ece94-f050-4b5b-b383-bba83393eaff</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:objectIdentifier>
      <premis:objectIdentifierType>LOCAL_ID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>a custom identifier provided by the CP</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isr">is represented by</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-c84a4912-f10d-46a5-b513-e4c4e2eefb43</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>

</premis:premis>
```

### /data/representations/representation_1/metadata/preservation/premis.xml

The `premis.xml` at the _representation level_ describes three PREMIS objects:

1. the representation;
2. the media file;
3. the subtitle file.

It also describes the various relationships between these objects:

1. the relation between the representation and the IE at the package level;
2. the relations between the representation, the media file and the subtitles file;
3. the relations between the media file and the subtitles file.

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

  <premis:object xsi:type="premis:representation">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-c84a4912-f10d-46a5-b513-e4c4e2eefb43</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship between representation and its files -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/inc">includes</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-e84e46b4-faaf-478d-a238-31b7be5b7e98</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-b3d4b82b-563d-4c14-8e12-23c8da858dd0</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship between representation and its IE -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/rep">represents</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-f58ece94-f050-4b5b-b383-bba83393eaff</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>
  </premis:object>

  <premis:object xsi:type="premis:file">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-e84e46b4-faaf-478d-a238-31b7be5b7e98</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:objectCharacteristics>
      <premis:fixity>
        <premis:messageDigestAlgorithm authority="cryptographicHashFunctions" authorityURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions" valueURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5">
                MD5
        </premis:messageDigestAlgorithm>
        <premis:messageDigest>22502b5dc38e893d99e9368c6ff70229</premis:messageDigest>
      </premis:fixity>
      <premis:size>5</premis:size>
      <premis:format>
        <premis:formatRegistry>
          <premis:formatRegistryName>PRONOM</premis:formatRegistryName>
          <premis:formatRegistryKey>fmt-199</premis:formatRegistryKey>
          <premis:formatRegistryRole authority="http://id.loc.gov/vocabulary/preservation/formatRegistryRole" valueURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole/spe">specification</premis:formatRegistryRole>
        </premis:formatRegistry>
      </premis:format>
    </premis:objectCharacteristics>

    <premis:originalName>broadcaster_news_20220525.mp4</premis:originalName>

    <!-- relationship between file and its representation -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isi">is included in</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-c84a4912-f10d-46a5-b513-e4c4e2eefb43</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship between the video file and the subtitles file -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/dep">dependency</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/irq">is required by</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-b3d4b82b-563d-4c14-8e12-23c8da858dd0</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>

  <premis:object xsi:type="premis:file">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-b3d4b82b-563d-4c14-8e12-23c8da858dd0</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:objectCharacteristics>
      <premis:fixity>
        <premis:messageDigestAlgorithm authority="cryptographicHashFunctions" authorityURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions" valueURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5">
                MD5
        </premis:messageDigestAlgorithm>
        <premis:messageDigest>daefffb93e6c3be7136ba40edae4f2f1</premis:messageDigest>
      </premis:fixity>
      <premis:size>3</premis:size>
      <premis:format>
        <premis:formatRegistry>
          <premis:formatRegistryName>PRONOM</premis:formatRegistryName>
          <premis:formatRegistryKey>fmt-1218</premis:formatRegistryKey>
          <premis:formatRegistryRole authority="http://id.loc.gov/vocabulary/preservation/formatRegistryRole" valueURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole/spe">specification</premis:formatRegistryRole>
        </premis:formatRegistry>
      </premis:format>
    </premis:objectCharacteristics>

    <premis:originalName>broadcaster_news_20220525.srt</premis:originalName>

    <!-- relationship between file and its representation -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isi">is included in</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-c84a4912-f10d-46a5-b513-e4c4e2eefb43</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship between the subtitles file and the video file -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/dep">dependency</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/req">requires</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-e84e46b4-faaf-478d-a238-31b7be5b7e98</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>

</premis:premis>
```
