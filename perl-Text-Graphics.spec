%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Graphics
Summary:	Text::Graphics perl module
Summary(pl):	Modu³ perla Text::Graphics
Name:		perl-Text-Graphics
Version:	1.0001
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	perl-Text-Wrapper
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Graphics - a text graphics rendering toolkit.

%description -l pl
Text::Graphics - zestaw narzêdzi do renderowania grafiki tekstowej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Text/Graphics.pm
%{_mandir}/man3/*
