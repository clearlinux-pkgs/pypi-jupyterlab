#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jupyterlab
Version  : 3.4.4
Release  : 152
URL      : https://files.pythonhosted.org/packages/34/d2/8ddc51ba1a4d1b40d667da29dc85d445428d2502b3842194d2d1a7522fd3/jupyterlab-3.4.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/34/d2/8ddc51ba1a4d1b40d667da29dc85d445428d2502b3842194d2d1a7522fd3/jupyterlab-3.4.4.tar.gz
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
BuildRequires : pypi(ipython)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(jupyter_core)
BuildRequires : pypi(jupyter_packaging)
BuildRequires : pypi(jupyter_server)
BuildRequires : pypi(jupyterlab_server)
BuildRequires : pypi(nbclassic)
BuildRequires : pypi(notebook)
BuildRequires : pypi(packaging)
BuildRequires : pypi(tornado)
BuildRequires : pypi-jupyter_packaging
BuildRequires : pypi-jupyterlab_server

%description
**[Installation](#installation)** |
**[Documentation](http://jupyterlab.readthedocs.io)** |
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
Requires: pypi(ipython)
Requires: pypi(jinja2)
Requires: pypi(jupyter_core)
Requires: pypi(jupyter_server)
Requires: pypi(jupyterlab_server)
Requires: pypi(nbclassic)
Requires: pypi(notebook)
Requires: pypi(packaging)
Requires: pypi(tornado)

%description python3
python3 components for the pypi-jupyterlab package.


%prep
%setup -q -n jupyterlab-3.4.4
cd %{_builddir}/jupyterlab-3.4.4
pushd ..
cp -a jupyterlab-3.4.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1658432122
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -msse2avx "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jupyterlab
cp %{_builddir}/jupyterlab-3.4.4/LICENSE %{buildroot}/usr/share/package-licenses/pypi-jupyterlab/fa62fa6d531b94e755b914b3291c8541ce40f411
cp %{_builddir}/jupyterlab-3.4.4/jupyterlab/static/1036.e3242066e92a791822b6.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-jupyterlab/01ebbe688c25d738b9ee0e2de8113f7351c88e7a
cp %{_builddir}/jupyterlab-3.4.4/jupyterlab/static/1944.9bb345a40325c23313e9.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-jupyterlab/0656099c1cf5c72718c57eb920abcffa02df0a93
cp %{_builddir}/jupyterlab-3.4.4/jupyterlab/static/3935.4159b022aa6d82e44127.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-jupyterlab/10645e5e81c59dc0f14b79252005ea68d42f1ba7
cp %{_builddir}/jupyterlab-3.4.4/jupyterlab/static/7294.f71c2889fedcd71bd1ee.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-jupyterlab/0036998e52f1b6442c90b9ea6df602bef0294cc5
cp %{_builddir}/jupyterlab-3.4.4/jupyterlab/static/jlab_core.081dc2b13065c79d8463.js.LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-jupyterlab/cd522246a57b87ba54b1b6b92174b9091f70e983
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
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
/usr/share/jupyter/jupyter_notebook_config.d/jupyterlab.json
/usr/share/jupyter/jupyterlab.json
/usr/share/jupyter/lab/schemas/@jupyterlab/application-extension/commands.json
/usr/share/jupyter/lab/schemas/@jupyterlab/application-extension/context-menu.json
/usr/share/jupyter/lab/schemas/@jupyterlab/application-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/application-extension/shell.json
/usr/share/jupyter/lab/schemas/@jupyterlab/application-extension/sidebar.json
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/palette.json
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/print.json
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/themes.json
/usr/share/jupyter/lab/schemas/@jupyterlab/apputils-extension/workspaces.json
/usr/share/jupyter/lab/schemas/@jupyterlab/cell-toolbar-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/cell-toolbar-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/codemirror-extension/commands.json
/usr/share/jupyter/lab/schemas/@jupyterlab/codemirror-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/completer-extension/consoles.json
/usr/share/jupyter/lab/schemas/@jupyterlab/completer-extension/files.json
/usr/share/jupyter/lab/schemas/@jupyterlab/completer-extension/notebooks.json
/usr/share/jupyter/lab/schemas/@jupyterlab/completer-extension/package.json.orig
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
/usr/share/jupyter/lab/schemas/@jupyterlab/fileeditor-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/fileeditor-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/help-extension/about.json
/usr/share/jupyter/lab/schemas/@jupyterlab/help-extension/jupyter-forum.json
/usr/share/jupyter/lab/schemas/@jupyterlab/help-extension/launch-classic.json
/usr/share/jupyter/lab/schemas/@jupyterlab/help-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/htmlviewer-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/htmlviewer-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/hub-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/hub-extension/plugin.json
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
/usr/share/jupyter/lab/schemas/@jupyterlab/mainmenu-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/mainmenu-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/markdownviewer-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/markdownviewer-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/notebook-extension/export.json
/usr/share/jupyter/lab/schemas/@jupyterlab/notebook-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/notebook-extension/panel.json
/usr/share/jupyter/lab/schemas/@jupyterlab/notebook-extension/tracker.json
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
/usr/share/jupyter/lab/schemas/@jupyterlab/toc-extension/plugin.json
/usr/share/jupyter/lab/schemas/@jupyterlab/tooltip-extension/consoles.json
/usr/share/jupyter/lab/schemas/@jupyterlab/tooltip-extension/files.json
/usr/share/jupyter/lab/schemas/@jupyterlab/tooltip-extension/notebooks.json
/usr/share/jupyter/lab/schemas/@jupyterlab/tooltip-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/translation-extension/package.json.orig
/usr/share/jupyter/lab/schemas/@jupyterlab/translation-extension/plugin.json
/usr/share/jupyter/lab/static/06f4d00923ea24697df5df0b92984175991d8bd25776a02d531bb401e393ec42.ttf
/usr/share/jupyter/lab/static/1033.890eeae47460e241b1e9.js
/usr/share/jupyter/lab/static/1036.e3242066e92a791822b6.js
/usr/share/jupyter/lab/static/1036.e3242066e92a791822b6.js.LICENSE.txt
/usr/share/jupyter/lab/static/1044.4e54e3e338cfaccdfb46.js
/usr/share/jupyter/lab/static/1057.a0608544097dd22a589e.js
/usr/share/jupyter/lab/static/1142.074d125bb59f5a332666.js
/usr/share/jupyter/lab/static/1249.047c76b5ea96a41605db.js
/usr/share/jupyter/lab/static/126.1e2fb998804b27c72a3e.js
/usr/share/jupyter/lab/static/1287.0e48071eeb17a3bea8e5.js
/usr/share/jupyter/lab/static/1358.9ab4f57e8227ce75f427.js
/usr/share/jupyter/lab/static/1397.4b53e533e7ca4d3f06fe.js
/usr/share/jupyter/lab/static/14c9db4ff87fde08f67b0a69dd594bab6d87174812a0dbd34c59833bfed8cc0e.woff
/usr/share/jupyter/lab/static/1842.1846f224482b066652bf.js
/usr/share/jupyter/lab/static/1944.9bb345a40325c23313e9.js
/usr/share/jupyter/lab/static/1944.9bb345a40325c23313e9.js.LICENSE.txt
/usr/share/jupyter/lab/static/198.ebf955f77b5c9807f163.js
/usr/share/jupyter/lab/static/2040.6489997c35a5d7b0b100.js
/usr/share/jupyter/lab/static/2249.0cc057d5b7da618aa4e0.js
/usr/share/jupyter/lab/static/2326849b6c3dfa217a0e9ecaec9553c910a4e2987c87315c85073d2b95a484f3.svg
/usr/share/jupyter/lab/static/2349.91555cd2ef72c84e9253.js
/usr/share/jupyter/lab/static/2353.baeba73a2e9f3d9e75d2.js
/usr/share/jupyter/lab/static/2356.f97dd8093f97f156efe4.js
/usr/share/jupyter/lab/static/2585.4d374708a4df1d35065d.js
/usr/share/jupyter/lab/static/2719.1001d896f21f09c3f99f.js
/usr/share/jupyter/lab/static/3029.8636761a48c8422ce37f.js
/usr/share/jupyter/lab/static/3087.06efd084edba2bea6ea1.js
/usr/share/jupyter/lab/static/3122.b1fda55c421da97a00a3.js
/usr/share/jupyter/lab/static/3236.4fabf963498daeeb9624.js
/usr/share/jupyter/lab/static/3308.3a94151c0d57440646ab.js
/usr/share/jupyter/lab/static/3387.bb8976de803b341fe7a3.js
/usr/share/jupyter/lab/static/3443.868b4f89289beb97adec.js
/usr/share/jupyter/lab/static/3496.ecb0e7fcc54191234ae6.js
/usr/share/jupyter/lab/static/3502.c915d993b864739407e3.js
/usr/share/jupyter/lab/static/3531.0bacde3facdc0c46766c.js
/usr/share/jupyter/lab/static/3532.5dff37bee3e7bf1673b8.js
/usr/share/jupyter/lab/static/3664.cfb68e6cb3654849310c.js
/usr/share/jupyter/lab/static/3791.6adeeacb6143a6599115.js
/usr/share/jupyter/lab/static/3935.4159b022aa6d82e44127.js
/usr/share/jupyter/lab/static/3935.4159b022aa6d82e44127.js.LICENSE.txt
/usr/share/jupyter/lab/static/3992.6587b8bb22d3b162cc6b.js
/usr/share/jupyter/lab/static/3d06af1f31cd83ace7a265a014b8fb5dee15770ecac8f7a55555190e627e03c2.ttf
/usr/share/jupyter/lab/static/406.6f87c9a21bbaa5f39fc4.js
/usr/share/jupyter/lab/static/407a9723fc717c94e287496080d773e18e29c3cac49e2630172343c65c0864a8.eot
/usr/share/jupyter/lab/static/4151.fd7ca59b64f0adc97032.js
/usr/share/jupyter/lab/static/4155.784ca1752696680bf373.js
/usr/share/jupyter/lab/static/43c072c16c9ee6d67acdfa6c6d6685ff1e74eb4237b7cc3c1348ab1c108b26af.woff2
/usr/share/jupyter/lab/static/4402.d24b4a44244e256d0126.js
/usr/share/jupyter/lab/static/4429.c4f083ef6b6e29345fd4.js
/usr/share/jupyter/lab/static/45.91c59b0e1dca32f01373.js
/usr/share/jupyter/lab/static/4570.53adcb6f69939da383ff.js
/usr/share/jupyter/lab/static/4631.96a143e70f005fef7b59.js
/usr/share/jupyter/lab/static/466.239a0c009f33f1cb7cab.js
/usr/share/jupyter/lab/static/4894.f5e3a48d18905b75d07f.js
/usr/share/jupyter/lab/static/501.d77919e38ba77753c7f8.js
/usr/share/jupyter/lab/static/5065.49dd76cb64fd444f785f.js
/usr/share/jupyter/lab/static/5096.96faf5ddac346a9ad9c3.js
/usr/share/jupyter/lab/static/5096.96faf5ddac346a9ad9c3.js.LICENSE.txt
/usr/share/jupyter/lab/static/5223.0006e6e211b7c197b9f1.js
/usr/share/jupyter/lab/static/5289.6c67522c6a1c32fc2ea2.js
/usr/share/jupyter/lab/static/5383.d630abf49f5cb82bb76f.js
/usr/share/jupyter/lab/static/5493.c4714ef77ba6a59aec45.js
/usr/share/jupyter/lab/static/5493.c4714ef77ba6a59aec45.js.LICENSE.txt
/usr/share/jupyter/lab/static/5505.d108d38d683afca0e4ed.js
/usr/share/jupyter/lab/static/5557.625f5943a166b494ee38.js
/usr/share/jupyter/lab/static/5619.b1928648a190b38e627a.js
/usr/share/jupyter/lab/static/6005.cda1ecd972909c2a0250.js
/usr/share/jupyter/lab/static/6064.1a4a55a09511d4907870.js
/usr/share/jupyter/lab/static/6064.1a4a55a09511d4907870.js.LICENSE.txt
/usr/share/jupyter/lab/static/6080.39703b8cc7bd284ce1bd.js
/usr/share/jupyter/lab/static/6218.63b338a58c855634089e.js
/usr/share/jupyter/lab/static/6504.f578fea4ca18a937babd.js
/usr/share/jupyter/lab/static/6550.f5dbb748ddae3ef4b27e.js
/usr/share/jupyter/lab/static/6598.e2d4d064ef6bca780c2c.js
/usr/share/jupyter/lab/static/6700.7d1bee36bbdf64ab0bd4.js
/usr/share/jupyter/lab/static/6777.1b7dcbf5a42c2daf11b8.js
/usr/share/jupyter/lab/static/679b5a5216bbdf913cc22d6ae44778c1ef975ee387a6c4c5de87e75d19a22232.svg
/usr/share/jupyter/lab/static/6952.1bd5bcfeb0d87e61efcb.js
/usr/share/jupyter/lab/static/6962.6d7125f759d926dcf34f.js
/usr/share/jupyter/lab/static/6975.e0560614fd629195c9bf.js
/usr/share/jupyter/lab/static/6989.75bf0da94e660a6c26f8.js
/usr/share/jupyter/lab/static/7034.fce307da76771c0ef0c8.js
/usr/share/jupyter/lab/static/7050.fc2b565767a93966c20e.js
/usr/share/jupyter/lab/static/714.a8445b6bf08d4979bfe3.js
/usr/share/jupyter/lab/static/7289.c749cf355edec3e37aa8.js
/usr/share/jupyter/lab/static/7294.f71c2889fedcd71bd1ee.js
/usr/share/jupyter/lab/static/7294.f71c2889fedcd71bd1ee.js.LICENSE.txt
/usr/share/jupyter/lab/static/7300.26360c57b8bd81344bd5.js
/usr/share/jupyter/lab/static/7454.5859b3e9803de4da9c05.js
/usr/share/jupyter/lab/static/7463.c34847707aeb55f90a82.js
/usr/share/jupyter/lab/static/74edc18b67c487e32f181719fdb347e2e77020744651f446e9acd7bd6821e2e7.woff
/usr/share/jupyter/lab/static/75a761159ae266c5332a4f266e07a5543712ffb76ee0260b07782195c04dc364.eot
/usr/share/jupyter/lab/static/7717.2a6e6bb4e5f6b92e9798.js
/usr/share/jupyter/lab/static/7730.7e3a9fb140d2d55a51fc.js
/usr/share/jupyter/lab/static/7755.d506a1d9dadf30b1e490.js
/usr/share/jupyter/lab/static/7788.5e16fdcc197e245776fd.js
/usr/share/jupyter/lab/static/7796.a62f2ce2891c993a18e5.js
/usr/share/jupyter/lab/static/7900.86dcbbbfb1a3d4f98375.js
/usr/share/jupyter/lab/static/8012.e4c8f67dc497d26c16fc.js
/usr/share/jupyter/lab/static/8059.6011120485fc3c4868d4.js
/usr/share/jupyter/lab/static/807.96166378e2efe232d81e.js
/usr/share/jupyter/lab/static/807.96166378e2efe232d81e.js.LICENSE.txt
/usr/share/jupyter/lab/static/8102.7f1644c3be420fb40db9.js
/usr/share/jupyter/lab/static/8428.dd5a93f02f55af0d3d8c.js
/usr/share/jupyter/lab/static/8523.9b232c15e4eb5bc08a37.js
/usr/share/jupyter/lab/static/8580.974138f8b6ddb72035f9.js
/usr/share/jupyter/lab/static/8657.bf693afb7646976b9a51.js
/usr/share/jupyter/lab/static/870.e515a8a325f5ddb19079.js
/usr/share/jupyter/lab/static/8708.35479b2d01be1e86804a.js
/usr/share/jupyter/lab/static/8819.743ff7148bbdf35c7bbb.js
/usr/share/jupyter/lab/static/8834.7621cb792c80bfa66e05.js
/usr/share/jupyter/lab/static/8843.35ec0f0b1f61c25e0401.js
/usr/share/jupyter/lab/static/8afc6e5e842baab16010c2ce6fcf48ec4ded8e1579a37c1f1bc027e120d04951.woff2
/usr/share/jupyter/lab/static/900.6a1241c0269d5df615c8.js
/usr/share/jupyter/lab/static/901.2ec3367a81663f96cc4b.js
/usr/share/jupyter/lab/static/9039.5f28fec36b1eba3e4a52.js
/usr/share/jupyter/lab/static/9109.1b114e9c83e36c6560df.js
/usr/share/jupyter/lab/static/911.0c08f040896753efc653.js
/usr/share/jupyter/lab/static/911.0c08f040896753efc653.js.LICENSE.txt
/usr/share/jupyter/lab/static/9316.c4abfd78d98bb182cd2f.js
/usr/share/jupyter/lab/static/9473.5a9c6a963b6aaa178bc3.js
/usr/share/jupyter/lab/static/9473.5a9c6a963b6aaa178bc3.js.LICENSE.txt
/usr/share/jupyter/lab/static/96.c281b119ab350d7dd3de.js
/usr/share/jupyter/lab/static/9845.8b6c837a5ff754554b39.js
/usr/share/jupyter/lab/static/9866.5db2f5cd62fb6e231305.js
/usr/share/jupyter/lab/static/aff76e5c986f295d4bc6f8142a78e2a31888b101c2d025db89f79c75f64fd90b.woff
/usr/share/jupyter/lab/static/bootstrap.js
/usr/share/jupyter/lab/static/build_log.json
/usr/share/jupyter/lab/static/c651b8a67d3193206f622c3c3b0fbca4a2f2727108c4212b52c1e2a2e84c9b31.ttf
/usr/share/jupyter/lab/static/cf83ffb8cf0023bd439dfdd5d02f1954b6ee027e85897d6cfc5f90bbca9ec1d2.eot
/usr/share/jupyter/lab/static/d0b4256abed72481585662971262eabee345c19f837af00d7ce24239d3b40eef.woff2
/usr/share/jupyter/lab/static/fa498fb2596a5235c5c86d7b68a7fbe76e9855c01af4b0e5ab41c41047c648e0.svg
/usr/share/jupyter/lab/static/index.html
/usr/share/jupyter/lab/static/index.out.js
/usr/share/jupyter/lab/static/jlab_core.081dc2b13065c79d8463.js
/usr/share/jupyter/lab/static/jlab_core.081dc2b13065c79d8463.js.LICENSE.txt
/usr/share/jupyter/lab/static/main.c047a5cb14c1d595046d.js
/usr/share/jupyter/lab/static/package.json
/usr/share/jupyter/lab/static/style.js
/usr/share/jupyter/lab/static/third-party-licenses.json
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/index.css
/usr/share/jupyter/lab/themes/@jupyterlab/theme-dark-extension/index.js
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/index.css
/usr/share/jupyter/lab/themes/@jupyterlab/theme-light-extension/index.js

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jupyterlab/0036998e52f1b6442c90b9ea6df602bef0294cc5
/usr/share/package-licenses/pypi-jupyterlab/01ebbe688c25d738b9ee0e2de8113f7351c88e7a
/usr/share/package-licenses/pypi-jupyterlab/0656099c1cf5c72718c57eb920abcffa02df0a93
/usr/share/package-licenses/pypi-jupyterlab/10645e5e81c59dc0f14b79252005ea68d42f1ba7
/usr/share/package-licenses/pypi-jupyterlab/cd522246a57b87ba54b1b6b92174b9091f70e983
/usr/share/package-licenses/pypi-jupyterlab/fa62fa6d531b94e755b914b3291c8541ce40f411

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
