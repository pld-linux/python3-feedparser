#
# Conditional build:
%bcond_with	tests	# unit tests (7 tests fail)

%define 	module	feedparser
Summary:	Parse RSS and Atom feeds in Python
Summary(pl.UTF-8):	Analiza źródeł RSS i Atom dla Pythona
Name:		python3-%{module}
Version:	6.0.11
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://github.com/kurtmckee/feedparser/archive/%{version}.tar.gz
# Source0-md5:	bbb8814240ef30c930ad8ea8eeb8e80b
Patch0:		re.patch
URL:		https://github.com/kurtmckee/feedparser
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Universal Feed Parser is a Python module for downloading and parsing
syndicated feeds. It can handle RSS 0.90, Netscape RSS 0.91, Userland
RSS 0.91, RSS 0.92, RSS 0.93, RSS 0.94, RSS 1.0, RSS 2.0, Atom 0.3,
Atom 1.0, and CDF feeds. It also parses several popular extension
modules, including Dublin Core and Apple's iTunes extensions.

%description -l pl.UTF-8
Universal Feed Parser to moduł Pythona do pobierania i analizy
syndykowanych źródeł (feedów). Obsługuje RSS 0.90, Netscape RSS 0.91,
Userland RSS 0.91, RSS 0.92, RSS 0.93, RSS 0.94, RSS 1.0, RSS 2.0,
Atom 0.3, Atom 1.0 oraz CDF. Potrafi obsłużyć także kilka popularnych
modułów rozszerzeń, w tym rozszerzenia Dublin Core oraz Apple iTunes.

%prep
%setup -q -n %{module}-%{version}
%patch -P0 -p1

%build
%py3_build

%if %{with tests}
%{__python3} tests/runtests.py
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE NEWS README.rst
%{py3_sitescriptdir}/feedparser
%{py3_sitescriptdir}/feedparser-%{version}-py*.egg-info
