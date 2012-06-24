Summary:	SLang based pager
Summary(pl):	Bazuj�cy na SLang'u pager
Name:		most
Version:	4.9.0
Release:	2
Copyright:	GPL
Group:		Utilities/Text
Group(pl):	Narz�dzia/Tekst
Source:		ftp://space.mit.edu/pub/davis/most/test/%{name}-%{version}.tar.gz
URL:		http://space.mit.edu/~davis/most.html
BuildPrereq:	slang-devel >= 1.3.6
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Most is a pager (like less & more). Allows, amongst other, the viewing of 
multiple files and on-the-fly uncompressing.

%description -l pl
Most jest pagerr'em (jak less czy more). Umo�liwia tak jak inne programy
tego typu przegl�danie wielu plik�w jednocze�nie i dekompresj�c tak�e pliki
przed rzpocz�ciem przegl�dania.

%prep
%setup -q

%build
LDFLAGS="-s"; export LDFLAGS
%configure

make SYS_INITFILE=/etc/most.conf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/etc,%{_bindir},%{_mandir}/man1,%{_datadir}/%{name}}

make install \
	BIN_DIR=$RPM_BUILD_ROOT%{_bindir} \
	MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	DOC_DIR=$RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}

install lesskeys.rc $RPM_BUILD_ROOT/etc/most.conf

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README *.rc *.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz
%config /etc/most.conf
%attr(755,root,root) %{_bindir}/most
%{_mandir}/man1/*

%changelog
* Fri Jun 25 1999 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.9.0-2]
- based on RH spec,
- spec rewrited by PLD team.
