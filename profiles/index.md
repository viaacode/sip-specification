---
layout:       default
title:        Profiles
parent:       SIP Specification
nav_order:    8
nav_exclude:  false
has_children: true
---
Status: WIP
{: .label .label-yellow }

SIP profiles define specific configurations of the meemoo SIP that are supported by the meemoo ingest pipeline.
They group different types of content that share a similar structure (e.g., there is only one representation or one file) and have the same metadata demands (e.g., all of the supplied metadata fits in the Dublin Core vocabulary).

A profile adds extra restrictions or extensions on top of the SIP specification.
Hence, the SIP validation process depends on both. 
A delivered SIP MUST indicate which profile it adheres to in the package `mets.xml` through the [`mets/@csip:OTHERCONTENTINFORMATIONTYPE` attribute]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/sip_structure/5_structure_package.md %}#OTHERCONTENTINFORMATIONTYPE).

<small>
Continue to [Use Cases]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/usecases/index.md %}).
</small>