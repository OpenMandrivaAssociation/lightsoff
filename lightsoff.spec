%define url_ver	%(echo %{version}|cut -d. -f1,2)
%define _disable_rebuild_configure 1

Name:		lightsoff
Version:	3.34.0
Release:	1
Summary:	GNOME Lightsoff game
License:	GPLv2+ and CC-BY-SA
Group:		Games/Puzzles
URL:		https://wiki.gnome.org/Lightsoff
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(clutter-1.0) >= 1.0.0
BuildRequires:	pkgconfig(clutter-gtk-1.0) >= 1.0.0
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:	pkgconfig(librsvg-2.0)
BuildRequires:	pkgconfig(vapigen)
BuildRequires:	intltool
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	meson
BuildRequires:	appstream-util
# For fix build issue:  "error: Package `librsvg-2.0' not found in specified Vala API directories or GObject-Introspection GIR directories" (penguin)
BuildRequires:  librsvg-vala-devel
# For help
Requires:	yelp

%description
A puzzle played on an 5X5 grid with the aim to turn off all the lights. Each
click on a tile toggles the state of the clicked tile and its non-diagonal
neighbors.

%prep
%setup -q

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.LightsOff.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.LightsOff.gschema.xml
%{_iconsdir}/*/*/apps/org.gnome.LightsOff.*
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.LightsOff-symbolic.svg
%{_datadir}/%{name}
%{_datadir}/metainfo/org.gnome.LightsOff.appdata.xml
