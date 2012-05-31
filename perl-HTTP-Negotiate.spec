#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	HTTP
%define		pnam	Negotiate
%include	/usr/lib/rpm/macros.perl
Summary:	HTTP::Negotiate - choose a variant to serve
Summary(pl.UTF-8):	HTTP::Negotiate - wybór wariantu do serwowania
Name:		perl-HTTP-Negotiate
Version:	6.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/HTTP/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1236195250e264d7436e7bb02031671b
URL:		http://search.cpan.org/dist/HTTP-Negotiate/
BuildRequires:	perl-devel >= 1:5.8.8
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTTP-Message >= 6
%endif
Requires:	perl-HTTP-Message >= 6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a complete implementation of the HTTP content
negotiation algorithm specified in draft-ietf-http-v11-spec-00.ps
chapter 12. Content negotiation allows for the selection of a
preferred content representation based upon attributes of the
negotiable variants and the value of the various Accept* header fields
in the request.

%description -l pl.UTF-8
Ten moduł udostepnia pełną implementację algorytmu negocjacji treści
HTTP opisanego w rozdziale 12 specyfikacji
draft-ietf-http-v11-spec-00.ps. Negocjacja treści pozwala na wybór
preferowanej reprezentacji treści w oparciu o atrybuty dostępnych
wariantów i wartości różnych pól nagłówków Accept* w żądaniu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/HTTP/Negotiate.pm
%{_mandir}/man3/HTTP::Negotiate.3pm*
