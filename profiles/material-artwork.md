---
layout:       default
title:        Material artwork
parent:       Profiles
grand_parent:  2.1
nav_order:    3
nav_exclude:  false
---
{% assign ma_constraints = site.data.2_1._data.MATERIAL_ARTWORK_PROFILE %}

# Profile: Material artwork 

The _Material artwork_ profile supports digital reproductions of artworks that are moveable material objects, often, but not always, displayed in or maintained by museums. 
This includes photographic registration of 2D artworks, such as paintings or drawings, in high and very high (gigapixel) resolution and high-polygon scans of 3D artworks, such as statues or sculptures.

This content profile specifies how to package different media files (e.g., TIFF, JPEG, OBJ or MTL), their metadata and the relationships between them in a meemoo SIP package.
It also allows extensions to the descriptive metadata using [Schema.org](https://schema.org).

**Permalink:** <https://data.hetarchief.be/id/sip/2.1/material-artwork>

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

{% assign constraints = ma_constraints | where_exp: "c",
"c.Section == 'general'" %}

{% include_relative _list_constraints.liquid constraints = constraints %}

Only the MD5 hashing algorithm is allowed to compute the fixity, thus:

{% assign constraints = ma_constraints | where_exp: "c",
"c.Section == 'md5'" %}

{% include_relative _list_constraints.liquid constraints = constraints %}

### Package METS

{% assign constraints = ma_constraints | where_exp: "c",
"c.Section == 'mets'" %}

{% include_relative _list_constraints.liquid constraints = constraints %}

### Descriptive Metadata

{% assign constraints = ma_constraints | where_exp: "c",
"c.Section == 'descriptive'" %}

{% include_relative _list_constraints.liquid constraints = constraints %}

### Validation

The XML files that are required by this profile can be validated using the following XML schema definitions:

| File | Format | XML Schema |
| `METS.xml` | METS v1.12.1 | [mets.xsd](https://www.loc.gov/standards/mets/mets.xsd) |
| `premis.xml` | PREMIS v3.0 | [premis-v3-0.xsd](https://www.loc.gov/standards/premis/v3/premis-v3-0.xsd) |
| `dc+schema.xml` | Dublin Core with Schema.org | dc+schema.xsd (not yet available) |

## Use Cases

Some use cases that implement this profile are:

{% include _usecases.liquid  %}
