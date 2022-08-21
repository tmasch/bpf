# bpf
Berthold's picture finder

WORK IN PROGRESS


submitted to the 9th International Conference for Art Libraries | October 14 and 15, 2022

https://www.zikg.eu/aktuelles/nachrichten/call-for-paper-art-information-reflection-and-the-future

Author: Dr. Berthold Kreß https://www.sustb-augsburg.de/ueber-uns/abteilungen-und-mitarbeiter/

Abstract:

This paper proposes a new concept for a database describing iconography, especially of illustrations of
manuscripts and printed books. Since about 2000, numerous manuscripts and rare books – for instance,
nearly two thirds of all books published in German-speaking countries in the 16 th century – have been
made fully available in digital format. The near-universal introduction of IIIF has facilitated handling this
material.

At first, digitisation was paralleled in some places with cataloguing images (e.g., Mandragore by the BnF),
but soon these projects were, as it seems, overwhelmed by the sheer numbers. Whilst models such as
CIDOC-CRM provide sophisticated structures to describe e.g. provenances, comparatively little work has
been dedicated to iconography. Most databases merely use free or standardised tags. Often, several tags
are necessary to describe an image. Great care is necessary to maintain consistency of the entries, virtually
ruling out employing students or volunteers. Connecting to a hierarchical system such as Iconclass or the
(more flexible) Warburg Institute Iconographic Database will facilitate consistency and allow for browsing
related subjects, but assigning to every complex subject-matter the one correct place in a hierarchical tree
can be problematic.

I became interested in iconographic classification through cataloguing manuscript and book illustrations in
the Warburg Database – inter alia over 70 manuscripts and incunables of the Speculum Humanae Salvationis,
the most popular late-Medieval ‘picture book’, and all digitised books printed before 1520 in Erfurt. In my
MA LIS thesis (Berlin, 2020, published in the Berliner Handreichungen, 480) I compared approaches to
cataloguing illustrations made suggestions for new data models. Based on it, I would like to offer two
concepts that might help overcome the difficulties described above.

The first is a data model that would expand the ‘iconographic tree’ of the Warburg Database into a
‘thicket’, allowing for a plurality of ways of browsing. Instead of a sequence of units and subunits it would
have ‘Iconography Records’ (for instance ‘Murder of Julius Caesar’) linked through the predicate ‘acting
person’ to ‘Person records’ of ‘Caesar’, ‘Brutus’, and ‘Cassius’, but likewise, if desired, through other
predicates to a ‘Place Record’ for ‘Rome’, or an ‘Action Record’ for ‘Assassination’. These records would
then be joined under different headings such as ‘Person from Ancient History’. When assigning to an
image an Iconography of which variants exists such different attributes of a personification, a checklist for
the hitherto recorded options would appear, prompting to choose the appropriate ones – and in turn
allowing the search for personifications with specific combinations of attributes.

The second element is an ingest module, a prototype of which has been devised following my suggestions
by Dr. Thomas Maschberger (Bonn). Instead of manually creating records for all illustrations, one would
input the URIs of IIIF manifests of a number of books. The module would download the individual
pages, cut out what it recognises as images, and connect them with metadata extracted from the manifest.
Users could correct the selections and add missing metadata in a review mode before exporting the
material into a database.

I studied History of Art in Munich (with Karl-August Wirth) and Cambridge, where my PhD on 16 th -
centruy diagrams was supervised by Jean Michel Massing. After several postdocs in Cambridge, I worked
in the Warburg Institute Photographic Collection before becoming a Volontär at Erfurt University
Library. Currently, I am Deputy Director of the Staats- und Stadtbibliothek Augsburg (my research on
cataloguing images is not connected to my work in Augsburg).
