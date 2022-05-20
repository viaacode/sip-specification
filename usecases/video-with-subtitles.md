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

A full sample SIP can be found [here](#sample).

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

| Intellectual Entity | the news episode on May 16th, 2022  |
| Representation | the archive master |
| File | the files `broadcaster_news_20220516.srt` and `broadcaster_news_20220516.mp4` |

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
    |   |   └── descriptive.xml
    |   └── preservation
    |       └── preservation.xml
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
                 └── preservation.xml
```

## The metadata

In total, the SIP contains 3 metadata files:
 
| `/data/metadata/descriptive/descriptive.xml` | Descriptive metadata about the IE residing on _Package level_. |
| `/data/metadata/preservation/preservation.xml` | Preservation metadata about the IE residing on _Package level_. |
| `/data/representations/representation_1/metadata/preservation/preservation.xml` | Preservation metadata about the representation and files residing on _Representation level_. |


### `/data/metadata/descriptive/descriptive.xml`

```xml
<?xml version='1.0' encoding='UTF-8'?>
<premis:premis xmlns:dcterms="http://purl.org/dc/terms/" xmlns:premis="http://www.loc.gov/premis/v3" xmlns:xs="http://www.w3.org/2001/XMLSchema/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance/">
  <premis:object>
      <premis:objectIdentifier>
         <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
         <premis:objectIdentifierValue>uuid-b21a86aa-97a3-4f7b-a9f5-4d330af641c0</premis:objectIdentifierValue>
      </premis:objectIdentifier>

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
  </premis:object>
</premis:premis>  
```

### `/data/metadata/preservation/preservation.xml`

```xml
<?xml version='1.0' encoding='UTF-8'?>
<premis:premis xmlns:dcterms="http://purl.org/dc/terms/" xmlns:premis="http://www.loc.gov/premis/v3" xmlns:xs="http://www.w3.org/2001/XMLSchema/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance/">

   <premis:object>
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


### `/data/representations/representation_1/metadata/preservation/preservation.xml`

```xml
<?xml version='1.0' encoding='UTF-8'?>
<premis:premis xmlns:dcterms="http://purl.org/dc/terms/" xmlns:premis="http://www.loc.gov/premis/v3" xmlns:xs="http://www.w3.org/2001/XMLSchema/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance/">
   <premis:object>
      <premis:originalName>the original filename</premis:originalName>
      <premis:objectCharacteristics>
         <premis:fixity>
            <premis:messageDigestAlgorithm authority="cryptographicHashFunctions" authorityURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions" valueURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5">MD5</premis:messageDigestAlgorithm>
            <premis:messageDigest>the md5 checksum of the essence</premis:messageDigest>
         </premis:fixity>
      </premis:objectCharacteristics>
   </premis:object>
</premis:premis>
```
