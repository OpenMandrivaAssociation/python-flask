%global srcname Flask
%global srcversion 0.10.1

Name:           python-flask
Version:        0.12.2
Release:        1
Summary:        A micro-framework for Python based on Werkzeug, Jinja 2 and good intentions
Group:          Development/Python
License:        BSD
URL:            http://flask.pocoo.org/
Source0:        https://files.pythonhosted.org/packages/source/F/Flask/Flask-%{version}.tar.gz
Patch1:		fix-test.patch
BuildArch:      noarch

BuildRequires:	graphviz

BuildRequires:  python-werkzeug 
BuildRequires:  python-sphinx
BuildRequires:	python-itsdangerous
BuildRequires:  python-jinja2
BuildRequires:	python-setuptools
BuildRequires:	python-devel

BuildRequires:	python2-setuptools
BuildRequires:	python2-werkzeug
BuildRequires:	python2-itsdangerous
BuildRequires:	python2-jinja2
BuildRequires:	python2-devel

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

%package -n python2-flask
Summary:	A micro-framework for Python based on Werkzeug, Jinja 2 and good intentions

%description -n python2-flask
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
%{__sed} -i "/platforms/ a\    requires=['Jinja2 (>=2.4)']," setup.py

%apply_patches

cp -a . %py2dir

%build
python setup.py build

pushd %py2dir
python setup.py build

%install
python setup.py install -O1 --skip-build --root %{buildroot}

# Need to install flask in the setuptools "develop" mode to build docs
# The BuildRequires on Werkzeug, Jinja2 and Sphinx is due to this as well.
export PYTHONPATH=%{buildroot}%{py_puresitedir}
python setup.py develop --install-dir %{buildroot}%{py_puresitedir}
make -C docs html

rm -rf %{buildroot}%{py_puresitedir}/site.py
rm -rf %{buildroot}%{py_puresitedir}/site.py[co]
rm -rf %{buildroot}%{py_puresitedir}/easy-install.pth
rm -rf docs/_build/html/.buildinfo
rm -rf examples/minitwit/*.pyc
rm -rf examples/flaskr/*.pyc
rm -rf examples/jqueryexample/*.pyc

find %{buildroot} -size 0 -delete

pushd %py2dir
python setup.py install -O1 --skip-build --root %{buildroot}

%check
python setup.py test

%files
%doc AUTHORS LICENSE PKG-INFO CHANGES README
%doc docs/_build/html examples
%{py_puresitedir}/*.egg-info
%{py_puresitedir}/*.egg-link
%{py_puresitedir}/flask

%files -n python2-flask
%doc AUTHORS LICENSE PKG-INFO CHANGES README
%doc docs/_build/html examples
%{py_puresitedir}/*.egg-info
%{py_puresitedir}/flask
