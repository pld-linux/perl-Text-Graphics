#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Text
%define		pnam	Graphics
%include	/usr/lib/rpm/macros.perl
Summary:	Text::Graphics perl module
Summary(pl.UTF-8):	Moduł perla Text::Graphics
Name:		perl-Text-Graphics
Version:	1.0001
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d21ee64f6c8817934a038d14019930fa
URL:		http://search.cpan.org/dist/Text-Graphics/
BuildRequires:	perl-Text-Wrapper
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Graphics - a text graphics rendering toolkit.

%description -l pl.UTF-8
Text::Graphics - zestaw narzędzi do renderowania grafiki tekstowej.

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
%doc README
%{perl_vendorlib}/Text/Graphics.pm
%{_mandir}/man3/*
