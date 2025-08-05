---
layout:       default
title:        Newspaper edition (without PDF)
parent:       Use cases
grand_parent:  1.2
nav_order:    4
nav_exclude:  false
has_children: false
sip_profile:  Newspaper
---

# Use Case: a newspaper edition digitised per page (without PDF)

The following use case describes how to package a newspaper edition digitised per page (without PDF file). It includes:

- TIFF files;
- ALTO XML files;
- basic descriptive metadata;
- basic preservation metadata.

It uses the [**Newspaper SIP profile**]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/profiles/bibliographic.md %}).

A full sample SIP can be downloaded [here](https://github.com/viaacode/documentation/tree/main/assets/sip_samples/newspaper_c44a0b0d-6e2f-4af2-9dab-3a9d447288d0/).

## The content

The following content is provided for packaging:

| `18950101_0001.tiff`<br>`18950101_0002.tiff`<br>`18950101_0003.tiff` | The essence: 3 image files in the TIFF media format representing 3 digitised newspaper pages from a newspaper edition issued on 01/01/1895. |
| `18950101_0001.xml`<br>`18950101_0002.xml`<br>`18950101_0003.xml` | The essence: 3 XML files in the ALTO XML media format representing the textual content of 3 digitised newspaper pages from a newspaper edition issued on 01/01/1895. |
| `metadata.xml` | A metadata record describing the newspaper edition. |

The metadata record can contain the following information:

- the newspaper title;
- the date the newspaper edition was issued;
- the number of pages;
- the ordering of pages;
- a list of meemoo licenses;
- information about the event that created the ALTO XML from the TIFF files;
- an identifier from the [Abraham Belgian Newspaper Catalog](https://krantencatalogus.be/);
- the md5 checksums of the media files;
- ...

Note that in some instances this metadata is not readily available in a dedicated separate metadata file. In that case it is sometimes possible to derive/parse basic metadata (such as the newspaper title, the issuance data, the order of pages etc.) from the structure and naming conventions used when the media files were packaged by a service provider. For example, in the case of the content defined above, the issuance of the newspaper edition and the ordering of the pages is captured in the file names.

## Applying the core concepts

Since the metadata only/mostly describes the newspaper edition rather than the separate pages making up the edition, we can view it as the main Intellectual Entity in the SIP.

We can distinguish between two sets of files representing the newspaper edition: a set containing image files (in the TIFF file format) and a set containing XML files (in the ALTO XML file format).

Since each set of files can have a meaning on its own (i.e. one could focus solely on the TIFF files to get an idea of what the pages looked liked or one could want to only look at the ALTO XML files to read the contents of the pages without the lay-out of the page itself), two separate representations can be made: one representation containing the TIFF files and one representation containing the ALTO XML files.

|_Intellectual Entity_|the newspaper edition issued on January 1st, 1895|
|_Representation 1_|a visual representation of the newspaper edition containing image files|
|_Representation 2_|a textual representation of the newspaper edition containing text files|
|_Files (rep. 1)_|the TIFF files: `18950101_0001.tiff`, `18950101_0002.tiff` and `18950101_0003.tiff`|
|_Files (rep.2)_|the ALTO XML files: `18950101_0001.xml`, `18950101_0002.xml` and `18950101_0003.xml`|

This case relies on the Newspaper profile because:

- there is one IE and multiple representations;
- the newspaper content can be better described using a dedicated metadata schema for bibliographic content such as [MODS](https://www.loc.gov/standards/mods/) instead of DCTERMS;
- since a newspaper contains multiple pages ordered in a sequence, we need a mechanism to represent that sequence in the metadata.

## Directory structure

We package the above in a meemoo SIP named `newspaper_c44a0b0d-6e2f-4af2-9dab-3a9d447288d0.zip`.
It has the following directory structure:

```plaintext
root_directory
│──manifest-md5.txt
│──bagit.txt
│
└──data
    │──mets.xml
    │──metadata
    |   |──descriptive
    |   |  └──mods.xml
    |   └──preservation
    |       └──premis.xml
    │
    └──representations
        │──representation_1
        │    │──mets.xml
        │    │──data
        │    |   |──18950101_0001.tiff
        │    |   |──18950101_0002.tiff
        │    │   └──18950101_0003.tiff
        │    │
        │    └──metadata
        │        └──preservation
        │            └──premis.xml
        │
        └──representation_2
             │──mets.xml
             │──data
             |   |──18950101_0001.xml
             |   |──18950101_0002.xml
             │   └──18950101_0003.xml
             │
             └──metadata
                └──preservation
                   └──premis.xml
```

## The metadata

In total, the SIP contains 5 metadata files:

|`data/metadata/descriptive/mods.xml`|Descriptive metadata about the IE residing at the _package level_ using the MODS metadata schema.|
|`data/metadata/preservation/premis.xml`|Preservation metadata about the IE residing at the _package level_, including any PREMIS events related to the SIP/package/representations.|
|`data/representations/representation_1/metadata/preservation/premis.xml`|Preservation metadata about the representation and TIFF files residing at the _representation level_.|
|`data/representations/representation_2/metadata/preservation/premis.xml`|Preservation metadata about the representation and ALTO XML files residing at the _representation level_.|


### data/metadata/descriptive/mods.xml

The `mods.xml` of the package level describes the IE using [the MODS metadata schema](https://www.loc.gov/standards/mods/).
It contains minimal metadata such as a title, a description, an identifier, a date of creation and of issuance...

The identifier is used to link the `mods.xml` file to the corresponding PREMIS object in the `preservation/premis.xml` file of the package level (this is similar to the use of `<dcterms:identifier/>` described [here]({{ site.baseurl }}{% link docs/diginstroom/sip/1.2/sip_structure/5_structure_package.md %}#shareduuidinfo)).

Note that only a subset of MODS elements are obligatory in the newspaper SIP profile.
The examples below and in the sample mentioned earlier therefore only serve as an illustration of possible elements rather than as an exhaustive list of obligatory elements.

```xml
<?xml version='1.0' encoding='UTF-8'?>
<mods:mods xmlns:mods="http://www.loc.gov/mods/v3" version="3.7" xmlns:xs="http://www.w3.org/2001/XMLSchema/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.loc.gov/mods/v3 http://www.loc.gov/standards/mods/v3/mods-3-7.xsd">

  <mods:titleInfo>
    <mods:title>Le Chat Blanc</mods:title>
  </mods:titleInfo>
  <mods:titleInfo type="alternative">
    <mods:title>Journal Indépendant: Le Chat Blanc</mods:title>
  </mods:titleInfo>
  <mods:identifier>uuid-e6a138e5-a0fc-41d3-a912-9491a3502f57</mods:identifier>
  <mods:typeOfResource>newspaper edition</mods:typeOfResource>
  <mods:genre authority="marcgt" authorityURI="https://www.loc.gov/standards/valuelist/marcgt.html">newspaper</mods:genre>
  <mods:genre authority="ngl" authorityURI="https://www.lib.washington.edu/gmm/collections/mcnews/ngl">amateur newspapers</mods:genre>
  <mods:originInfo>
    <mods:issuance>serial</mods:issuance>
    <mods:dateIssued xsi:type="edtf:EDTF-level0" encoding="edtf">2022-08-02</mods:dateIssued>
    <mods:place>
      <mods:placeTerm type="text">Ghent, Belgium</mods:placeTerm>
      <mods:placeTerm type="code" authority="iso3166" authorityURI="https://www.iso.org/iso-3166-country-codes.html">BEL</mods:placeTerm>
    </mods:place>
  </mods:originInfo>
  <mods:subject>
    <mods:topic>chat blanc</mods:topic>
    <mods:topic>cats</mods:topic>
  </mods:subject>
  <mods:relatedItem type="series">
    <mods:identifier type="abraham_id" typeURI="https://anet.be">c:bnc:99999</mods:identifier>
    <mods:identifier type="abraham_uri" typeURI="https://anet.be">https://anet.be/record/opacbnc/c:bnc:99999/N</mods:identifier>
  </mods:relatedItem>
  <mods:physicalDescription>
    <mods:form authority="marcform" authorityURI="https://www.loc.gov/standards/valuelist/marcform.html">print</mods:form>
    <mods:extent unit="pages">3</mods:extent>
  </mods:physicalDescription>
  <mods:note type="license">VIAA-PUBLIEK-METADATA-LTD</mods:note>

</mods:mods>
```

### data/metadata/preservation/premis.xml

The `premis.xml` of the package level describes the IE and the relationships with its representations.
It also contains a transcription event that details how the ALTO XML was created from the TIFF files using OCR.

Note that the identifier in the `<premis:objectIdentifier>` element is shared with the `<mods:identifier/>` (in the `descriptive/mods.xml` file) in order to link the PREMIS IE object to its descriptions in the two files.


```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

  <!-- IE for the newspaper edition -->
  <premis:object xsi:type="premis:intellectualEntity">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-e6a138e5-a0fc-41d3-a912-9491a3502f57</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship with representation 1: TIFFs -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isr">is represented by</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-d8fd6dde-53a5-4614-823c-32f64588efe6</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship with representation 2: ALTO XMLs -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isr">is represented by</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-1fca6190-a4bd-4773-8529-272b9e7d536a</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

  </premis:object>

  <!-- Transcription event for generating ALTO XML from TIFF via OCR -->
  <premis:event>
    <premis:eventIdentifier>
      <premis:eventIdentifierType>UUID</premis:eventIdentifierType>
      <premis:eventIdentifierValue>uuid-34ae79f8-a8e7-4768-a269-4d6d895662d6</premis:eventIdentifierValue>
    </premis:eventIdentifier>
    <premis:eventType>transcription</premis:eventType>
    <premis:eventDateTime>2022-02-16T10:01:15.014+02:00</premis:eventDateTime>
    <premis:eventDetailInformation>
      <premis:eventDetail>Generate ALTO XML from TIFF via OCR</premis:eventDetail>
    </premis:eventDetailInformation>
    <premis:linkingObjectIdentifier>
      <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
      <premis:linkingObjectIdentifierValue>uuid-d8fd6dde-53a5-4614-823c-32f64588efe6</premis:linkingObjectIdentifierValue>
      <premis:linkingObjectRole>source</premis:linkingObjectRole>
    </premis:linkingObjectIdentifier>
    <premis:linkingObjectIdentifier>
      <premis:linkingObjectIdentifierType>UUID</premis:linkingObjectIdentifierType>
      <premis:linkingObjectIdentifierValue>uuid-1fca6190-a4bd-4773-8529-272b9e7d536a</premis:linkingObjectIdentifierValue>
      <premis:linkingObjectRole>outcome</premis:linkingObjectRole>
    </premis:linkingObjectIdentifier>
  </premis:event>

</premis:premis>
```

### data/representations/representation_1/metadata/preservation/premis.xml

The `premis.xml` file of the first representation describes four PREMIS objects (of which the first two are shown in the example below):

1. the representation;
2. the TIFF file `18950101_0001.tiff`;
3. the TIFF file `18950101_0002.tiff`;
4. the TIFF file `18950101_0003.tiff`.

It also describes the various relationships between these objects:

1. the relation between the representation and the IE at the package level;
2. the relations between the representation and the TIFF files;
3. the relations between the TIFF files and the ALTO XML files of the second representation (relying on the transcription event described in the `premis.xml` file of the package level).

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

  <premis:object xsi:type="premis:representation">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-d8fd6dde-53a5-4614-823c-32f64588efe6</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship between representation and its files -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/inc">includes</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-8c767f3d-c116-40fc-8491-951dfb14aa1b</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-1711cd43-19d2-4d89-9259-17443fc7d75f</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-ba513329-b0ff-4216-883e-928845774b8c</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship between representation and its IE -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/rep">represents</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-e6a138e5-a0fc-41d3-a912-9491a3502f57</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>
  </premis:object>

  <premis:object xsi:type="premis:file">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-8c767f3d-c116-40fc-8491-951dfb14aa1b</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:objectCharacteristics>
      <premis:fixity>
        <premis:messageDigestAlgorithm authority="cryptographicHashFunctions" authorityURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions" valueURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5">
                MD5
        </premis:messageDigestAlgorithm>
        <premis:messageDigest>d41d8cd98f00b204e9800998ecf8427e</premis:messageDigest>
      </premis:fixity>
      <premis:size>0</premis:size>
      <premis:format>
        <premis:formatRegistry>
          <premis:formatRegistryName>PRONOM</premis:formatRegistryName>
          <premis:formatRegistryKey>fmt/353</premis:formatRegistryKey>
          <premis:formatRegistryRole authority="formatRegistryRole" authorityURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole" valueURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole/spe">specification</premis:formatRegistryRole>
        </premis:formatRegistry>
      </premis:format>
    </premis:objectCharacteristics>

    <premis:originalName>18950101_0001.tiff</premis:originalName>

    <!-- relationship between file and its representation -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isi">is included in</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-d8fd6dde-53a5-4614-823c-32f64588efe6</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship between tiff file and its alto encoded text -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/der">derivation</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/iso">is source of</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-3df17198-806c-4749-a54a-01cbf747227f</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
      <premis:relatedEventIdentifier>
        <premis:relatedEventIdentifierType>UUID</premis:relatedEventIdentifierType>
        <premis:relatedEventIdentifierValue>uuid-34ae79f8-a8e7-4768-a269-4d6d895662d6</premis:relatedEventIdentifierValue>
      </premis:relatedEventIdentifier>
    </premis:relationship>

  </premis:object>

  [similar to above for files 18950101_0002.tiff and 18950101_0003.tiff]

</premis:premis>
```

### data/representations/representation_2/metadata/preservation/premis.xml

The `premis.xml` file of the second representation describes four PREMIS objects (of which the first two are shown in the example below):

1. the representation;
2. the ALTO XML file `18950101_0001.xml`;
3. the ALTO XML file `18950101_0002.xml`;
4. the ALTO XML file `18950101_0003.xml`.

It also describes the various relationships between these objects:

1. the relation between the representation and the IE at the package level;
2. the relations between the representation and the ALTO XML files;
3. the relations between the ALTO XML files and the TIFF files of the first representation (relying on the transcription event described in the `premis.xml` file of the package level).

```xml
<?xml version="1.0" encoding="UTF-8"?>
<premis:premis version="3.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:premis="http://www.loc.gov/premis/v3" xsi:schemaLocation="http://www.loc.gov/premis/v3 https://www.loc.gov/standards/premis/premis.xsd">

  <premis:object xsi:type="premis:representation">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-1fca6190-a4bd-4773-8529-272b9e7d536a</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <!-- relationship between representation and its files -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/inc">includes</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-3df17198-806c-4749-a54a-01cbf747227f</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-3d2dfddb-6348-43b7-865d-ba9a12ef5c79</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-ab2d5dbd-3662-448a-bfab-1a0b5c4b6349</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship between representation and its IE -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/rep">represents</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-e6a138e5-a0fc-41d3-a912-9491a3502f57</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>
  </premis:object>

  <premis:object xsi:type="premis:file">

    <premis:objectIdentifier>
      <premis:objectIdentifierType>UUID</premis:objectIdentifierType>
      <premis:objectIdentifierValue>uuid-3df17198-806c-4749-a54a-01cbf747227f</premis:objectIdentifierValue>
    </premis:objectIdentifier>

    <premis:objectCharacteristics>
      <premis:fixity>
        <premis:messageDigestAlgorithm authority="cryptographicHashFunctions" authorityURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions" valueURI="http://id.loc.gov/vocabulary/preservation/cryptographicHashFunctions/md5">
                MD5
        </premis:messageDigestAlgorithm>
        <premis:messageDigest>d41d8cd98f00b204e9800998ecf8427e</premis:messageDigest>
      </premis:fixity>
      <premis:size>0</premis:size>
      <premis:format>
        <premis:formatRegistry>
          <premis:formatRegistryName>PRONOM</premis:formatRegistryName>
          <premis:formatRegistryKey>fmt/101</premis:formatRegistryKey>
          <premis:formatRegistryRole authority="formatRegistryRole" authorityURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole" valueURI="http://id.loc.gov/vocabulary/preservation/formatRegistryRole/spe">specification</premis:formatRegistryRole>
        </premis:formatRegistry>
      </premis:format>
    </premis:objectCharacteristics>

    <premis:originalName>18950101_0001.xml</premis:originalName>

    <!-- relationship between file and its representation -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/str">structural</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/isi">is included in</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-1fca6190-a4bd-4773-8529-272b9e7d536a</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
    </premis:relationship>

    <!-- relationship between alto xml file and the tiff it's derived from via OCR -->
    <premis:relationship>
      <premis:relationshipType authority="relationshipType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipType/der">derivation</premis:relationshipType>
      <premis:relationshipSubType authority="relationshipSubType" authorityURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType" valueURI="http://id.loc.gov/vocabulary/preservation/relationshipSubType/hss">has source</premis:relationshipSubType>
      <premis:relatedObjectIdentifier>
        <premis:relatedObjectIdentifierType>UUID</premis:relatedObjectIdentifierType>
        <premis:relatedObjectIdentifierValue>uuid-8c767f3d-c116-40fc-8491-951dfb14aa1b</premis:relatedObjectIdentifierValue>
      </premis:relatedObjectIdentifier>
      <premis:relatedEventIdentifier>
        <premis:relatedEventIdentifierType>UUID</premis:relatedEventIdentifierType>
        <premis:relatedEventIdentifierValue>uuid-34ae79f8-a8e7-4768-a269-4d6d895662d6</premis:relatedEventIdentifierValue>
      </premis:relatedEventIdentifier>
    </premis:relationship>

  </premis:object>

  [similar to above for files 18950101_0002.xml and 18950101_0003.xml]

</premis:premis>
```
