%global tl_name bearwear
%global tl_revision 54826

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Shirts to dress TikZbears
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/bearwear
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bearwear.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bearwear.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/bearwear.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package offers tools to create shirts for TikZbears from the
TikZlings package.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/bearwear
%dir %{_datadir}/texmf-dist/source/latex/bearwear
%dir %{_datadir}/texmf-dist/tex/latex/bearwear
%doc %{_datadir}/texmf-dist/doc/latex/bearwear/README.md
%doc %{_datadir}/texmf-dist/doc/latex/bearwear/baer.png
%doc %{_datadir}/texmf-dist/doc/latex/bearwear/bearwear-doc.tex
%doc %{_datadir}/texmf-dist/doc/latex/bearwear/bearwear.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bearwear/flag.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bearwear/latex-project-logo.pdf
%doc %{_datadir}/texmf-dist/doc/latex/bearwear/montblanc.jpg
%doc %{_datadir}/texmf-dist/doc/latex/bearwear/tartan3.jpg
%doc %{_datadir}/texmf-dist/doc/latex/bearwear/ulrike.pdf
%doc %{_datadir}/texmf-dist/source/latex/bearwear/bearwear.dtx
%doc %{_datadir}/texmf-dist/source/latex/bearwear/bearwear.ins
%{_datadir}/texmf-dist/tex/latex/bearwear/bearwear.sty
