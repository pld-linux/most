Summary:	SLang based pager
Summary(pl.UTF-8):	Pager bazujący na SLangu
Name:		most
Version:	5.2.0
Release:	2
License:	GPL v2+
Group:		Applications/Text
Source0:	http://www.jedsoft.org/releases/most/%{name}-%{version}.tar.gz
# Source0-md5:	13229d5d271c5058429c890f155adf45
Patch0:		%{name}-autoconf.patch
Patch1:		%{name}-no-strip.patch
URL:		http://www.jedsoft.org/most/
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	sed >= 4.0
BuildRequires:	slang-devel >= 1.3.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Most is a pager (like less & more). Allows, amongst other, the viewing
of multiple files and on-the-fly uncompressing.

%description -l pl.UTF-8
Most jest pagerem (jak less czy more). Umożliwia tak jak inne programy
tego typu przeglądanie wielu plików jednocześnie i dekompresując także
pliki przed rozpoczęciem przeglądania.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%{__sed} -i -e 's@%{_prefix}/lib@%{_prefix}/%{_lib}@' autoconf/aclocal.m4

%build
cp -f /usr/share/automake/config.* autoconf
cp -f autoconf/configure.ac .
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
	DOC_DIR=$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

cp -p doc/lesskeys.rc $RPM_BUILD_ROOT%{_sysconfdir}/most.conf

# clean docdir
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README changes.txt doc/most-fun.txt
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/most.conf
%attr(755,root,root) %{_bindir}/most
%{_mandir}/man1/most.1*
