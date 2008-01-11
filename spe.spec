%define name spe
%define tname SPE
%define version 0.8.2.a_wx2.6.1.0
%define tversion 0.8.2.a-wx2.6.1.0
%define release %mkrel 2

Summary: Stani's Python Editor 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://download.berlios.de/python/%{tname}-%{tversion}.tar.bz2
License: GPL
Group: Editors
Url: http://pythonide.stani.be 
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: python-devel
BuildRequires: ImageMagick
Requires: wxPython >= 2.6.1.0

%description
Spe is a free python IDE with auto indentation & completion, call tips, 
syntax coloring & highlighting, UML diagrams, class explorer, source index, 
auto todo list, sticky notes, pycrust shell, file browsers, drag&drop, 
context help, Blender support,

%prep
%setup -q -n %{tname}-%{tversion}

%build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

%define logo build/lib/_%{name}/images/%{name}.png
%define iconname %{name}.png
convert %logo -geometry 48x48 %{buildroot}%{_liconsdir}/%{iconname}
convert %logo -geometry 32x32 %{buildroot}%{_iconsdir}/%{iconname}
convert %logo  -geometry 16x16 %{buildroot}%{_miconsdir}/%{iconname} 


mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=SPE
Comment=Stani's Python Editor
Exec=%{_bindir}/%{name}
Icon=%{iconname}
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-MoreApplications-Editors;TextEditor;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_menus}

%postun
%{clean_menus}

%files
%defattr(-,root,root)
%dir %{py_libdir}/site-packages/_%{name}
%{py_puresitedir}/_%{name}/*
%{py_puresitedir}/*.egg-info
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop
%{_miconsdir}/%{iconname}
%{_iconsdir}/%{iconname}
%{_liconsdir}/%{iconname}



