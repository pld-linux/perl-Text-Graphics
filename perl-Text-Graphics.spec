%include	/usr/lib/rpm/macros.perl
Summary:	Text-Graphics perl module
Summary(pl):	Modu³ perla Text-Graphics
Name:		perl-Text-Graphics
Version:	1.0001
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-Graphics-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-Text-Wrapper
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Text-Graphics - a text graphics rendering toolkit.

%description -l pl
Text-Graphics - zestaw narzêdzi do renderowania grafiki tekstowej.

%prep
%setup -q -n Text-Graphics-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Text/Graphics
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz

%{perl_sitelib}/Text/Graphics.pm
%{perl_sitearch}/auto/Text/Graphics

%{_mandir}/man3/*
