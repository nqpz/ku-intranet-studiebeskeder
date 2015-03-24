# Installationsguide

## Prerequisites

* Perl
* nginx
* uwsgi

## Installation

1. Vælg et passende subdomæne. (`<subdomain>` i resten af dokumentet.)
1. Check repo'et ud til `/srv/<subdomain>`
1. Kør: `cpan -i CHI Digest::SHA FindBin HTML::Query IO::All Mojolicious WWW::Mechanize`
1. Opret mappen `/var/run/web/`:

        sudo mkdir /var/run/web
        sudo chown www-data:www-data /var/run/web
        sudo chmod 0755 /var/run/web

1. Opret filen `.ku_credentials`, og skriv `<ku_brugernavn>:<ku_løsen>` i den.
1. Ret `nginx_config` så `hostname.her.dk` erstattes med `<subdomain>`.
1. Kopier `nginx_config` over i `/etc/nginx/sites-enabled/<subdomain>`.
1. Ret `uwsgi_config.yaml`, så `hostname.her.dk` erstattes med `<subdomain>`.
1. Kopier `uwsgi_config.yaml` over i `/etc/uwsgi/apps-enabled/<subdomain>.yaml`.
1. Genstart uwsgi med `sudo service uwsgi restart`.
1. Genstart nginx med `sudo service nginx restart`.
1. Håb på at jeg ikke har glemt et skridt i denne guide.
