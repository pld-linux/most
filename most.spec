Summary:	SLang based pager
Summary(pl):	Bazujący na SLang'u pager
Name:		most
Version:	4.9.5
Release:	3
License:	GPL
Group:		Applications/Text
Source0:	ftp://space.mit.edu/pub/davis/most/%{name}-%{version}.tar.bz2
# Source0-md5:	22e25b5351ce53524faa57745dd8a58c
URL:		http://www.jedsoft.org/most/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	slang-devel >= 1.3.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Most is a pager (like less & more). Allows, amongst other, the viewing
of multiple files and on-the-fly uncompressing.

%description -l pl
Most jest pagerem (jak less czy more). Umożliwia tak jak inne
programy tego typu przeglądanie wielu plików jednocześnie i
dekompresując także pliki przed rozpoczęciem przeglądania.

%prep
%setup -q

%{__perl} -pi -e 's@/usr/lib@/usr/%{_lib}@' autoconf/aclocal.m4

%build
cp -f /usr/share/automake/config.* autoconf
cp -f autoconf/configure.in .
cp -f autoconf/aclocal.m4 acinclude.m4
%{__aclocal}
%{__autoconf}
%configure \
	--disable-warnings

%{__make} \
	SYS_INITFILE=%{_sysconfdir}/most.conf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_mandir}/man1,%{_datadir}/%{name}}

%{__make} install \
	BIN_DIR=$RPM_BUILD_ROOT%{_bindir} \
	MAN_DIR=$RPM_BUILD_ROOT%{_mandir} \
	DOC_DIR=$RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}

install lesskeys.rc $RPM_BUILD_ROOT%{_sysconfdir}/most.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README *.rc *.txt
%config %{_sysconfdir}/most.conf
%attr(755,root,root) %{_bindir}/most
%{_mandir}/man1/*.1*
