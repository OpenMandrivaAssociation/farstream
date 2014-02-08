%define gstapi	1.0
%define api	0.2
%define major	2
%define libname	%mklibname %{name} %{api} %{major}
%define girname	%mklibname %{name}-gir %{api}
%define devname	%mklibname -d %{name}

Summary:	An audio/video communications framework
Name:		farstream
Version:	0.2.2
Release:	4
License:	LGPLv2+
Group:		Networking/Instant messaging
Url:		http://www.freedesktop.org/wiki/Software/Farstream
Source0:	http://freedesktop.org/software/farstream/releases/%{name}/%{name}-%{version}.tar.gz
Source1:	http://freedesktop.org/software/farstream/releases/%{name}/%{name}-%{version}.tar.gz.asc

BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gstreamer-%{gstapi})
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{gstapi})
BuildRequires:	pkgconfig(nice)

%description
The Farstream (formerly Farsight) project is an effort to create a framework to
deal with all known audio/video conferencing protocols. On one side it offers a
generic API that makes it possible to write plugins for different streaming
protocols, on the other side it offers an API for clients to use those plugins.

The main target clients for Farstream are Instant Messaging applications. These
applications should be able to use Farstream for all their Audio/Video
conferencing needs without having to worry about any of the lower level
streaming and NAT traversal issues.

%package -n %{libname}
Summary:	Farstream library
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
Shared libraries for %{name}.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package -n	gstreamer%{gstapi}-%{name}
Summary:	Set of plugins for GStreamer used Audio/Video conferencing
Group:		Sound
Requires:	gstreamer%{gstapi}-plugins-good
Requires:	gstreamer%{gstapi}-nice
Requires:	gstreamer%{gstapi}-voip

%description -n gstreamer%{gstapi}-%{name}
This is a set of plugins for GStreamer that will be used by Farstream
for Audio/Video conferencing.

%package -n %{devname}
Summary:	Headers of %name for development
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Requires:	%{girname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Headers of %{name} for development.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--enable-gupnp \
	--with-package-name="%{_vendor} %{name}" \
	--with-package-origin="http://openmandriva.org"

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/lib%{name}-%{api}.so.%{major}*
%{_libdir}/%{name}-%{api}/*.so

%files -n %{girname}
%{_libdir}/girepository-1.0/Farstream-%{api}.typelib

%files -n gstreamer%{gstapi}-%{name}
%{_libdir}/gstreamer-%{gstapi}/*.so
%{_datadir}/%{name}/%{api}/fsrtpconference/default-codec-preferences
%{_datadir}/%{name}/%{api}/fsrtpconference/default-element-properties
%{_datadir}/%{name}/%{api}/fsrawconference/default-element-properties

%files -n %{devname}
%doc ChangeLog
%doc %{_datadir}/gtk-doc/html/%{name}-libs-%{gstapi}/ 
%doc %{_datadir}/gtk-doc/html/%{name}-plugins-%{api}/
%{_includedir}/%{name}-%{api}/
%{_datadir}/gir-1.0/Farstream-%{api}.gir
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/lib%{name}-%{api}.so

