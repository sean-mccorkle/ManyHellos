package ManyHellos::ManyHellosClient;

use JSON::RPC::Client;
use POSIX;
use strict;
use Data::Dumper;
use URI;
use Bio::KBase::Exceptions;
my $get_time = sub { time, 0 };
eval {
    require Time::HiRes;
    $get_time = sub { Time::HiRes::gettimeofday() };
};

use Bio::KBase::AuthToken;

# Client version should match Impl version
# This is a Semantic Version number,
# http://semver.org
our $VERSION = "0.1.0";

=head1 NAME

ManyHellos::ManyHellosClient

=head1 DESCRIPTION


This is a single-language prototype for parallel subjob execution.  All this
does is run several "hello world" programs.


=cut

sub new
{
    my($class, $url, @args) = @_;
    

    my $self = {
	client => ManyHellos::ManyHellosClient::RpcClient->new,
	url => $url,
	headers => [],
    };

    chomp($self->{hostname} = `hostname`);
    $self->{hostname} ||= 'unknown-host';

    #
    # Set up for propagating KBRPC_TAG and KBRPC_METADATA environment variables through
    # to invoked services. If these values are not set, we create a new tag
    # and a metadata field with basic information about the invoking script.
    #
    if ($ENV{KBRPC_TAG})
    {
	$self->{kbrpc_tag} = $ENV{KBRPC_TAG};
    }
    else
    {
	my ($t, $us) = &$get_time();
	$us = sprintf("%06d", $us);
	my $ts = strftime("%Y-%m-%dT%H:%M:%S.${us}Z", gmtime $t);
	$self->{kbrpc_tag} = "C:$0:$self->{hostname}:$$:$ts";
    }
    push(@{$self->{headers}}, 'Kbrpc-Tag', $self->{kbrpc_tag});

    if ($ENV{KBRPC_METADATA})
    {
	$self->{kbrpc_metadata} = $ENV{KBRPC_METADATA};
	push(@{$self->{headers}}, 'Kbrpc-Metadata', $self->{kbrpc_metadata});
    }

    if ($ENV{KBRPC_ERROR_DEST})
    {
	$self->{kbrpc_error_dest} = $ENV{KBRPC_ERROR_DEST};
	push(@{$self->{headers}}, 'Kbrpc-Errordest', $self->{kbrpc_error_dest});
    }

    #
    # This module requires authentication.
    #
    # We create an auth token, passing through the arguments that we were (hopefully) given.

    {
	my $token = Bio::KBase::AuthToken->new(@args);
	
	if (!$token->error_message)
	{
	    $self->{token} = $token->token;
	    $self->{client}->{token} = $token->token;
	}
        else
        {
	    #
	    # All methods in this module require authentication. In this case, if we
	    # don't have a token, we can't continue.
	    #
	    die "Authentication failed: " . $token->error_message;
	}
    }

    my $ua = $self->{client}->ua;	 
    my $timeout = $ENV{CDMI_TIMEOUT} || (30 * 60);	 
    $ua->timeout($timeout);
    bless $self, $class;
    #    $self->_validate_version();
    return $self;
}




=head2 manyHellos

  $output_obj = $obj->manyHellos($input_params)

=over 4

=item Parameter and return types

=begin html

<pre>
$input_params is a ManyHellos.ManyHellosInputParams
$output_obj is a ManyHellos.ManyHellosOutputObj
ManyHellosInputParams is a reference to a hash where the following keys are defined:
	hello_msg has a value which is a string
	num_jobs has a value which is an int
	time_limit has a value which is an int
ManyHellosOutputObj is a string

</pre>

=end html

=begin text

$input_params is a ManyHellos.ManyHellosInputParams
$output_obj is a ManyHellos.ManyHellosOutputObj
ManyHellosInputParams is a reference to a hash where the following keys are defined:
	hello_msg has a value which is a string
	num_jobs has a value which is an int
	time_limit has a value which is an int
ManyHellosOutputObj is a string


=end text

