%define name	frmg
%define version	1.2.0
%define release	%mkrel 2
%define _disable_ld_as_needed 1  

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Small preliminary example of a French grammar based on DyAlog
License:	GPL
Group:		Sciences/Computer science
Url:		https://mgkit.gforge.inria.fr/
Source:		https://gforge.inria.fr/frs/download.php/5681/%{name}-%{version}.tar.gz
Buildrequires:	dyalog
Buildrequires:	dyalog-xml-devel
Buildrequires:	dyalog-sqlite-devel
Buildrequires:	mgtools
Buildrequires:	mgcomp
Buildrequires:	perl-tag_utils
Buildrequires:	libxslt-proc
Buildrequires:  perl(Parse::Eyapp)
#depends on dyalog which doesn't exist on x86_64
ExclusiveArch: %ix86
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
A new small preliminary example of a French grammar generated from a
MetaGrammar and compiled with DyALog

It is based on a previous MetaGrammar (frenchmg), itself based on an previous
version developed by Lionel Clément.

A new simplified notation is been used to simplify the writing of the
MetaGrammar, with still conversion to an XML exchange format.

The MetaGrammar exploits several new functionnalities allowed by mgcomp (MG
compiler) and DyALog to be more compact. We can cite MG classes with namespace
(to use several times a same class but with different namespaces in a terminal
class), free node ordering when possible (interleaving), conditionnal nodes,
...

%package viewer
Summary:	%{name} viewer
Group:		Sciences/Computer science
Requires:	%{name} = %{version}
Requires:	apache-mod_perl

%description viewer
A mod_perl-based viewer for %{name}.

%prep
%setup -q

%build
export LD_LIBRARY_PATH=%{_libdir}/DyALog
%configure2_5x --with-modperldir=%{_var}/www/perl
# parallel build is broken
make

%install
rm -rf %{buildroot}
%makeinstall_std REGISTER=/bin/true

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc INSTALL NOTES.txt README
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/*
%{_datadir}/%{name}
%{_libdir}/pkgconfig/frmg.pc

%files viewer
%defattr(-,root,root)
%{_var}/www/perl/%{name}

