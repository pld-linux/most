Summary:	SLang based pager
Summary(pl):	Bazuj±cy na SLang'u pager
Name:		most
Version:	4.9.0
Release:	1
Copyright:	GPL
Group:		Utilities/Text
Source:		ftp://space.mit.edu/pub/davis/most/test/%{name}-%{version}.tar.gz
URL:		http://space.mit.edu/~davis/most.html
BuildPrereq:	slang-devel >= 1.3.6
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Most is a pager (like less & more). Allows, amongst other, the viewing of 
multiple files and on-the-fly uncompressing.

%description -l pl
Most jest pagerr'em (jak less czy more). Umo¿liwia tak jak inne programy
tego typu przegl±danie wielu plików jednocze¶nie i dekompresj±c tak¿e pliki
przed rzpoczêciem przegl±dania.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-s" \
./configure %{_target} \
	--prefix=%{_prefix}

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
* Fri May 21 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.9.0-2]
- now package is FHS 2.0 compliant,
- added BuildPrereq rules,
- added gzipping %doc and man pages,
- added /etc/most.conf %config file,
- added using more macros.

* Fri Aug 28 1998 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [4.8.1-1]
- %%{version} macro instead %%{PACKAGE_VERSION},
- added LDFLAGS=-s (for dynamic linking with slang),
- added pl translation,
- added -q %setup parameter,
- added using %%{name} macro in Buildroot and Source,

* Sat Sep 20 1997 Tomasz K³oczko <kloczek@idk.com.pl>
  [4.8-1]
- removed macro %version,
- removed "Requires: slang",
- added %attr macros in %files (allows build package from non root account),

* Mon Jul 14 1997 Manoj Kasichainula <manojk@io.com>
  [4.7-1]
- Initial release for 4.7.
