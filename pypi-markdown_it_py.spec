#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-markdown_it_py
Version  : 3.0.0
Release  : 23
URL      : https://files.pythonhosted.org/packages/38/71/3b932df36c1a044d397a1f92d1cf91ee0a503d91e470cbd670aa66b07ed0/markdown-it-py-3.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/38/71/3b932df36c1a044d397a1f92d1cf91ee0a503d91e470cbd670aa66b07ed0/markdown-it-py-3.0.0.tar.gz
Summary  : Python port of markdown-it. Markdown parsing, done right!
Group    : Development/Tools
License  : MIT
Requires: pypi-markdown_it_py-bin = %{version}-%{release}
Requires: pypi-markdown_it_py-license = %{version}-%{release}
Requires: pypi-markdown_it_py-python = %{version}-%{release}
Requires: pypi-markdown_it_py-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# markdown-it-py
[![Github-CI][github-ci]][github-link]
[![Coverage Status][codecov-badge]][codecov-link]
[![PyPI][pypi-badge]][pypi-link]
[![Conda][conda-badge]][conda-link]
[![Code style: black][black-badge]][black-link]
[![PyPI - Downloads][install-badge]][install-link]

%package bin
Summary: bin components for the pypi-markdown_it_py package.
Group: Binaries
Requires: pypi-markdown_it_py-license = %{version}-%{release}

%description bin
bin components for the pypi-markdown_it_py package.


%package license
Summary: license components for the pypi-markdown_it_py package.
Group: Default

%description license
license components for the pypi-markdown_it_py package.


%package python
Summary: python components for the pypi-markdown_it_py package.
Group: Default
Requires: pypi-markdown_it_py-python3 = %{version}-%{release}

%description python
python components for the pypi-markdown_it_py package.


%package python3
Summary: python3 components for the pypi-markdown_it_py package.
Group: Default
Requires: python3-core
Provides: pypi(markdown_it_py)
Requires: pypi(mdurl)

%description python3
python3 components for the pypi-markdown_it_py package.


%prep
%setup -q -n markdown-it-py-3.0.0
cd %{_builddir}/markdown-it-py-3.0.0
pushd ..
cp -a markdown-it-py-3.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685979500
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-markdown_it_py
cp %{_builddir}/markdown-it-py-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-markdown_it_py/ab5a711cce75e49bdbd08bbcb728262e30580e5d || :
cp %{_builddir}/markdown-it-py-%{version}/LICENSE.markdown-it %{buildroot}/usr/share/package-licenses/pypi-markdown_it_py/5ff31979b5da51a43fc76f781675a8f86aed52f2 || :
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/markdown-it

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-markdown_it_py/5ff31979b5da51a43fc76f781675a8f86aed52f2
/usr/share/package-licenses/pypi-markdown_it_py/ab5a711cce75e49bdbd08bbcb728262e30580e5d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
