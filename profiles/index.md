---
layout:       default
title:        Profiles
parent:       SIP Specification 1.0
nav_order:    8
nav_exclude:  false
has_children: true
---
# SIP content profiles

SIP content profiles define specific configurations of the meemoo SIP specification that are supported by the meemoo ingest pipeline.
They group different types of content that share a similar structure (e.g., there is only one representation or one file) and/or have the same metadata demands (e.g. all of the supplied metadata fits in the DCTERMS vocabulary).

A profile adds extra restrictions or extensions on top of the SIP specification.
Hence, the SIP validation process depends on both.
A delivered SIP MUST indicate which profile it adheres to in the package `mets.xml` through the [`mets/@csip:CONTENTINFORMATIONTYPE` attribute]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/sip_structure/5_structure_package.md %}#CONTENTINFORMATIONTYPE).

<small>
Continue to [Basic profile]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/profiles/basic.md %}).
</small>