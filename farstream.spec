%define api		0.1
%define major		0
%define girmajor	0.1
%define libname		%mklibname %{name} %{api} %{major}
%define develname	%mklibname -d %{name}
%define girname		%mklibname %{name}-gir %{girmajor}

Summary:	An audio/video communications framework
Name:		farstream
Version:	0.1.2
Release:	%mkrel 1
License:	LGPLv2+
URL:		http://www.freedesktop.org/wiki/Software/Farstream
Group:		Networking/Instant messaging
Source0:  	http://freedesktop.org/software/farstream/releases/%{name}/%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10) >= 0.10.33
BuildRequires:	pkgconfig(nice) >= 0.1.0
BuildRequires:	pkgconfig(gst-python-0.10) >= 0.10.10
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(gobject-introspection-1.0)
# Added 04/2012 (wally)
Obsoletes:	farsight2

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
Provides: 	%{name} = %{version}-%{release}
Obsoletes:	%{_lib}farstream_0.1-0 < 0.1.1-2

%description -n %{libname}
Shared libraries for %{name}.

%package -n	gstreamer0.10-%{name}
Summary:	Set of plugins for GStreamer used Audio/Video conferencing
Group:		Sound
Requires:	%{libname} = %{version}-%{release}
Requires:	gstreamer0.10-plugins-good
Requires:	gstreamer0.10-nice >= 0.1.0
Requires:	gstreamer0.10-voip
# Added 04/2012 (wally)
Obsoletes:	gstreamer0.10-farsight2

%description -n gstreamer0.10-%{name}
This is a set of plugins for GStreamer that will be used by Farstream
for Audio/Video conferencing.

%package -n   	python-%{name}
Summary:	Python bindings for %{name}
Group:		Development/Python
# Added 04/2012 (wally)
Obsoletes:	python-farsight2

%description -n	python-%{name}
Python bindings for %{name}.

%package -n %{develname}
Summary:	Headers of %name for development
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
# Added 04/2012 (wally)
Obsoletes:	%{_lib}farsight2-devel

%description -n %{develname}
Headers of %{name} for development.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}

%description -n %{girname}
GObject Introspection interface description for %{name}.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--enable-gupnp \
	--with-package-name="%{_vendor} %{name}" \
	--with-package-origin="http://www.mandriva.com"
%make

%install
%makeinstall_std

find %{buildroot} -name '*.la' -delete

%files -n %{libname}
%{_libdir}/lib%{name}-%{api}.so.%{major}*
%{_libdir}/%{name}-%{api}/*.so

%files -n gstreamer0.10-%{name}
%{_libdir}/gstreamer-0.10/*.so
%{_datadir}/%{name}/%{api}/fsrtpconference/default-codec-preferences
%{_datadir}/%{name}/%{api}/fsrtpconference/default-element-properties
%{_datadir}/%{name}/%{api}/fsrawconference/default-element-properties


%files -n python-%{name}
%{python_sitearch}/%{name}.so

%files -n %{develname}
%doc ChangeLog
# Farstream build bug? (0.10 instead of 0.1)
%doc %{_datadir}/gtk-doc/html/%{name}-libs-0.10/ 
%doc %{_datadir}/gtk-doc/html/%{name}-plugins-%{api}/
%{_includedir}/%{name}-%{api}/
%{_datadir}/gir-1.0/Farstream-%{girmajor}.gir
%{_libdir}/pkgconfig/%{name}-%{api}.pc
%{_libdir}/lib%{name}-%{api}.so

%files -n %{girname}
%{_libdir}/girepository-1.0/Farstream-%{girmajor}.typelib
