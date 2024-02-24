# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-markupsafe
Epoch: 100
Version: 2.1.3
Release: 1%{?dist}
Summary: Implements a XML/HTML/XHTML Markup safe string for Python 3
License: BSD-3-Clause
URL: https://github.com/pallets/markupsafe/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-Cython3
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
A library for safe markup escaping. Python 3 version.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-MarkupSafe
Summary: Implements a XML/HTML/XHTML Markup safe string for Python 3
Requires: python3
Provides: python3-MarkupSafe = %{epoch}:%{version}-%{release}
Provides: python3dist(MarkupSafe) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-MarkupSafe = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(MarkupSafe) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-MarkupSafe = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(MarkupSafe) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-MarkupSafe
A library for safe markup escaping. Python 3 version.

%files -n python%{python3_version_nodots}-MarkupSafe
%license LICENSE.rst
%{python3_sitearch}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-MarkupSafe
Summary: Implements a XML/HTML/XHTML Markup safe string for Python 3
Requires: python3
Provides: python3-MarkupSafe = %{epoch}:%{version}-%{release}
Provides: python3dist(MarkupSafe) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-MarkupSafe = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(MarkupSafe) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-MarkupSafe = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(MarkupSafe) = %{epoch}:%{version}-%{release}

%description -n python3-MarkupSafe
A library for safe markup escaping. Python 3 version.

%files -n python3-MarkupSafe
%license LICENSE.rst
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-markupsafe
Summary: Implements a XML/HTML/XHTML Markup safe string for Python 3
Requires: python3
Provides: python3-markupsafe = %{epoch}:%{version}-%{release}
Provides: python3dist(markupsafe) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-markupsafe = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(markupsafe) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-markupsafe = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(markupsafe) = %{epoch}:%{version}-%{release}

%description -n python3-markupsafe
A library for safe markup escaping. Python 3 version.

%files -n python3-markupsafe
%license LICENSE.rst
%{python3_sitearch}/*
%endif

%changelog
