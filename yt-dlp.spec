Name     : yt-dlp
Version  : 2022.11.11
Release  : 1
URL      : https://github.com/yt-dlp/yt-dlp
Source0  : https://github.com/yt-dlp/yt-dlp/archive/refs/tags/2022.11.11.tar.gz
Summary  : yt-dlp is a youtube-dl fork based on the now inactive youtube-dlc. 
Group    : Development/Tools
License  : Apache-2.0
BuildRequires : python3-dev
BuildRequires : pypi-setuptools 
BuildRequires : pypi-wheel
BuildRequires : pypi-twine
BuildRequires : pypi-brotli
BuildRequires : pypi-brotlicffi
BuildRequires : pypi-certifi
BuildRequires : pandoc

%description
yt-dlp is a youtube-dl fork based on the now inactive youtube-dlc. 

%prep
%setup -q -n yt-dlp-%{version}

%build
unset http_proxy
unset no_proxy 
unset https_proxy
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
pip3 install PyInstaller
make all tar
python devscripts/make_lazy_extractors.py
unset LD_LIBRARY_PATH
python pyinst.py


%install
install -D -m755 dist/yt-dlp_linux %{buildroot}/usr/bin/yt-dlp


%files
%defattr(-,root,root,-)
/usr/bin/yt-dlp
