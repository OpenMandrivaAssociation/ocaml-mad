Name:           ocaml-mad
Version:        0.3.5
Release:        %mkrel 1
Summary:        Bindings for the mad library
License:        GPL
Group:          Development/Other
URL:            http://sourceforge.net/projects/savonet/files/
Source0:        ocaml-mad-%{version}.tar.gz
# wget http://downloads.sourceforge.net/project/savonet/ocaml-mad/%{version}/ocaml-mad-%{version}.tar.gz?use_mirror=freefr
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml-findlib
BuildRequires:  libmad

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

%build
%configure
make all opt
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
%doc doc
%{_libdir}/ocaml/mad/*.a
%{_libdir}/ocaml/mad/*.cmxa
%{_libdir}/ocaml/mad/*.cmx
%{_libdir}/ocaml/mad/*.mli

