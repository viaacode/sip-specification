---
layout:       default
title:        Basic
parent:       Profiles
grand_parent:  SIP Specification 1.0
nav_order:    1
nav_exclude:  false
---
# Profile: Basic 

The basic profile supports simple cases consisting of a single media file accompanied by limited metadata.

**Permalink:** <https://data.hetarchief.be/id/sip/1.0/basic>

**Directory structure:**

```plaintext
root_directory
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
           |  |── file_1.xyz
           │  └── ...
           │
           └──metadata
              └──preservation
                 └── premis.xml
```


## Requirements

- The `csip:CONTENTINFORMATIONTYPE` attribute MUST be set to `https://data.hetarchief.be/id/sip/1.0/basic`.
- There MUST be exactly one IE.
- The IE MUST be represented by exactly one representation.
- There MUST NOT be any descriptive metadata at the representation level.
- A descriptive metadata file `descriptive/dc.xml` MUST be present at the package level.
- Descriptive metadata MUST be limited to the DCTERMS metadata schema according to the [package level requirements]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/sip_structure/5_structure_package.md %}#dc-requirements).
- Preservation metadata MUST be limited to the PREMIS metadata schema.
- There MUST be preservation metadata at the package level in the `preservation/premis.xml` file.
- There MUST be preservation metadata at the representation level in the `preservation/premis.xml` file.

## Use Cases

Some use cases that implement this profile are:

{% include _usecases.liquid  %}
