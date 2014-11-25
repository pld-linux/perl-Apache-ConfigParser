#
# Conditional build:
%bcond_without	tests	# don't perform "make test"

%define		pdir	Apache
%define		pnam	ConfigParser
%include	/usr/lib/rpm/macros.perl
Summary:	Apache::ConfigParser - load Apache configuration files
Summary(pl.UTF-8):	Apache::ConfigParser - wczytywanie plików konfiguracyjnych Apache'a
Name:		perl-Apache-ConfigParser
Version:	1.01
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2c1a863a2fc9d32313f277066bd9ea81
URL:		http://search.cpan.org/dist/Apache-ConfigParser/
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Test-Simple
BuildRequires:	perl-Tree-DAG_Node
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Apache::ConfigParser module is used to load an Apache
configuration file to allow programs to determine Apache's
configuration directives and contexts. The resulting object contains a
tree based structure using the Apache::ConfigParser::Directive class,
which is a subclass of Tree::DAG_node, so all of the methods that
enable tree based searches and modifications from Tree::DAG_Node are
also available. The tree structure is used to represent the ability to
nest sections, such as <VirtualHost>, <Directory>, etc.

%description -l pl.UTF-8
Moduł Apache::ConfigParser służy do odczytywania pliku
konfiguracyjnego Apache'a, pozwalając programom na określenie dyrektyw
konfiguracyjnych i ich kontekstu. Wynikowy obiekt zawiera strukturę
drzewiastą używającą klasy Apache::ConfigParser::Directive, która jest
podklasą Tree::DAG_Node, więc dostępne są także wszystkie metody z
Tree::DAG_Node, pozwalające na przeszukiwanie drzewa i modyfikowanie.
Struktura drzewiasta jest używana do reprezentowania możliwości
zagnieżdżania sekcji takich jak <VirtualHost>, <Directory> itp.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# get rid of pod docuementation
rm -f $RPM_BUILD_ROOT%{perl_vendorlib}/Apache/ConfigParser{,/}*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
