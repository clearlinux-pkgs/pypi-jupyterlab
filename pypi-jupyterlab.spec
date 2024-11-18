#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
# autospec version: v21
# autospec commit: 5424026
#
Name     : pypi-jupyterlab
Version  : 4.3.1
Release  : 199
URL      : https://files.pythonhosted.org/packages/37/4b/f56825c4715e213f8d7784a1185eac74820eb86f3e2bf3753c22e839222d/jupyterlab-4.3.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/37/4b/f56825c4715e213f8d7784a1185eac74820eb86f3e2bf3753c22e839222d/jupyterlab-4.3.1.tar.gz
Summary  : JupyterLab computational environment
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause HPND MIT
Requires: pypi-jupyterlab-bin = %{version}-%{release}
Requires: pypi-jupyterlab-data = %{version}-%{release}
Requires: pypi-jupyterlab-license = %{version}-%{release}
Requires: pypi-jupyterlab-python = %{version}-%{release}
Requires: pypi-jupyterlab-python3 = %{version}-%{release}
Requires: pypi(jupyterlab_server)
BuildRequires : buildreq-distutils3
BuildRequires : pypi(hatchling)
BuildRequires : pypi-jupyter_packaging
BuildRequires : pypi-jupyterlab_server
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
**[Installation](#installation)** |
**[Documentation](https://jupyterlab.readthedocs.io)** |
**[Contributing](#contributing)** |
**[License](#license)** |
**[Team](#team)** |
**[Getting help](#getting-help)** |

%package bin
Summary: bin components for the pypi-jupyterlab package.
Group: Binaries
Requires: pypi-jupyterlab-data = %{version}-%{release}
Requires: pypi-jupyterlab-license = %{version}-%{release}

%description bin
bin components for the pypi-jupyterlab package.


%package data
Summary: data components for the pypi-jupyterlab package.
Group: Data

%description data
data components for the pypi-jupyterlab package.


%package license
Summary: license components for the pypi-jupyterlab package.
Group: Default

%description license
license components for the pypi-jupyterlab package.


%package python
Summary: python components for the pypi-jupyterlab package.
Group: Default
Requires: pypi-jupyterlab-python3 = %{version}-%{release}

%description python
python components for the pypi-jupyterlab package.


%package python3
Summary: python3 components for the pypi-jupyterlab package.
Group: Default
Requires: python3-core
Provides: pypi(jupyterlab)
Requires: pypi(async_lru)
Requires: pypi(httpx)
Requires: pypi(ipykernel)
Requires: pypi(jinja2)
Requires: pypi(jupyter_core)
Requires: pypi(jupyter_lsp)
Requires: pypi(jupyter_server)
Requires: pypi(jupyterlab_server)
Requires: pypi(notebook_shim)
Requires: pypi(packaging)
Requires: pypi(setuptools)
Requires: pypi(tornado)
Requires: pypi(traitlets)

%description python3
python3 components for the pypi-jupyterlab package.


%prep
%setup -q -n jupyterlab-4.3.1
cd %{_builddir}/jupyterlab-4.3.1
pushd ..
cp -a jupyterlab-4.3.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1731945879
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . jupyter-ydoc
python3 -m build --wheel --skip-dependency-check --no-isolation

pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
pypi-dep-fix.py . jupyter-ydoc
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jupyterlab
cp %{_builddir}/jupyterlab-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jupyterlab/109af8791cb65c3196cadbf313ab582d3a4edeed || :
cp %{_builddir}/jupyterlab-%{version}/jupyterlab/static/1909.7487a09fefbe7f9eabb6.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-jupyterlab/b8340cc7166c3efc8fa891de21b9b52fd70151cb || :
cp %{_builddir}/jupyterlab-%{version}/jupyterlab/static/232.5419cbec68e3fd0cf431.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-jupyterlab/cd522246a57b87ba54b1b6b92174b9091f70e983 || :
cp %{_builddir}/jupyterlab-%{version}/jupyterlab/static/4728.b5a1c080d13a8d15602a.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-jupyterlab/01ebbe688c25d738b9ee0e2de8113f7351c88e7a || :
cp %{_builddir}/jupyterlab-%{version}/jupyterlab/static/9892.6d289e7baed8c64d88e2.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-jupyterlab/84edab031b618e7ed5e6e4b764e1877913d64820 || :
python3 -m installer --destdir=%{buildroot} dist/*.whl
pypi-dep-fix.py %{buildroot} jupyter-ydoc
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
python3 -m installer --destdir=%{buildroot}-v3 dist/*.whl
popd
## install_append content
mkdir -p  %{buildroot}/usr/share/jupyter/
mv %{buildroot}/usr/etc/jupyter/jupyter_notebook_config.d %{buildroot}/usr/share/jupyter/
mv %{buildroot}/usr/etc/jupyter/jupyter_server_config.d/jupyterlab.json  %{buildroot}/usr/share/jupyter/
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jlpm
/usr/bin/jupyter-lab
/usr/bin/jupyter-labextension
/usr/bin/jupyter-labhub

%files data
%defattr(-,root,root,-)
/usr/share/applications/jupyterlab.desktop
/usr/share/icons/hicolor/scalable/apps/jupyterlab.svg
/usr/share/jupyter/jupyter_notebook_config.d/jupyterlab.json
/usr/share/jupyter/jupyterlab.json
/usr/share/jupyter/lab/schemas/@jupyterlab/application-extension/commands.json
/usr/share/jupyter/lab/schemas/@jupyterlab/application-extension/context-menu.json
/usr/share/jupyter/lab/schemas/@jupyterlab/application-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/application-extension/property-inspector.json
/usr/share/jupyter/lab/schemas/@jupyterlab/application-extension/shell.json
/usr/share/jupyter/lab/schemas/@jupyterlab/application-extension/top-bar.json
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/notification.json
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/palette.json
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/print.json
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/sanitizer.json
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/sessionDialogs.json
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/themes.json
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/utilityCommands.json
/usr/share/jupyter/lab/schemas/@jupyterlab/cell-toolbar-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/cell-toolbar-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/celltags-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/celltags-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/codemirror-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/codemirror-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/completer-extension/inline-completer.json
/usr/share/jupyter/lab/schemas/@jupyterlab/completer-extension/manager.json
/usr/share/jupyter/lab/schemas/@jupyterlab/completer-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/console-extension/completer.json
/usr/share/jupyter/lab/schemas/@jupyterlab/console-extension/foreign.json
/usr/share/jupyter/lab/schemas/@jupyterlab/console-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/console-extension/tracker.json
/usr/share/jupyter/lab/schemas/@jupyterlab/csvviewer-extension/csv.json
/usr/share/jupyter/lab/schemas/@jupyterlab/csvviewer-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/csvviewer-extension/tsv.json
/usr/share/jupyter/lab/schemas/@jupyterlab/debugger-extension/main.json
/usr/share/jupyter/lab/schemas/@jupyterlab/debugger-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/docmanager-extension/download.json
/usr/share/jupyter/lab/schemas/@jupyterlab/docmanager-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/docmanager-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/documentsearch-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/documentsearch-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/extensionmanager-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/extensionmanager-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/filebrowser-extension/browser.json
/usr/share/jupyter/lab/schemas/@jupyterlab/filebrowser-extension/download.json
/usr/share/jupyter/lab/schemas/@jupyterlab/filebrowser-extension/open-browser-tab.json
/usr/share/jupyter/lab/schemas/@jupyterlab/filebrowser-extension/open-with.json
/usr/share/jupyter/lab/schemas/@jupyterlab/filebrowser-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/filebrowser-extension/widget.json
/usr/share/jupyter/lab/schemas/@jupyterlab/fileeditor-extension/completer.json
/usr/share/jupyter/lab/schemas/@jupyterlab/fileeditor-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/fileeditor-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/help-extension/about.json
/usr/share/jupyter/lab/schemas/@jupyterlab/help-extension/jupyter-forum.json
/usr/share/jupyter/lab/schemas/@jupyterlab/help-extension/launch-classic.json
/usr/share/jupyter/lab/schemas/@jupyterlab/help-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/htmlviewer-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/htmlviewer-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/hub-extension/menu.json
/usr/share/jupyter/lab/schemas/@jupyterlab/hub-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/imageviewer-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/imageviewer-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/inspector-extension/consoles.json
/usr/share/jupyter/lab/schemas/@jupyterlab/inspector-extension/inspector.json
/usr/share/jupyter/lab/schemas/@jupyterlab/inspector-extension/notebooks.json
/usr/share/jupyter/lab/schemas/@jupyterlab/inspector-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/launcher-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/launcher-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/logconsole-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/logconsole-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/lsp-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/lsp-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/mainmenu-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/mainmenu-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/markdownviewer-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/markdownviewer-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/mathjax-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/mathjax-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/metadataform-extension/metadataforms.json
/usr/share/jupyter/lab/schemas/@jupyterlab/metadataform-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/notebook-extension/completer.json
/usr/share/jupyter/lab/schemas/@jupyterlab/notebook-extension/export.json
/usr/share/jupyter/lab/schemas/@jupyterlab/notebook-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/notebook-extension/panel.json
/usr/share/jupyter/lab/schemas/@jupyterlab/notebook-extension/tools.json
/usr/share/jupyter/lab/schemas/@jupyterlab/notebook-extension/tracker.json
/usr/share/jupyter/lab/schemas/@jupyterlab/running-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/running-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/settingeditor-extension/form-ui.json
/usr/share/jupyter/lab/schemas/@jupyterlab/settingeditor-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/settingeditor-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/shortcuts-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/shortcuts-extension/shortcuts.json
/usr/share/jupyter/lab/schemas/@jupyterlab/statusbar-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/statusbar-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/terminal-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/terminal-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/toc-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/toc-extension/registry.json
/usr/share/jupyter/lab/schemas/@jupyterlab/tooltip-extension/consoles.json
/usr/share/jupyter/lab/schemas/@jupyterlab/tooltip-extension/files.json
/usr/share/jupyter/lab/schemas/@jupyterlab/tooltip-extension/notebooks.json
/usr/share/jupyter/lab/schemas/@jupyterlab/tooltip-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/translation-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/translation-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/workspaces-extension/menu.json
/usr/share/jupyter/lab/schemas/@jupyterlab/workspaces-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/workspaces-extension/sidebar.json
/usr/share/jupyter/lab/static/100.1d14ca44a3cc8849349f.js
/usr/share/jupyter/lab/static/1017.67e7fc6c0221ce9cbeb7.js
/usr/share/jupyter/lab/static/1039.3fe94e87219c0ed159d3.js
/usr/share/jupyter/lab/static/1096.dd4c563e0483cbbeb9c9.js
/usr/share/jupyter/lab/static/1162.9eab2d3a6a73e2cd3b63.js
/usr/share/jupyter/lab/static/1189.c1482e88f0e949753db6.js
/usr/share/jupyter/lab/static/1208.4b9ab7b231d39ebdbc3f.js
/usr/share/jupyter/lab/static/1219.b5630aa3a46050fddc27.js
/usr/share/jupyter/lab/static/1268.e75d8a6dd557ac8957ca.js
/usr/share/jupyter/lab/static/1423.c662e4e18c51217c3fa7.js
/usr/share/jupyter/lab/static/1436.2c11d9dee0ad6f49e968.js
/usr/share/jupyter/lab/static/1445.a0e099c27d073217031a.js
/usr/share/jupyter/lab/static/1449.7026e8748d2a77e15d5b.js
/usr/share/jupyter/lab/static/1456.396bed90b4c5c24ebca9.js
/usr/share/jupyter/lab/static/1491.62ed4ab1f893d55a7df5.js
/usr/share/jupyter/lab/static/1495.13603dd823bbf5eb08b3.js
/usr/share/jupyter/lab/static/1510.f5643744900a492cca08.js
/usr/share/jupyter/lab/static/1673.b0ee25168543434bdbca.js
/usr/share/jupyter/lab/static/1737.a5fc97075f693ec36fe6.js
/usr/share/jupyter/lab/static/1786.37675c1099a3e0f0e18d.js
/usr/share/jupyter/lab/static/1832.b1ede2fe899bdec88938.js
/usr/share/jupyter/lab/static/1834.7445ad0c82371ac40737.js
/usr/share/jupyter/lab/static/1887.56f83f163a18c61efb16.js
/usr/share/jupyter/lab/static/1909.7487a09fefbe7f9eabb6.js
/usr/share/jupyter/lab/static/1909.7487a09fefbe7f9eabb6.js.LICENSE.txt
/usr/share/jupyter/lab/static/1954.f1c519cb1415c7da3e8c.js
/usr/share/jupyter/lab/static/1960.f8d8ef8a91360e60f0b9.js
/usr/share/jupyter/lab/static/1962.f2e82dd21240eba50714.js
/usr/share/jupyter/lab/static/1969.86e3168e52802569d650.js
/usr/share/jupyter/lab/static/1986.26029e99ef54a5652df8.js
/usr/share/jupyter/lab/static/1991.84fc123d7cfe8ae2948e.js
/usr/share/jupyter/lab/static/1cb1c39ea642f26a4dfe.woff
/usr/share/jupyter/lab/static/2280.6614699f54522fffbc00.js
/usr/share/jupyter/lab/static/232.5419cbec68e3fd0cf431.js
/usr/share/jupyter/lab/static/232.5419cbec68e3fd0cf431.js.LICENSE.txt
/usr/share/jupyter/lab/static/2337.50f794e5c2bde01decab.js
/usr/share/jupyter/lab/static/2353.ab70488f07a7c0a7a3fd.js
/usr/share/jupyter/lab/static/246.326a6482593e8a7bcd58.js
/usr/share/jupyter/lab/static/2467.4227742ac4b60289f222.js
/usr/share/jupyter/lab/static/247.84259ab142dd8c151fc2.js
/usr/share/jupyter/lab/static/2574.7d463f2a193d49883bdc.js
/usr/share/jupyter/lab/static/2576.b98b7b23adeec4cb6932.js
/usr/share/jupyter/lab/static/2590.99e505d19b964439aa31.js
/usr/share/jupyter/lab/static/2624.388e72c15e07152af2e5.js
/usr/share/jupyter/lab/static/2633.ea053b40991eb5adbc69.js
/usr/share/jupyter/lab/static/2641.a1707f70457d7ff4a82a.js
/usr/share/jupyter/lab/static/265.6f9e37c0b72db64203b1.js
/usr/share/jupyter/lab/static/2658.d1cae1b08b068d864368.js
/usr/share/jupyter/lab/static/26683bf201fb258a2237.woff
/usr/share/jupyter/lab/static/2681.a47f40e38ecd31ccd687.js
/usr/share/jupyter/lab/static/2707.61050e600b0aa9624127.js
/usr/share/jupyter/lab/static/2729.cafaf0caf2c0c83ac9fe.js
/usr/share/jupyter/lab/static/2794.05495c139ed000b57598.js
/usr/share/jupyter/lab/static/2823.0b6015b5e03c08281f41.js
/usr/share/jupyter/lab/static/2880.8483d51b11998bfe8e4b.js
/usr/share/jupyter/lab/static/29.bc9be9d891ab1856f060.js
/usr/share/jupyter/lab/static/2957.bc5eb9549a0b15c44916.js
/usr/share/jupyter/lab/static/2959.b24c9f67d639376f5ead.js
/usr/share/jupyter/lab/static/2965.698cf1ac2623483351b2.js
/usr/share/jupyter/lab/static/2965.698cf1ac2623483351b2.js.LICENSE.txt
/usr/share/jupyter/lab/static/30e889b58cbc51adfbb0.woff
/usr/share/jupyter/lab/static/3111.33574d9124842f355bce.js
/usr/share/jupyter/lab/static/3112.0757b31e24c5334fda73.js
/usr/share/jupyter/lab/static/321.0fb994fd384a54491584.js
/usr/share/jupyter/lab/static/3257.30af681f0c294efb65f7.js
/usr/share/jupyter/lab/static/3257.30af681f0c294efb65f7.js.LICENSE.txt
/usr/share/jupyter/lab/static/32792104b5ef69eded90.woff
/usr/share/jupyter/lab/static/3282.81fc10ff22608a9b5e5f.js
/usr/share/jupyter/lab/static/3282.81fc10ff22608a9b5e5f.js.LICENSE.txt
/usr/share/jupyter/lab/static/3293.45e37a0c8e23d360f5c6.js
/usr/share/jupyter/lab/static/3303.b5596c0715d2d58332fb.js
/usr/share/jupyter/lab/static/3330.a6d6a93bb012ea4f3589.js
/usr/share/jupyter/lab/static/3372.8eeafd96de9a7a205f40.js
/usr/share/jupyter/lab/static/339.62fb1e5a084681d24bfa.js
/usr/share/jupyter/lab/static/3415.a4a8c7afbbc19af6d014.js
/usr/share/jupyter/lab/static/3450.499466688807e6e40372.js
/usr/share/jupyter/lab/static/3489.7a81d2fa7123a8f139db.js
/usr/share/jupyter/lab/static/3538.5ce64a6194b4409fce29.js
/usr/share/jupyter/lab/static/355254db9ca10a09a3b5.woff
/usr/share/jupyter/lab/static/3616.a4271ffcf2ac3b4c2338.js
/usr/share/jupyter/lab/static/36e0d72d8a7afc696a3e.woff
/usr/share/jupyter/lab/static/3709.e33bc30c83272aa85628.js
/usr/share/jupyter/lab/static/373c04fd2418f5c77eea.eot
/usr/share/jupyter/lab/static/3763.a857fdcb9f31499444d0.js
/usr/share/jupyter/lab/static/3780.c9294dc98ae926717741.js
/usr/share/jupyter/lab/static/3788.df595483a01971a2b157.js
/usr/share/jupyter/lab/static/3799.eaa0438bc5c41bad0516.js
/usr/share/jupyter/lab/static/3824.5e23be1e37fce5b7c6b3.js
/usr/share/jupyter/lab/static/3832.c6026c483bb46cc8e599.js
/usr/share/jupyter/lab/static/3974.79f68bca9a02c92dab5e.js
/usr/share/jupyter/lab/static/3991.ee9a327e63c1f7c8c890.js
/usr/share/jupyter/lab/static/3bc6ecaae7ecf6f8d7f8.woff
/usr/share/jupyter/lab/static/3de784d07b9fa8f104c1.woff
/usr/share/jupyter/lab/static/3f6d3488cf65374f6f67.woff
/usr/share/jupyter/lab/static/4001.80ab3ef5300d7ce2d1fe.js
/usr/share/jupyter/lab/static/4050.dfaf4ace414ab9752223.js
/usr/share/jupyter/lab/static/4053.4945facc348478fd59f4.js
/usr/share/jupyter/lab/static/4068.9cc41f46f729f2c4369b.js
/usr/share/jupyter/lab/static/4076.b4d803d8bf1bd6c97854.js
/usr/share/jupyter/lab/static/4090.eec44f90a54aa383426c.js
/usr/share/jupyter/lab/static/4266.155b468271987c81d948.js
/usr/share/jupyter/lab/static/4296.721da424585874d0789e.js
/usr/share/jupyter/lab/static/4323.b2bd8a329a81d30ed039.js
/usr/share/jupyter/lab/static/4353.2fc2fc223680eaebc6cf.js
/usr/share/jupyter/lab/static/4364.ee19f1b28fb1bebc3895.js
/usr/share/jupyter/lab/static/4372.645626a2452c190dbb22.js
/usr/share/jupyter/lab/static/4372.645626a2452c190dbb22.js.LICENSE.txt
/usr/share/jupyter/lab/static/4408.f24dd0edf35e08548967.js
/usr/share/jupyter/lab/static/4462.a1dfac2be4cef60e89de.js
/usr/share/jupyter/lab/static/4484.0c7c43754e97c96f0f89.js
/usr/share/jupyter/lab/static/4486.8d2f41ae787607b7bf31.js
/usr/share/jupyter/lab/static/4528.77904f4c3e3d458f55e4.js
/usr/share/jupyter/lab/static/4606.cba21bae1bd61d5466b4.js
/usr/share/jupyter/lab/static/4611.bd2b768223b0cd570834.js
/usr/share/jupyter/lab/static/4616.04cfbd55593c51921cc7.js
/usr/share/jupyter/lab/static/4701.ceb0e0f9fc8a3b4aaccd.js
/usr/share/jupyter/lab/static/4728.b5a1c080d13a8d15602a.js
/usr/share/jupyter/lab/static/4728.b5a1c080d13a8d15602a.js.LICENSE.txt
/usr/share/jupyter/lab/static/4735.7731d551ca68bcb58e9f.js
/usr/share/jupyter/lab/static/4797.cc42a6dd4442057422aa.js
/usr/share/jupyter/lab/static/481e39042508ae313a60.woff
/usr/share/jupyter/lab/static/4838.8db4c61349bfba200547.js
/usr/share/jupyter/lab/static/4855.29e8dc6982ba4873487d.js
/usr/share/jupyter/lab/static/4878.f7557c5c99a54b40c49b.js
/usr/share/jupyter/lab/static/4885.31ef585c7876a28ffb95.js
/usr/share/jupyter/lab/static/492.5f186062d2dcdf79c86c.js
/usr/share/jupyter/lab/static/4928.6cb408e4def87534970d.js
/usr/share/jupyter/lab/static/4958.7499f6a88cb80b756a65.js
/usr/share/jupyter/lab/static/4981.eed4ddb90566e90e3df4.js
/usr/share/jupyter/lab/static/5085.a38923f36b551620798a.js
/usr/share/jupyter/lab/static/5090.404be96d8a6eae1e719a.js
/usr/share/jupyter/lab/static/5090.404be96d8a6eae1e719a.js.LICENSE.txt
/usr/share/jupyter/lab/static/5211.5b71830476810a6188e4.js
/usr/share/jupyter/lab/static/5224.8a6bbc774d20be66fdfb.js
/usr/share/jupyter/lab/static/5244.eefac84704ad30f00af3.js
/usr/share/jupyter/lab/static/5246.8992e5e0cc14a6b85a27.js
/usr/share/jupyter/lab/static/5317.f4bba2e3d0f4fdd088f7.js
/usr/share/jupyter/lab/static/5318.d5df5c275e925c22d780.js
/usr/share/jupyter/lab/static/5338.38c32bdfb0695f9b501f.js
/usr/share/jupyter/lab/static/5446.bdc12eba40091c1cc6c4.js
/usr/share/jupyter/lab/static/5492.44728a640c37a4b4aa0c.js
/usr/share/jupyter/lab/static/5521.cc7da8760b98f2dd2c18.js
/usr/share/jupyter/lab/static/5566.c76ea61eb723ee84e2cf.js
/usr/share/jupyter/lab/static/5606.e03dfa10c124a03f36ba.js
/usr/share/jupyter/lab/static/5829.1847cc3acbe7acefa6d3.js
/usr/share/jupyter/lab/static/5846.eec92db7873f0c8534d6.js
/usr/share/jupyter/lab/static/5847.930208c25e45ecf30657.js
/usr/share/jupyter/lab/static/5862.be1ec453e8db6844c62d.js
/usr/share/jupyter/lab/static/5877.72ab5a29e95ce21981e4.js
/usr/share/jupyter/lab/static/5890.ee1e537ee61f811b444d.js
/usr/share/jupyter/lab/static/5895.cda43bb9605deeb0d817.js
/usr/share/jupyter/lab/static/5929.d561797f8259994ecdd8.js
/usr/share/jupyter/lab/static/5942.05cbcd55c5f45ff7db43.js
/usr/share/jupyter/lab/static/5987.7e967df5417044d337a4.js
/usr/share/jupyter/lab/static/5cda41563a095bd70c78.woff
/usr/share/jupyter/lab/static/6060.52dca011e9f2f279fc5e.js
/usr/share/jupyter/lab/static/6095.6e79e3bad86e054aa8c8.js
/usr/share/jupyter/lab/static/6145.c422868290460078c013.js
/usr/share/jupyter/lab/static/6166.2bc9ac8e2156c0701a52.js
/usr/share/jupyter/lab/static/6170.65d899f43342f1e34bf1.js
/usr/share/jupyter/lab/static/6180.4753680838e288dc88ca.js
/usr/share/jupyter/lab/static/6275.e99f9312900c481b467d.js
/usr/share/jupyter/lab/static/6294.b3cb5e16527b9d09b4a2.js
/usr/share/jupyter/lab/static/6372.25d926454a35e061a88b.js
/usr/share/jupyter/lab/static/6412.ebdf8da40f1ba8272df9.js
/usr/share/jupyter/lab/static/6460.d9aaa1e48da295c6035d.js
/usr/share/jupyter/lab/static/6483.79f1ab5249584f984bf4.js
/usr/share/jupyter/lab/static/6492.236d5001cdad5cc56624.js
/usr/share/jupyter/lab/static/6540.51c00e890179a4832552.js
/usr/share/jupyter/lab/static/6540.51c00e890179a4832552.js.LICENSE.txt
/usr/share/jupyter/lab/static/6733.2d8d3e01d56d79a52e7e.js
/usr/share/jupyter/lab/static/6733.2d8d3e01d56d79a52e7e.js.LICENSE.txt
/usr/share/jupyter/lab/static/6767.4b82d96c237ca7e31bc6.js
/usr/share/jupyter/lab/static/6831.1df8fa4cabb5b1c19803.js
/usr/share/jupyter/lab/static/6843.dabcc3c9658bc6ded6d1.js
/usr/share/jupyter/lab/static/6874.bb2f7fbc6ce56eecc800.js
/usr/share/jupyter/lab/static/6896.af1d649e0efae70b7b1a.js
/usr/share/jupyter/lab/static/6941.465bebbd3d8a024f5f15.js
/usr/share/jupyter/lab/static/6993.6175f20787993c74adde.js
/usr/share/jupyter/lab/static/700.a1c8028a095361ff4522.js
/usr/share/jupyter/lab/static/700.a1c8028a095361ff4522.js.LICENSE.txt
/usr/share/jupyter/lab/static/7114.a44f4e4afe0f4cf18421.js
/usr/share/jupyter/lab/static/7136.b312751fbb25b73f5e71.js
/usr/share/jupyter/lab/static/721921bab0d001ebff02.woff
/usr/share/jupyter/lab/static/7250.b88d0a5e237ff5ff1aad.js
/usr/share/jupyter/lab/static/7260.b47dcaccbe7991104e8a.js
/usr/share/jupyter/lab/static/7269.962f078e97afc4f68e79.js
/usr/share/jupyter/lab/static/72bc573386dd1d48c5bb.woff
/usr/share/jupyter/lab/static/731.82a7b980b5b7f4b7a14f.js
/usr/share/jupyter/lab/static/7318.7cc6b4b0b3151b205ecb.js
/usr/share/jupyter/lab/static/7403.b747dcf7bd81025f084b.js
/usr/share/jupyter/lab/static/7445.7c793c8e1720f8ec4f85.js
/usr/share/jupyter/lab/static/7575.2e3e32236d5667bba43f.js
/usr/share/jupyter/lab/static/7587.3112240b6b82407b0f16.js
/usr/share/jupyter/lab/static/7642.b6cd0e20dd6a6b2a008c.js
/usr/share/jupyter/lab/static/7694.1cbff84dccb512476b7c.js
/usr/share/jupyter/lab/static/7756.93d0ab41829355a147ab.js
/usr/share/jupyter/lab/static/7769.d39df7673ee2660a9ac4.js
/usr/share/jupyter/lab/static/7803.0c8929610218552319bf.js
/usr/share/jupyter/lab/static/7856.dd9523e57bed80f1f694.js
/usr/share/jupyter/lab/static/7881.c5a234ce171f347c94e2.js
/usr/share/jupyter/lab/static/7990.fc875753fcfcc9b4eebc.js
/usr/share/jupyter/lab/static/7990.fc875753fcfcc9b4eebc.js.LICENSE.txt
/usr/share/jupyter/lab/static/79d088064beb3826054f.eot
/usr/share/jupyter/lab/static/8.4322fee36e778f503059.js
/usr/share/jupyter/lab/static/8103.00fa0c157eb92e5cf3ba.js
/usr/share/jupyter/lab/static/8217.801fbb0b549a74238760.js
/usr/share/jupyter/lab/static/8232.76805a0a87d0f6bb62ad.js
/usr/share/jupyter/lab/static/8258.c8c00e66a0bef38665f4.js
/usr/share/jupyter/lab/static/8313.64e3db0b24dd1a70aecb.js
/usr/share/jupyter/lab/static/8326.9dda93079a9e4f1b9be6.js
/usr/share/jupyter/lab/static/8368.c75a4b32ae45ec88465d.js
/usr/share/jupyter/lab/static/84.fe0a55d7756c37585fb4.js
/usr/share/jupyter/lab/static/8418.42e29778d4b49fb54e8e.js
/usr/share/jupyter/lab/static/867.e814bf26fbfc77fc4f16.js
/usr/share/jupyter/lab/static/870673df72e70f87c91a.woff
/usr/share/jupyter/lab/static/874.5f20565dc761ebc32874.js
/usr/share/jupyter/lab/static/8753.56da17175b663d61f9d3.js
/usr/share/jupyter/lab/static/8768.77e44e6422514f0a02c7.js
/usr/share/jupyter/lab/static/8778.ccda60c082ef77e33789.js
/usr/share/jupyter/lab/static/8779.6eebdb56785e3d38a457.js
/usr/share/jupyter/lab/static/8816.d7ec52fb31e9c6749593.js
/usr/share/jupyter/lab/static/8830.d5bb102ed8737ffe38cb.js
/usr/share/jupyter/lab/static/8896.426656fa4c4a1021375e.js
/usr/share/jupyter/lab/static/88b98cad3688915e50da.woff
/usr/share/jupyter/lab/static/89.933673451ca4a51053cb.js
/usr/share/jupyter/lab/static/8ea8791754915a898a31.woff2
/usr/share/jupyter/lab/static/8ea8dbb1b02e6f730f55.woff
/usr/share/jupyter/lab/static/9023.2ff687d7ff50df3719fc.js
/usr/share/jupyter/lab/static/9046.99c477ea375dcbb8c7ca.js
/usr/share/jupyter/lab/static/9085.5a959b5878e7afd8a878.js
/usr/share/jupyter/lab/static/9085.5a959b5878e7afd8a878.js.LICENSE.txt
/usr/share/jupyter/lab/static/9123.501219cd782693d6539f.js
/usr/share/jupyter/lab/static/9137.179a3c47465e7fb8f067.js
/usr/share/jupyter/lab/static/9296.176231372f63ddcb8e6c.js
/usr/share/jupyter/lab/static/9311.46cc03d7b667d8413fec.js
/usr/share/jupyter/lab/static/9329.c878986b50c10afaca34.js
/usr/share/jupyter/lab/static/9400.90fd1d2212781c80b587.js
/usr/share/jupyter/lab/static/9474.01b4e1d1e3376f4a5919.js
/usr/share/jupyter/lab/static/9517.7056cafdf1da3a136d45.js
/usr/share/jupyter/lab/static/9582.c10e0d8d04b7da1a22da.js
/usr/share/jupyter/lab/static/961.29c067b15a524e556eed.js
/usr/share/jupyter/lab/static/961.29c067b15a524e556eed.js.LICENSE.txt
/usr/share/jupyter/lab/static/9635.8953d15dfdfc8308dfcf.js
/usr/share/jupyter/lab/static/9652.a8d2e5854bcae4d40041.js
/usr/share/jupyter/lab/static/9674eb1bd55047179038.svg
/usr/share/jupyter/lab/static/9746.c7e86b432363dfd28caa.js
/usr/share/jupyter/lab/static/9834b82ad26e2a37583d.woff2
/usr/share/jupyter/lab/static/9892.6d289e7baed8c64d88e2.js
/usr/share/jupyter/lab/static/9892.6d289e7baed8c64d88e2.js.LICENSE.txt
/usr/share/jupyter/lab/static/9908.600b47cfa84ff9cdf6a7.js
/usr/share/jupyter/lab/static/a009bea404f7a500ded4.woff
/usr/share/jupyter/lab/static/a3b9817780214caf01e8.svg
/usr/share/jupyter/lab/static/af04542b29eaac04550a.woff
/usr/share/jupyter/lab/static/af6397503fcefbd61397.ttf
/usr/share/jupyter/lab/static/af96f67d7accf5fd2a4a.woff
/usr/share/jupyter/lab/static/b418136e3b384baaadec.woff
/usr/share/jupyter/lab/static/be0a084962d8066884f7.svg
/usr/share/jupyter/lab/static/bootstrap.js
/usr/share/jupyter/lab/static/build_log.json
/usr/share/jupyter/lab/static/c49810b53ecc0d87d802.woff
/usr/share/jupyter/lab/static/c56da8d69f1a0208b8e0.woff
/usr/share/jupyter/lab/static/cb9e9e693192413cde2b.woff
/usr/share/jupyter/lab/static/cda59d6efffa685830fd.ttf
/usr/share/jupyter/lab/static/e4299464e7b012968eed.eot
/usr/share/jupyter/lab/static/e42a88444448ac3d6054.woff2
/usr/share/jupyter/lab/static/e8711bbb871afd8e9dea.ttf
/usr/share/jupyter/lab/static/f9217f66874b0c01cd8c.woff
/usr/share/jupyter/lab/static/fc6ddf5df402b263cfb1.woff
/usr/share/jupyter/lab/static/index.html
/usr/share/jupyter/lab/static/index.out.js
/usr/share/jupyter/lab/static/jlab_core.e3a3a97fe081da5cfa40.js
/usr/share/jupyter/lab/static/main.e36901c9a645a44c1a74.js
/usr/share/jupyter/lab/static/package.json
/usr/share/jupyter/lab/static/style.js
/usr/share/jupyter/lab/static/third-party-licenses.json
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/index.css
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/index.js
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-high-contrast-extension/index.css
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-high-contrast-extension/index.js
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/index.css
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/index.js

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jupyterlab/01ebbe688c25d738b9ee0e2de8113f7351c88e7a
/usr/share/package-licenses/pypi-jupyterlab/109af8791cb65c3196cadbf313ab582d3a4edeed
/usr/share/package-licenses/pypi-jupyterlab/84edab031b618e7ed5e6e4b764e1877913d64820
/usr/share/package-licenses/pypi-jupyterlab/b8340cc7166c3efc8fa891de21b9b52fd70151cb
/usr/share/package-licenses/pypi-jupyterlab/cd522246a57b87ba54b1b6b92174b9091f70e983

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
