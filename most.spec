Summary:	SLang based pager
Summary(pl):	Bazujący na SLang'u pager
Name:		most
Version:	4.9.4
Release:	1
License:	GPL
Group:		Applications/Text
Source0:	ftp://space.mit.edu/pub/davis/most/%{name}-%{version}.tar.bz2
# Source0-md5:	97b32c74dd32ee259b2b4abb540d32b2
URL:		http://space.mit.edu/~davis/most.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	slang-devel >= 1.3.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Most is a pager (like less & more). Allows, amongst other, the viewing
of multiple files and on-the-fly uncompressing.

%description -l pl
Most jest pager'em (jak less czy more). Umożliwia tak jak inne
programy tego typu przeglądanie wielu plików jednocześnie i
dekompresjąc także pliki przed rzpoczęciem przeglądania.

%prep
%setup -q

%build
cp -f autoconf/configure.in .
cp -f autoconf/aclocal.m4 acinclude.m4
%{__aclocal}
%{__autoconf}
%configure \
	--disable-warnings

%{__make} SYS_INITFILE=%{_sysconfdir}/most.conf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_mandir}/man1,%{_datadir}/%{name}}

%{__make} install \
	BIN_DIR=$RPM_BUILD_ROOT%{_bindir} \
	MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	DOC_DIR=$RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}

install lesskeys.rc $RPM_BUILD_ROOT%{_sysconfdir}/most.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README *.rc *.txt
%config %{_sysconfdir}/most.conf
%attr(755,root,root) %{_bindir}/most
%{_mandir}/man1/*
