Name:		python-jaraco.functools
Version:	4.6.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/j/jaraco.functools/jaraco_functools-%{version}.tar.gz
Summary:	Functools like those found in stdlib
URL:		https://pypi.org/project/jaraco.functools/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(coherent.licensed)
BuildSystem:	python
BuildArch:	noarch

%description
Functools like those found in stdlib

%build -p
# The sdist is not a git checkout, so setuptools_scm needs the version.
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}

%files
%{py_sitedir}/jaraco/functools
%{py_sitedir}/jaraco_functools-*.*-info
