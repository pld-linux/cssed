%define	rel	1
Summary:	CSS editor for web developers
Summary(pl):	Edytor CSS dla programistów stron
Name:		cssed
Version:	pre0.1
Release:	1
Group:		Development/Tools
License:	GPL
Source0:	http://dl.sourceforge.net/%{name}/%{name}-%{version}-%{rel}.tar.gz
# Source0-md5:	154d808510e19566ab49d1f58749494e
Patch0:		%{name}-opt.patch
URL:		http://cssed.sourceforge.net
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libgnomeui-devel >= 2.0
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
%patch0 -p1

%build
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/cssed
%{_datadir}/%{name}
%{_pixmapsdir}/%{name}-icon.png
%{_desktopdir}/%{name}.desktop
