Summary:	CSS editor for web developers
Summary(pl):	Edytor CSS dla programist�w stron
Name:		cssed
Version:	0.2.1
Release:	1
Group:		Development/Tools
License:	GPL
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
# Source0-md5:	dd799e6cdbb2ea6e9e13b0bf22af8493
URL:		http://cssed.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.0.0
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
cssed jest edytorem CSS opartym o GTK+ dla programist�w stron WWW. Nie 
jest jeszcze uko�czony i jest to tylko wersja beta, ale ju� pokazuje 
swoje pot�ne mo�liwo�ci. Umo�liwia mi�dzy innymi przyspieszenie 
kodowania CSS przez autouzupe�nianie oraz pod�wietlanie sk�adni CSS.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

install pixmaps/%{name}-icon.png \
	$RPM_BUILD_ROOT%{_pixmapsdir}/%{name}-icon.png

cat << EOF > $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
[Desktop Entry]
Name=Cssed
Comment=CSS editor
Exec=%{name}
Icon=%{name}-icon.png
Terminal=0
Type=Application
EOF

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
