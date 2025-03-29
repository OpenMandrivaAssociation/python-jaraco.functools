Name:		python-jaraco.functools
Version:	4.1.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/j/jaraco.functools/jaraco_functools-%{version}.tar.gz
Summary:	Functools like those found in stdlib
URL:		https://pypi.org/project/jaraco.functools/
License:	None
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Functools like those found in stdlib

%files
%{py_sitedir}/jaraco/functools
%{py_sitedir}/jaraco_functools-*.*-info
