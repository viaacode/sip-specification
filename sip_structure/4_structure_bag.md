---
layout:       default
title:        Bag level
parent:       Structure
grand_parent:  1.0
nav_order:    5
nav_exclude:  false
---
Retired
{: .label .label-red }
# Bag level
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

1. TOC
{:toc}

The bag is the top level of the meemoo SIP and is essentially a wrapper around a SIP submitted by a CP for ingest in the meemoo archive.
It is a compressed directory that conforms to the [BagIt 1.0 specification (RFC 8493)](https://www.rfc-editor.org/rfc/rfc8493.html).

A bag serves a purely practical purpose as a transfer container between a CP's archive and meemoo's ingest space.
Therefore, it will be unpacked during ingest and is deleted after processing.
As such it will not appear in the meemoo archive as a separate entity.

***Example***

```plaintext
root_directory
│── manifest-md5.txt
│── bagit.txt
│
└──data
   │   ...
```

***Requirements***

- A bag MUST be a compressed archive file.
- A bag MUST contain a `bagit.txt` file.
- A bag MUST contain a `manifest-md5.txt` file.
- A bag MUST contain a `/data` directory.
- The contents of a bag MUST be character-encoded according to UTF-8.
- A bag MUST be a ZIP file.
- A bag MAY contain a `bag-info.txt` file.

## manifest-md5.txt (file)

The `manifest-md5.txt` file lists all files in the bag across the different directories together with their corresponding checksums created with the MD5 message-digest algorithm.
It is used during processing of the bag to allow for data integrity checking.

***Example***

```plaintext
2c28e2b32a6e5e94669a516036838429  ./data/mets.xml
95fc1f5cfd89b97bacf49473267752f5  ./data/representations/representation_2/mets.xml
18513a8d61c6f2cbaaeeedd754b01d6b  ./data/representations/representation_2/data/D523F963.jpg
fde6c913b4105cc06174fba8cd3b864e  ./data/representations/representation_2/metadata/preservation/premis.xml
31d402b829f673afe24f698dc462bbde  ./data/representations/representation_2/metadata/descriptive/dc_1.xml
fc030be17b9c7fd3f86b0cf095a64a33  ./data/representations/representation_1/mets.xml
d4985ba4b67ff067a0e84c53b6d35355  ./data/representations/representation_1/data/1450.jpeg
b7ae37f6094794e313402b9d064978e8  ./data/representations/representation_1/data/1445.jpeg
7a1a5145d1f54b01537b76e52b19b804  ./data/representations/representation_1/metadata/preservation/premis.xml
e45622b2b8536d312203e1cb7d5548c7  ./data/representations/representation_1/metadata/descriptive/dc_1.xml
c50c40b09a5f04ecf441f136c1c6581e  ./data/metadata/preservation/premis.xml
9d55815152e83db76a32f74990d79cd3  ./data/metadata/descriptive/dc_3.xml
cd17cbb2153946c8462e10b337e0e9c1  ./data/metadata/descriptive/dc_1.xml
fbab574560f2d548fd84c6c1fd1cb7f2  ./data/metadata/descriptive/dc_2.xml
eaa2c609ff6371712f623f5531945b44  ./bagit.txt
d67fe46437a03a307c7b28c819b56a95  ./manifest-md5.txt
```

***Requirements***

- The `manifest-md5.txt` file MUST list all files contained in the bag.
- The `manifest-md5.txt` file MUST NOT list any directories.
- The `manifest-md5.txt` file MUST NOT list any files outside of the bag.
- Each line of the `manifest-md5.txt` file MUST be of the form *checksum filepath*, where *filepath* is the pathname of a file relative to the bag-level directory, and *checksum* is a hex-encoded checksum calculated by the MD5 message-digest algorithm.
- The slash ('/') character MUST be used as a path separator in *filepath*.
- One or more linear whitespace characters (spaces or tabs) MUST separate each *checksum* from each *filepath*.
- Each line of the `manifest-md5.txt` file MUST be terminated with an LF, a CR or a CRLF.

## bagit.txt (file)

The `bagit.txt` file contains exactly two lines in the exact order specified in the example below.
The first line specifies to which version of the [BagIt specification](https://www.rfc-editor.org/rfc/rfc8493.html) the bag conforms, while the second line identifies the character set encoding of the bag and its files.

***Example***

```plaintext
BagIt-Version: 1.0
Tag-File-Character-Encoding: UTF-8
```

***Requirements***

- The first line of the `bagit.txt` file MUST specify the exact version of the BagIt standard. The version MUST be 0.97 or later.
- The second line of the `bagit.txt` file MUST specify the character set encoding of the bag and its files. This encoding MUST be UTF-8.

## /data (directory)

The `/data` directory contains the content of the bag divided across a number of different files and directories.
Each `/data` directory MUST contain exactly one package, consisting of the combination of a `mets.xml` file, a `/metadata` directory and a `/representations` directory.
See the [package level]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/sip_structure/5_structure_package.md %}) for more information and the requirements of the `/data` directory.

***Example***

```plaintext
root_directory
│   ...
│
└──data
   │──mets.xml
   │
   │──metadata
   │      ...
   │──representations
   │      ...
```

<small>
Continue to [package level]({{ site.baseurl }}{% link docs/diginstroom/sip/1.0/sip_structure/5_structure_package.md %}).
</small>