=item Description



=back

=cut

 sub manyHellos
{
    my($self, @args) = @_;

# Authentication: required

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function manyHellos (received $n, expecting 1)");
    }
    {
	my($input_params) = @args;

	my @_bad_arguments;
        (ref($input_params) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument 1 \"input_params\" (value was \"$input_params\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to manyHellos:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'manyHellos');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "ManyHellos.manyHellos",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'manyHellos',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method manyHellos",
					    status_line => $self->{client}->status_line,
					    method_name => 'manyHellos',
				       );
    }
}
 


=head2 manyHellos_prepare

  $res = $obj->manyHellos_prepare($input_params)

=over 4

=item Parameter and return types

=begin html

<pre>
$input_params is a ManyHellos.ManyHellos_prepareInputParams
$res is a ManyHellos.ManyHellos_prepareResult
ManyHellos_prepareInputParams is a reference to a hash where the following keys are defined:
	num_jobs has a value which is an int
ManyHellos_prepareResult is a string

</pre>

=end html

=begin text

$input_params is a ManyHellos.ManyHellos_prepareInputParams
$res is a ManyHellos.ManyHellos_prepareResult
ManyHellos_prepareInputParams is a reference to a hash where the following keys are defined:
	num_jobs has a value which is an int
ManyHellos_prepareResult is a string


=end text

=item Description



=back

=cut

 sub manyHellos_prepare
{
    my($self, @args) = @_;

# Authentication: required

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function manyHellos_prepare (received $n, expecting 1)");
    }
    {
	my($input_params) = @args;

	my @_bad_arguments;
        (ref($input_params) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument 1 \"input_params\" (value was \"$input_params\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to manyHellos_prepare:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'manyHellos_prepare');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "ManyHellos.manyHellos_prepare",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'manyHellos_prepare',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method manyHellos_prepare",
					    status_line => $self->{client}->status_line,
					    method_name => 'manyHellos_prepare',
				       );
    }
}
 


=head2 manyHellos_runEach

  $res = $obj->manyHellos_runEach($input_params)

=over 4

=item Parameter and return types

=begin html

<pre>
$input_params is a ManyHellos.ManyHellos_runEachInputParams
$res is a ManyHellos.ManyHellos_runEachResult
ManyHellos_runEachInputParams is a reference to a hash where the following keys are defined:
	num_jobs has a value which is an int
ManyHellos_runEachResult is a string

</pre>

=end html

=begin text

$input_params is a ManyHellos.ManyHellos_runEachInputParams
$res is a ManyHellos.ManyHellos_runEachResult
ManyHellos_runEachInputParams is a reference to a hash where the following keys are defined:
	num_jobs has a value which is an int
ManyHellos_runEachResult is a string


=end text

=item Description



=back

=cut

 sub manyHellos_runEach
{
    my($self, @args) = @_;

# Authentication: required

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function manyHellos_runEach (received $n, expecting 1)");
    }
    {
	my($input_params) = @args;

	my @_bad_arguments;
        (ref($input_params) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument 1 \"input_params\" (value was \"$input_params\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to manyHellos_runEach:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'manyHellos_runEach');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "ManyHellos.manyHellos_runEach",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'manyHellos_runEach',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method manyHellos_runEach",
					    status_line => $self->{client}->status_line,
					    method_name => 'manyHellos_runEach',
				       );
    }
}
 


=head2 manyHellos_collect

  $res = $obj->manyHellos_collect($input_params)

=over 4

=item Parameter and return types

=begin html

<pre>
$input_params is a ManyHellos.ManyHellos_collectInputParams
$res is a ManyHellos.ManyHellos_collectResult
ManyHellos_collectInputParams is a reference to a hash where the following keys are defined:
	num_jobs has a value which is an int
ManyHellos_collectResult is a string

</pre>

=end html

=begin text

$input_params is a ManyHellos.ManyHellos_collectInputParams
$res is a ManyHellos.ManyHellos_collectResult
ManyHellos_collectInputParams is a reference to a hash where the following keys are defined:
	num_jobs has a value which is an int
