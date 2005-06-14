Summary:   A vector graphics library
Name:      cairo
Version:   0.5.0
Release:   2
URL:       http://cairographics.org
Source0:   %{name}-%{version}.tar.gz
License:   LGPL/MPL
Group:     System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-root

Requires: /sbin/ldconfig
BuildRequires: pkgconfig
BuildRequires: libpixman-devel >= 0.1.5

%description 
Cairo is a vector graphics library designed to provide high-quality
display and print output. Currently supported output targets include
the X Window System, OpenGL (via glitz), in-memory image buffers, and
image files (PDF and PostScript).  Cairo is designed to produce
identical output on all output media while taking advantage of display
hardware acceleration when available (eg. through the X Render
Extension or OpenGL).

%package devel
Summary: Cairo developmental libraries and header files
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Developmental libraries and header files required for developing or
compiling software which links to the cairo library, which is an open
source vector graphics library.

%prep
%setup -q

%build
%configure --enable-warnings --disable-glitz --disable-quartz \
	--disable-atsui --disable-xcb --disable-win32
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall 
rm $RPM_BUILD_ROOT/%{_libdir}/*.la
%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig 
%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO

%{_libdir}/libcairo*.so.* 

%files devel
%defattr(-,root,root,-)
%{_includedir}/cairo/*
%{_libdir}/libcairo*.a
#%{_libdir}/libcairo*.la
%{_libdir}/libcairo.so
%{_libdir}/pkgconfig/cairo.pc

%changelog
* Tue Jun 14 2005 Kristian Høgsberg <krh@redhat.com> 0.5.0-2
- Add libpixman-devel BuildRequires.
- Explicitly disable win32 backend.

* Tue May 17 2005 Kristian Høgsberg <krh@redhat.com> - 0.5.0-1
- Update to 0.5.0.

* Sun Jan 23 2005 Kristian Høgsberg <krh@redhat.com> - 0.3.0-1
- Update to 0.3.0, explicitly disable more backends.

* Tue Nov 16 2004 Kristian Høgsberg <krh@redhat.com> - 0.2.0-1
- Incorporate changes suggested by katzj: Require: ldconfig and run it
  in %post and %postun, don't pass CFLAGS to make.

* Mon Aug  9 2004 Kristian Høgsberg <krh@redhat.com> - 0.2.0-1
- Update license, explicitly disable glitz.
- Create package.
