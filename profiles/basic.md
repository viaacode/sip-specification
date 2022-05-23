---
layout:       default
title:        Basic
parent:       Profiles
nav_order:    3
nav_exclude:  false
---
Status: WIP
{: .label .label-yellow }
# Profile: Basic 

The basic profile supports simple cases consisting of a single digital object accompanied by limited metadata.

**Content information type:** <https://data.hetarchief.be/id/sip-profile/basic>

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
    |   |   └── descriptive.xml
    |   └── preservation
    |       └── preservation.xml
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
                 └── preservation.xml
```


## Requirements

- The `csip:OTHERCONTENTINFORMATIONTYPE` attribute MUST be set to `https://data.hetarchief.be/id/sip-profile/basic`.
- There MUST only be exactly one [_Intellectual Entity (IE)_](#dfn-ie).
- An _IE_ MUST contain exactly one [_Representation_](#dfn-ie).
- There MUST NOT be any descriptive metadata at [_representation level_]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/sip_structure/6_structure_representation.md %}). 
- Descriptive metadata file `descriptive/descriptive.xml` MAY be present at [_package level_]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/sip_structure/5_structure_package.md %}), but MUST be limited to the [Dublin Core Metadata Initiative Metadata Terms](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) schema.


## Metadata

- licenses
- local ids

## Use Cases

Some use cases that implement this profile are:

{% for page in site.pages %}
{% if page.sip_profile == "basic" %}
- [{{ page.title }}]({{ page.url }})
{% endif %}
{% endfor %}


 