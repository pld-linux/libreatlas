Summary:	Geography Education application built on top of SpatiaLite and RasterLite
Summary(pl.UTF-8):	Geograficzny program edukacyjny stworzony w oparciu o SpatiaLite i RasterLite
Name:		libreatlas
Version:	1.0.0a
Release:	6
License:	GPL v3+
Group:		Applications
Source0:	http://www.gaia-gis.it/gaia-sins/libreatlas-sources/%{name}-%{version}.tar.gz
# Source0-md5:	d09d57d2cbb0b05be0e3ff9ad925d86a
Patch0:		%{name}-link.patch
Patch1:		wxWidgets3.patch
URL:		https://www.gaia-gis.it/fossil/libreatlas
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake
BuildRequires:	freexl-devel
BuildRequires:	geos-devel
BuildRequires:	libgeotiff-devel >= 1.2.5
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	librasterlite-devel
BuildRequires:	libspatialite-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtiff-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	pkgconfig
BuildRequires:	proj-devel >= 4
BuildRequires:	wxGTK2-unicode-devel >= 2.8.12-4
BuildRequires:	zlib-devel
Requires:	libgeotiff-devel >= 1.2.5
Requires:	wxGTK2-unicode >= 2.8.12-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LibreAtlas is an open source Geography Education application built on
top of SpatiaLite and RasterLite. It uses LibreAtlas databases which
are a digital alternative to a paper atlas.

%description -l pl.UTF-8
LibreAtlas to mający otwarte źródła geograficzny program edukacyjny,
stworzony w oparciu o SpatiaLite i RasterLite. Wykorzystuje bazy
danych LibreAtlas, będące cyfrową alternatywą dla atlasu papierowego.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

mkdir wx-bin
ln -sf /usr/bin/wx-gtk2-unicode-config wx-bin/wx-config

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
# configure refers to wx-config with no option to override
PATH=$(pwd)/wx-bin:$PATH
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}
sed -ne '2,$p' gnome_resource/LibreAtlas.desktop >$RPM_BUILD_ROOT%{_desktopdir}/LibreAtlas.desktop
cp -p gnome_resource/LibreAtlas.png $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/LibreAtlas
%{_desktopdir}/LibreAtlas.desktop
%{_pixmapsdir}/LibreAtlas.png
