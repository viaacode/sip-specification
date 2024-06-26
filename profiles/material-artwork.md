---
layout:       default
title:        Material artwork
parent:       Profiles
grand_parent:  2.0
nav_order:    3
nav_exclude:  false
---
Editor's Draft
{: .label .label-yellow }
# Profile: Material artwork 

The _Material artwork_ profile supports digital reproductions of artworks that are moveable material objects, often, but not always, displayed in or maintained by museums. 
This includes photographic registration of 2D artworks, such as paintings or drawings, in high and very high (gigapixel) resolution and high-polygon scans of 3D artworks, such as statues or sculptures.

This content profile specifies how to package different media files (e.g., TIFF, JPEG, OBJ or MTL), their metadata and the relationships between them in a meemoo SIP package.
It also allows extensions to the descriptive metadata using [Schema.org](https://schema.org).

**Permalink:** <https://data.hetarchief.be/id/sip/2.0/material-artwork>

## Example Directory structure

### 2D photoregistration

```plaintext
root_directory
│── METS.xml
│── metadata
|   |── descriptive
|   |   └── dc+schema.xml
|   └── preservation
|       └── premis.xml
│
└── representations
   └──representation_1       # overview with frame
      │── METS.xml
      └──data
      │  └── PID_overzichtsopname_metlijst_tiff.tiff
      │
      └──metadata
         |── descriptive     (optional)
         |   └── dc+schema.xml
         └──preservation
            └── premis.xml
   └──representation_2       # overview without frame
      │── METS.xml
      └──data
      │  └── PID_overzichtsopname_zonderlijst_tiff.tif
      │
      └──metadata
         |── descriptive     (optional)
         |   └── dc+schema.xml    
         └──preservation
            └── premis.xml
   └──representation_3       # composed stitch 
      │── METS.xml
      └──data
      │  └── PID_stitch_tiff.tif
      │
      └──metadata
         |── descriptive     (optional)    
         |   └── dc+schema.xml    
         └──preservation
            └── premis.xml
   └──representation_4       # stitch 
      │── METS.xml
      └──data
      |  |── PID_deelopname1_tiff.tif
      |  |── PID_deelopname2_tiff.tif
      │  └── ...
      │
      └──metadata
         |── descriptive     (optional)  
         |   └── dc+schema.xml    
         └──preservation
            └── premis.xml
```

### 3D scan

```plaintext
root_directory
│── METS.xml
│── metadata
|   |── descriptive
|   |   └── dc+schema.xml
|   └── preservation
|       └── premis.xml
│
└── representations
   └──representation_1       # high-poly capture for print
      │── METS.xml
      └──data  
      │  └── PID_ARCH_STL.STL              
      │
      └──metadata
         |── descriptive     (optional)
         |   └── dc+schema.xml
         └──preservation
            └── premis.xml
   └──representation_2       # high-poly capture
      │── METS.xml
      └──data
      |  |── PID_ARCH_OBJ.OBJ       # polygon file    
      |  |── PID_ARCH_TIFF_COLOR.TIFF      # texture image       
      │  └── PID_ARCH_MTL.MTL              # texture mapping file
      │
      └──metadata
         |── descriptive     (optional)
         |   └── dc+schema.xml
         └──preservation
            └── premis.xml
   └──representation_3       # low-poly capture
      │── METS.xml
      └──data
      |  |── PID_VER_OBJ.OBJ       # polygon file    
      |  |── PID_VER_COLOR_BMP.BMP             # texture image       
      │  └── PID_VER_MTL.MTL                   # texture mapping file
      │
      └──metadata
         |── descriptive     (optional)
         |   └── dc+schema.xml   
         └──preservation
            └── premis.xml
   └──representation_4       # quality assessment reference
      │── METS.xml
      └──data
      |  |── PID_REF_OBJ.OBJ               # polygon file    
      |  |── PID_REF_BMP.BMP               # texture image      
      |  |── PID_REF_IJK_BMP.BMP           # reference texture image     
      │  └── PID_REF_MTL.MTL               # texture mapping file
      │
      └──metadata
         |── descriptive     (optional)
         |   └── dc+schema.xml    
         └──preservation
            └── premis.xml
```

## Requirements

### General

- There MUST be exactly one IE at the root. There MAY be other sub-IE's that are part of the root IE or other sub-IE's (e.g. to describe panels of a triptych individually).
- There MUST be at least one representation, but there MAY be multiple: either containing different captures or resolutions of the same IE or representing a different IE.
- Each representation MUST contain at least one file. 
- Preservation metadata MUST be limited to the PREMIS metadata schema.
- There MUST be preservation metadata at the package level in the `preservation/premis.xml` file.
- There MUST be preservation metadata at the representation level in the `preservation/premis.xml` file.
- Only the MD5 hashing algorithm is allowed to compute the fixity, thus:
  - The value of element `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:fixity/premis:messageDigestAlgorithm` MUST be set to `MD5`.
  - The value of attribute `premis:premis/premis:object[@xsi:type="premis:file"]/premis:objectCharacteristics/premis:fixity/premis:messageDigestAlgorithm/@valueURI` MUST be set to `"http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5"`.

### Package METS

- The `csip:CONTENTINFORMATIONTYPE` attribute MUST be set to `OTHER` and the `csip:OTHERCONTENTINFORMATIONTYPE` attribute MUST be set to `https://data.hetarchief.be/id/sip/2.0/material-artwork`.
- The `TYPE` attribute in the `METS.xml` file MUST be set to
  - `Photographs - Digital` (for 2D objects) or
  - `Scanned 3D Objects (output from photogrammetry scanning)` (for 3D objects).
- The `mets/dmdSec/mdRef/@MDTYPE` attribute MUST be set to `OTHER` and `mets/dmdSec/mdRef/@OTHERMDTYPE` attribute must be set to `DC+SCHEMA`.
  

### Descriptive Metadata

- A descriptive metadata file `descriptive/dc+schema.xml` describing the IE MUST be present at the package level.
- A descriptive metadata file `descriptive/dc+schema.xml` describing the representation MAY be present at the representation level (e.g. to indicate diverting licenses). 
- Descriptive metadata in `dc+schema.xml` MUST be limited to the [DCTERMS](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) and [SCHEMA](http://schema.org) elements outlined in the [basic profile]({{ site.baseurl }}{% link docs/diginstroom/sip/2.0/profiles/basic.md %}#dc-requirements).
- The [DCTERMS](https://www.dublincore.org/schemas/xmls/qdc/dcterms.xsd) and [SCHEMA](http://schema.org) metadata MUST follow the [basic profile requirements]({{ site.baseurl }}{% link docs/diginstroom/sip/2.0/profiles/basic.md %}#dc-requirements) regarding the use of elements and attributes.
- Some descriptive metadata elements of datatype [String]({{ site.baseurl }}{% link docs/diginstroom/sip/2.0/2_terminology.md %}#string) MUST contain an attribute `@xml:lang` that indicates the language of the metadata element's value (in order to, for example, specify a title or description in multiple languages); these are indicated with `[@xml:lang=*]` in the table below. Other elements MUST NOT contain this attribute.
- The value of the `@xml:lang` attribute MUST be a valid [IETF BCP 47 language tag](https://www.rfc-editor.org/info/bcp47)(see [here](https://www.iana.org/assignments/language-subtag-registry/language-subtag-registry) for a list). 

### Validation

The XML files that are required by this profile can be validated using the following XML schema definitions:

| File | Format | XML Schema |
| `METS.xml` | METS v1.12.1 | [mets.xsd](https://www.loc.gov/standards/mets/mets.xsd) |
| `premis.xml` | PREMIS v3.0 | [premis-v3-0.xsd](https://www.loc.gov/standards/premis/v3/premis-v3-0.xsd) |
| `dc+schema.xml` | Dublin Core with Schema.org | dc+schema.xsd (not yet available) |

## Use Cases

Some use cases that implement this profile are:

{% include _usecases.liquid  %}
