Summary:     SLang based pager
Summary(pl): Bazujący na SLang'u pager
Name:        most
Version:     4.8.1
Release:     1
Copyright:   GPL
Group:       Utilities/Text
URL:         http://space.mit.edu/~davis/most.html
Source:      ftp://space.mit.edu/pub/davis/most/test/%{name}%{version}.tar.gz
BuildRoot:   /tmp/%{name}-%{version}-build

%description
Most is a pager (like less & more). Allows, amongst other, the viewing of 
multiple files and on-the-fly uncompressing.

%description -l pl
Most jest pagerr'em (jak less czy more). Umożliwia tak jak inne programy
tego typu przeglądanie wielu plików jednocześnie i dekompresjąc także pliki
przed rzpoczęciem przeglądania.

%prep
%setup -q -n %{name}

%build
LDFLAGS="-s" CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target} \
	--prefix=/usr
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,man/man1}

make install	BIN_DIR=$RPM_BUILD_ROOT/usr/bin \
		MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(644, root, root) %doc README *.rc *.doc *.txt
%attr(755, root, root) /usr/bin/most
%{_mandir}/man1/most.1

%changelog
* Fri Aug 28 1998 Tomasz Kłoczko <kloczek@rudy.mif.pg.gda.pl>
  [4.8.1-1]
- %%{version} macro instead %%{PACKAGE_VERSION},
- added LDFLAGS=-s (for dynamic linking with slang),
- added pl translation,
- added -q %setup parameter,
- added using %%{name} macro in Buildroot and Source,

* Sat Sep 20 1997 Tomasz Kłoczko <kloczek@idk.com.pl>
  [4.8-1]
- removed macro %version,
- removed "Requires: slang",
- added %attr macros in %files (allows build package from non root account),

* Mon Jul 14 1997 Manoj Kasichainula <manojk@io.com>
  [4.7-1]
- Initial release for 4.7.
