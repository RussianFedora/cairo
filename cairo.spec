Summary:   A vector graphics library
Name:      cairo
Version:   0.2.0
Release:   1
URL:       http://cairographics.org
Source0:   %{name}-%{version}.tar.gz
License:   LGPL/MPL
Group:     System Environment/Libraries
BuildRoot: %{_tmppath}/%{name}-%{version}-root

BuildRequires: /sbin/ldconfig
BuildRequires: pkgconfig

%description 
Cairo is a vector graphics library designed to provide high-quality
display and print output. Currently supported output targets include
the X Window System, OpenGL (via glitz), in-memory image buffers, and
image files (PNG and PostScript). Initial work has begin on support
for PDF file output. Cairo is designed to produce identical output on
all output media while taking advantage of display hardware
acceleration when available (eg. through the X Render Extension or
OpenGL).

%package devel
Summary: cairo developmental libraries and header files
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}

%description devel
Developmental libraries and header files required for developing or
compiling software which links to the cairo library, which is an open
source vector graphics library.

%prep
%setup -q

%build
%configure --enable-warnings --disable-glitz
make CFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall 
/sbin/ldconfig -n %{_libdir}
rm $RPM_BUILD_ROOT/%{_libdir}/*.la
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README TODO

%{_libdir}/libcairo*.so.* 

%files devel
%defattr(-,root,root,-)
%{_includedir}/cairo-features.h
%{_includedir}/cairo.h
%{_libdir}/libcairo*.a
#%{_libdir}/libcairo*.la
%{_libdir}/libcairo.so
%{_libdir}/pkgconfig/cairo.pc

%changelog
* Mon Aug  9 2004 Kristian Høgsberg <krh@redhat.com> - 0.2.0-1
- Update license, explicitly disable glitz.
- Create package.
