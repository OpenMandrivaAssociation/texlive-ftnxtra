# revision 17317
# category Package
# catalog-ctan /macros/latex/contrib/ftnxtra
# catalog-date 2010-03-03 22:26:40 +0100
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-ftnxtra
Version:	0.1
Release:	1
Summary:	Extends the applicability of the \footnote command
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ftnxtra
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ftnxtra.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ftnxtra.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ftnxtra.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package treats footnotes in \caption, the tabular
environment, and \chapter and other \section-like commands.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
