Summary:	SLang based pager
Summary(pl):	Bazuj±cy na SLang'u pager
Name:		most
Version:	4.9.2
Release:	1
License:	GPL
Group:		Applications/Text
Group(de):	Applikationen/Text
Group(fr):	Utilitaires/Texte
Group(pl):	Aplikacje/Tekst
Source0:	ftp://space.mit.edu/pub/davis/most/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_fixes.patch
URL:		http://space.mit.edu/~davis/most.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	slang-devel >= 1.3.6
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Most is a pager (like less & more). Allows, amongst other, the viewing
of multiple files and on-the-fly uncompressing.

%description -l pl
Most jest pager'em (jak less czy more). Umo¿liwia tak jak inne
programy tego typu przegl±danie wielu plików jednocze¶nie i
dekompresj±c tak¿e pliki przed rzpoczêciem przegl±dania.

%prep
%setup -q
%patch0 -p1

%build
aclocal
autoconf
automake -a -c || :
%configure \
	--disable-warnings

%{__make} SYS_INITFILE=/etc/most.conf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_bindir},%{_mandir}/man1,%{_datadir}/%{name}}

%{__make} install \
	BIN_DIR=$RPM_BUILD_ROOT%{_bindir} \
	MAN_DIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	DOC_DIR=$RPM_BUILD_ROOT%{_defaultdocdir}/%{name}-%{version}

install lesskeys.rc $RPM_BUILD_ROOT%{_sysconfdir}/most.conf

gzip -9nf README *.rc *.txt

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *gz
%config %{_sysconfdir}/most.conf
%attr(755,root,root) %{_bindir}/most
%{_mandir}/man1/*
