#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	ConfigParser
Summary:	Apache::ConfigParser - load Apache configuration files
Summary(pl):	Apache::ConfigParser - wczytywanie plików konfiguracyjnych Apache'a
Name:		perl-Apache-ConfigParser
Version:	0.06
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3726cb960475e9153deef2ad6e203c3f
BuildRequires:	perl-devel >= 5.6
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

%description -l pl
Modu³ Apache::ConfigParser s³u¿y do odczytywania pliku
konfiguracyjnego Apache'a, pozwalaj±c programom na okre¶lenie dyrektyw
konfiguracyjnych i ich kontekstu. Wynikowy obiekt zawiera strukturê
drzewiast± u¿ywaj±c± klasy Apache::ConfigParser::Directive, która jest
podklas± Tree::DAG_Node, wiêc dostêpne s± tak¿e wszystkie metody z
Tree::DAG_Node, pozwalaj±ce na przeszukiwanie drzewa i modyfikowanie.
Struktura drzewiasta jest u¿ywana do reprezentowania mo¿liwo¶ci
zagnie¿d¿ania sekcji takich jak <VirtualHost>, <Directory> itp.

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
