#!/usr/bin/env perl
use 5.012;
use warnings;

use FindBin qw/$Bin/;
use HTML::Query qw/Query/;
use IO::All -utf8;
use WWW::Mechanize;
use JSON;

my ($USERNAME, $PASSWORD) = io("$Bin/.ku_credentials")->slurp =~ /^([^:]+):(.*)$/;

die(<<END) unless $USERNAME;
    Place a file named '.ku_credentials' in the folder you run the program from.
    In it, put username:password for intranet.ku.dk login.
END

my $mech = WWW::Mechanize->new();
$mech->agent_alias('Windows Mozilla');

sub login {
    if ($mech->uri->as_string =~ qr/CookieAuth\.dll/) {
        # Login page; we need to log in.

        $mech->submit_form(
            with_fields => {
                username => $USERNAME,
                password => $PASSWORD
            },
        );
    }
}

sub get_message_html {
    my $url = shift;
    $mech->get($url);
    my $q = Query( text => $mech->response->decoded_content );
    my $content = $q->query('.content')->first;
    return $content->as_HTML;
}

sub messages {
    $mech->get('https://intranet.ku.dk/nyheder/studiebeskeder/Sider/default.aspx');
    login();
    my $q = Query( text => $mech->response->decoded_content );
    my @news = $q->query('.NewsListing .NewsItem .NewsItemHeader')->get_elements;
    my $res = [];
    for my $item (@news) {
        $q = Query( $item );
        my $a = $q->query('.NewsItemTitle a')->first;
        my $title = $a->as_text;
        my $url = $a->attr('href');
        my $origin = $q->query('.NameDate')->first;
        my ($source, $date) = $origin->as_text =~ qr/[\s\n\r]*(.*?)[\s\n\r]*\|[\s\n\r]*(\d{2}-\d{2}-\d{4})/s;
        my $html = get_message_html($url);
        push( @$res, {
            title => $title,
            url => $url,
            source => $source,
            date => $date,
            html => $html
              } );
    }
    return $res;
}

print encode_json(messages());
