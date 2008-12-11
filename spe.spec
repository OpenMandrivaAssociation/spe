Summary:	A Python-based IDE 
Name:		spe
Version:	0.8.4.h
Release:	%{mkrel 1}
Source0:	http://download.berlios.de/python/%{name}-%{version}-wx2.6.1.0.tar.gz
License:	GPLv2+
Group:		Development/Python
URL:		http://pythonide.stani.be 
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python-devel
BuildRequires:	imagemagick
Requires:	wxPython >= 2.6.1.0
Requires:	pychecker

%description
Spe is a free Python IDE with auto indentation & completion, call tips, 
syntax coloring & highlighting, UML diagrams, class explorer, source index, 
auto todo list, sticky notes, pycrust shell, file browsers, drag&drop, 
context help and Blender support.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --compile --optimize=2

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{48x48,32x32,16x16}/apps
convert build/lib/_spe/images/spe.png -scale 48x48 %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert build/lib/_spe/images/spe.png -scale 32x32 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert build/lib/_spe/images/spe.png -scale 16x16 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=SPE
Comment=Python IDE
Exec=%{_bindir}/%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Development;IDE;
EOF

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr(-,root,root)
%{py_puresitedir}/_%{name}
%{py_puresitedir}/*.egg-info
%{_bindir}/%{name}*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png

