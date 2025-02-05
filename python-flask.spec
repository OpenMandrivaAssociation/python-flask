%global srcname Flask

Name:           python-flask
Version:	2.0.3
Release:	3
Summary:        A micro-framework for Python based on Werkzeug, Jinja 2 and good intentions
Group:          Development/Python
License:        BSD
URL:            https://flask.pocoo.org/
Source0:	https://files.pythonhosted.org/packages/84/9d/66347e6b3e2eb78647392d3969c23bdc2d8b2fdc32bd078c817c15cb81ad/Flask-2.0.3.tar.gz
BuildArch:      noarch

BuildRequires:	graphviz

BuildRequires:  python-werkzeug 
BuildRequires:  python-sphinx
BuildRequires:	python-itsdangerous
BuildRequires:  python-jinja2
BuildRequires:	python-setuptools
BuildRequires:	python-devel

Requires:       python-werkzeug 
Requires:       python-sphinx
Requires:       python-jinja2
Requires:	    python-itsdangerous

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
%license LICENSE.rst
%doc CHANGES.rst README.rst
%{_bindir}/flask
%{python_sitelib}/*.egg-info
%{python_sitelib}/flask
