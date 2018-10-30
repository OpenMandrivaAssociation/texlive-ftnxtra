# revision 29652
# category Package
# catalog-ctan /macros/latex/contrib/ftnxtra
# catalog-date 2013-04-04 15:10:30 +0200
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-ftnxtra
Version:	0.1
Release:	12
Summary:	Extend the applicability of the \footnote command
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ftnxtra
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ftnxtra.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ftnxtra.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ftnxtra.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package treats footnotes in \caption, the tabular
environment, and \chapter and other \section-like commands.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ftnxtra/ftnxtra.sty
%doc %{_texmfdistdir}/doc/latex/ftnxtra/README
%doc %{_texmfdistdir}/doc/latex/ftnxtra/ftnxtra.pdf
%doc %{_texmfdistdir}/doc/latex/ftnxtra/ftnxtra.tex
#- source
%doc %{_texmfdistdir}/source/latex/ftnxtra/ftnxtra.dtx
%doc %{_texmfdistdir}/source/latex/ftnxtra/ftnxtra.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
