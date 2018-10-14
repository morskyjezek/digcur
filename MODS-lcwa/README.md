# LCWA MODS

_*NB:* This was forked into its own repo for distribution to a Library Carpentry workshop in September 2018: https://github.com/morskyjezek/LCWA-MODS._

This folder has a python notebook with information about downloading
[MODS](http://www.loc.gov/standards/mods/) records for use as sample data to
practice parsing XML in python. These sample files were generated in August of
2018 from MODS metadata records for archived Web sites collected by the Library
of Congress:

These are newer MODS records that don't have LCSH:
```
lcwaN0010234,lcwaN0001999,lcwaN0003238,lcwaN0010144,lcwaN0010145,
lcwaN0012178,lcwaN0012179,lcwaN0012180,lcwaN0012184,lcwaN0012195,
lcwaN0010932,lcwaN0010933,lcwaN0010936,lcwaN0010937,lcwaN0010940,
```

These have LCSH in `<subject>`:

`lcwaN0010888,lcwaN0010226,lcwaN0009692,lcwaN0009700,lcwaN0010401`

These are election sites that include `<subject>` with both [lcsh](https://en.wikipedia.org/wiki/LCSH)
and "local" headings noted as "lcwat", which represent a taxonomy that was
developed for the quick categorization of sites during the nomination and
harvesting process:
`lcwaE0008846,lcwaE0008263,lcwaE0008338,lcwaE0008918,lcwaE0008001`
