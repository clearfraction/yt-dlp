Name     : yt-dlp
Version  : %(unset https_proxy && curl -s https://api.github.com/repos/yt-dlp/yt-dlp-nightly-builds/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")')
Release  : 1
URL      : https://github.com/yt-dlp/yt-dlp-nightly-builds/
#Source0  : https://github.com/yt-dlp/yt-dlp-nightly-builds/archive/refs/tags/%%{version}.tar.gz
Source00 : https://github.com/yt-dlp/yt-dlp-nightly-builds/releases/download/%{version}/yt-dlp.tar.gz
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
BuildRequires : pandoc wget

%description
yt-dlp is a youtube-dl fork based on the now inactive youtube-dlc. 

%prep
%setup -q -n yt-dlp

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
curl -LO https://github.com/yt-dlp/yt-dlp/archive/refs/heads/master.zip
unzip master.zip && mv yt-dlp-master/.github . && rm -rf master.zip
make


%install
%make_install PREFIX=/usr
rm -rf %{buildroot}/usr/{share,man}

%files
%defattr(-,root,root,-)
/usr/bin/yt-dlp