ManyHellos_collectResult is a string


=end text

=item Description



=back

=cut

 sub manyHellos_collect
{
    my($self, @args) = @_;

# Authentication: required

    if ((my $n = @args) != 1)
    {
	Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
							       "Invalid argument count for function manyHellos_collect (received $n, expecting 1)");
    }
    {
	my($input_params) = @args;

	my @_bad_arguments;
        (ref($input_params) eq 'HASH') or push(@_bad_arguments, "Invalid type for argument 1 \"input_params\" (value was \"$input_params\")");
        if (@_bad_arguments) {
	    my $msg = "Invalid arguments passed to manyHellos_collect:\n" . join("", map { "\t$_\n" } @_bad_arguments);
	    Bio::KBase::Exceptions::ArgumentValidationError->throw(error => $msg,
								   method_name => 'manyHellos_collect');
	}
    }

    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
	    method => "ManyHellos.manyHellos_collect",
	    params => \@args,
    });
    if ($result) {
	if ($result->is_error) {
	    Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
					       code => $result->content->{error}->{code},
					       method_name => 'manyHellos_collect',
					       data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
					      );
	} else {
	    return wantarray ? @{$result->result} : $result->result->[0];
	}
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method manyHellos_collect",
					    status_line => $self->{client}->status_line,
					    method_name => 'manyHellos_collect',
				       );
    }
}
 
  
sub status
{
    my($self, @args) = @_;
    if ((my $n = @args) != 0) {
        Bio::KBase::Exceptions::ArgumentValidationError->throw(error =>
                                   "Invalid argument count for function status (received $n, expecting 0)");
    }
    my $url = $self->{url};
    my $result = $self->{client}->call($url, $self->{headers}, {
        method => "ManyHellos.status",
        params => \@args,
    });
    if ($result) {
        if ($result->is_error) {
            Bio::KBase::Exceptions::JSONRPC->throw(error => $result->error_message,
                           code => $result->content->{error}->{code},
                           method_name => 'status',
                           data => $result->content->{error}->{error} # JSON::RPC::ReturnObject only supports JSONRPC 1.1 or 1.O
                          );
        } else {
            return wantarray ? @{$result->result} : $result->result->[0];
        }
    } else {
        Bio::KBase::Exceptions::HTTP->throw(error => "Error invoking method status",
                        status_line => $self->{client}->status_line,
                        method_name => 'status',
                       );
    }
}
   

sub version {
    my ($self) = @_;
    my $result = $self->{client}->call($self->{url}, $self->{headers}, {
        method => "ManyHellos.version",
        params => [],
    });
    if ($result) {
        if ($result->is_error) {
            Bio::KBase::Exceptions::JSONRPC->throw(
                error => $result->error_message,
                code => $result->content->{code},
                method_name => 'manyHellos_collect',
            );
        } else {
            return wantarray ? @{$result->result} : $result->result->[0];
        }
    } else {
        Bio::KBase::Exceptions::HTTP->throw(
            error => "Error invoking method manyHellos_collect",
            status_line => $self->{client}->status_line,
            method_name => 'manyHellos_collect',
        );
    }
}

sub _validate_version {
    my ($self) = @_;
    my $svr_version = $self->version();
    my $client_version = $VERSION;
    my ($cMajor, $cMinor) = split(/\./, $client_version);
    my ($sMajor, $sMinor) = split(/\./, $svr_version);
    if ($sMajor != $cMajor) {
        Bio::KBase::Exceptions::ClientServerIncompatible->throw(
            error => "Major version numbers differ.",
            server_version => $svr_version,
            client_version => $client_version
        );
    }
    if ($sMinor < $cMinor) {
        Bio::KBase::Exceptions::ClientServerIncompatible->throw(
            error => "Client minor version greater than Server minor version.",
            server_version => $svr_version,
            client_version => $client_version
        );
    }
    if ($sMinor > $cMinor) {
        warn "New client version available for ManyHellos::ManyHellosClient\n";
    }
    if ($sMajor == 0) {
        warn "ManyHellos::ManyHellosClient version is $svr_version. API subject to change.\n";
    }
}

