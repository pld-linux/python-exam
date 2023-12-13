#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Helpers for better testing
Summary(pl.UTF-8):	Moduł pomocniczy do lepszego testowania
Name:		python-exam
Version:	0.10.6
Release:	1
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/exam/
Source0:	https://files.pythonhosted.org/packages/source/e/exam/exam-%{version}.tar.gz
# Source0-md5:	0bf84acc2427a8a3d58d13d7297ff84a
Patch0:		%{name}-mock.patch
URL:		https://pypi.org/project/exam/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-mock
BuildRequires:	python-nose
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-nose
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Exam is a Python toolkit for writing better tests. It aims to remove a
lot of the boiler plate testing code one often writes, while still
following Python conventions and adhering to the unit testing
interface.

%description -l pl.UTF-8
Exam to zestaw narzędzi pythonowych do pisania lepszych testów. Celem
jest usunięcie dużej części powtarzalnego kodu testującego, który
zwykle się pisze przy zachowaniu zgodności z konwencjami Pythona i
interfejsem testów jednostkowych.

%package -n python3-exam
Summary:	Helpers for better testing
Summary(pl.UTF-8):	Moduł pomocniczy do lepszego testowania
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-exam
Exam is a Python toolkit for writing better tests. It aims to remove a
lot of the boiler plate testing code one often writes, while still
following Python conventions and adhering to the unit testing
interface.

%description -n python3-exam -l pl.UTF-8
Exam to zestaw narzędzi pythonowych do pisania lepszych testów. Celem
jest usunięcie dużej części powtarzalnego kodu testującego, który
zwykle się pisze przy zachowaniu zgodności z konwencjami Pythona i
interfejsem testów jednostkowych.

%prep
%setup -q -n exam-%{version}
%patch0 -p1

%build
%if %{with python2}
%py_build

%if %{with tests}
nosetests-%{py_ver} tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
nosetests-%{py3_ver} tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/exam
%{py_sitescriptdir}/exam-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-exam
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/exam
%{py3_sitescriptdir}/exam-%{version}-py*.egg-info
%endif
