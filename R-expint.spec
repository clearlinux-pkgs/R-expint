#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-expint
Version  : 0.1.6
Release  : 40
URL      : https://cran.r-project.org/src/contrib/expint_0.1-6.tar.gz
Source0  : https://cran.r-project.org/src/contrib/expint_0.1-6.tar.gz
Summary  : Exponential Integral and Incomplete Gamma Function
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-expint-lib = %{version}-%{release}
BuildRequires : buildreq-R

%description
Ei(x), and the incomplete gamma function G(a, x) defined for
  negative values of its first argument. The package also gives easy
  access to the underlying C routines through an API; see the package
  vignette for details. A test package included in sub-directory
  example_API provides an implementation. C routines derived from the

%package lib
Summary: lib components for the R-expint package.
Group: Libraries

%description lib
lib components for the R-expint package.


%prep
%setup -q -c -n expint
cd %{_builddir}/expint

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589516733

%install
export SOURCE_DATE_EPOCH=1589516733
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library expint
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library expint
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library expint
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc expint || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/expint/CITATION
/usr/lib64/R/library/expint/DESCRIPTION
/usr/lib64/R/library/expint/INDEX
/usr/lib64/R/library/expint/Meta/Rd.rds
/usr/lib64/R/library/expint/Meta/features.rds
/usr/lib64/R/library/expint/Meta/hsearch.rds
/usr/lib64/R/library/expint/Meta/links.rds
/usr/lib64/R/library/expint/Meta/nsInfo.rds
/usr/lib64/R/library/expint/Meta/package.rds
/usr/lib64/R/library/expint/Meta/vignette.rds
/usr/lib64/R/library/expint/NAMESPACE
/usr/lib64/R/library/expint/NEWS.Rd
/usr/lib64/R/library/expint/R/expint
/usr/lib64/R/library/expint/R/expint.rdb
/usr/lib64/R/library/expint/R/expint.rdx
/usr/lib64/R/library/expint/doc/expint.R
/usr/lib64/R/library/expint/doc/expint.Rnw
/usr/lib64/R/library/expint/doc/expint.pdf
/usr/lib64/R/library/expint/doc/index.html
/usr/lib64/R/library/expint/example_API/DESCRIPTION
/usr/lib64/R/library/expint/example_API/NAMESPACE
/usr/lib64/R/library/expint/example_API/R/pkg.R
/usr/lib64/R/library/expint/example_API/man/pkg.Rd
/usr/lib64/R/library/expint/example_API/src/bar.c
/usr/lib64/R/library/expint/example_API/src/foo.c
/usr/lib64/R/library/expint/example_API/src/init.c
/usr/lib64/R/library/expint/example_API/src/locale.h
/usr/lib64/R/library/expint/example_API/src/pkg.h
/usr/lib64/R/library/expint/help/AnIndex
/usr/lib64/R/library/expint/help/aliases.rds
/usr/lib64/R/library/expint/help/expint.rdb
/usr/lib64/R/library/expint/help/expint.rdx
/usr/lib64/R/library/expint/help/paths.rds
/usr/lib64/R/library/expint/html/00Index.html
/usr/lib64/R/library/expint/html/R.css
/usr/lib64/R/library/expint/include/expintAPI.h

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/expint/libs/expint.so
/usr/lib64/R/library/expint/libs/expint.so.avx2
