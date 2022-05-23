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
It illustrates the most minimal implementation that conforms to meemoo's SIP specification and the [**Basic SIP profile**]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/profiles/basic.md %}).

A full sample SIP can be found [here](https://github.com/viaacode/documentation/tree/master/assets/sip_samples/cbee2999-1db5-4a69-9260-f216dee75623).

## The content

The following content is provided for packaging:

| `D523F963.jpg` | The essence: an image in the JPEG media format containing a photo taken in January 2022 depicting a cat lying on a sofa |
| `metadata.xml` | A metadata record describing the contents of the essence. |

The metadata record contains the following information:

- the title of the photo
- three keywords

## Applying the core concepts

Since the metadata record is only about one thing: the photo, we can apoint it as the sole Intellectual Entity present. 
Only one version of the image was supplied, hence there is only one representation of the episode containing the `D523F963.jpg` file. 

| _Intellectual Entity_ | photo taken in January 2022 depicting a cat  |
| _Representation_ | the archive master |
| _File_ | the file `D523F963.jpg` |

This case uses in the Basic profile because:
- there is only one IE and one Representation;
- the metadata can be mapped entirely to the Dublin Core and PREMIS vocabularies.

## Directory structure

We package the above in a meemoo SIP named `cbee2999-1db5-4a69-9260-f216dee75623.zip`.
It has the following directory structure:

```plaintext
cbee2999-1db5-4a69-9260-f216dee75623.zip
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

```xml
<?xml version='1.0' encoding='UTF-8'?>
<metadata xmlns:dcterms="http://purl.org/dc/terms/" 
          xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance/">
    <dcterms:identifier>uuid-541292c3-223a-4b80-b747-66bc86ff4a89</dcterms:identifier>
    
    <!-- general title for the representation -->
    <dcterms:title>Colour representation of the Felis Catus Flamens lying on a sofa</dcterms:title>

    <!-- date when representation was created -->
    <dcterms:created xsi:type="edtf">2022-01~</dcterms:created>

    <!-- multiple keywords about the representation -->
    <dcterms:subject>Cat</dcterms:subject>
    <dcterms:subject>Felis Catus Flamens</dcterms:subject>
    <dcterms:subject>Sofa</dcterms:subject>
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
   </premis:object>
</premis:premis>  
```


### /data/representations/representation_1/metadata/preservation/premis.xml

The `premis.xml` on _package level_ describes two PREMIS objects:
1. the representation
2. the image file

```xml
<?xml version='1.0' encoding='UTF-8'?>
<premis:premis xmlns:premis="http://www.loc.gov/premis/v3">
   <!-- Representation: archive master -->
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

   <!-- Image file: D523F963.jpg -->
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
#### 2. Image file (`/data/representations/representation_1/data/D523F963.jpg`)

```xml
<premis:object>
   <premis:objectCategory>file</premis:objectCategory>
   <premis:originalName>D523F963.jpg</premis:originalName>
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