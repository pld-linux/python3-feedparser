#
# Conditional build:
%bcond_with	tests	# perform "make test" (3 tests fail)

%define 	module	feedparser
Summary:	Parse RSS and Atom feeds in Python
Summary(pl.UTF-8):	Biblioteka Feed Parser dla Pythona
Name:		python3-%{module}
Version:	6.0.8
Release:	2
License:	BSD
Group:		Libraries/Python
Source0:	https://github.com/kurtmckee/feedparser/archive/%{version}.tar.gz
# Source0-md5:	bd9a217102307b1c4518bff2cab56bb7
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
Ten pakiet umożliwia analizę źródeł RSS i Atom w Pythonie.

%prep
%setup -q -n %{module}-%{version}

%build
%py3_build
%{?with_tests:cd feedparser; PYTHONPATH=../build-3 %{__python3} feedparsertest.py; cd ..}

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files -n python3-%{module}
%defattr(644,root,root,755)
%doc LICENSE NEWS README.rst
%{py3_sitescriptdir}/feedparser
%{py3_sitescriptdir}/feedparser-*.egg-info
