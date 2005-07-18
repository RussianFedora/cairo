%define freetype_version 2.1.3-3
%define fontconfig_version 2.0
%define libpixman_version 0.1.5

Summary:   A vector graphics library
Name:      cairo
Version:   0.5.2
Release:   1
URL:       http://cairographics.org
Source0:   %{name}-%{version}.tar.gz
License:   LGPL/MPL
Group:     System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-root

Requires: /sbin/ldconfig
BuildRequires: pkgconfig
BuildRequires: libpixman-devel >= %{libpixman_version}
BuildRequires: xorg-x11-devel
BuildRequires: libpng-devel
BuildRequires: freetype-devel >= %{freetype_version}
BuildRequires: fontconfig-devel >= %{fontconfig_version}

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
Requires: libpixman-devel >= %{libpixman_version}
Requires: xorg-x11-devel
Requires: libpng-devel
Requires: freetype-devel >= %{freetype_version}
Requires: fontconfig-devel >= %{fontconfig_version}

%description devel
Developmental libraries and header files required for developing or
compiling software which links to the cairo library, which is an open
source vector graphics library.

%prep
%setup -q

%build
%configure --enable-warnings --disable-glitz --disable-quartz \
	--disable-atsui --disable-xcb --disable-win32 \
	--disable-gtk-doc
make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall 
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm $RPM_BUILD_ROOT%{_libdir}/*.a

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
%{_includedir}/*
%{_libdir}/libcairo*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gtk-doc/*

%changelog
* Mon Jul 18 2005 Kristian Høgsberg <krh@redhat.com> 0.5.2-1
- Update to cairo-0.5.2 and drop bitmap font patch.

* Wed Jul  6 2005 Kristian Høgsberg <krh@redhat.com> - 0.5.1-5
- Fix typo in use of libpixman_version macro (Thanks to Michael
  Schwendt, #162550).

* Sun Jun 26 2005 Kristian Høgsberg <krh@redhat.com> - 0.5.1-4
- Add more missing devel package requires (libpng-devel and
  xorg-x11-devel) (#161688)
- Add Owens patch (cairo-0.5.1-bitmap-fonts.patch) to make bitmap
  fonts work with cairo (#161653).

* Wed Jun 22 2005 Kristian Høgsberg <krh@redhat.com> - 0.5.1-3
- Add requirement on libpixman-devel for devel package.

* Tue Jun 21 2005 Kristian Høgsberg <krh@redhat.com> - 0.5.1-2
- Package gtk docs as part of devel package.
- Nuke static library.
- Update devel files so /usr/include/cairo is owned by devel package.

* Mon Jun 20 2005 Kristian Høgsberg <krh@redhat.com> - 0.5.1-1
- Update to cairo 0.5.1.
- Remove gtk-doc files, since --disable-gtk-doc doesn't work.
- Disable gtk-doc and add freetype and fontconfig BuildRequires.

* Tue Jun 14 2005 Kristian Høgsberg <krh@redhat.com> - 0.5.0-2
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
