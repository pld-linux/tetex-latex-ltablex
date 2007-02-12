
%define short_name ltablex
%define	texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

Summary:	Support for multipage tables with auto column width
Summary(pl.UTF-8):   Obsługa wielostronnych tabel z automatyczną szerokością kolumn
Name:		tetex-latex-%{short_name}
Version:	1.0
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
Source0:	ftp://ftp.ctan.org/tex-archive/macros/latex/contrib/ltablex/ltablex.sty
# Source0-md5:	63114642a66a1095d78435d8dde6d12a
Requires:	tetex-latex
Requires(post,postun):	/usr/bin/texhash
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The package modifies the tabularx environment to combine the features
of the tabularx package (auto-sized columns in a fixed width table)
with those of the longtable package (multi-page tables).

%description -l pl.UTF-8
Pakiet modyfikuje środowisko tabularx łącząc cechy pakietu tabularx
(automatyczna szerokość kolumn w tabeli o narzuconej szerokości) z
cechami pakietu longtable (wielostronicowe tabele).

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

install %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%{_datadir}/texmf/tex/latex/%{short_name}
