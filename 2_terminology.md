---
layout:       default
title:        Terminology
parent:       SIP Specification
grand_parent:  Digitale instroom
nav_order:    2
nav_exclude:  false
---
# Terminology

<dl>
    <dt>Administrative metadata</dt>
    <dd>Metadata about the origin of content, e.g. which Content Partner delivered the SIP to meemoo.</dd>
    <dt>Bag</dt>
    <dd>The topmost layer of the meemoo SIP. It serves as a wrapper around the SIP for transport and follows the <a href="https://www.rfc-editor.org/rfc/rfc8493.html">BagIt standard</a>.</dd>
    <dt>Content</dt>
    <dd>Digital content such as media files and metadata files.</dd>
    <dt>Content Partner (CP)</dt>
    <dd>Organisations that have a collaboration agreement with meemoo for storing their digital or digitized content.</dd>
    <dt>Content Profile</dt>
    <dd>A Content Profile is an extension of meemoo's SIP specification for the ingest of specific types of media files, e.g. newspapers, 3D objects, collection items with extensive metadata... A Content Profile boils down to additional requirements on top of the current specification.</dd>
    <dt>Descriptive metadata</dt>
    <dd>Metadata about the content represented in a digital reproduction. Its main goal is discovery and identification, e.g. the title of a picture or painting.</dd>
    <dt>Essence</dt>
    <dd>An alternative term for a media file (without additional metadata), such as a digital picture, a digital audio file...</dd>
    <dt>Intellectual Entity (IE)</dt>
    <dd>A distinct intellectual or artistic creation that is considered to be relevant to a designated community in the context of digital preservation.</dd>
    <dt>OAIS</dt>
    <dd>This term refers to the ISO OAIS Reference Model for an Open Archival Information System. This model is defined by recommendation <a href="https://public.ccsds.org/Pubs/650x0m2.pdf">CCSDS 650.0-B-2</a> of the Consultative Committee for Space Data Systems.</dd>
    <dt>Package</dt>
    <dd>The middle layer of the meemoo SIP. It consists of a number of directories and metadata files, containing the lowest (i.e. representation) layer of the meemoo SIP.</dd>
    <dt>Package METS</dt>
    <dd>The metadata file conforming to the <a href="https://www.loc.gov/standards/mets/mets.xsd">METS standard</a> situated at the package level of the SIP (i.e. at <code>/data/mets.xml</code>)</dd>
    <dt>Preservation metadata</dt>
    <dd>Metadata about the context and structure of a digital object. It is an essential part of current digital preservation strategies and data management. Examples include file size, the checksum of a file and how/when the file was created.</dd>
    <dt>Representation</dt>
    <dd>A set of files (including metadata) needed for a complete rendition of an IE. Note that an IE can be represented by multiple representations (e.g. a high quality representation and a low quality representation).</dd>
    <dt>Representation METS</dt>
    <dd>The metadata file conforming to the <a href="https://www.loc.gov/standards/mets/mets.xsd">METS standard</a> situated at one of the different representation directories of the representation level of the SIP (e.g. at <code>/data/representation/representation_1/mets.xml</code>)</dd>
    <dt>Sidecar</dt>
    <dd>An alternative term for a file exclusively containing metadata.</dd>
    <dt>Structural metadata</dt>
    <dd>Metadata about the structural relation between digital objects, e.g. how digital files relate to one another. This is especially relevant for e.g. newspaper, where each page has a relation with the previous/following page.</dd>
    <dt>Submission Information Package (SIP)</dt>
    <dd>The information package (containing media and metadata files) sent by the Content Partner to meemoo for ingest.</dd>
    <dt>Unicode</dt>
    <dd>The <a href="http://www.unicode.org/versions/latest/">Unicode Standard</a> is a standard for the consistent encoding, representation and handling of text. It can be implemented by different character encodings, with <a href="https://datatracker.ietf.org/doc/html/rfc3629">UTF-8</a> being the dominant encoding for the World Wide Web and internet technologies in general.</dd>
    <dt>XML</dt>
    <dd>The <a href="http://www.w3.org/TR/xml/">Extensible Markup Language</a> (i.e. XML) is a markup language and file format for storing, transmitting and reconstructing arbitrary data. At meemoo it is used to store administrative, descriptive, preservation and structural metadata about media files in meemoo's digital archive.</dd>
    <dt>XSD</dt>
    <dd><a href="https://www.w3.org/XML/Schema">XML Schema Definition</a> is a way to formally describe the elements in a XML document. It can be used for validation against existing metadata schemas and standards.</dd>
</dl>

## Datatypes

In the context of noting metadata values, the following datatypes are mentioned throughout this specification:

| Datatype       | Definition |
| -------------- | ---------- |
| <a id="integer"></a>Integer        | An arbitrary-size non negative integer number as defined in [XML Schema Part 2:Datatypes Second Edition](https://www.w3.org/TR/xmlschema-2/#nonNegativeInteger). |
| <a id="string"></a>String         | A sequence of zero or more Unicode (UTF-8) characters, usually wrapped in double quotes, using backslash escapes (if necessary). A character is represented as a single character string. |
| <a id="xsd-datetime"></a>XML Schema datetime            | Date and time notation according to the [XML Schema Part 2: Datatypes Second Edition](https://www.w3.org/TR/xmlschema-2/#dateTime) standard. Compatible with [ISO 8601:2004](https://www.w3.org/TR/xmlschema-2/#dateTime). |
| <a id="edtf"></a>EDTF           | Date and time, following the [Extended Date Time Format](https://www.loc.gov/standards/datetime/) up to level 1 plus the value `XXXX` to indicate an unknown date. All [XML Schema datetimes](#xsd-datetime) dates are also valid EDTF dates. |
| <a id="mimetype"></a>IANA mime type | Media types defined by the [Internet Assigned Numbers Authority](https://www.iana.org/assignments/media-types/media-types.xhtml). |
| <a id="md5"></a>MD5        | String result from applying the MD5 message-digest algorithm to a digital file object. |
| <a id="id"></a>ID | A string identifier consisting of alphanumerical characters (i.e. letters, digits, underscores, hyphens and periods), defined as the NCName datatype in the [XSD Datatypes specification](https://www.w3.org/TR/xmlschema11-2/#NCName).<br><br>Every ID MUST start with a letter or an underscore and it MUST be unique within the SIP. |
| <a id="uuid"></a>UUID           | A Universally Unique Identifier as defined in [RFC4122](https://datatracker.ietf.org/doc/html/rfc4122). Note that a UUID is also an instance of an ID, if it starts with a letter or an underscore.|
| <a id="or-id"></a>OR-id            | Organisation ID; a unique sequence of 10 Unicode ([UTF-8](https://datatracker.ietf.org/doc/html/rfc3629)) characters attributed by meemoo to each of its Content Partners. Note that an OR-id is also an instance of an ID. |
| <a id="uri"></a>URI            | A Uniform Resource Identifier as defined in [RFC3986](https://datatracker.ietf.org/doc/html/rfc3986), which extends the URL. |
| <a id="url"></a>URL            | A Uniform Resource Locator as defined in [RFC1738](https://datatracker.ietf.org/doc/html/rfc1738). |

<small>
Continue to [Core Concepts]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/3_core-concepts.md %}).
</small>
