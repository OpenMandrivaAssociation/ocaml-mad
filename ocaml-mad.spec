Name:           ocaml-mad
Version:        0.4.0
Release:        3
Summary:        Bindings for the mad library
License:        GPL
Group:          Development/Other
URL:            https://sourceforge.net/projects/savonet/files/
Source0:        http://downloads.sourceforge.net/savonet/ocaml-mad/ocaml-mad-%{version}.tar.gz
Patch1:         ocaml-mad-0.3.5-docblock.patch
BuildRequires:  ocaml-findlib
BuildRequires:  ocaml
BuildRequires:  libmad-devel

%description
Bindings for the mad library which provides functions for encoding
wave audio files into mp3.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q
%patch1 -p1

%build
%configure
make
make doc

%install
rm -rf %{buildroot}
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}/%{_libdir}/ocaml
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/stublibs
mkdir -p $OCAMLFIND_DESTDIR/mad
make install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING CHANGES README
%dir %{_libdir}/ocaml/mad
%{_libdir}/ocaml/mad/META
%{_libdir}/ocaml/mad/*.cma
%{_libdir}/ocaml/mad/*.cmi
%{_libdir}/ocaml/stublibs/*.so*

%files devel
%defattr(-,root,root)
%doc doc/html
%{_libdir}/ocaml/mad/*.a
%{_libdir}/ocaml/mad/*.cmxa
%{_libdir}/ocaml/mad/*.cmx
%{_libdir}/ocaml/mad/*.mli



%changelog
* Sat Aug 21 2010 Florent Monnier <blue_prawn@mandriva.org> 0.4.0-1mdv2011.0
+ Revision: 571674
- updated to version 0.4.0

* Mon Jan 25 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.6-1mdv2010.1
+ Revision: 496364
- new version

* Mon Aug 10 2009 Florent Monnier <blue_prawn@mandriva.org> 0.3.5-2mdv2010.0
+ Revision: 413705
- patched openfile segfault

* Sat Aug 01 2009 Florent Monnier <blue_prawn@mandriva.org> 0.3.5-1mdv2010.0
+ Revision: 405319
- corrected deps
- import ocaml-mad

