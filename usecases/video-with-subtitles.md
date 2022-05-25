---
layout:       default
title:        Video file with subtitles
parent:       Use cases
nav_order:    2
nav_exclude:  false
has_children: false
sip_profile:  basic
---
Status: WIP
{: .label .label-yellow }
# Use Case: a video file with subtitles

The following use case describes how to package
- a video file;
- a subtitle file; and
- some basic descriptive metadata.

It uses the [**Basic SIP profile**]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/profiles/basic.md %}).

A full sample SIP can be downloaded [here]({{ site.baseurl }}{% link assets/sip_samples/d3e1a978-3dd8-4b46-9314-d9189a1c94c6.zip %}).

## The content

The following content is provided for packaging:

| `broadcaster_news_20220516.mp4` | The essence: a video file in the MPEG4 media format containing a recording of a news episode on May 16th, 2022  |
| `broadcaster_news_20220516.srt` | The collateral: a file containing subtitles in the [SubRip subtitle file format](https://www.matroska.org/technical/subtitles.html#srt-subtitles) |
| `metadata.xml` | A metadata record describing the contents of the essence. |

The metadata record contains the following information:

- the title of the episode
- the publisher of the episode 
- the description of the episode 
- a custom identifier by the CP
- a list of keywords  
- the series the episode is part of
- the original filename
- a list of meemoo licenses 
- the audio transcript of the episode 
- the date the episode was aired 
- the rights owner 
- the md5 checksum of the essence

## Applying the core concepts

Since the metadata record is only about one thing: the news episode, we can apoint it as the sole Intellectual Entity present. 
Only one version of the recording was supplied, hence there is only one representation of the episode containing the `broadcaster_news_20220516.mp4` file. 
Because `broadcaster_news_20220516.srt` depends on `broadcaster_news_20220516.mp4` and has little meaning without it,
it is not considered a seperate representation, but included in same representation.

| _Intellectual Entity_ | the news episode on May 16th, 2022  |
| _Representation_ | the archive master |
| _File_ | the files `broadcaster_news_20220516.srt` and `broadcaster_news_20220516.mp4` |

This case uses in the Basic profile because:
- there is only one IE and one Representation;
- the metadata can be mapped entirely to the Dublin Core and PREMIS vocabularies.

## Directory structure

We package the above in a meemoo SIP named `broadcaster_news_20220516_sip.zip`.
It has the following directory structure:

```plaintext
broadcaster_news_20220516_sip.zip
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
 
| `/data/metadata/descriptive/dc.xml` | Descriptive metadata about the IE residing on _Package level_. |
| `/data/metadata/preservation/premis.xml` | Preservation metadata about the IE residing on _Package level_. |
| `/data/representations/representation_1/metadata/preservation/premis.xml` | Preservation metadata about the representation and files residing on _Representation level_. |


### /data/metadata/descriptive/dc.xml

```xml
<?xml version='1.0' encoding='UTF-8'?>
<metadata xmlns:dcterms="http://purl.org/dc/terms/" 
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance/"
          xmlns:schema="https://schema.org/">
   <!-- matches te identifier of the premis:object defined in the preservation/premis.xml -->
   <dcterms:identifier>uuid-b21a86aa-97a3-4f7b-a9f5-4d330af641c0</dcterms:identifier>

   <dcterms:title>the title of the episode</dcterms:title>
   <dcterms:publisher>the title of the episode</dcterms:publisher>
   <dcterms:description>the description of the episode</dcterms:description>
   <dcterms:created xsi:type="edtf:EDTF">the date the episode was aired</dcterms:created>
   <dcterms:issued xsi:type="edtf:EDTF">XXXX</dcterms:issued>
   <!-- list of keywords -->
   <dcterms:subject>Keyword 1</dcterms:subject>
   <dcterms:subject>Keyword 2</dcterms:subject>
   <!-- VIAA licenses -->
   <dcterms:license>VIAA-PUBLIEK-METADATA-LTD<dcterms:license>
   <dcterms:rightsHolder schema:roleName="auteursrechthouder">the rights owner</dcterms:rightsHolder>
   <!-- This is not part of basic profile? -->
   <schema:transcript>
      the audio transcript of the episode
   </schema:transcript>
</metadata>  
```

### /data/metadata/preservation/premis.xml

```xml
<?xml version='1.0' encoding='UTF-8'?>
<premis:premis xmlns:premis="http://www.loc.gov/premis/v3">
   <premis:object>
      <premis:objectCategory>intellectual entity</premis:objectCategory>
      <premis:objectIdentifier>
         <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
         <premis:objectIdentifierValue>uuid-b21a86aa-97a3-4f7b-a9f5-4d330af641c0</premis:objectIdentifierValue>
      </premis:objectIdentifier>
      <premis:objectIdentifier>
         <premis:objectIdentifierType>local_id</premis:objectIdentifierType>
         <premis:objectIdentifierValue>a custom identifier by the CP</premis:objectIdentifierValue>
      </premis:objectIdentifier>
   </premis:object>
</premis:premis>
```


### /data/representations/representation_1/metadata/preservation/premis.xml

The `premis.xml` on _package level_ describes three PREMIS objects:
1. the representation
2. the media file
3. the subtitle file


```xml
<?xml version='1.0' encoding='UTF-8'?>
<premis:premis xmlns:premis="http://www.loc.gov/premis/v3">
   <!-- Representation -->
   <premis:object>
      <premis:objectCategory>representation</premis:objectCategory>
      <premis:objectIdentifier>
         <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
         <premis:objectIdentifierValue>
            uuid-541292c3-223a-4b80-b747-66bc86ff4a89
         </premis:objectIdentifierValue>
      </premis:objectIdentifier>
      ...
   </premis:object>

   <!-- Media file: broadcaster_news_20220516.mp4 -->
   <premis:object>
      <premis:objectCategory>file</premis:objectCategory>
         <premis:objectIdentifier>
            <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
         <premis:objectIdentifierValue>
            uuid-bd610fa4-077c-40cc-a278-74220df0a0c1
         </premis:objectIdentifierValue>
      </premis:objectIdentifier>
      ...
   </premis:object>

   <!-- Subtitles: broadcaster_news_20220516.srt -->
   <premis:object>
      <premis:objectCategory>file</premis:objectCategory>
      <premis:objectIdentifier>
         <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
         <premis:objectIdentifierValue>
               uuid-950ea040-5e79-4223-b804-b76660ec7e85
         </premis:objectIdentifierValue>
      </premis:objectIdentifier>
      ...
   </premis:object>
</premis:premis>
```

#### 1. Representation

```xml
<premis:object>
   <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-541292c3-223a-4b80-b747-66bc86ff4a89</premis:objectIdentifierValue>
   </premis:objectIdentifier>

   <!-- relationship between representation and its files -->
   <premis:relationship>
      <premis:relationshipType authority="relationshipType" 
                                 authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" 
                                 valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">
         structural
      </premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" 
                                 authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" 
                                 valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/inc">
         includes
      </premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
            <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
            <premis:relatedObjectIdentifierValue>uuid-bd610fa4-077c-40cc-a278-74220df0a0c1</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
      <premis:relatedObjectIdentifier>
            <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
            <premis:relatedObjectIdentifierValue>uuid-950ea040-5e79-4223-b804-b76660ec7e85</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
   </premis:relationship>

   <!-- relationship between representation and its IE-->
   <premis:relationship>
      <premis:relationshipType authority="relationshipType" 
                                 authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" 
                                 valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">
      structural
      </premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" 
                                    authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" 
                                    valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/rep">
      represents
      </premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
            <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
            <premis:relatedObjectIdentifierValue>uuid-b21a86aa-97a3-4f7b-a9f5-4d330af641c0</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
   </premis:relationship>
</premis:object>
```
#### 2. Media file (`/data/representations/representation_1/data/broadcaster_news_20220516.mp4`)

```xml
<premis:object>
   <premis:objectCategory>file</premis:objectCategory>
   <premis:originalName>broadcaster_news_20220516.mp4</premis:originalName>
   <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-bd610fa4-077c-40cc-a278-74220df0a0c1</premis:objectIdentifierValue>
   </premis:objectIdentifier>

   <premis:objectCharacteristics>
      <premis:fixity>
            <premis:messageDigestAlgorithm authority="cryptographicHashFunctions" 
                                          authorityURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions" 
                                          valueURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5">
               MD5
            </premis:messageDigestAlgorithm>
            <premis:messageDigest>b7ae37f6094794e313402b9d064978e8</premis:messageDigest>
      </premis:fixity>
   </premis:objectCharacteristics>
</premis:object>
```

#### 3. Subtitle file (`/data/representations/representation_1/data/broadcaster_news_20220516.srt`)

```xml
<premis:object>
   <premis:objectCategory>file</premis:objectCategory>
   <premis:originalName>broadcaster_news_20220516.srt</premis:originalName>
   <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>
            uuid-950ea040-5e79-4223-b804-b76660ec7e85
      </premis:objectIdentifierValue>
   </premis:objectIdentifier>
   <premis:objectCharacteristics>
      <premis:fixity>
            <premis:messageDigestAlgorithm authority="cryptographicHashFunctions" 
                                          authorityURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions" 
                                          valueURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5">
            MD5
   </premis:messageDigestAlgorithm>
            <premis:messageDigest>d4985ba4b67ff067a0e84c53b6d35355</premis:messageDigest>
      </premis:fixity>
   </premis:objectCharacteristics>
   <!-- dependency relationship between the subtitle and the media file-->
   <premis:relationship>
      <premis:relationshipType authority="relationshipType" 
                                 authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" 
                                 valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/dep">
            dependency
      </premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" 
                                    authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" 
                                    valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/req">
               requires</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
            <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
            <premis:relatedObjectIdentifierValue>
               uuid-bd610fa4-077c-40cc-a278-74220df0a0c1
            </premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
   </premis:relationship>
</premis:object>
```
