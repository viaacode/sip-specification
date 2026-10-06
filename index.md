---
title:        "1.0"
nav_order:    5
---
# meemoo Submission Information Package (SIP) Specification

**Permalink:** <https://data.hetarchief.be/id/sip/1.0>

<b>Status:</b> <span class="label label-red">Retired</span>

**Version:** [1.0](index.md)

**Previous version:** N/A

**Published:** 2022-09-30

**Publisher:** [meemoo.be](http://meemoo.be)

**Alternate formats:** [Web pages](index.md)<!--, [single-page HTML](), [PDF]()-->

**Editors:** [Milan Valadou](mailto:milan.valadou@meemoo.be), [Bert Lemmens](mailto:bert.lemmens@meemoo.be), [Miel Vander Sande](mailto:miel.vandersande@meemoo.be)

**Contributors:** [Maarten De Schrijver](mailto:maarten.deschrijver@meemoo.be), [Mattias Poppe](mailto:mattias.poppe@meemoo.be)

<small>
This specification is © 2022 [meemoo vzw](http://meemoo.be) and the meemoo SIP contributors.
</small>

<small>
Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at <http://www.apache.org/licenses/LICENSE-2.0>
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
</small>

<small>
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in [BCP 14](https://www.rfc-editor.org/info/bcp14) [[RFC2119]](https://datatracker.ietf.org/doc/html/rfc2119) [[RFC8174]](https://datatracker.ietf.org/doc/html/rfc8174) when, and only when, they appear in all capitals, as shown here.
</small>

!!! important
    Except sections explicitly marked as informative, all guidelines, examples and notes in this specification are to be considered normative.


## Abstract

The meemoo Submission Information Package (henceforth SIP) specification describes how data and metadata should be packaged when delivered to meemoo for ingest.
It serves as a generic base for content-specific profiles for the ingest of specific use-cases (e.g. a single media file with accompanying metadata, newspapers, 3D objects etc.).
