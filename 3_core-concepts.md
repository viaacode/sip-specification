---
layout:       default
title:        Core concepts
parent:       2.1
grand_parent:  SIP Specification 
nav_order:    3
nav_exclude:  false
---

# Core Concepts
{: .no_toc }

This section introduces the core concepts of the PREMIS data model, which are fundamental to the meemoo SIP.
In essence, digital content is delivered as one of more (digital) _representations_ of an _intellectual entity_. 
In turn, a representation is comprised of one or more _files_.
These concepts are used throughout the remainder of this specification, and are reflected in the SIP's directory structure.

<figure class="mx-auto">
  <img src="../../../../../assets/images_spec/premis_objects.png" alt="Premis Object Diagram" /> 
  <figcaption>The PREMIS Object data model as adopted by the meemoo SIP.</figcaption>
</figure>

## Intellectual Entities, Representations and Files {#dfn-ie}

The [PREMIS Data Dictionary for Preservation Metadata](https://www.loc.gov/standards/premis/v3/premis-3-0-final.pdf) defines an **Intellectual Entity** (henceforth IE) as 'a distinct intellectual or artistic creation that is considered to be relevant to a designated community in the context of digital preservation'.
At meemoo, the IE embodies the intangible subject matter of the digital content; it is what users search for on the meemoo dissemination platforms.

An IE can be represented by one or more (digital) **Representations**, defined by PREMIS as 'a set of files (including metadata) needed for a complete rendition of an intellectual entity'.
At meemoo, a representation is a logical grouping of files that belong together and are needed to correctly read or display a digital reproduction.
Examples of such a logical grouping include (but are not limited to):

- a colour representation (e.g. photographs printed in colour);
- a black-and-white representation (e.g. black-and-white photographs);
- a representation from a certain perspective/angle (e.g. photographs shot from a one point perspective);
- ...

The **Files** that are included in a representation are the actual bits and bytes of the delivered content.
They have a specific media format and are not solely defined in/by the metadata.

This three-way distinction also allows including metadata about different aspects of the SIP's content.
For example, metadata about the content represented in a digital reproduction (which would be situated at the package level, since it covers the IE) can be separated from metadata purely about the digital reproduction itself (which would be situated at the representation level, since it covers (one of) the representation(s) of the IE).

Examples of these three concepts are given in the table below.

| Intellectual Entity | Representation | File |
|:------------------- | -------------- | ---- |
| a painting | the stitched high-resolution archive master of the painting | the `.tiff` files that compose the stiched archive master |
| an episode of a certain TV series | a browse copy of the episode | the `.mov` file and accompagnying `.srt` subtitle file |
| a newspaper edition of a certain date | an OCR rendition of the newspaper edition | the ALTO `.xml` files containing the newspaper's edition's textual content |

## Content profiles

A generic data model is necessary to ensure a scalable SIP design to current and future use cases.
However, not every utilization of this model is allowed at ingest in the meemoo archive.
Depending on the type of content, a specific mapping is required, which is captured in the different [content profiles]({{ site.baseurl }}{% link docs/diginstroom/sip/2.1/profiles/index.md %}).
A content profile determines

- whether an IE is subdivided further into other IEs (i.e. nesting of IEs);
- what the representations of any IE are;
- which files should be included in each representation;
- what metadata schemas can be used and where.

Content that is delivered to meemoo must therefore always be packaged in a meemoo SIP that adheres to a specific content profile.

{: .important }
Generally speaking, it is up to the content partner to decide what aspect of its collection is considered as an IE and what profile to use.
Note that this decision may have an impact on the expressivity of the metadata (eg. the basic profile only supports descriptive metadata in the Dublin Core vocabulary), the dissemination of the SIP's content and, in particular, on how its content is rendered on e.g. meemoo's dissemination platforms.
Typically, something that has individual descriptive metadata at the source (e.g. an entry in a collection registration or asset management system) and is expected to be distinguishable in search, should be viewed as an IE.

## Example

Consider a digitised newspaper edition with 10 pages.
Each page is digitised separately as a TIFF file and a JPEG file, resulting in 20 digital reproductions.
Finally, OCR is applied to each TIFF file, resulting in yet another 10 ALTO XML files (containing the textual representation of each newspaper page).
Using the concepts defined above, we view the newspaper edition as a whole as the IE.


<!-- TODO: We might want to update this section, since we model it differently in the meantime. -->
We have one IE (i.e. the newspaper edition) and we can discern between three representations of that IE: a high-resolution representation containing the TIFF files for e.g. reproduction, a low-resolution representation containing the JPEG files for e.g. browse copies on the web and a textual representation containing the ALTO XML files for e.g. searching through the actual textual content of the newspaper pages.

<figure class="mx-auto">
  <img src="../../../../../assets/images_spec/newspaper_situation_1.png" alt="Newspaper example" /> 
  <figcaption>Newspaper example</figcaption>
</figure>

<small>
Continue to [Structure]({{ site.baseurl }}{% link docs/diginstroom/sip/2.1/sip_structure/index.md %}).
</small>
