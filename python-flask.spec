%global srcname Flask
%global srcversion 0.9

Name:           python-flask
Version:        0.9
Release:        1
Summary:        A micro-framework for Python based on Werkzeug, Jinja 2 and good intentions
Group:          Development/Python
License:        BSD
URL:            http://flask.pocoo.org/
Source0:        http://pypi.python.org/packages/source/F/Flask/%{srcname}-%{srcversion}.tar.gz
BuildArch:      noarch
BuildRequires:  python-werkzeug python-sphinx
BuildRequires:  python-jinja2
Requires:       python-werkzeug python-sphinx
Requires:       python-jinja2
%py_requires -d

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
%setup -q -n %{srcname}-%{srcversion}
%{__sed} -i "1i __requires__ = ['Jinja2>=2.4']" setup.py

%build
%{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

# Need to install flask in the setuptools "develop" mode to build docs
# The BuildRequires on Werkzeug, Jinja2 and Sphinx is due to this as well.
export PYTHONPATH=%{buildroot}%{python_sitelib}
%{__python} setup.py develop --install-dir %{buildroot}%{python_sitelib}
make -C docs html

rm -rf %{buildroot}%{python_sitelib}/site.py
rm -rf %{buildroot}%{python_sitelib}/site.py[co]
rm -rf %{buildroot}%{python_sitelib}/easy-install.pth
rm -rf docs/_build/html/.buildinfo
rm -rf examples/minitwit/*.pyc
rm -rf examples/flaskr/*.pyc
rm -rf examples/jqueryexample/*.pyc

%check
%{__python} setup.py test

%files
%doc AUTHORS LICENSE PKG-INFO CHANGES README
%doc docs/_build/html examples
%{python_sitelib}/*.egg-info
%{python_sitelib}/*.egg-link
%{python_sitelib}/flask
