Summary:	CSS editor for web developers
Summary(pl):	Edytor CSS dla programistów stron
Name:		cssed
Version:	0.4.0
Release:	1
Group:		Development/Tools
License:	GPL
Source0:	http://dl.sourceforge.net/cssed/%{name}-%{version}.tar.gz
# Source0-md5:	ff7c818d1f819b7d76b4f714be64e08e
Source1:	%{name}.desktop
URL:		http://cssed.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	vte-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cssed is a GTK+ CSS editor for web developers. It's not finished yet
and it's a beta release candidate only, but it's already a powerfull
CSS editor. cssed have features that allow any developer to speed his
coding as autocompletion or CSS syntax higlighting.

%description -l pl
cssed jest edytorem CSS opartym o GTK+ dla programistów stron WWW. Nie 
jest jeszcze ukoñczony i jest to tylko wersja beta, ale ju¿ pokazuje 
swoje potê¿ne mo¿liwo¶ci. Umo¿liwia miêdzy innymi przyspieszenie 
kodowania CSS przez autouzupe³nianie oraz pod¶wietlanie sk³adni CSS.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make} \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install pixmaps/%{name}-icon.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/%{name}-icon.png

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/cssed
%{_datadir}/%{name}
%{_pixmapsdir}/%{name}-icon.png
%{_desktopdir}/%{name}.desktop
%{_mandir}/man?/*
