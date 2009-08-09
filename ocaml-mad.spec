Name:           ocaml-mad
Version:        0.3.5
Release:        %mkrel 2
Summary:        Bindings for the mad library
License:        GPL
Group:          Development/Other
URL:            http://sourceforge.net/projects/savonet/files/
Source0:        http://downloads.sourceforge.net/savonet/ocaml-mad/ocaml-mad-%{version}.tar.gz
Patch0:         ocaml-mad-0.3.5-openfile.patch
Patch1:         ocaml-mad-0.3.5-docblock.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml-findlib
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
%patch0 -p1
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

