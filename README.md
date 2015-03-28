# Webservice til at udtrække studiebeskeder fra KUs intranet

Denne tjeneste udtrækker studiebeskedsmetadata.


# Installationsguide

## Afhængigheder

* Perl og nogle pakker fra CPAN
* Python
* Shell


## Installation

1. Kør `cpan -i LWP::Protocol::https FindBin HTML::Query IO::All WWW::Mechanize`.
2. Opret filen `.ku_credentials`, og skriv `<ku_brugernavn>:<ku_løsen>` i den.
3. Sæt et eller andet op (fx cron) der kører `gen_all.sh` en gang i mellem.
4. Sæt en eller anden webserver op der kører `serve_json.sh` og `serve_html.sh`.
