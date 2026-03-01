%global srcname flask

Name:           python-flask
Version:	3.1.3
Release:	1
Summary:        A micro-framework for Python based on Werkzeug, Jinja 2 and good intentions
Group:          Development/Python
License:        BSD
URL:            https://flask.palletsprojects.com/en/stable/
Source0:	https://files.pythonhosted.org/packages/source/f/flask/flask-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:	graphviz

BuildRequires:  python%{pyver}dist(werkzeug)
BuildRequires:  python%{pyver}dist(sphinx)
BuildRequires:	python%{pyver}dist(itsdangerous)
BuildRequires:  python%{pyver}dist(jinja2)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	pkgconfig(python3)

Requires:       python%{pyver}dist(werkzeug)
Requires:       python%{pyver}dist(sphinx)
Requires:       python%{pyver}dist(jinja2)
Requires:	python%{pyver}dist(itsdangerous)

%description
Flask is called a “micro-framework” because the idea to keep the core
simple but extensible. There is no database abstraction layer, no form
validation or anything else where different libraries already exist
that can handle that. However Flask knows the concept of extensions
that can add this functionality into your application as if it was
implemented in Flask itself. There are currently extensions for object
relational mappers, form validation, upload handling, various open
authentication technologies and more.

%prep
%autosetup -n %{srcname}-%{version}

# drop bundled egg-info
rm -rf Flask.egg-info/

%build
%py_build

%install
%py_install

%files
%doc CHANGES.rst
%{_bindir}/flask
%{python_sitelib}/*.dist-info
%{python_sitelib}/flask