=head1 TYPES



=head2 ManyHellosInputParams

=over 4



=item Description

Main service call:  manyHellos()


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
hello_msg has a value which is a string
num_jobs has a value which is an int
time_limit has a value which is an int

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
hello_msg has a value which is a string
num_jobs has a value which is an int
time_limit has a value which is an int


=end text

=back



=head2 ManyHellosOutputObj

=over 4



=item Definition

=begin html

<pre>
a string
</pre>

=end html

=begin text

a string

=end text

=back



=head2 ManyHellos_prepareInputParams

=over 4



=item Description

prepare()


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
num_jobs has a value which is an int

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
num_jobs has a value which is an int


=end text

=back



=head2 ManyHellos_prepareResult

=over 4



=item Definition

=begin html

<pre>
a string
</pre>

=end html

=begin text

a string

=end text

=back



=head2 ManyHellos_runEachInputParams

=over 4



=item Description

runEach()


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
num_jobs has a value which is an int

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
num_jobs has a value which is an int


=end text

=back



=head2 ManyHellos_runEachResult

=over 4



=item Definition

=begin html

<pre>
a string
</pre>

=end html

=begin text

a string

=end text

=back



=head2 ManyHellos_collectInputParams

=over 4



=item Description

collect()


=item Definition

=begin html

<pre>
a reference to a hash where the following keys are defined:
num_jobs has a value which is an int

</pre>

=end html

=begin text

a reference to a hash where the following keys are defined:
num_jobs has a value which is an int


=end text

=back



=head2 ManyHellos_collectResult

=over 4



=item Definition

=begin html

<pre>
a string
</pre>

=end html

=begin text

a string

=end text

=back



=cut

package ManyHellos::ManyHellosClient::RpcClient;
use base 'JSON::RPC::Client';
use POSIX;
use strict;

#
# Override JSON::RPC::Client::call because it doesn't handle error returns properly.
#

sub call {
    my ($self, $uri, $headers, $obj) = @_;
    my $result;


    {
	if ($uri =~ /\?/) {
	    $result = $self->_get($uri);
	}
	else {
	    Carp::croak "not hashref." unless (ref $obj eq 'HASH');
	    $result = $self->_post($uri, $headers, $obj);
	}

    }

    my $service = $obj->{method} =~ /^system\./ if ( $obj );

    $self->status_line($result->status_line);

    if ($result->is_success) {

        return unless($result->content); # notification?

        if ($service) {
            return JSON::RPC::ServiceObject->new($result, $self->json);
        }

        return JSON::RPC::ReturnObject->new($result, $self->json);
    }
    elsif ($result->content_type eq 'application/json')
    {
        return JSON::RPC::ReturnObject->new($result, $self->json);
    }
    else {
        return;
    }
}


sub _post {
    my ($self, $uri, $headers, $obj) = @_;
    my $json = $self->json;

    $obj->{version} ||= $self->{version} || '1.1';

    if ($obj->{version} eq '1.0') {
        delete $obj->{version};
        if (exists $obj->{id}) {
            $self->id($obj->{id}) if ($obj->{id}); # if undef, it is notification.
        }
        else {
            $obj->{id} = $self->id || ($self->id('JSON::RPC::Client'));
        }
    }
    else {
        # $obj->{id} = $self->id if (defined $self->id);
	# Assign a random number to the id if one hasn't been set
	$obj->{id} = (defined $self->id) ? $self->id : substr(rand(),2);
    }

    my $content = $json->encode($obj);

    $self->ua->post(
        $uri,
        Content_Type   => $self->{content_type},
        Content        => $content,
        Accept         => 'application/json',
	@$headers,
	($self->{token} ? (Authorization => $self->{token}) : ()),
    );
}



1;
